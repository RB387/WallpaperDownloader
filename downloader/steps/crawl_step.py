import asyncio
from datetime import date, timedelta
from calendar import month_name
from typing import List, Iterable

import aiohttp

from lib.pipeline_director import AbstractPipelineStep
from lib.request import request
from lib.storage import AbstractStorage
from downloader.constants import URL_TEMPLATE


class CrawlStep(AbstractPipelineStep):
    """
    Pipeline step that downloads all html pages with wallpapers

    If year is not parametrized, then current will be used
    If month is not parametrized, then all months of year will be used
    """
    def __init__(self, storage: AbstractStorage, config: dict):
        """
        :param storage: Storage where to save crawled pages
        :param config: Dictionary that contains key and month values for parametrization
        """
        self.storage = storage
        self.year = config.get('year') or date.today().year
        self.month = config.get('month')

    async def get_workers_tasks(self) -> List[asyncio.Task]:
        """
        :return: AsyncIO Tasks that crawl required pages
        """
        worker_tasks = []
        for url in self._get_urls():
            worker_tasks.append(
                asyncio.create_task(
                    self._crawl(url)
                )
            )
        return worker_tasks

    def _get_urls(self) -> Iterable[str]:
        """
        If month number is None, then will be downloaded all months
        :return:
        """
        if self.month is None:
            for month_number in range(1, 13):
                yield self._get_url_for_month(month_number)
        else:
            yield self._get_url_for_month(self.month)

    def _get_url_for_month(self, month: int) -> str:
        """
        Generates url with wallpapers for chosen month and year

        :param month: Required month
        :return: string that contains url for crawling
        """
        current_date = date(day=1, month=month, year=self.year)
        post_date = current_date - timedelta(1)
        return URL_TEMPLATE.format(
            post_date.year,
            post_date.month,
            month_name[month].lower(),
            self.year,
        )

    async def _crawl(self, url: str):
        """
        Send request with received url and if response is successful,
        then save content to storage
        :param url: url for request
        :return: None
        """
        async with aiohttp.ClientSession() as session:
            response = await request(session, url)
            if response is not None:
                await self.storage.add(await response.text())
