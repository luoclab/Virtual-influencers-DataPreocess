# Virtual influencers’ physical appearance and its effect on user engagement and gift-giving
![Framework Overview](src/overview.jpg)  

**Abstract**

The physical appearance of virtual influencers have raised the attention of scholars, but empirical evidence regarding its specific features and quantitative impacts remains limited. This study analyzed 2,456 live streaming sessions, utilizing OpenCV and the Image Color Summarizer tool to quantify key physical appearance traits (non-human and color feature) and employed multi-variable regression analysis to examine the actual influence of physical appearance traits on user engagement and gift-giving behavior. The empirical findings reveal that non-human feature significantly reduce user engagement but increase gift-giving behavior, highlighting the complexity of anthropomorphism. Additionally, warm degree always has a positive effect on both user engagement and gift-giving behavior. The proved moderating effects show that lightness and chroma have a significant moderating effect on the relationship between the appearance of the virtual influencers and both user engagement and gift-giving behavior. These findings enrich the theoretical framework by integrating the theory of Uncanny Valley, anthropomorphism, and color psychology, indicating that appearance cues can elicit different effects depending on the outcome objective. It provides novel insights for optimizing virtual influencer design and marketing campaign strategies.

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

