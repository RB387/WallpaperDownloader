import logging
from typing import Optional as Opt
from yarl import URL

from aiohttp import ClientSession, ClientResponse


async def request(session: ClientSession, url: URL) -> Opt[ClientResponse]:
    """
    Function used to filter successful requests and log failed

    :param session: aiohttp session that will send request
    :param url: request url
    :return: aiohttp ClientResponse if response status is 200
    """
    response = await session.get(url, verify_ssl=False)

    if response.status == 200:
        return response

    logging.error(f"Got {response.status} at url {url}")
    return None
