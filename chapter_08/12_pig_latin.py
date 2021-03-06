# 12. Молодежный жаргон. Напишите программу, которая на входе принимает
# предложение и преобразует каждое его слово в "молодежный жаргон" . В одной
# из его версий во время преобразования слова в молодежный жаргон первая
# буква удаляется и ставится в конец слова. Затем в конец слова добавляется
# слог "ки". Вот пример. English: 'I slept most of the night'
# Pig Latin: 'Ila leptsay ostmay foay hetay ightnay'


my_string = "I slept most of the night"
print(my_string)


def pig_latin(string):
    my_string2 = string.split()
    for i in my_string2:
        i_new = i[1:] + i[0]
        print(i_new + 'AY', end=' ')


pig_latin(my_string)

