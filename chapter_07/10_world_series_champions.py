# world series champions


def main():
    open_file = open('WorldSeriesWinners.txt', 'r')
    content = open_file.readlines()
    open_file.close()
    index = 0
    content_list = []
    while index < len(content):
        content[index] = content[index].rstrip('\n')
        content_list.append(content[index])
        index += 1
    print(content_list)
    name_team = input('Name team: ')
    name_team, total_win = search_win(content_list, name_team)
    print("The team:", name_team, "has been winner", total_win, "times.")


# фунция для поиска в списке команд ,
# какое количекство лет она была победетелем
def search_win(content_list, name_team):
    total_win = 0
    for name in content_list:
        if name == name_team:
            total_win += 1
    return name_team, total_win


main()