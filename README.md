# Bias Aware Face Mask Detection Dataset (BAFMD)
We present a novel face mask detection dataset that contains images posted on Twitter during the pandemic from around the world. Unlike previous datasets, Bias-Aware Face Mask Detection (BAFMD) dataset contains more images from underrepresented race and age groups to mitigate the problem for the face mask detection task.



![mask_visualization](https://user-images.githubusercontent.com/18146534/199670602-09dadda1-b0dc-4f2f-ad39-b42b2ad5c2a0.png)
Fig. 1 : The dataset contains more than 13,000 face masks with various textures and colors. We present some example face masks from the dataset.  

![dataset_overall_image_2](https://user-images.githubusercontent.com/18146534/199670726-bed96270-2c80-4686-8350-b7cb3caa462d.png)
Fig. 2 : Images are collected from Twitter and therefore contain pictures from daily life and public appearances. Although our dataset contains mostly images in-the-wild, here we only show images that contains public figures. 


## About the Dataset and How to Download
<a href="BAFMD_image_urls.tsv">BAFM_image_urls.tsv</a> contains all the annotated image names and their URLs. First column shows the image filename and second column shows the URL.
If you run the <a href="fetch_dataset.py">fetch_dataset.py</a> script, it will download all the available images and place them to the different folders (train_set and test_set). Also, the script will move the annotations to the regarding folders. Please note that downloading process takes some time.

## Annotation Type 
There are two different annotation files for each image. Both annotation files have the same bounding boxes. Regarding your label format, you can choose the one that you will use. 

1-) image_name.txt annotation that uses YOLO labeling format which is object class, object coordinates, height, and width. All of them are normalized between 0 and 1

2-) image_name.xml annotation that uses Pascal VOC labeling format. It contains image size, object coordinates and class names. 

## Dataset Copyrights 
Bias Aware Face Mask Detection (BAFMD) dataset is available for non-commercial research purposes only.

The dataset collected from Twitter, therefore you have to check the licensing information from Twitter to use the images for your purpose.

## Citation ##
This dataset has been explained and has been used in [our paper]([https://arxiv.org/abs/2103.08773](https://arxiv.org/abs/2211.01207)). Cite our paper, if you downloaded and used our dataset.

```
@misc{kantarci2022,
  doi = {10.48550/ARXIV.2211.01207},
  url = {https://arxiv.org/abs/2211.01207},
  author = {Kantarcı, Alperen and Ofli, Ferda and Imran, Muhammad and Ekenel, Hazım Kemal},
  title = {Bias-Aware Face Mask Detection Dataset},
  publisher = {arXiv},
  year = {2022},
}

```
