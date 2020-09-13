import asyncio

import pytest
from types import MethodType

from downloader.steps.crawl_step import CrawlStep
from downloader.steps.download_images_step import DownloadImagesStep
from tests.test_integration.patches import patched_save_image


@pytest.mark.integration
@pytest.mark.asyncio
async def test_crawl_step(year_config, storage):
    step = CrawlStep(config=year_config, storage=storage)

    tasks = await step.get_workers_tasks()
    await asyncio.gather(*tasks)

    assert len(storage.storage) == 12


@pytest.mark.integration
@pytest.mark.asyncio
async def test_download_images_step(month_config, storage):
    step = DownloadImagesStep(config=month_config, storage=storage)
    step._save_image = MethodType(patched_save_image, step)

    tasks = await step.get_workers_tasks()
    await asyncio.gather(*tasks)

    assert step.counter >= 250
