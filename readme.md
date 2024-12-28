# Welcome to the Ultimate Video-to-Slide Conversion Machine!

Ever watched a video with great slides but wished you could just grab those frames and turn them into a PowerPoint? Well, look no further! This tool will do exactly that! We extract frames from your video, compare each one with the next, and only keep the ones that are different. The result? A seamless PowerPoint presentation built from your video content!

This was born during the times of endless Zoom classes when teachers decided to record their slides but not share them. Well, we've got your back!

---

## **Getting Started**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/TheRealMarVin/video_to_powerpoint.git
   ```

2. **Install Dependencies:** We keep it simple and use Python (because Python makes everything better). Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script:** Provide your video folder and customize your preferences:

   ```bash
   python main.py --video_folder videos --output_folder ./out --presentation_folder ./presentation --slide_layout 6 --output_name my_slides.pptx
   ```

   Replace `videos` with your folder containing video files, customize the `output_folder` for extracted frames, set your desired `presentation_folder`, select a `slide_layout`, and specify an optional `output_name` for the PowerPoint presentation.

4. **Admire Your Work:** Open the generated `.pptx` file in your `presentation_folder` and bask in your genius.

---

## **Arguments Explained**

- `--video_folder`: Folder containing your video files. Defaults to `videos`.
- `--output_folder`: Folder for temporary frame extraction. Defaults to `./out`.
- `--presentation_folder`: Folder to save the final PowerPoint presentations. Defaults to `./presentation`.
- `--slide_layout`: PowerPoint slide layout to use. Defaults to `6` (blank layout).
- `--output_name`: Custom name for the output PowerPoint file. If not specified, it defaults to the video file's base name.
- `--distance_threshold`: Minimum distance (RMS) between frames to consider them unique. Defaults to `5`.

---

## **Planned Features**

- **Filters:** Choose specific time ranges or frames to include.
- **Themes:** Apply PowerPoint slide templates for aesthetic brilliance.

---

## **Contribute**

Found a bug? Got a feature request? Want to add a "meme mode"? Fork the repo and send us a pull request. Let’s make video-to-slide magic together.

---

## **License**

MIT License. Because sharing is caring.

