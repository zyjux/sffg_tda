#!/usr/bin/env bash
#    1. -61deg E; 10deg N : -40deg E; 24deg N (for season DJF and MAM)
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [-61,-40] --lat_range [10,24] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region1_DJF_Terra --satellite Terra &&
python image_download.py --year_range [2007,2018] --months [3,4,5] --lon_range [-61,-40] --lat_range [10,24] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region1_MAM_Terra --satellite Terra &
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [-61,-40] --lat_range [10,24] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region1_DJF_Aqua --satellite Aqua &&
python image_download.py --year_range [2007,2018] --months [3,4,5] --lon_range [-61,-40] --lat_range [10,24] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region1_MAM_Aqua --satellite Aqua &
#    2. 159deg E; 8deg N : 180deg E; 22deg N (for season DJF)
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [159,180] --lat_range [8,22] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region2_DJF_Terra --satellite Terra&&
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [159,180] --lat_range [8,22] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region2_DJF_Aqua --satellite Aqua&
#    3. -135deg E; -15deg N : -114deg E; -1deg N (for season DJF and SON)
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [-135,-114] --lat_range [-15,-1] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region3_DJF_Terra --satellite Terra&&
python image_download.py --year_range [2007,2018] --months [9,10,11] --lon_range [-135,-114] --lat_range [-15,-1] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region3_SON_Terra --satellite Terra&
python image_download.py --year_range [2007,2018] --months [12,1,2] --lon_range [-135,-114] --lat_range [-15,-1] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region3_DJF_Aqua --satellite Aqua&&
python image_download.py --year_range [2007,2018] --months [9,10,11] --lon_range [-135,-114] --lat_range [-15,-1] --save_path D:/research/crowdsourced_clouds/sugar-flower-fish-or-gravel/raw_data/Region3_SON_Aqua --satellite Aqua&

