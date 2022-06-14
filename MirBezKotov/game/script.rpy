# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define m = Character('Матвей', color="#c8ffc8")
define a = Character('Андрей', color="#c2ffc5")
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene fon

    show matwey poxyi

    m "Здравствуйте мои дорогие друзья, сейчас я поведую вам историю о моём лете."

    m "Дело было так.... "

    m "А хотя... похуй)"

    scene fon andrei

    show andrei lol

    a "Всмысле похуй?"

    a "Зрителям не похуй на меня!"

    menu:
        a "Мотя ты чо пидр?"

        "Нет ты чо ахуел?":
            jump ti_pidor

        "Да":
            jump pizda

label ti_pidor:
        a "А мне кажется что ты хуесос ебливый жырный уебан"
        jump dialog_yeban

label pizda:
        a "Пизда"
        jump dialogpizda

label dialog_yeban:
    scene fon
    show matwey poxyi

    m "Сам такой"
    m "Подставляй попочку)"
    jump rrr

label dialogpizda:
    scene fon
    show matwey poxyi
    m "Чья"

    scene fon andrei
    show andrei lol
    a "Твоей жирной мамаши"

    scene fon
    show matwey poxyi
    m "Ты чо про мать сказал сука эдакая"

    scene fon andrei
    show andrei lol
    a "Я говорю что я ее трахал во все щели, уебок вонючий"

    scene fon
    show matwey poxyi
    m "Ну все, ты напросился"
    jump rrr

label rrr:
    scene fon
    show matwey poxyi

    m "Дальше думай сам сука сюжет"







    return
