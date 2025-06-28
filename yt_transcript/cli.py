#!/usr/bin/env python
import sys
import click
from pathlib import Path
from yt_transcript.transcript import get_video_id, get_transcript
import importlib.metadata
from loguru import logger

# from yt_transcript.audio import download_audio

version = importlib.metadata.version("yt-transcript")
print(f"Using yt-transcript version: {version}")


CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    show_defaults = True,
)


@click.group()
def cli(context_settings=CONTEXT_SETTINGS):
    """Command line interface for yt-transcript"""
    logger.info("yt-transcript CLI started")
    pass

@cli.command('transcript')
@click.argument("url")
@click.option("--output", "-o", type=click.File("w"), default="-", required=False)
@click.option("--timestamp", "-t", is_flag=True, default=False)
@click.version_option(version=version)
def yt_transcript_main(url, output, timestamp):
    """ Get the transcript of a YouTube video and output it to a file or stdout """
    try:
        video_id = get_video_id(url)
        logger.info(f"Transcript for video ID: {video_id}")
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
        logger.success("Transcript written successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")


@cli.command()
@click.argument("url")
@click.option("--output", "-o", type=click.Path(), default="audio.mp3", required=False)
@click.option("--quality", "-q", type=click.Choice(['highest', 'lowest'], case_sensitive=False), default='highest', required=False)
def download_audio_cmd(url, output, quality):
    """ Download the audio of a YouTube video """
    try:
        video_id = get_video_id(url)
        logger.info(f"Downloading audio for video ID: {video_id}")
        # Import here to avoid import error if module doesn't exist
        from yt_transcript.audio import download_audio
        download_audio(url, output, quality)
        logger.success(f"Audio downloaded to {output}")
    except Exception as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    cli()