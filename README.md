# Virtual-influencers-DataPreocess
this repositoty is a utility tools
# Virtual Influencers Image Processing Pipeline
A reproducible workflow for color analysis and anime character extraction
https://img.shields.io/badge/license-MIT-blue.svg

https://src/overview.jpg

📌 Overview
This repository provides a transparent and replicable pipeline for:

Image color analysis (OpenCV + Image Color Summarizer)

Anime character detection/extraction (pre-trained models)

Cold/warm tone calculation (RGB-based metric)

Designed for future studies on virtual influencers' visual characteristics.

🔧 Methodology
1. OpenCV-based Color Processing
Application:

Reads images in RGB mode and extracts per-pixel channel values

Computes cold/warm tone scores using the formula from Figure 2 in the paper

Batch processes all images with fixed parameters

Reproducibility:
✅ Fixed image processing logic (process_colors.py)
✅ All parameters hardcoded (no hidden config)
✅ Compatible with alternative libraries (PIL, scikit-image)

Future Extensions:

Implement HSV/LAB color spaces (hsv_extension.py [planned])

Add human perception weighting

2. Image Color Summarizer
Application:

Quantifies dominant colors via k-means clustering (k=5)

Extracts:

HSV/LCH values per cluster

Cluster proportions (results/summary_stats.csv)

Reproducibility:
✅ Included config file (config/summarizer_config.ini)
✅ Verified consistency between local/online versions
✅ Sample outputs provided (data/processed/)

Future Extensions:

Test different clustering algorithms

Compare across color models (Lab vs YCbCr)

3. Anime Character Detection
Application:

Face detection via anime-face-detector

Background removal using segmentation_module

Reproducibility:
✅ Frozen model weights (models/)
✅ Example outputs (data/cropped_characters/)

Future Extensions:

Fine-tune for specific attributes (expressions, accessories)

Apply to non-anime art styles
