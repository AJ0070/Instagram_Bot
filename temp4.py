from instagrapi import Client
from pathlib import Path
import os
import time

# Initialize the Instagram client
cl = Client()

# Set the timeout for API requests
cl = Client(request_timeout=60)  # Set the timeout to 60 seconds

# Login to your Instagram account
cl.login("petcu.re", "Jashmann123@")

# Set the folder path containing the reels
folder_path = r"D:\RedditVideoMakerBot\results\confession"

# Function to upload a reel and delete the files
def upload_and_delete(file_path, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            # Upload the reel
            media = cl.video_upload(
                file_path,
                caption="Follow if you are not GAY!!\n\n\n\n #confession #mentalhealth #selflove #rawandreal #reelitreal #instareels #instareelsvideo #reelsvideo #mentalhealthmatters #selfdiscovery"
            )
            
            print(f"Uploaded reel: {os.path.basename(file_path)}")
            
            # Delete the video file
            os.remove(file_path)
            
            # Delete the thumbnail file
            thumbnail_path = os.path.splitext(file_path)[0] + ".jpg"
            os.remove(thumbnail_path)
            
            return  # Exit the function if the upload is successful
        except Exception as e:
            print(f"Error uploading {os.path.basename(file_path)}: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in 60 seconds... ({retries}/{max_retries})")
                time.sleep(60)  # Wait for 1 minute before retrying
            else:
                print(f"Maximum number of retries reached for {os.path.basename(file_path)}. Skipping file.")
                return

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a video
    if filename.endswith(".mp4"):
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Call the upload_and_delete function
        upload_and_delete(file_path)