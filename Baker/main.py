import asyncio
import time

class Baker:
    def __init__(self, t_oven, dict_cake):
        self.flag_oven = False  # духовка разогрелась
        self.t_oven = t_oven  # время разогрева
        self.dict_cake = dict_cake  # задачи: торты - словарь
        self.lst_cake = []  # имена тортов для которых готово тесто

# духовка нагревается
    async def oven(self, delay):
        await asyncio.sleep(delay)
        self.flag_oven = True
        print("Духовка разогрелась")

# Готовится тесто
    async def dough_cake(self, cake, t_dough):
        await asyncio.sleep(t_dough)
        print(f'Тесто для {cake} готово')
        self.lst_cake.append(cake)

# Пекется торт        
    async def oven_cake(self, cake):
        await asyncio.sleep(3)  # время выпекания
        print(f'{cake} готов!!!')

# Цикл планирования событий
    async def loop(self):
        while not self.flag_oven:
            await asyncio.sleep(0.05)
        for _ in range(3):
            while not self.lst_cake:
                await asyncio.sleep(0.05)
            await self.oven_cake(self.lst_cake.pop(0))
            
# Запускаю цикл программы            
    async def main(self):
        task_loop = asyncio.create_task(self.loop())  # задача: контролирующий цикл
        task_oven = asyncio.create_task(self.oven(self.t_oven)) # задача: нагрев духовки
        tasks = [asyncio.create_task(self.dough_cake(k, t)) for k, t in self.dict_cake.items()]  # готовка теста для тортов
        await task_loop  # запускаю контролирущий цикл, остальные задачи тоже запустятся

    def run(self):
        asyncio.run(self.main())


start = time.time()
data_cake = {'торт1': 2, 'торт2': 3, 'торт3': 2}
baker = Baker(t_oven= 3, dict_cake=data_cake)
baker.run()
print('*******')
print(time.time() - start)
