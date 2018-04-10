import urllib
import os

download_photo


def download_photo(self, img_url, filename):
    try:
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd() + DOWNLOADED_IMAGE_PATH
            file_path = "%s%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False
    except:
        return False
    return True