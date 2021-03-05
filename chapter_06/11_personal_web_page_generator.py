# 11. Генератор персональной веб-страницы. Напишите программу, которая
# запрашивает у пользователя его имя и просит пользователя ввести
# предложение, которое его описывает. Вот пример экрана программы: Введите
# свое имя: Джу.пия Тейлор. Enter. Опишите себя: Моя специализация -
# информатика, я являюсь членом джаз-кпуба и надеюсь стать разработчиком. Enter.

def main():
    name_body = input('Name: ')
    description_body = input('Опиши себя: ')
    open_file = open('sergio_6.10ex.html', 'w')
    open_file.write('<!DOCTYPE html>' + '\n')
    open_file.write('<head>' + '\n')
    open_file.write('    <meta charset="UTF-8">' + '\n')
    open_file.write('<title>Title</title>' + '\n')
    open_file.write('</head>' + '\n')
    open_file.write('<body>' + '\n')
    open_file.write('<center>' + '\n')
    open_file.write('    <h1>' + str(name_body) + '</h1>' + '\n')
    open_file.write('</center>' + '\n')
    open_file.write('<hr />' + '\n')
    open_file.write('   <center><h3>' + str(description_body)
                    + '</h3></center>' + '\n')
    open_file.write('<hr />' + '\n')
    open_file.write('</body>' + '\n')
    open_file.write('</html>' + '\n')
    open_file.close()


main()