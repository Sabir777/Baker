import asyncio

class Baker:
    def __init__(self, t_oven, lst_dt):
        self.flag_oven = False
        self.t_oven = t_oven
        self.lst_dt = lst_dt

    async def oven(self, delay):
        await asyncio.sleep(delay)
        self.flag_oven = True
        print("Духовка разогрелась")

    async def cake(self, number, delay1, delay2):
        await asyncio.sleep(delay1)
        print(f'Тесто для торта №{number} готово')
        while not self.flag_oven:
            await asyncio.sleep(0)
        await asyncio.sleep(delay2)
        print(f'Торт №{number} готов!!!')

    async def main(self):
        tasks = [asyncio.create_task(self.oven(self.t_oven))]  # создаю список задач
        tasks += [asyncio.create_task(self.cake(n, t1, t2)) for n, t1, t2 in self.lst_dt]
        for task in tasks:
            await task

    def run(self):
        asyncio.run(self.main())


lst_task = [(1, 1, 3), (2, 2, 3), (3, 3, 3)]
baker = Baker(3, lst_task)
baker.run()
