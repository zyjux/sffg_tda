# Sugar, Fish, Flowers, and Gravel with Topological Data Analysis

## Introduction

This is a repository containing code examples for running _persistent homology_, a tool from the mathematical field of _topological data analysis (TDA)_ on the [Sugar, Fish, Flowers, and Gravel dataset by Stevens et. al](https://github.com/raspstephan/sugar-flower-fish-or-gravel), more fully described in the [paper here](https://journals.ametsoc.org/view/journals/bams/101/11/bamsD190324.xml).

## Dependencies

To begin, install [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your system and create a clean environment, and if you have not already then install the following packages from [conda-forge](https://conda-forge.org/):

```
python >= 3.9
numpy
matplotlib
PIL
pandas
scikit-learn
tqdm
gudhi
```

The final package, [GUDHI](https://gudhi.inria.fr/), contains the software implementations of TDA algorithms that we will principally use in this example.

## Downloading Data

To download the image data, navigate to the `image_download` folder, update the `download_all.ps1` (for Windows Powershell) or `download_all.sh` (for Unix-based systems) scripts with where you would like the data to be stored, then execute that script.
