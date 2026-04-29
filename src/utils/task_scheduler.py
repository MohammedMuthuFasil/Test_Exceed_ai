import asyncio
from collections.abc import Awaitable, Callable


class TaskScheduler:
    def __init__(self):
        self.tasks: list[Awaitable[object]] = []

    def schedule(self, coro_fn: Callable[..., Awaitable[object]], *args: object) -> None:
        self.tasks.append(coro_fn(*args))

    async def run(self) -> None:
        await asyncio.gather(*self.tasks)


async def example_task(name: str, duration: float) -> None:
    print(f"Task {name} started")
    await asyncio.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")


async def main() -> None:
    scheduler = TaskScheduler()
    scheduler.schedule(example_task, "A", 2)
    scheduler.schedule(example_task, "B", 3)
    scheduler.schedule(example_task, "C", 1)

    await scheduler.run()


if __name__ == "__main__":
    asyncio.run(main())