import random

class event_1:
    '''Class of realizing of the first simple event.'''
    events_affect = {'Крысы съели запасы в амбаре.': [-100, 'еды'],
                    'Наступила засуха. Урожайность упала.': [-100, 'еды'],
                    'Благоприятная погода на протяжении всего года. Урожайность выросла.': [100, 'еды'],
                    'Нашли затерянный корбаль у берега с сокровищами.': [200, 'золота'],
                    'В государстве началась эпидемия чумы.': [-100, 'рабочих'],
                    'Произошло сильное наводнение.': [-100, 'еды'],
                    'Произошел сильный пожар на оружейном складе.': [-100, 'золота'],
                    'На торговые корабли напали пираты.': [-100, 'товаров'],
                    'На территории страны нашли богатое месторождение каменного угля.': [200, 'сырья'],
                    'В стране резко выросла рождаемость.': [150, 'рабочих'],
                    'Купцы успешно преодолели кругосветное путешествие.': [200, 'золота']}
    events = []
    for i in events_affect.keys():
        events.append(i)

    king = 'Султан Сулейман-Великолепный'
    year = 1550
    territory = 50000
    soldier = 700
    worker = 2300
    rezidents = worker + soldier
    rich = 1500
    material = 1500
    food = 4000
    products = 1000
    displeasure = 0
    displ = {'янычары': 0, 'рабочие': 0}
    deads = 0
    church = 0

    def __init__(self):
        self.event = random.choice(__class__.events)
        self.affect = __class__.events_affect[self.event][0]
        if self.affect > 0:
            self.get_lost = 'Приобретено:'
        else:
            self.get_lost = 'Потеряно:'
        self.resourse = __class__.events_affect[self.event][1]
        if __class__.year == 1550:
            print('ВЕЛИКАЯ ОСМАНСКАЯ ИМПЕРИЯ'.center(60, '-'))
            print(('Правитель: '+str(__class__.king)).center(60) + '\n'+'Год: '+str(__class__.year) + '\n'+'Территория: '+str(__class__.territory))
            print('-' * 60)
            print('Ресурсы'.ljust(30, ' ') + '|' + '\n'+('Золото: '+str(__class__.rich)).ljust(30, ' ') + '|')
            print('Еда: '+str(__class__.food).ljust(25, ' ') + '|' + ('Жители: '+str(__class__.rezidents)).rjust(20, ' '))
            print(('Сырье: '+str(__class__.material).ljust(23, ' ') + '|' + ('Янычары: '+str(__class__.soldier)).rjust(20, ' ')))
            print(('Товары: '+str(__class__.products).ljust(22, ' ') + '|' + ('Рабочие: '+str(__class__.worker)).rjust(21, ' ')))
            print(('Уровень смуты: '+str(__class__.displeasure)).ljust(30, ' ') + '|')
            print('-' * 60)
            print()
        f = change_resourse(self.resourse, self.affect)
        print(f"СОБЫТИЕ:\n{self.event} {self.get_lost} {abs(self.affect)} ед. {self.resourse}.")
        k = hard_event()

class change_resourse:
    '''Class of changing values of resources after making a decision in events.'''
    def __init__(self, resourse, affect):
        self.resourse = resourse
        self.affect = affect
        f = __class__.change(self)
    def change(self):
        if self.resourse == 'еды':
            event_1.food += self.affect
        elif self.resourse == 'золота':
            event_1.rich += self.affect
        elif self.resourse == 'сырья':
            event_1.material += self.affect
        elif self.resourse == 'смуты':
            event_1.displeasure += self.affect
            if event_1.displeasure < 0:
                event_1.displeasure = 0
        elif self.resourse == 'товаров':
            event_1.products += self.affect
        elif self.resourse == 'рабочих':
            event_1.worker += self.affect
        elif self.resourse == 'территорий':
            event_1.territory += self.affect
        elif self.resourse == 'ресурсов':
            event_1.rich += self.affect


class hard_event:
    '''Class of realizing of the second managed event.'''
    events_affect = {'В Румынии торговцы нашли новое сырье - метриал для производства ковров. Привезти в страну?': {'затраты': [-200, 'золота'], 'да': ['Рабочие научились производить новый товар - ковры. Они благодарны.', 400, 'товаров', -100, 'смуты'], 'нет': ['', 0, '', '', '']},
                     'Появилась возможность напасть на соседнее гос-во, чтобы завладеть своими исконными землями.': {'затраты': [-400, 'янычар'], 'да': ['Империя приобрела новые территории.', 600, 'рабочих', 1000, 'территорий'], 'нет': ['Янычары недовольны правителем, который не воспользовался случаем.', 300, 'смуты', '', '']},
                     'Поступило предложение провести реформу, повышающую налоги с рабочих.': {'затраты': [0, 'ресурсов'], 'да': ['Увеличилась казна Османской Империи.', 1000, 'золота', 500, 'смуты'], 'нет': ['Янычары недовольны, что казна пустеет.', 200, 'смуты', '', ''],},
                     'Нашли удобное расположение для нового порта. Начать постройку?': {'затраты': [-800, 'сырья'], 'да': ['Увеличилась торговля с другими странами.', 1000, 'товаров', 500, 'золота'], 'нет': ['Торговцы недовольны, что правитель не развивает экономику.', 300, 'смуты', '', '']},
                     'В стране начали появляться изобретатели. Начать спонсировать?': {'затраты': [-500, 'золота'], 'да': ['Изобретатели создали новейшее удобрение. Урожайность увеличилась.', 700, 'еды', '',''], 'нет': ['Изобретатели начали покидать Османскую Империю.', 300, 'смуты', '', '']},
                     'Один из жителей - Серкан Болат, решил устроить переворот и стать правителем. Янычары просят больше золота для решения вопроса. Заплатить?': {'затраты': [700, 'золота'], 'да': ['Злоумышленник пойман.', -300, 'смуты', '', ''], 'нет': ['Серкан Болат продолжил настраивать население против Султана.', 300, 'смуты', '', '']},
                     'Приехали иностранные послы. Встретить их радушно и устроить пир?': {'затраты': [-1000, 'еды'], 'да': ['Благодаря теплому приему отношения с соседями улучшились. Но жители страны в недоумении.', 1000, 'золота', 150, 'смуты'], 'нет': ['Соседние страны стали неохотно поставлять в Империю ресурсы.', -500, 'сырья', -100, 'золота']}}

    events = []
    for i in events_affect.keys():
        events.append(i)
    def __init__(self):
        self.event = random.choice(__class__.events)
        self.cost = __class__.events_affect[self.event]['затраты'][0]
        self.value = __class__.events_affect[self.event]['затраты'][1]
        self.cost_22 = None
        self.value_22 = None
        if self.cost > 0:
            self.get_lost = 'Будет приобретено:'
        else:
            self.get_lost = 'Будет потрачено:'
        print()
        print('УПРАВЛЯЕМОЕ СОБЫТИЕ:')
        print(f"{self.event} {self.get_lost} {abs(self.cost)} ед. {self.value}.", end=' ')
        self.answer = input().lower()
        while self.answer not in ['да', 'нет']:
            self.answer = input('Введите "Да" или "Нет". ').lower()
        if self.answer == 'да':
            self.result_2 = __class__.events_affect[self.event]['да'][0]
            self.cost_2 = __class__.events_affect[self.event]['да'][1]
            self.value_2 = __class__.events_affect[self.event]['да'][2]
            if __class__.events_affect[self.event]['да'][3] != '':
                self.cost_22 = __class__.events_affect[self.event]['да'][3]
                self.value_22 = __class__.events_affect[self.event]['да'][4]
        else:
            self.result_2 = __class__.events_affect[self.event]['нет'][0]
            self.cost_2 = __class__.events_affect[self.event]['нет'][1]
            self.value_2 = __class__.events_affect[self.event]['нет'][2]
        f = __class__.choice(self)

    def choice(self):
        print('Результат:')
        if __class__.events_affect[self.event][self.answer] == ['', 0, '', '', '']:
            print('Выбор не повлиял на ситуацию в Османской Империи.')
        elif self.answer == 'да':
            f = change_resourse(self.value, self.cost)
            if self.cost_2 < 0:
                print(f"- {self.result_2} Число {self.value_2} уменьшилось на {abs(self.cost_2)} ед.")
            else:
                print(f"- {self.result_2} Число {self.value_2} увеличилось на {abs(self.cost_2)} ед.")
            if self.cost_22 != None and self.cost_22 < 0 :
                print(f"- Число {self.value_22} уменьшилось на {abs(self.cost_22)} ед.")
                f = change_resourse(self.value_22, self.cost_22)
            elif self.cost_22 != None and self.cost_22 > 0:
                print(f"- Число {self.value_22} увеличилось на {abs(self.cost_22)} ед.")
                f = change_resourse(self.value_22, self.cost_22)
            print()
            f = change_resourse(self.value_2, self.cost_2)
        elif self.answer == 'нет':
            if self.cost_2 < 0:
                print(f"- {self.result_2} Число {self.value_2} уменьшилось на {abs(self.cost_2)} ед.")
            else:
                print(f"- {self.result_2} Число {self.value_2} увеличилось на {abs(self.cost_2)} ед.")
            print()
            f = change_resourse(self.value_2, self.cost_2)

        event_1.rezidents = event_1.worker + event_1.soldier
        print('ВЕЛИКАЯ ОСМАНСКАЯ ИМПЕРИЯ'.center(60, '-'))
        print(('Правитель: ' + str(event_1.king)).center(60) + '\n' + 'Год: ' + str(event_1.year) + '\n' + 'Территория: ' + str(event_1.territory))
        print('-' * 60)
        print('Ресурсы'.ljust(30, ' ') + '|' + '\n' + ('Золото: ' + str(event_1.rich)).ljust(30, ' ') + '|')
        print('Еда: ' + str(event_1.food).ljust(25, ' ') + '|' + ('Жители: ' + str(event_1.rezidents)).rjust(20, ' '))
        print(('Сырье: ' + str(event_1.material).ljust(23, ' ') + '|' + ('Янычары: ' + str(event_1.soldier)).rjust(20, ' ')))
        print(('Товары: ' + str(event_1.products).ljust(22, ' ') + '|' + ('Рабочие: ' + str(event_1.worker)).rjust(21, ' ')))
        print(('Уровень смуты: ' + str(event_1.displeasure)).ljust(30, ' ') + '|')
        print('-' * 60)
        print()

        f = management()

class management:

    def __init__(self):
        print('УПРАВЛЕНИЕ РЕСУРСАМИ:')
        self.materials = input(f"Сколько сырья закупить в другом гос-ве для производства товаров? В наличии {event_1.rich} ед. золота. ")
        self.materials = int(__class__.check_input(self, self.materials, event_1.rich))
        event_1.rich -= self.materials
        event_1.material += self.materials

        self.worker_grow = input(f"Сколько рабочих отправить на выращивание еды? Свободных рабочих {event_1.worker} чел. ")
        self.worker_grow = int(__class__.check_input(self, self.worker_grow, event_1.worker))
        if event_1.worker - self.worker_grow > event_1.material:
            event_1.displ['рабочие'] += event_1.worker - self.worker_grow - event_1.material
            event_1.displeasure += event_1.worker - self.worker_grow - event_1.material
            event_1.products += event_1.material
            event_1.material = 0
        else:
            event_1.material -= event_1.worker - self.worker_grow
            event_1.products += event_1.worker - self.worker_grow
        event_1.food += int(self.worker_grow * 1.5)

        if event_1.food < event_1.rezidents:
            event_1.displ['рабочие'] += (event_1.rezidents - event_1.food) // 2
            event_1.displ['янычары'] += (event_1.rezidents - event_1.food) // 2
            event_1.displeasure += event_1.rezidents - event_1.food
            event_1.deads += event_1.rezidents - event_1.food
            event_1.worker -= (event_1.rezidents - event_1.food) // 2
            event_1.soldier -= (event_1.rezidents - event_1.food) // 2
            event_1.rezidents -= event_1.rezidents - event_1.food
            event_1.food = 0
        else:
            event_1.food -= event_1.rezidents

        self.for_sell = input(f"Сколько товаров продать соседнему гос-ву? В наличии {event_1.products} ед. товара. ")
        self.for_sell= int(__class__.check_input(self, self.for_sell, event_1.products))
        event_1.products -= self.for_sell
        event_1.rich += int(self.for_sell * 1.5)
        f = __class__.check_minus()

        self.pay_soldier = input(f"Сколько заплатить янычарам? В наличии {event_1.rich} ед. золота, {event_1.soldier} янычар. ")
        self.pay_soldier = int(__class__.check_input(self, self.pay_soldier, min(event_1.soldier, event_1.rich)))
        if self.pay_soldier < event_1.soldier:
            event_1.displ['янычары'] += event_1.soldier - self.pay_soldier
            event_1.displeasure += event_1.soldier - self.pay_soldier
            event_1.soldier -= (event_1.soldier - self.pay_soldier) // 3
            event_1.rich -= self.pay_soldier
        else:
            event_1.rich -= self.pay_soldier
            self.hire_soldier = input(f"Сколько еще янычар нужно нанять? В наличии {event_1.rich} ед. золота. ")
            self.hire_soldier = int(__class__.check_input(self, self.hire_soldier, event_1.rich))
            if self.hire_soldier != 0:
                event_1.rich -= self.hire_soldier
                event_1.soldier += self.hire_soldier
                event_1.rezidents += self.hire_soldier
        if event_1.food >= 300 and event_1.rich >= 300 and event_1.material >= 300:
            self.build = input(f"Возможно возвести мечеть, потратив еду, золото и сырье по 300 ед. Смута янычар и рабочих уменьшится на 500 ед.\nВ наличии {event_1.food} ед. еды, {event_1.rich} ед. золота, {event_1.material} ед. сырья.\nПосторить? ")
            while self.build not in ['да', 'нет']:
                self.build = input('Введите "Да" или "Нет". ').lower()
            if self.build == 'да':
                event_1.food -= 300
                event_1.rich -= 300
                event_1.material -= 300
                event_1.church += 1
                event_1.displeasure -= 1000
                event_1.displ['рабочие'] -= 500
                event_1.displ['янычары'] -= 500

        f = sumup()

    def check_input(self, value, limit = None):
        while value.isdigit() == False or int(value) > limit:
            value = input('Введите целое, неотрицательное число, соответствующее наличию. ')
        return value

    @staticmethod
    def check_minus():
        if event_1.soldier < 0:
            event_1.soldier = 0
        if event_1.worker < 0:
            event_1.worker = 0


class sumup:
    '''Class of summarizing the results and starting the next year.'''
    def __init__(self):
        event_1.rezidents = event_1.soldier + event_1.worker
        if event_1.displeasure < 0:
            event_1.displeasure = 0
        if event_1.displ['рабочие'] < 0:
            event_1.displ['рабочие'] = 0
        if event_1.displ['янычары'] < 0:
            event_1.displ['янычары'] = 0
        print()
        print('ИТОГ:')
        print('ВЕЛИКАЯ ОСМАНСКАЯ ИМПЕРИЯ'.center(60, '-'))
        print(('Правитель: ' + str(event_1.king)).center(60) + '\n' + 'Год: ' + str(event_1.year) + '\n' + 'Территория: ' + str(event_1.territory))
        print('-' * 60)
        print('Ресурсы'.ljust(30, ' ') + '|' + '\n' + ('Золото: ' + str(event_1.rich)).ljust(30, ' ') + '|')
        print('Еда: ' + str(event_1.food).ljust(25, ' ') + '|' + ('Жители: ' + str(event_1.rezidents)).rjust(20, ' '))
        print(('Сырье: ' + str(event_1.material).ljust(23, ' ') + '|' + ('Янычары: ' + str(event_1.soldier)).rjust(20, ' ')))
        print(('Товары: ' + str(event_1.products).ljust(22, ' ') + '|' + ('Рабочие: ' + str(event_1.worker)).rjust(21, ' ')))
        print(('Уровень смуты: ' + str(event_1.displeasure)).ljust(30, ' ') + '|')
        print('-' * 60)
        print('Смута по категориям: ')
        print(('Рабочиe: ' + str(event_1.displ['рабочие'])).center(60, ' '))
        print(('Янычары: ' + str(event_1.displ['янычары'])).center(60, ' '))
        print(('Количество смертей: ' + str(event_1.deads)))
        print(f"Возведено мечетей:  {event_1.church} шт.")
        print('=' * 60)
        print()

        if event_1.displeasure >= 2000:
            print('Произошло восстание всех жителей и они свергли правителя.\nИмперия распалась.')
        elif event_1.displ['янычары'] >= event_1.soldier // 2:
            print(f"Янычары убили правителя. Империя распалась.\nИгра завершена.")
        elif max(event_1.displ['рабочие'], event_1.displ['янычары']) >= 700:
            self.riot = max(event_1.displ, key=event_1.displ.get)
            print(f"Восстали {self.riot}.", end=' ')
            if self.riot == 'янычары':
                print(f"Янычары убили правителя. Империя распалась.\nИгра завершена.")
            else:
                print(f"Нужно отправить янычар для подавления восстания. Нужно {event_1.displ[self.riot] // 3} янычар и {event_1.displ[self.riot] // 3} золота. В наличии {event_1.rich} ед. золота и {event_1.soldier} янычар.")
                if event_1.soldier > event_1.displ[self.riot] // 3:
                    if event_1.displ[self.riot] // 3 > event_1.rich:
                        print('Восстание не удастся подавить, так как не хватает ресурсов. Правитель свергнут. ')
                    else:
                        answer = input('Отправить янычар? ').lower()
                        while answer not in ['да', 'нет']:
                            answer = input('Введите "Да" или "Нет". ').lower()
                        if answer == 'нет':
                            print('Восстание разраслось по всей стране. Правитель свергнут. ')
                        else:
                            event_1.rich -= event_1.displ[self.riot] // 3
                            event_1.displeasure -= event_1.displ[self.riot] // 3
                            event_1.displ[self.riot] -= event_1.displ[self.riot] // 3
                            print('Восстание подавлено.')
                            event_1.year += 1
                            print(f"НАСТУПИЛ НОВЫЙ {event_1.year} ГОД")
                            print('ВЕЛИКАЯ ОСМАНСКАЯ ИМПЕРИЯ'.center(60, '-'))
                            print(('Правитель: ' + str(event_1.king)).center(60) + '\n' + 'Год: ' + str(event_1.year) + '\n' + 'Территория: ' + str(event_1.territory))
                            print('-' * 60)
                            print('Ресурсы'.ljust(30, ' ') + '|' + '\n' + ('Золото: ' + str(event_1.rich)).ljust(30,' ') + '|')
                            print('Еда: ' + str(event_1.food).ljust(25, ' ') + '|' + ('Жители: ' + str(event_1.rezidents)).rjust(20, ' '))
                            print(('Сырье: ' + str(event_1.material).ljust(23, ' ') + '|' + ('Янычары: ' + str(event_1.soldier)).rjust(20, ' ')))
                            print(('Товары: ' + str(event_1.products).ljust(22, ' ') + '|' + ('Рабочие: ' + str(event_1.worker)).rjust(21, ' ')))
                            print(('Уровень смуты: ' + str(event_1.displeasure)).ljust(30, ' ') + '|')
                            print('-' * 60)
                            print()
                            f = event_1()
                else:
                    print(f"Восстание не удастся подавить, так как не хватает ресурсов.\nПравитель свергнут. Империя распалась.")
        else:
            if event_1.year % 3 == 0 and event_1.year != 1550:
                answer = input('Продолжить игру? ').lower()
                while answer not in ['да', 'нет']:
                    answer = input('Введите "Да" или "Нет". ').lower()
                if answer == 'да':
                    event_1.year += 1
                    print(f"НАСТУПИЛ НОВЫЙ {event_1.year} ГОД")
                    f = event_1()
                else:
                    print('Игра завершена')
            else:
                event_1.year += 1
                print(f"НАСТУПИЛ НОВЫЙ {event_1.year} ГОД")
                f = event_1()

f = event_1()