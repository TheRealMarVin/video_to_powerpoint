import math
import operator
from PIL import Image
import os
import glob
import subprocess
import shutil
from functools import reduce
import tempfile
import logging

logging.basicConfig(level=logging.INFO)


# this was found on https://stackoverflow.com/questions/1927660/compare-two-images-the-python-linux-way
def are_images_same(file1, file2, threshold=5):
    h1 = Image.open(file1).histogram()
    h2 = Image.open(file2).histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms < threshold  # Consider images the same if RMS is very low


def construct_ffmpeg_command(video, tmp_folder, frame_type="I", format="png"):
    return [
        "ffmpeg", "-i", video, "-vf", f"select='eq(pict_type,{frame_type})'",
        "-vsync", "0", "-f", f"image2", f"{tmp_folder}/%09d.{format}"
    ]


def extract_images_for_frame(video, out_dir, distance_threshold):
    with tempfile.TemporaryDirectory() as tmp_folder:
        cmd = construct_ffmpeg_command(video, tmp_folder)
        logging.info(f"Running FFmpeg: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        logging.info("Frame extraction completed.")

        filelist = sorted(glob.glob(os.path.join(tmp_folder, '*.png')))
        if not filelist:
            raise ValueError("No frames found in temporary folder.")

        for index in range(len(filelist) - 1):
            if not are_images_same(filelist[index], filelist[index + 1], distance_threshold):
                _, tail = os.path.split(filelist[index])
                shutil.copyfile(filelist[index], os.path.join(out_dir, tail))

        # Always copy the last frame
        _, tail = os.path.split(filelist[-1])
        shutil.copyfile(filelist[-1], os.path.join(out_dir, tail))
        logging.info("Duplicate frames removed.")
