import time
import random

# normal search


def normal_search(list, item):
    start_time = time.time()
    i = 0
    high = len(list)-1
    iter = 0

    while i <= high:

        guess = list[i]
        if guess == item:
            print("Normal Search: To guess number {} it needs {} iteration which takes {:f} miliseconds".format(
                guess, iter, ((time.time()-start_time)*1000)))
        else:
            iter += 1
            print("Normal Search: Iteration {} quess: {}".format(iter, guess))
            # print(guess)
    return None
# binary search


def binary_search(list, item):
    start_time = time.time()
    low = 0
    high = len(list)-1
    iter = 0

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            print("To guess number {} it needs {} iteration which takes {:f} miliseconds".format(
                guess, iter, ((time.time()-start_time)*1000)))
        if guess > item:
            high = mid - 1
            iter += 1
            print("Iteration {} quess: {}".format(iter, guess))
            # print(guess)
        else:
            low = mid + 1
            iter += 1
            print("Iteration {} quess: {}".format(iter, guess))
            # print(guess)
    return None


def list_generator(minimum, maximum, by_step, exp_range):
    my_list = [random.randrange(minimum, maximum, by_step)
               for i in range(exp_range)]
    my_list.sort()
    return my_list


list = list_generator(1, 500, 1, 20)


print(binary_search(list, list[5]))
#print(normal_search(list, list[5]))
