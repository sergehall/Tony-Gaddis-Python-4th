# pattern2
# ##
# # #
# #  #
# #   #
# #    #
# .......#

NUM_STEPS = int(input("Enter the desired number of characters "
                      "between hashtags: "))
# create loop structure
for i in range(NUM_STEPS):
    print('#', end='')
    for j in range(i):
        print(' ', end='')
    print('#')
