from abc import ABC, abstractmethod
import asyncio

class ProcessingStrategy(ABC):
    @abstractmethod
    async def process(self, data):
        pass

class FastStrategy(ProcessingStrategy):
    async def process(self, data):
        await asyncio.sleep(0.1)
        return f"Fast processed {data}"

class SlowStrategy(ProcessingStrategy):
    async def process(self, data):
        await asyncio.sleep(1)
        return f"Slow processed {data}"