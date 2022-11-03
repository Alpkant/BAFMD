import mimetypes
import urllib.request as urllib2
import os 
from tqdm import tqdm
import shutil

def is_url_image(url):    
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def check_url(url):
    """Returns True if the url returns a response code between 200-300,
       otherwise return False.
    """
    try:
        headers = {
            "Range": "bytes=0-10",
            "User-Agent": "MyTestAgent",
            "Accept": "*/*"
        }

        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        return response.code in range(200, 209)
    except Exception:
        return False

def is_image_and_ready(url):
    return is_url_image(url) and check_url(url)

def read_image_names(filename):
    with open(filename,"r") as f:
        images_with_extensions = f.readlines()
        images_without_extensions = [i.split(".")[0] for i in images_with_extensions]
    return images_without_extensions

def main():
    # Set appropriate folder and file paths
    image_urls_tsv = "BAFMD_image_urls.tsv"
    train_set_image_names= read_image_names("BAFMD_train_images.txt")
    test_set_image_names= read_image_names("BAFMD_test_images.txt")
    # annotations will be read from annotation dir
    annotation_dir = "annotations"
    # images will be downloaded to the train_dir and test_dir
    # annotations will also be copied to the directories
    train_dir = "train_set"
    test_dir = "test_set"
    os.makedirs("train_set",exist_ok=True)
    os.makedirs("test_set",exist_ok=True)
    
    with open(image_urls_tsv, "r") as f:
        image_urls = f.readlines()


    num_invalids = 0
    with open("BAFMD_unavailable_urls.tsv","w") as f:
        for image_url_pair in tqdm(image_urls):
            # First check whether the image is available on Twitter publicly
            url_info = image_url_pair.strip().split("\t")
            filename = url_info[0]
            url = url_info[1]
            if not is_image_and_ready(url):
                print(f"Couldn't download {filename}\t{url}\n")
                num_invalids += 1
                f.write("{}\t{}\n".format(filename,url))
                continue
            # If image is available download and copy to appropriate directory
            if filename in train_set_image_names:
                # Get the image and save it to belonging set directory
                with open(os.path.join(train_dir,filename+"."+url.split(".")[-1]),"wb") as image_f:
                    image_f.write(urllib2.urlopen(url).read())
                    image_f.close()
                # Copy annotations to the image folder
                shutil.copy(os.path.join(annotation_dir,filename+".xml"),train_dir)
                shutil.copy(os.path.join(annotation_dir,filename+".txt"),train_dir)
            elif filename in test_set_image_names:
                with open(os.path.join(test_dir,filename+"."+url.split(".")[-1]),"wb") as image_f:
                    image_f.write(urllib2.urlopen(url).read())
                    image_f.close()
                # Copy annotations to the image folder
                shutil.copy(os.path.join(annotation_dir,filename+".xml"),test_dir)
                shutil.copy(os.path.join(annotation_dir,filename+".txt"),test_dir)
            else:
                # Possible mistake in given filename tsv file
                print(f"Given filename ({filename}) does not belong either train or test set.")
                print("Please fix the problem by downloading the original tsv file.")
                exit()

if __name__ == "__main__":
    main()
