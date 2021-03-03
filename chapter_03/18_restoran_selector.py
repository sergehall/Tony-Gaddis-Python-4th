vegina = False
vegan = False
gluten = False
q_asked = 0

while q_asked == 0:
    vaginas = str(input('Any veginas: y/n? '))
    if vaginas == "y":
        vegina = True
        q_asked = q_asked + 1
    elif vaginas == "n":
        vegina = False
        q_asked = q_asked + 1
    else:
        print('Incorrect answer!')

while q_asked == 1:
    vegans = str(input('Any vegans: y/n? '))
    if vegans == "y":
        vegan = True
        q_asked = q_asked + 1
    elif vegans == "n":
        vegan = False
        q_asked = q_asked + 1
    else:
        print('Incorrect answer!')

while q_asked == 2:
    glutens = str(input('Any glutens: y/n? '))
    if glutens == "y":
        gluten = True
        q_asked = q_asked + 1
    elif glutens == "n":
        gluten = False
        q_asked = q_asked + 1
    else:
        print('Incorrect answer!')

if gluten and vegan and vegina:
    print('Right')
else:
    print('Wrong')
