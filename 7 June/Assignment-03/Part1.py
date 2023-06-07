# Q1).
import random
import string

with open("random_strings.txt", "w") as file:
    for _ in range(1000):
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        file.write(random_string + "\n")
#................................................................................................

# Q2).
import random
import string

file_size = 5 * 1024 * 1024  # 5 MB
line_size = 100  # Average line size in bytes

with open("random_strings_large.txt", "w") as file:
    while file.tell() < file_size:
        random_string = ''.join(random.choice(string.ascii_letters) for _ in range(line_size - 1))
        file.write(random_string + "\n")
#................................................................................................

# Q3).
import random
import string

file_size = 5 * 1024 * 1024  # 5 MB
line_size = 100  # Average line size in bytes

for i in range(1, 11):
    with open(f"random_strings_{i}.txt", "w") as file:
        while file.tell() < file_size:
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(line_size - 1))
            file.write(random_string + "\n")

            
#................................................................................................

# Q4).
import random
import string

file_sizes = [1, 2, 3, 4, 5]  # File sizes in GB
line_size = 100  # Average line size in bytes

for size in file_sizes:
    file_size = size * 1024 * 1024 * 1024  # Convert GB to bytes
    with open(f"random_strings_{size}GB.txt", "w") as file:
        while file.tell() < file_size:
            random_string = ''.join(random.choice(string.ascii_letters) for _ in range(line_size - 1))
            file.write(random_string + "\n")

#................................................................................................

# Q5).
import os

for size in file_sizes:
    filename = f"random_strings_{size}GB.txt"
    with open(filename, "r") as file:
        content = file.read().upper()
    with open(filename, "w") as file:
        file.write(content)
        
        
#................................................................................................

# Q6).
import os
import threading

file_sizes = [1, 2, 3, 4, 5]  # File sizes in GB
line_size = 100  # Average line size in bytes

def convert_to_uppercase(filename):
    with open(filename, "r") as file:
        content = file.read().upper()
    with open(filename, "w") as file:
        file.write(content)

threads = []

for size in file_sizes:
    filename = f"random_strings_{size}GB.txt"
    thread = threading.Thread(target=convert_to_uppercase, args=(filename,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

#................................................................................................

# Q7).
from google_images_download import google_images_download

def download_images(keyword, limit):
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": keyword,
        "limit": limit,
        "print_urls": True
    }
    paths = response.download(arguments)
    return paths[0][keyword]  # Use [0][keyword] to access the list of downloaded paths

keyword = "cat"  # Keyword to search for
limit = 10  # Number of images to download

image_paths = download_images(keyword, limit)
print("Downloaded images:")
for path in image_paths:
    print(path)


#................................................................................................

# Q8).
from pytube import YouTube

def download_videos(keyword, limit):
    query = keyword + " video"
    search_results = YouTube.search(query, limit=limit)
    video_urls = [result['url'] for result in search_results]
    
    for url in video_urls:
        try:
            video = YouTube(url)
            video.streams.get_highest_resolution().download()
            print("Downloaded:", video.title)
        except Exception as e:
            print("Error occurred while downloading:", e)

keyword = "Machine Learning"  # Keyword to search for
limit = 10  # Number of videos to download

download_videos(keyword, limit)


#................................................................................................

# Q9).
from moviepy.editor import VideoFileClip

def convert_videos_to_audio(video_files):
    for file in video_files:
        try:
            video = VideoFileClip(file)
            audio = video.audio
            audio_file = file.replace(".mp4", ".mp3")  # Change the extension to .mp3
            audio.write_audiofile(audio_file)
            print("Converted to audio:", audio_file)
        except Exception as e:
            print("Error occurred while converting to audio:", e)

video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Replace with the actual video files

convert_videos_to_audio(video_files)


#................................................................................................

