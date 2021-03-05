#  10. Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые
#  выходные. Президент клуба попросил вас написать две программы: •
#  программу, которая читает имя каждого игрока и его счет в игре, вводимые с
#  клавиатуры, и затем сохраняет их в виде записей в файле golf.txt ( каждая
#  запись будет иметь поле для имени игрока и поле для счета игрока);
#  • программу, которая читает записи из файла golf.txt и выводит их на экран.

def main():

    open_file = open('golf.txt', 'w')
    num_gamers = int(input('Num of players: '))
    while num_gamers != 0:
        open_file.write(input('Name: ') + '\n')
        open_file.write(input('count players: ') + '\n')
        num_gamers -= 1
    open_file.close()

    print_contents = input('Желаете распечатать "y" если "да", '
                           'любой символ если "нет": ')
    if print_contents == 'y':
        open_file = open('golf.txt', 'r')
        name = open_file.readline()
        while name != '':
            count = open_file.readline()
            name = name.rstrip('\n')
            count = count.rstrip('\n')
            print(name, ': ', count, sep='')
            name = open_file.readline()
        open_file.close()


main()