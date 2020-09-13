from aiohttp.client_exceptions import ClientResponse


async def patched_save_image(self, response: ClientResponse):
    if hasattr(self, "counter"):
        self.counter += 1
    else:
        self.counter = 1
