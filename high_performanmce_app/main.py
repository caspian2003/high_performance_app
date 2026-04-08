import asyncio
from src.processor import Processor
from src.monitor import Monitor

async def main():
    monitor = Monitor()
    processor = Processor()

    data = ["file1", "file2", "file3", "file4"]

    results = await processor.process_data(data)

    for r in results:
        print(r)

    monitor.report()

if __name__ == "__main__":
    asyncio.run(main())