import time

def choose_character():
    person1 = {"name": "Алиса", "age": "18 лет"}
    person2 = {"name": "Лена", "age": "17 лет"}

    while True:
        person = input("Выберите персонажа (Алиса или Лена):")

        if person == "Алиса":
            values1 = person1["name"], person1["age"]
            print("Ваш персонаж:", values1)
        elif person == "Лена":
            values2 = person2["name"], person2["age"]
            print("Ваш персонаж:", values2)
        else:
            print("Введены недопустимые значения")
            break
        return person

def library_scenario(person):
    print("В библиотеке сидел лишь один парень. Похоже он спит...")
    time.sleep(0.5)
    actions = ["попробовать разбудить его", "взять книгу"]
    print(actions)
    
    while True:
        choice = input("Что сделать? ")
        if choice == "1":
            print("Парень недовольно открыл глаза. \"Тебе нечем заняться? Лучше уйди отсюда\". Вы молча вышли из библиотеки и до начала урока сидели перед кабинетом.")
            time.sleep(2)
        elif choice == "2":
            print("Взяв книгу, вы сидели и читали за соседним столом. К началу уроков парень проснулся и, улыбнувшись вам, вышел из библиотеки")
            time.sleep(1.4)
        else:
            print("Введены некорректные данные")
            continue
        break

def schoolyard_scenario(person):
    print("Вы вышли во двор и увидели двух парней, сидевших на скамейке")
    time.sleep(1)
    actions = ["подойти и познакомиться", "прогуляться по периметру школы"]
    print(actions)
    
    while True:
        choice = input("Что сделать?")

        if choice == "1":
            name1 = "Максим"
            name2 = "Саша"
            if person == "Алиса":
                print("Вы: \"Привет. Меня зовут Алиса. Я здесь первый день. Не против, если я составлю вам компанию?\"")
                time.sleep(1)
            elif person == "Лена":
                print("Вы: \"Привет. Меня зовут Лена. Я здесь первый день. Не против, если я составлю вам компанию?\"")
                time.sleep(1)
            print(f"Светловолосый парень: \"Привет. Нет, не против. Меня зовут {name1}, а это мой брат {name2}.\" {name2} оторвался от игры на телефоне и махнул вам рукой. Вы сидели и болтали до начала урока")
            time.sleep(4)
        elif choice == "2":
            print("Из интересного вы нашли только оранжерею, и затем пошли на урок, так никого и не встретив")
            time.sleep(1.2)
        else:
            print("Введены некорректные данные")
            continue
        break

def cafeteria_scenario(person):
    print("В столовой вы увидели двух девушек, которые сидели в самом углу и шептались")
    time.sleep(1)
    actions = ["пройти мимо", "подсесть к ним за столик"]
    print(actions)
    
    while True:
        choice = input("Что сделать?")

        if choice == "1":
            print("Вы прошли мимо их столика и купили в буфете поесть. Попробовав еду, вы поняли, что лучше брать поесть из дома...")
            time.sleep(1.3)
        elif choice == "2":
            text = "\"кто тебя сюда звал? не видишь, что мы разговариваем?\""
            print(f"Брюнетка: {text.upper()}")
            time.sleep(0.7)
            print("Вы поняли, что лучше не связываться с этими истеричками. Точно не в первый день...")
            time.sleep(0.7)
        else:
            print("Введены некорректные данные")
            continue
        break

def lunch_break_scenario():
    print("Прозвенел звонок, и вы отправились на уроки.")
    time.sleep(0.8)
    print("На перемене вы вышли во двор и услышали крики.\nВы: \"Надо посмотреть, что там происходит.\"")
    time.sleep(1)
    actions = ["проверить оранжерею", "выйти за калитку"]
    print(actions)

    while True:
        choice = input("Куда пойти?")

        if choice == "1":
            print("Пока вы дошли до оранжереи, голоса уже стихли")
            time.sleep(0.5)
            break

        elif choice == "2":
            if mesto == "библиотека":
                print("Вы увидели парня, который спал в библиотеке перед уроками. Он ссорился с блондином, которого вы еще не встречали. Вы молча наблюдали издалека с толпой зевак. Вам еще предстоит узнать, что между ними произошло...")
                time.sleep(4)
            elif mesto != "библиотека":
                print("Вы увидели ссору двух парней. \nВы: \"Ничего интересного. Наверное девушку не поделили.\"")
                time.sleep(1)
            break

        else:
            print("Введены некорректные данные")

    print("Вы пошли на следующий урок. Остаток дня прошел без происшествий, и вы пошли домой. Конец 1 эпизода.")

# Main
chosen_person = choose_character()

if chosen_person == "Алиса" or chosen_person == "Лена":
    if chosen_person == "Алиса":
        mesto = input("Нажмите Enter, чтобы начать историю")
    elif chosen_person == "Лена":
        mesto = input("Нажмите Enter, чтобы начать историю")
    while True:
        mesto = input("Куда отправитесь перед началом урока? (библиотека, школьный дворик, столовая):")
        if mesto == "1":
            library_scenario(chosen_person)
        elif mesto == "2":
            schoolyard_scenario(chosen_person)
        elif mesto == "3":
            cafeteria_scenario(chosen_person)
        else:
            print("Введены некорректные данные")
            continue
        
        lunch_break_scenario()
        break
else:
    print("Произошла ошибка при выборе персонажа.")
