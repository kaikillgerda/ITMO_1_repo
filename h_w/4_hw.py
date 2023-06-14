# --- ЗАДАНИЕ №1 ---
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square_calc(self):
        square = self.width * self.height
        print("Площадь прямоугольника = {}".format(square))

    def perimeter_calc(self):
        perimeter = (self.width + self.height) * 2
        print("Периметр прямоугольника = {}".format(perimeter))


obj_1 = Rectangle(7, 8)
obj_2 = Rectangle(2, 5)
obj_3 = Rectangle(15, 100)

obj_1.square_calc()
obj_1.perimeter_calc()
obj_2.square_calc()
obj_2.perimeter_calc()
obj_3.square_calc()
obj_3.perimeter_calc()


# --- ЗАДАНИЕ №2 ---
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        addit = self.a + self.b
        print("Сумма чисел = {}".format(addit))

    def multiplication(self):
        multi = self.a * self.b
        print("Произведение чисел = {}".format(multi))

    def division(self):
        div = self.a / self.b
        print("Частное чисел = {}".format(div))

    def subtraction(self):
        sub = self.a - self.b
        print("Разница чисел = {}".format(sub))


Math(5, 7).addition()
Math(2, 4).multiplication()
Math(8, 16).division()
Math(52, -2).subtraction()


# --- ЗАДАНИЕ №3 ---

class DemoQA:
    def __init__(self, text, type='button', loc=' '):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print('Клик по кнопке ' + self.text)


text_box = DemoQA('Text Box')
check_box = DemoQA('Check Box')
radio_button = DemoQA('Radio Button')
web_tables = DemoQA('Web Tables')
buttons = DemoQA('Buttons')
links = DemoQA('Links')
broken_links_images = DemoQA('Broken Links Images')
upload_and_download = DemoQA('Upload and download')
dynamic_properties = DemoQA('Dymamic Properties')

print(text_box.text)
text_box.click()
print(check_box.text)
check_box.click()
print(radio_button.text)
radio_button.click()
print(web_tables.text)
web_tables.click()
print(buttons.text)
buttons.click()
print(links.text)
links.click()
print(broken_links_images.text)
broken_links_images.click()
print(upload_and_download.text)
upload_and_download.click()
print(dynamic_properties.text)
dynamic_properties.click()
