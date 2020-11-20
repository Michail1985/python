from random import choice #randint

# диапазон бочонков
c = [c for c in range(1, 91)]

# перебор случайных неповторяющихся бочонков из диапазон
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 90:
            x = choice(c)
            c.remove(x)
            self.a += 1
            return x
        else:
            raise StopIteration


class Card:

    def __init__(self):
        self.content = self._get_content()

    def _get_content(self):
        content = {}
        a = True

            # генерируем содержимое карточки до тех пор, пока
            # карточка не пройдет проверку на корректность
        while a:
            #   b += 1
            c = [c for c in range(1, 91)]
            for row in range(1, 4):
                col = [col for col in range(1, 10)]
                i = 0
                col_list = []

                while True:
                    col_1 = choice(col)

                    if col_1 == 9:
                        number = [number for number in range(80, 91)]
                    elif col_1 == 1:
                        number = [number for number in range(1, 10)]
                    else:
                        number = [number for number in range(10 * (col_1 - 1), 10 * col_1)]
                    number_1 = choice(number)

                    if number_1 in c:
                        c.remove(number_1)
                        col_list.append(number_1)
                        col_list.sort()
                        col.remove(col_1)
                        i += 1
                    else:
                        continue

                    if i == 5:
                        break

                new_row = []
                for count_1 in range(1, 10):
                    if col_list == []:
                        new_row.append('  ')
                    else:
                        for count in col_list:
                            if count < 10 and count_1 == 1:
                                new_row.append(str(count) + ' ')
                                col_list.remove(count)
                                break
                            else:
                                if count_1 == count // 10 + 1:
                                    new_row.append(str(count))
                                    col_list.remove(count)
                                    break
                                elif count == 90 and count_1 == 9:
                                    new_row.append(str(count))
                                    col_list.remove(count)
                                else:
                                    new_row.append('  ')
                                    break
                    content[row] = new_row

            cols = [[] for _ in range(9)]
            for rows in content:
                x = content[rows]
                count = 1
                for pos in x:
                    cols[count - 1].append(pos)
                    count += 1

            for col in cols:
                if col.count('  ') != 3:
                    a = False
                else:
                    a = True
                    break
        return content

    # отрисовка карточки
    def draw(self, title):
        print(title.center(26, '-'))
        for rows in self.content:
            x = self.content[rows]
            print(' '.join(map(str, x)))
        print('-'.center(26, '-'))

    # зачеркивание номера в карточке
    def cross_out_number(self, number):
        for row in self.content:
            x = self.content[row]
            row_numbers = []
            for value in x:
                try:
                    value = int(value)
                except ValueError:
                    if value != '--':
                        value = '  '
                finally:
                    row_numbers.append(value)
            self.content[row] = row_numbers
            for n, i in enumerate(row_numbers):
                if i == number:
                    row_numbers[n] = '--'
                    return True
            if row_numbers[0] != '  ' and row_numbers[0] != '--':
                row_numbers[0] = str(row_numbers[0]) + ' '
        return False

class Player:

    def __init__(self, name, card=None, is_pc=False):
        self.name = name
        self._card = card
        self.is_pc = is_pc
        print(f'{self.name}', '(Компьютер)' if self.is_pc else '(Человек)', 'сел за стол.')

    def get_card(self, card):
        self._card = card

    def show_card(self):
        self._card.draw(self.name)

    def check_card(self, barrel):
        x = self._card.cross_out_number(barrel)
        return x

class Game:

    def __init__(self, players):
        self._players = players
        self._bag_of_barrels = iter(MyNumbers())
        self._cards = cards_generator(100)

    def get_barrel(self):
        return next(self._bag_of_barrels)

    def _give_cards_to_players(self):
        for player in self._players:
            player.get_card(next(self._cards))

    def start(self):
        input('Чтобы раздать карточки игрокам нажмите "Enter".')
        a = 0
        b = 0
        self._give_cards_to_players()
        stop = False
        while not stop:
            for player in self._players:
                player.show_card()
            barrel = self.get_barrel()
            print(f'Выпал бочонок с номером {barrel}!\nОсталось {len(c)} бочонков.')
            for player in self._players:
                if not player.is_pc:
                    choices = input(f'{player.name} - Зачеркнуть номер на карточке? y/n ')
                    check = player.check_card(barrel)
                    if choices == 'n' and check is False:
                        print('Игра продолжается!')
                    elif choices != 'n' and check is True:
                        a += 1
                        print(a)
                        if a == 15:
                            print(f'Стоп игра! Игрок {player.name} выйграл!')
                            stop = True
                            break
                        else:
                            print('Игра продолжается!')
                    else:
                        print(f'Стоп игра! Игрок {player.name} проиграл!')
                        stop = True
                        break
                else:
                    check_pk = player.check_card(barrel)
                    if check_pk is True:
                        b += 1
                        if b == 15:
                            print(f'Стоп игра! Компьютер выйграл!')
                            stop = True
                            break


def cards_generator(num_of_cards):
    while num_of_cards > 0:
        num_of_cards -= 1
        yield Card()

card = Card()
card.draw('Игра лото!')

while True:
    you_name = input('Введите имя: ')
    if you_name != '':
        player = Player(you_name)
        pc = Player("PC", is_pc=True)
        players = [player, pc]
        break
    else:
        print('Имя не указано!')

game = Game(players)
game.start()