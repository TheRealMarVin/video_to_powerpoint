import math, operator

import pptx
from PIL import Image
import sys
import os
import glob
import subprocess
import shutil
from functools import reduce

from pptx import Presentation

from video_extract import extract_video_frame, extract_images_for_frame


def get_page(url):
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    print((r.status))
    print((r.data))

    return None




def to_power_point(img_folder):
    prs = Presentation()

    filelist = glob.glob(os.path.join(img_folder, '*.png'))
    filelist.sort()
    for file in filelist:
        title_slide_layout = prs.slide_layouts[6] # 6 is blank
        slide = prs.slides.add_slide(title_slide_layout)
        width = pptx.util.Cm(33.86)
        slide.shapes.add_picture(file, 0, 0, width=width)

    prs.save('./test.pptx')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://sitescours.monportail.ulaval.ca/ena/site/module?editionModule=false&idSite=121706&idPage=2790239&idModule=1030262&_js=true'
    # get_page(url)

    video = "C:/Users/naked_000/Desktop/video(1).mp4"
    out_dir = "./out"

    extract_images_for_frame(video, out_dir)
    to_power_point(out_dir)
