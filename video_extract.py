"""
This module handles video frame extraction, duplicate removal, and preparation for further processing.
It includes utilities for comparing frames, generating FFmpeg commands, and managing temporary directories.
"""

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
    """
    Compare two images to determine if they are the same based on RMS difference of histograms.

    Args:
        file1 (str): Path to the first image.
        file2 (str): Path to the second image.
        threshold (int): RMS threshold to consider images as duplicates. Defaults to 5.

    Returns:
        bool: True if images are considered the same, False otherwise.
    """
    h1 = Image.open(file1).histogram()
    h2 = Image.open(file2).histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a, b: (a - b) ** 2, h1, h2)) / len(h1))
    return rms < threshold

def construct_ffmpeg_command(video, tmp_folder, frame_type="I", format="png", start_time=None, end_time=None, duration=None):
    """
    Construct the FFmpeg command to extract video frames.

    Args:
        video (str): Path to the video file.
        tmp_folder (str): Temporary folder to save extracted frames.
        frame_type (str): Type of frames to extract (e.g., "I"). Defaults to "I".
        format (str): Image format for output frames. Defaults to "png".
        start_time (float, optional): Start time in seconds for extraction.
        end_time (float, optional): End time in seconds for extraction.
        duration (float, optional): Duration in seconds for extraction.

    Returns:
        list: FFmpeg command as a list of arguments.
    """
    cmd = ["ffmpeg"]

    # Add start time if specified
    if start_time:
        cmd.extend(["-ss", str(start_time)])

    cmd.extend(["-i", video])

    # Add end time or duration if specified
    if duration:
        cmd.extend(["-t", str(duration)])
    elif end_time:
        cmd.extend(["-to", str(end_time)])

    cmd.extend([
        "-vf", f"select='eq(pict_type,{frame_type})'",
        "-vsync", "0", "-f", "image2",
        f"{tmp_folder}/%09d.{format}"
    ])
    return cmd

def extract_images_for_frame(video, out_dir, start_time=None, end_time=None, duration=None, distance_threshold=5):
    """
    Extract unique frames from a video, removing duplicates based on RMS difference.

    Args:
        video (str): Path to the video file.
        out_dir (str): Directory to save extracted unique frames.
        start_time (float, optional): Start time in seconds for extraction.
        end_time (float, optional): End time in seconds for extraction.
        duration (float, optional): Duration in seconds for extraction.
        distance_threshold (int): RMS threshold to consider frames as duplicates. Defaults to 5.

    Raises:
        ValueError: If end time is earlier than start time.
        ValueError: If duration is negative.
        ValueError: If no frames are found in the temporary folder.
    """
    if start_time is not None and end_time is not None and end_time < start_time:
        raise ValueError(f"End time ({end_time}s) cannot be earlier than start time ({start_time}s).")

    if duration is not None and duration < 0:
        raise ValueError(f"Duration ({duration}s) cannot be negative.")

    with tempfile.TemporaryDirectory() as tmp_folder:
        cmd = construct_ffmpeg_command(video, tmp_folder, start_time=start_time, end_time=end_time, duration=duration)
        logging.info(f"Running FFmpeg: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        logging.info("Frame extraction completed.")

        filelist = sorted(glob.glob(os.path.join(tmp_folder, '*.png')))
        if not filelist:
            raise ValueError("No frames found in temporary folder.")

        for index in range(len(filelist) - 1):
            if index == 0 or not are_images_same(filelist[index], filelist[index + 1], distance_threshold):
                _, tail = os.path.split(filelist[index])
                shutil.copyfile(filelist[index], os.path.join(out_dir, tail))

        # Always copy the last frame
        _, tail = os.path.split(filelist[-1])
        shutil.copyfile(filelist[-1], os.path.join(out_dir, tail))
        logging.info("Duplicate frames removed.")
