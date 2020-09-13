import pytest

from lib.storage import ListStorage


@pytest.mark.unit
@pytest.mark.parametrize(
    "data",
    (([1, 2, 3, 4, 5]),),
)
@pytest.mark.asyncio
async def test_list_storage(data):
    storage = ListStorage()

    for element in data:
        await storage.add(element)

    assert await storage.get() == data
