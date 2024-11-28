#Переводчик чисел в текст

spells = "One Two Three Four Five".split()

def get_num():
    while True:
        try:
            num = int(input("Введите число от 1 до 5: "))
            if num not in range(1,6):
                raise ValueError
        except ValueError:
            print("Ошибка, некорректное число")
        else:
            return num

def main():
    while True:
        print("Соответствующее слово: " + spells[get_num()-1])

main()