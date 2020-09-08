import shutil

from power_point_builder import to_power_point
from video_extract import extract_images_for_frame
import os
import glob


def get_page(url):
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    print((r.status))
    print((r.data))

    return None


def get_video_name(video_folder):
    filelist = glob.glob(os.path.join(video_folder, '*.mp4'))
    return filelist


def path_leaf(path):
    _, tail = os.path.split(path)
    base_name, _ = os.path.splitext(tail)
    return base_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://sitescours.monportail.ulaval.ca/ena/site/module?editionModule=false&idSite=121706&idPage=2790239&idModule=1030262&_js=true'
    # get_page(url)

    #video = "C:/Users/naked_000/Desktop/video(1).mp4"
    out_dir = "./out"

    videos = get_video_name("videos")
    for video in videos:
        extract_images_for_frame(video, out_dir)
        base_name = path_leaf(video)

        to_power_point(out_dir, base_name)
        shutil.rmtree(out_dir)

    print("Done")
