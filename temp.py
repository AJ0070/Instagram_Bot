from instabot import Bot
import os
import sys
from PIL import Image

# Fix for Pillow update: replace ANTIALIAS with LANCZOS
if hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.LANCZOS

def main():
    # Set up the Instabot
    bot = Bot()

    try:
        bot.login(username="petcu.re", password="Jashmann123@")
    except Exception as e:
        print(f"Failed to log in: {e}")
        return

    # Set the directory where the reels are stored
    reel_folder = r"D:\RedditVideoMakerBot\results\confession"

    # Loop through the files in the folder
    for filename in os.listdir(reel_folder):
        if filename.endswith(".mp4"):
            # Construct the full file path
            file_path = os.path.join(reel_folder, filename)

            try:
                # Upload the reel
                bot.upload_video(file_path, caption=" Follow if you are not GAY!! #confession #mentalhealth #selflove #rawandreal #reelitreal #instareels #instareelsvideo #reelsvideo #mentalhealthmatters #selfdiscovery")
                print(f"Uploaded reel: {filename}")
            except Exception as e:
                print(f"Failed to upload {filename}: {e}")

if __name__ == "__main__":
    main()
