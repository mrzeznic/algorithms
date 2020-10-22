import time
import random
import pandas as pd

# normal search


def normal_search(list, item):
    start_time = time.time()
    i = 0
    high = len(list)-1

    while i <= high:
        if i == item:
            ns_time = ((time.time()-start_time)*1000)
            # print("Normal Search: To guess number {} it needs {}
            # iteration which takes {:f} miliseconds".format(
            #    item, i, ((time.time()-start_time)*1000)))         
            break
        else:
            i += 1
            # print("Normal Search: Iteration {} quess: {}".format(i, i))
            # print(guess)
    return ns_time
# binary search


def binary_search(list, item):
    start_time = time.time()
    low = 0
    high = len(list)-1
    i = 0

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            bs_time = ((time.time()-start_time)*1000)
            # print("Binary Search: To guess number {} it needs {}
            #  iteration which takes {:f} miliseconds".format(
            #     guess, iter, ((time.time()-start_time)*1000)))
            break
        if guess > item:
            high = mid - 1
            i += 1
            # print("Binary Search:
            # Iteration {} quess: {}".format(iter, guess))
            # print(guess)
        else:
            low = mid + 1
            i += 1
            # print("Binary Search:
            # Iteration {} quess: {}".format(iter, guess))
            # print(guess)
    return bs_time


def list_generator(minimum, maximum, by_step, exp_range):
    my_list = [random.randrange(minimum, maximum, by_step)
               for i in range(exp_range)]
    my_list.sort()
    return my_list


# setting for search
list = list_generator(1, 5000, 1, 200)

looked_value = random.randint(list[0], len(list))

ns = normal_search(list, list[looked_value])
bs = binary_search(list, list[looked_value])

print(ns)
print(bs)
print(list[looked_value])
print(normal_search(list,list[looked_value]))
print(len(list))


# return table
d = {'Normal Search': [ns], 'Binary Search': [bs],
     'Normal/Binary': [ns]/[bs], 'Value': [looked_value]}
df = pd.DataFrame(data=d)
print(df)
