from instagrapi import Client
from pathlib import Path
import os
import time

# Initialize the Instagram client
cl = Client()

# Set the timeout for API requests
cl = Client(request_timeout=60)  # Set the timeout to 60 seconds

# Login to your Instagram account
cl.login("", "")

# Set the folder path containing the reels
folder_path = r"D:\RedditVideoMakerBot\results\confession"

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a video
    if filename.endswith(".mp4"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Upload the reel
        media = cl.video_upload(
            file_path,
            caption="Follow if you are not GAY!! #confession #mentalhealth #selflove #rawandreal #reelitreal #instareels #instareelsvideo #reelsvideo #mentalhealthmatters #selfdiscovery"
        )
        
        print(f"Uploaded reel: {filename}")