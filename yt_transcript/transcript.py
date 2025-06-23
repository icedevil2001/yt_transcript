import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

def get_video_id(url):
    if "youtube.com" in url:
        return url.replace('\\','').split("v=")[1].split("&")[0]
    elif "youtu.be" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        raise RuntimeError(f"Transcript not available: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while fetching the transcript: {e}")
    


def main():
    url = input("Enter YouTube URL: ")
    try:
        video_id = get_video_id(url)
        transcript = get_transcript(video_id)
        for entry in transcript:
            print(f"{entry['start']}: {entry['text']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()