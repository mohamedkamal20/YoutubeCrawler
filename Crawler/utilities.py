import os
import requests
import uuid


def save_image(url, is_original=False):

    response = requests.get("{}".format(url))
    image_name = uuid.uuid4()
    this_folder = os.path.dirname(os.path.abspath(__file__))
    if is_original:
        image = open(os.path.join(this_folder, "images/original/{}.jpeg".format(image_name)), "wb")
        image.write(response.content)
        image.close()
    else:
        image = open(os.path.join(this_folder, "images/thumbnail/{}.jpeg".format(image_name)), "wb")
        image.write(response.content)
        image.close()
    return image_name


def remove_image(image_name, is_original=False):

    this_folder = os.path.dirname(os.path.abspath(__file__))
    if is_original:
        image_path = os.path.join(this_folder, "images/original/{}.jpeg".format(image_name))
        if os.path.isfile(image_path):
            os.remove(image_path)
    else:
        image_path = os.path.join(this_folder, "images/thumbnail/{}.jpeg".format(image_name))
        if os.path.isfile(image_path):
            os.remove(image_path)

'''
def download_video(url):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    video = YouTube(url)
    video.streams.first().download(this_folder + "videos/")
'''