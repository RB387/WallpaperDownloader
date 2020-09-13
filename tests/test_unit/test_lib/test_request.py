from yarl import URL

import pytest
from aiohttp import ClientSession
from lib.request import request


@pytest.mark.unit
@pytest.mark.parametrize(
    'url, expected',
    (
            (
                URL('https://www.test.com/'),
                'PASS TEST'
            ),
            (
                URL('https://www.testerror.com/'),
                None
            )
    )
)
@pytest.mark.vcr(vcr_record=None)
@pytest.mark.asyncio
async def test_request(url, expected):
    async with ClientSession() as session:
        result = await request(session, url)

        if result is not None:
            assert await result.text() == expected
        else:
            assert result == expected
