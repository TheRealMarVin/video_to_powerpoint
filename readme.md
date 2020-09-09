# Introduction
This project is used to convert video to powerpoint presentation. It will extract every frame of the video and compare them to the next frame. If the image is different both are kept for the powerpoint presentation. I made this tool because during the covid time some teacher made video presentation of slides and not providing the slide.

# Install
Create a Anaconda environment using the environment.yml and you are good to go.

# How to use
Place your video in a folder named videos at the root of this project. Run the main script and wait. The app will process all the videos in this folder.
The output will be placed in a folder named presentation at the root of this project.

# Troubleshoot
if you stop execution it might have created some folder called "decomp" or "out". If they exist I chose to crash at the moment. So just delete them and run again.