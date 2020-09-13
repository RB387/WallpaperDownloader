import pytest

from downloader.config import get_config
from lib.storage import ListStorage


@pytest.fixture
def year_config():
    return get_config(year=2019, month=None, resolution='800x600')


@pytest.fixture
def month_config():
    return get_config(year=2020, month=3, resolution='800x600')


@pytest.fixture(scope='module')
def storage():
    return ListStorage()
