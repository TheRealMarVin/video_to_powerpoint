import pptx
import os
import glob

from pptx import Presentation


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
