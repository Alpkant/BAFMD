# Bias Aware Face Mask Detection Dataset (BAFMD)
We present a novel face mask detection dataset that contains images posted on Twitter during the pandemic from around the world. Unlike previous datasets, Bias-Aware Face Mask Detection (BAFMD) dataset contains more images from underrepresented race and age groups to mitigate the problem for the face mask detection task.



![mask_visualization](https://user-images.githubusercontent.com/18146534/199670602-09dadda1-b0dc-4f2f-ad39-b42b2ad5c2a0.png)
Fig. 1 : The dataset contains more than 13,000 face masks with various textures and colors. We present some example face masks from the dataset.  

![dataset_overall_image_2](https://user-images.githubusercontent.com/18146534/199670726-bed96270-2c80-4686-8350-b7cb3caa462d.png)
Fig. 2 : Images are collected from Twitter and therefore contain pictures from daily life and public appearances. Although our dataset contains mostly images in-the-wild, here we only show images that contains public figures. 


## How to Download
Please fill out [this form](https://forms.gle/H7tMCZaeXDKzVH3QA) and then email/notify bafmd@googlegroups.com to request the data. After the approval, you will get image URLs, train/test splits and annotation files. 
BAFM_image_urls.tsv contains all the annotated image names and their URLs. First column shows the image filename and second column shows the URL.
BAFMD_train_images.txt contains image names that are belong to the training set that has been used in the paper.
BAFMD_test_images.txt contains image names that are belong to the test set that has been used in the paper.

You should put annotation folder and all other files under the same folder with <a href="fetch_dataset.py">fetch_dataset.py</a> script. Your dataset folder should look like this.

```
BAFMD Dataset Folder
│   BAFMD_image_urls.tsv
│   BAFMD_train_images.txt    
│   BAFMD_test_images.txt
|   fetch_dataset.py
└───annotations
│    │   image1.jpg
│    │   image1.txt
│    |   image1.xml
│    │   image2.jpg
│    │   .
│    │   .

```

If you run the <a href="fetch_dataset.py">fetch_dataset.py</a> script, it will download all the available images and place them to the different folders (train_set and test_set). Also, the script will move the annotations to the regarding folders. Please note that downloading process takes some time. 


## Annotation Type 
There are two different annotation files for each image. Both annotation files have the same bounding boxes. Regarding your label format, you can choose the one that you will use. 

1-) image_name.txt annotation that uses YOLO labeling format which is object class, object coordinates, height, and width. All of them are normalized between 0 and 1

2-) image_name.xml annotation that uses Pascal VOC labeling format. It contains image size, object coordinates and class names. 

## Licence and Terms of Use
This work is licensed with the MIT License. See [LICENSE](LICENSE) for details.
By downloading the data you accept the [BAFMD dataset Terms of Usage.](https://bit.ly/BAFMD-terms-of-usage)
Bias Aware Face Mask Detection (BAFMD) dataset is available for non-commercial research purposes only.
The dataset collected from Twitter, therefore you have to check the terms of usage from Twitter to use the images for your purpose as well.

## Citation ##
This dataset has been explained and has been used in [our preprint](https://arxiv.org/abs/2211.01207) and [article](https://link.springer.com/article/10.1007/s11042-024-20226-7). Please cite our paper, if you downloaded and used our dataset.
You can cite it as : 
```
Kantarcı, A., Ofli, F., Imran, M. et al. Bias-aware face mask detection dataset. Multimed Tools Appl (2024). https://doi.org/10.1007/s11042-024-20226-7
```

or the following bibtex:
```
@article{BAFMD2024,
  doi = {https://doi.org/10.1007/s11042-024-20226-7},
  url = {https://link.springer.com/article/10.1007/s11042-024-20226-7},
  author = {Kantarcı, Alperen and Ofli, Ferda and Imran, Muhammad and Ekenel, Hazım Kemal},
  title = {Bias-Aware Face Mask Detection Dataset},
  journal = {Multimedia Tools and Applications},
  publisher={Springer},
  year = {2024},
}
```
