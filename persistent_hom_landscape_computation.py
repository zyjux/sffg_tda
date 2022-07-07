#
# This script does the primary computations for transforming image samples to
# TDA data. We load the data, choose some random samples from each class, 
# then subsample those and compute the persistent homology for each. The
# annotation information for our random sample is saved as TDA_sample_df.pkl,
# the landscapes are saved in TDA_landscapes.pkl, and the locations of the sub-
# sampling boxes are saved in TDA_boxes.pkl.
#
import pandas as pd
import numpy as np
from PIL import Image
import pickle
import gudhi
import gudhi.wasserstein as wass
import gudhi.representations as gr
from collections import namedtuple
from tqdm import tqdm

# Initialize randomizer
rng = np.random.default_rng()

# Set path to raw images - change to where you downloaded data to
IMGPATH = 'D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/'

# Load datasets
print('Loading dataset')
annos_full = pd.read_pickle('./processed_data/annos_full.pkl')

# Process subject labels
print('Pre-processing dataset')
subj_ids_full = annos_full.subject_ids.unique()

# Fix out of bounds errors and ensure our annotations are fully within each image
def clamp_width(r):
    x = r['x'] + r['width']
    if x > 2100:
        o = r['width'] - (x-2100)
    else:
        o = r['width']
    return o


def clamp_height(r):
    x = r['y'] + r['height']
    if x > 1400:
        o = r['height'] - (x-1400)
    else:
        o = r['height']
    return o


annos_full['x'] = annos_full.x.apply(lambda x: np.clip(x, 0, 2099))
annos_full['y'] = annos_full.y.apply(lambda x: np.clip(x, 0, 1399))

annos_full['width'] = annos_full.apply(clamp_width, axis=1)
annos_full['height'] = annos_full.apply(clamp_height, axis=1)

# Set parameters: 
# n_rows number of annotations of each type
# n_samples is the number of boxes from each annotation
# sample_size is the size of each subsampling box
patterns = ('Sugar', 'Fish', 'Flower', 'Gravel')
n_rows = 200
n_samples = 6
sample_size = 96

# Create both training and testing datasets
for purpose in ['train_', 'test_']:

    # Set up filename
    fn_prefix = './processed_data/' + purpose

    # Choose n rows randomly from those annotations which are at least 128 x 128
    print('Selecting samples for ' + purpose)
    dfs = []
    for pattern in patterns:
        filt_df = annos_full.iloc[[a and b and c for a, b, c in zip(
            list(annos_full.height >= 128),
            list(annos_full.width >= 128),
            list(annos_full.tool_label == pattern)
        )]]
        row_chooser = rng.integers(0, len(filt_df), size = n_rows)
        dfs.append(filt_df.iloc[row_chooser])
    df = pd.concat(dfs)

    # Save sampled dataset
    print('Saving samples')
    df.to_pickle(fn_prefix + 'TDA_sample_df.pkl')

    # Initialize namedtuples for storing persistent homology data
    tda_data = namedtuple('tda_data', ['H0', 'H1'])

    # Initialize empty lists to store barcodes, landscapes, and subsample box information
    representations = []
    boxes = []
    # Process each annotation
    print('Processing samples\n')
    for box in tqdm(df.itertuples(), total=len(patterns)*n_rows):
        # Compute filename for image
        fn = IMGPATH + box.fn
        # Open image as grayscale and initialize plot
        with Image.open(fn).convert('L') as img:
            # Compute coordinates of random subsamples
            x_coords = rng.integers(box.x, box.x + box.width - sample_size, size = n_samples)
            y_coords = rng.integers(box.y, box.y + box.height - sample_size, size = n_samples)

            # Initialize empty lists to store homology data in
            H0 = []
            H1 = []
            for i in range(n_samples):
                # Pull the sample as a numpy array and compute its sublevelset persistent homology
                img_sample = np.array(img.crop((x_coords[i], y_coords[i], x_coords[i] + sample_size, y_coords[i] + sample_size)))
                cmplx = gudhi.CubicalComplex(top_dimensional_cells=255 - img_sample[:, :])
                cmplx.compute_persistence(homology_coeff_field=2)
                # Record H0 and H1 persistence, ignoring the H0 infinite bar
                H0.append(np.reshape(cmplx.persistence_intervals_in_dimension(0)[:-1, :], newshape=(-1, 2)))
                H1.append(np.reshape(cmplx.persistence_intervals_in_dimension(1), newshape=(-1, 2)))

            # Record the unioned barcodes and box coordinates
            lscape = gr.Landscape(num_landscapes=5, resolution=200, sample_range=[0, 255])
            H0_lscapes = lscape.transform(H0)
            H1_lscapes = lscape.transform(H1)
            rep = tda_data(np.mean(H0_lscapes, 0), np.mean(H1_lscapes, 0))

            # Save the information from this annotation to our global lists
            representations.append(rep)
            boxes.append([(a, b) for a, b in zip(x_coords, y_coords)])

    # Record the side length of the subsamples as the last entry in the boxes list
    boxes.append(sample_size)

    # Save boxes and representations
    print('Saving files\n')
    with open(fn_prefix + 'TDA_landscapes.pkl', 'wb') as rep_file:
        pickle.dump(representations, rep_file)
    with open(fn_prefix + 'TDA_sample_boxes.pkl', 'wb') as bx_file:
        pickle.dump(boxes, bx_file)
