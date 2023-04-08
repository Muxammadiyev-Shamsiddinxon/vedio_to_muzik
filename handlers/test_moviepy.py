import moviepy
from moviepy.editor import *


#audioclip = AudioFileClip("a.mp3")
video1 = VideoFileClip("video2/1.mp4")
video2 = VideoFileClip("video2/2.mp4")

video3 = concatenate_videoclips([video1,video2])
video3.write_videofile("video2/3.mp4")







