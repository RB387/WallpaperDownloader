import asyncio
import os
import logging
import click

from downloader.constants import LOG_FORMAT
from downloader.pipeline_director import WallpaperDownloaderPipelineDirector
from downloader.config import get_config


@click.option("--year", help="Year of posts with wallpaper", type=int)
@click.option("--month", help="Month of posts with wallpaper", type=int)
@click.option(
    "--resolution", default="1920x1080", help="Resolution of wallpapers", type=str
)
@click.command()
def main(year, month, resolution):
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    logging.info("Started main execution")

    config = get_config(year=year, month=month, resolution=resolution)
    _start_pipeline(config)

    logging.info("Finished main execution")


def _start_pipeline(config):
    _create_output_folder(config["files_path"])
    director = WallpaperDownloaderPipelineDirector(config)

    asyncio.run(director.start_pipeline())


def _create_output_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        logging.info(f"Successfully created directory at {path}")


if __name__ == "__main__":
    main()
