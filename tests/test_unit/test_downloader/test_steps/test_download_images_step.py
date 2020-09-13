import pytest

from downloader.steps.download_images_step import DownloadImagesStep
from lib.storage import ListStorage


class TestDownloadImagesStep:
    @pytest.mark.unit
    @pytest.mark.parametrize(
        "config, page_content, expected",
        (
            (
                {"resolution": "1920x1080", "files_path": None},
                """
                    <ul>
                        <li><a href="url1">800x600</a></li>
                        <li><a href="url2">1280x720</a></li>
                        <li><a href="url3">1920x1080</a></li>
                        <li><a href="url4">Ultra Super 40K</a></li>
                    </ul>
                    <ul>
                        <li><a href="url5">800x600</a></li>
                        <li><a href="url6">1280x720</a></li>
                        <li><a href="url7">Ultra Super 40K</a></li>
                    </ul>
                    <li><a href="url8">1920x1080</a></li>
                    <ul>
                        <li><a href="url9">800x600</a></li>
                        <li><a href="url10">1920x1080</a></li>
                    </ul>
                """,
                ["url3", "url10"],
            ),
            (
                {"resolution": "800x600", "files_path": None},
                """
                    <ul>
                        <li><a href="url2">1280x720</a></li>
                        <li><a href="url3">1920x1080</a></li>
                        <li><a href="url4">Ultra Super 40K</a></li>
                    </ul>
                    <ul>
                        <li><a href="url6">1280x720</a></li>
                        <li><a href="url7">Ultra Super 40K</a></li>
                    </ul>
                    <li><a href="url8">800x600</a></li>
                    <ul>
                        <li><a href="url10">1920x1080</a></li>
                    </ul>
                """,
                [],
            ),
        ),
    )
    def test_extract_image_urls(self, config, page_content, expected):
        step = DownloadImagesStep(config=config, storage=ListStorage())
        result = step._extract_image_urls(page_content)
        assert result == expected
