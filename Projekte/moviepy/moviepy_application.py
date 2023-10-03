from moviepy.editor import *

def load_video():
    # loading video
    clip = VideoFileClip("D:/Desktop/A22.avi")
    print("duration: "+str(clip.duration)+"s")

    # getting subclip as video is large
    clip = clip.subclip(0, 10) # Zeitspanne eingeben
    return clip

def rotate_video(degree):
    clip = load_video()
    clip = clip.rotate(int(degree))
    return clip

def show_video(clip):
    clip.preview(fps = 20)

def save_video(clip, name):
    clip.write_videofile(name)

if __name__ == "__main__":
    print("start")
    video = rotate_video(90)
    save_video(video, "D:/Desktop/A22_copy.mp4")
    show_video(video)
    print("end")

