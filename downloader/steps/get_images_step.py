import asyncio
from os.path import join
from typing import List
from yarl import URL

import aiohttp
import aiofiles
from lxml import html
from aiohttp import ClientResponse

from lib.pipeline_director import AbstractPipelineStep
from lib.request import request
from lib.storage import AbstractStorage


class GetImagesStep(AbstractPipelineStep):
    """
        Pipeline step that extracts images urls and downloads
    """
    def __init__(self, storage: AbstractStorage, config: dict):
        """
        :param storage: Storage where contains crawled results from previous step
        :param config: Dictionary that contains resolution and files_path values
        """
        self.storage = storage
        self.resolution = config['resolution']
        self.files_path = config['files_path']

    async def get_workers_tasks(self) -> List[asyncio.Task]:
        """
        :return: AsyncIO Tasks that downloads images from crawled pages
        """
        worker_tasks = []
        for page_content in await self.storage.get():
            images_urls = self._extract_image_urls(page_content)
            for image_url in images_urls:
                worker_tasks.append(
                    asyncio.create_task(
                        self._download_image(URL(image_url))
                    )
                )
        return worker_tasks

    def _extract_image_urls(self, page_content: str) -> List[str]:
        """
        Extract images urls from html page
        :param page_content: string with html
        :return: list of images urls
        """
        etree = html.fromstring(page_content)
        images_urls = etree.xpath(f".//ul/li/a[contains(., '{self.resolution}')]/@href")

        return images_urls

    async def _download_image(self, image_url: URL):
        async with aiohttp.ClientSession() as session:
            response = await request(session, image_url)
            if response is not None:
                await self._save_image(response)

    async def _save_image(self, response: ClientResponse):
        async with aiofiles.open(join(self.files_path, response.url.parts[-1]), mode='wb') as f:
            await f.write(await response.read())

