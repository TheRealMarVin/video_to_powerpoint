import argparse
import logging
from power_point_builder import to_power_point
from video_extract import extract_images_for_frame
import os
import glob
import tempfile

def get_video_name(video_folder):
    supported_formats = ('*.mp4', '*.avi', '*.mkv')
    filelist = []
    for ext in supported_formats:
        filelist.extend(glob.glob(os.path.join(video_folder, ext)))
    return filelist

def path_leaf(path):
    _, tail = os.path.split(path)
    base_name, _ = os.path.splitext(tail)
    return base_name

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_folder", default="videos", help="Folder containing videos")
    parser.add_argument("--output_folder", default="./out", help="Output folder for frames")
    parser.add_argument("--presentation_folder", default="./presentation/", help="Folder to save PowerPoint presentations")
    parser.add_argument("--slide_layout", type=int, default=6, help="Slide layout to use for the presentation")
    parser.add_argument("--output_name", default=None, help="Custom name for the output PowerPoint file")
    parser.add_argument("--distance_threshold", default=5, help="Minimum distance between two slides")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    videos = get_video_name(args.video_folder)
    for video in videos:
        logging.info(f"Processing video: {video}")
        try:
            with tempfile.TemporaryDirectory() as out_dir:
                extract_images_for_frame(video, out_dir, args.distance_threshold)
                base_name = path_leaf(video)
                to_power_point(out_dir, base_name, export_folder=args.presentation_folder, slide_layout=args.slide_layout, output_name=args.output_name)
                logging.info(f"Successfully processed {video}")
        except Exception as e:
            logging.error(f"Failed to process {video}: {e}")

    logging.info("All videos processed.")
