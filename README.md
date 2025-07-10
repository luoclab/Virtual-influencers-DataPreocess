# Virtual influencers’ physical appearance and its effect on user engagement and gift-giving
![Framework Overview](src/overview.jpg)  

**Abstract**

**Purpose:** The physical appearance of virtual influencers has raised the attention of researchers. This study aims to find and prove the quantified physical appearance traits of virtual influencers (non-human and color feature) on user engagement and gift-giving behavior. 

**Methods:** OpenCV, Image Color Summarizer and multi-variable regression analysis were utilized to test hypotheses on a sample of 2456 live streaming sessions.

**Results:** The empirical findings reveal the significant relationships among non-human feature, warm degree, user engagement and gift-giving behavior. Non-human feature has negative impact on user engagement but positive impact on gift-giving behavior. Warm degree always has a positive effect on both user engagement and gift-giving behavior. In addition, the proved moderating effects show that lightness and chroma has a significant moderating effect on the relationship between appearance of the virtual influencers and both user engagement and gift-giving behavior.

**Conclusion:** This study refines physical appearance into more specifical feature such as non-human feature and color effects to adapt the concept of virtual influencers. It examines its actual impact, and extends the conceptual framework of effectiveness of virtual influencers by comprehending the theory of Uncanny valley and color psychology.

# Virtual Influencers Data Processing Pipeline

## 1.opencv
We use OpenCV to read the image and extract the color value (R, G, B) pixel by pixel based on the RGB color model. Then, according to the formula shown in Figure 2 in the paper, we calculate the cold and warm value of each pixel and take the average of the cold and warm values ​​of all pixels as the cold and warm value of the entire image. The code is in opencv/

## 2.Colorsummarizer
We use the open source image color summarization tool [colorsummarizer](https://mk.bcgsc.ca/colorsummarizer/)
 for color feature extraction. Our configuration file is in the colorsummarizer/ file path
To support batch processing, we use the local version of the tool and test to confirm that it is consistent with the online version.

## 3. Anime Character Detection and Extraction

This module identifies and extracts anime-style virtual influencer characters from images for downstream tasks.

We use the following opensource tools:

### 3.1 Anime Character Face Detection  
We use the open-source project [Anime Face Detector](https://github.com/qhgz2013/anime-face-detector) to detect characters in the image. The model returns bounding boxes, which are used to crop out the character region.

### 3.2 Background Removal  
We apply [Pixian.AI](https://pixian.ai/) to remove the background from the cropped character image, keeping only the character with a transparent background.

### Sample Outputs  
Randomly selected examples are available in the following folder:sample/

