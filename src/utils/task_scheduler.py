import asyncio
import nest_asyncio

nest_asyncio.apply()

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def schedule(self,coro,*args):
        self.tasks.append(coro(*args))
        
    async def run(self):
        await asyncio.gather(*self.tasks)
async def example_task(name,duration):
    print(f"Task {name} started")
    await asyncio.sleep(duration)
    print(f"Task {name} completed after {duration} seconds")

async def main():
    scheduler = TaskScheduler()
    scheduler.schedule(example_task,"A",2)
    scheduler.schedule(example_task,"B",3)
    scheduler.schedule(example_task,"C",1)
    
    await scheduler.run()
asyncio.run(main())