# from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress
 

def download_audio(url, output, quality='highest'):
    """
    Download audio from a YouTube video.
    
    :param url: YouTube video URL
    :return: None
    """
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Downloading audio from: {yt.title}")
        # print(dir(yt.streams))ll
        if quality == 'highest':
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        elif quality == 'lowest':
            audio_stream = yt.streams.filter(only_audio=True).order_by('abr').asc().first()
        else:
            raise ValueError("Resource must be 'highest' or 'lowest'.")
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Audio stream found: {audio_stream}")
        if audio_stream:
            audio_stream.download(output_path=output)
            print(f"Audio downloaded successfully from {url}")
        else:
            raise RuntimeError("No audio stream available for this video.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while downloading audio: {e}")
# url = "url"
 
# yt = YouTube(url, on_progress_callback = on_progress)
# print(yt.title)
 
# ys = yt.streams.get_highest_resolution()
# ys.download()


# def download_audio(video_id, output_file):
#     try:
#         yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
#         audio_stream = yt.streams.filter(only_audio=True).first()
#         if audio_stream:
#             audio_stream.download(filename=output_file)
#             print(f"Audio downloaded to {output_file}")
#         else:
#             raise RuntimeError("No audio stream available for this video.")
#     except Exception as e:
#         raise RuntimeError(f"An error occurred while downloading audio: {e}")
    

#  from pytube import YouTube
#  YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
#  yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()