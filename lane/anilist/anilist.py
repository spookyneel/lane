import aiohttp
from attrify import Attrify as Atr
from . import queries


class AniList:
    def __init__(
            self,
            base_url: str = 'https://graphql.anilist.co'
    ) -> None:
        self.base_url = base_url

    async def request(self, params: dict = None):
        async with aiohttp.ClientSession() as ses:
            async with ses.post(
                    self.base_url,
                    json=params
            ) as resp:
                return await resp.json()

    async def anime(self, query: str) -> Atr:
        return Atr(await self.request({'query': queries.anime, 'variables': {'search': query}})).data.Media

    async def manga(self, query: str) -> Atr:
        return Atr(await self.request({'query': queries.manga, 'variables': {'search': query}})).data.Media

    async def character(self, query: str) -> Atr:
        return Atr(await self.request({'query': queries.character, 'variables': {'search': query}})).data.Character

    async def airing(self, query: str) -> Atr:
        return Atr(await self.request({'query': queries.airing, 'variables': {'search': query}})).data.Media
