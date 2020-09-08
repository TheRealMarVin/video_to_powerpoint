from power_point_builder import to_power_point
from video_extract import extract_video_frame, extract_images_for_frame


def get_page(url):
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    print((r.status))
    print((r.data))

    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://sitescours.monportail.ulaval.ca/ena/site/module?editionModule=false&idSite=121706&idPage=2790239&idModule=1030262&_js=true'
    # get_page(url)

    video = "C:/Users/naked_000/Desktop/video(1).mp4"
    out_dir = "./out"

    extract_images_for_frame(video, out_dir)
    to_power_point(out_dir)
