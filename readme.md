# Welcome to the Ultimate Video-to-Slide Conversion Machine!

Ever watched a video with great slides but wished you could just grab those frames and turn them into a PowerPoint? Well, look no further! This tool will do exactly that! We extract frames from your video, compare each one with the next, and only keep the ones that are different. The result? A seamless PowerPoint presentation built from your video content!

This was born during the times of endless Zoom classes when teachers decided to record their slides but not share them. Well, we've got your back!

---

## **What Does It Do?**

**Video to PowerPoint** takes any video, breaks it down into individual frames, and then neatly packages those frames into a PowerPoint file (.pptx). Imagine:

- Highlighting critical video moments for a presentation
- Creating time-lapse slideshows
- Impressing your boss with your tech wizardry

No more manually taking screenshots or guessing frame numbers. Let the script do the heavy lifting while you sip on your coffee (or tea, we’re inclusive here).

---

## **Features**

- **Frame Extraction:** Automatically extracts frames from any video file.
- **Dynamic Slide Generation:** Each frame gets its very own slide.
- **Compatible with Any Video Format:** If your media player can play it, we can frame it.

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

3. **Run the Script:** Provide your video file and customize your preferences:

   ```bash
   python video_to_powerpoint.py --video_path your_video.mp4 --output slides.pptx
   ```

   Replace `your_video.mp4` with your video file and give your PowerPoint masterpiece a name.

4. **Admire Your Work:** Open the generated `.pptx` file and bask in your genius.

---

## **Arguments Explained**

- `--video_path`: Path to your video file. Mandatory.
- `--output`: Name for your PowerPoint file. Defaults to `output.pptx` because we like predictable filenames.

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

---

Happy Slide-Making! 🎥➡️📽️➡️📑

