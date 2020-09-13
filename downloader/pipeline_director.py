from typing import Tuple

from lib.pipeline_director import AbstractPipelineDirector, AbstractPipelineStep
from lib.storage import ListStorage
from downloader.steps.crawl_step import CrawlStep
from downloader.steps.download_images_step import DownloadImagesStep


class WallpaperDownloaderPipelineDirector(AbstractPipelineDirector):
    def _get_pipeline_steps(self) -> Tuple[AbstractPipelineStep]:
        storage = ListStorage()
        return (
            CrawlStep(
                storage=storage,
                config=self.config,
            ),
            DownloadImagesStep(
                storage=storage,
                config=self.config,
            ),
        )
