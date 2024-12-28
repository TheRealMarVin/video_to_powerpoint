import os
import glob
from pptx import Presentation
import logging

def to_power_point(img_folder, base_name, export_folder="./presentation/", slide_layout=6, output_name=None):
    if not os.path.exists(img_folder):
        raise FileNotFoundError(f"Image folder not found: {img_folder}")

    filelist = sorted(glob.glob(os.path.join(img_folder, '*.png')))
    if not filelist:
        raise ValueError(f"No PNG files found in {img_folder}")

    if not os.path.exists(export_folder):
        os.makedirs(export_folder)

    logging.basicConfig(level=logging.INFO)
    prs = Presentation()

    for file in filelist:
        logging.info(f"Adding image {file} to slide")
        slide = prs.slides.add_slide(prs.slide_layouts[slide_layout])
        slide_width = prs.slide_width
        slide.shapes.add_picture(file, 0, 0, width=slide_width)

    output_name = output_name or f"{base_name}.pptx"
    prs.save(os.path.join(export_folder, output_name))
    logging.info(f"Presentation saved at {os.path.join(export_folder, output_name)}")
