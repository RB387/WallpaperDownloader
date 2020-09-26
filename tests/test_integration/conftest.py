import pytest

from downloader.config import get_config
from lib.storage import ListStorage


@pytest.fixture
def config():
    return get_config(year=2019, month=None, resolution="800x600")


@pytest.fixture(scope="module")
def storage():
    return ListStorage()
