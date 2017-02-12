# Я не понял, что от меня требовалось показать в этой задаче.
# Очевидно, я сделал её неверно, но путь будет так.

class Printer:
    def log(self, *values):
        for value in values:
            print(value)

class FormattedPrinter():
    def log(*values):
        print('***')
        for value in values:
            print(value)
        print('***')

FormattedPrinter.log('1', '2', '3')
