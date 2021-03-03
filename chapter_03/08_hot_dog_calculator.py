# hot dog cookout calculator
import math

pack_sous = 10
pack_bul = 8
people = int(input("Enter the amount of individuals who will be there?: "))
hot_dog = float(input("Enter the amount of hot dogs for each person: "))
total_hot_dog = math.ceil(people * hot_dog)
print('total_hot_dog = ', total_hot_dog)
min_pack_sous = float(total_hot_dog / pack_sous)
print('min_pack_sous = ', math.ceil(min_pack_sous))
min_pack_bul = float(total_hot_dog / pack_bul)
print('min_pack_bul = ', math.ceil(min_pack_bul))
ext_sous = float(abs(math.ceil(min_pack_sous) * pack_sous - total_hot_dog))
print('ext_sous = ', math.ceil(ext_sous))
ext_bul = float(abs(math.ceil(min_pack_bul) * pack_bul - total_hot_dog))
print('ext_bul = ', math.ceil(ext_bul))
