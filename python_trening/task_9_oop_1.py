from task_9_checks import Checks
class Input(Checks):

    def __init__(self, loc, text):
        super().__init__(loc)
        # self.loc = loc
        self.text = text


search = Input('input#search ', ' Поиск информации')


class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        # self.loc = loc
        self.text = text


make = Button('button#make ', ' Вывод информации')


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        # self.loc = loc
        self.text = text


head = Title('header#title ', ' Информация в хэдере')


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        # self.loc = loc
        self.text = text


finder = Link('button#link ', " Рабочие ссылки")

print(search.check_text() + search.text)
print(make.check_text() + make.text)
print(head.check_text() + head.text)
print(finder.check_text() + finder.text)
