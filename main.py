#!/usr/env/bin python3
import sys
import click
from pathlib import Path
from yt_transcript.transcript import get_video_id, get_transcript
import importlib.metadata


version = importlib.metadata.version("yt-transcript")

@click.command(context_settings=dict(help_option_names=["-h", "--help"], ignore_unknown_options=True, show_default=True))
@click.argument("url")
@click.option("--output", "-o", type=click.File("w"), default="-", required=False)
@click.option("--timestamp", "-t", is_flag=True, default=False)
@click.version_option(version=version)
def main(url, output, timestamp):
    """ Get the transcript of a YouTube video and output it to a file or stdout """
    try:
        video_id = get_video_id(url)
        transcript = get_transcript(video_id)
        if output.name != "<stdout>":
            sys.stdout = output
        if timestamp:
            text = ""
            for entry in transcript:
                text += (
                    f"{entry['start']}: {str(entry['text'])}".replace('\n', ' ')) + "\n"
        else:
            text = ''.join([str(x['text']).replace('\n', ' ') for x in transcript])
            text = text.replace('\n', ' ').replace('.', '. ')
        output.write(text)
    except Exception as e:
        print(f"Error: {e}")
        

if __name__ == "__main__":
    main()