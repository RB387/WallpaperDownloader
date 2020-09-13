import pytest

from lib.storage import ListStorage
from downloader.steps.crawl_step import CrawlStep


class TestCrawlStep:
    @pytest.mark.unit
    @pytest.mark.parametrize(
        'config, month, expected',
        (
            (
                {'year': 2020},
                2,
                'https://www.smashingmagazine.com/2020/01/desktop-wallpaper-calendars-february-2020/'
            ),
            (
                {'year': 2020},
                1,
                'https://www.smashingmagazine.com/2019/12/desktop-wallpaper-calendars-january-2020/'
            ),
        )
    )
    def test_get_url_for_month(self, config, month, expected):
        step = CrawlStep(config=config, storage=ListStorage())
        assert step._get_url_for_month(month) == expected

    @pytest.mark.unit
    @pytest.mark.parametrize(
        'config, expected',
        (
            (
                {'year': 2020, 'month': 2},
                ['https://www.smashingmagazine.com/2020/01/desktop-wallpaper-calendars-february-2020/']
            ),
            (
                {'year': 2020},
                [
                    'https://www.smashingmagazine.com/2019/12/desktop-wallpaper-calendars-january-2020/',
                    'https://www.smashingmagazine.com/2020/01/desktop-wallpaper-calendars-february-2020/',
                    'https://www.smashingmagazine.com/2020/02/desktop-wallpaper-calendars-march-2020/',
                    'https://www.smashingmagazine.com/2020/03/desktop-wallpaper-calendars-april-2020/',
                    'https://www.smashingmagazine.com/2020/04/desktop-wallpaper-calendars-may-2020/',
                    'https://www.smashingmagazine.com/2020/05/desktop-wallpaper-calendars-june-2020/',
                    'https://www.smashingmagazine.com/2020/06/desktop-wallpaper-calendars-july-2020/',
                    'https://www.smashingmagazine.com/2020/07/desktop-wallpaper-calendars-august-2020/',
                    'https://www.smashingmagazine.com/2020/08/desktop-wallpaper-calendars-september-2020/',
                    'https://www.smashingmagazine.com/2020/09/desktop-wallpaper-calendars-october-2020/',
                    'https://www.smashingmagazine.com/2020/10/desktop-wallpaper-calendars-november-2020/',
                    'https://www.smashingmagazine.com/2020/11/desktop-wallpaper-calendars-december-2020/'
                ]
            ),
        )
    )
    def test_get_urls(self, config, expected):
        step = CrawlStep(config=config, storage=ListStorage())
        assert list(step._get_urls()) == expected
