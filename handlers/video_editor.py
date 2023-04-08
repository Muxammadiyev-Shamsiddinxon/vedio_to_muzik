import moviepy.editor
from moviepy.editor import VideoFileClip


def muzik_ajrat(id):
    video = moviepy.editor.VideoFileClip(f"video/{id}.mp4")
    muzik = video.audio
    muzik.write_audiofile(f"video/{id}.mp3")
    video.close()
    video.close()




def video_cut(id, time1,time2):
    videoclip = VideoFileClip(f"video/{id}.mp4")
    video_cut = videoclip.subclip(t_start=(0,0,time1),t_end=(0, 0,time2))
    video_cut.write_videofile(f"video/video{id}.mp4")
    videoclip.close()

