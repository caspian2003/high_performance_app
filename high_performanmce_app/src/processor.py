import asyncio
from functools import lru_cache
from src.strategy import FastStrategy

class Processor:
    def __init__(self):
        self.strategy = FastStrategy()

    @lru_cache(maxsize=100)
    def cached_task(self, data):
        return f"Cached {data}"

    async def process_data(self, items):
        tasks = [self.strategy.process(item) for item in items]
        return await asyncio.gather(*tasks)