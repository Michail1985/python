from time import sleep
try:
    class TrafficLight:
        __collor = ['Красный', 'Желтый', 'Зеленый']

        def running(self):
            i = 0
            while i in range(0, 4):
                print(TrafficLight.__collor[i])
                if i == 0 and TrafficLight.__collor[i] == 'Красный':
                    sleep(7)
                elif i == 1 and TrafficLight.__collor[i] == 'Желтый':
                    sleep(1)
                elif i == 2 and TrafficLight.__collor[i] == 'Зеленый':
                    sleep(6)
                    i = -1
                else:
                    print('Процесс завершен! Сбой порядка режимов.')
                    break
                i += 1
    t = TrafficLight()
    t.running()
except IndexError:
    print('Скрипт завершен!')