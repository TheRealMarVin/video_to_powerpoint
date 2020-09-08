import math, operator

import pptx
from PIL import Image
import sys
import os
import glob
import subprocess
import shutil
from functools import reduce


# this was found on some stackoverflow
def are_image_same(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    h1 = image1.histogram()
    h2 = image2.histogram()
    rms = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))

    return rms == 0


def extract_video_frame(video, out_dir, tmp_folder="decomp"):
    if not os.path.exists(tmp_folder):
        os.mkdir(tmp_folder)
    else:
        sys.exit("{} already exists, exit".format(tmp_folder))

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    cmd = ["ffmpeg", "-i", video, "-vf", "select='eq(pict_type,I)'", "-vsync", "0", "-f", "image2",
           "{}/%09d.png".format(tmp_folder)]

    print(("Running ffmpeg: " + " ".join(cmd)))


    subprocess.call(cmd)

    print("Done, now eliminating duplicate images and moving unique ones to output folder...")


def remove_duplicate_frame(out_dir, tmp_folder="decomp"):
    filelist = glob.glob(os.path.join(tmp_folder, '*.png'))
    filelist.sort()

    for index in range(0, len(filelist)):
        if index < len(filelist) - 1:
            if not are_image_same(filelist[index], filelist[index + 1]):
                _, tail = os.path.split(filelist[index])
                shutil.copyfile(filelist[index], out_dir + os.path.sep + tail)
        else:
            shutil.copyfile(filelist[index], out_dir + os.path.sep + tail)

    shutil.rmtree(tmp_folder)


def extract_images_for_frame(video, out_dir, tmp_folder="decomp"):
    extract_video_frame(video, out_dir, tmp_folder)
    remove_duplicate_frame(out_dir, tmp_folder)
