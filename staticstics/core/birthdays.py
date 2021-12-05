import numpy as np
from collections import Counter
from math import factorial as fact

'''
Intuitive approach
I have mastered this approach as it is is just a program
'''
def sim_probability_of_birthday(people, epochs=1000):
    total = 0.0
    temp_epoch = epochs

    while temp_epoch > 0:
        day_born = np.random.choice(365, people)
        freq = Counter(day_born)
        common = freq.most_common()
        if common[0][1] > 1.0:
            total += 1.0
        temp_epoch -= 1

    return round(total/epochs, 10)


'''
Mathematical approach - almost
I understand this approach very well
'''
def probability_of_birthday(n):
    q = 1.0
    for i in range(n):
        probability = 1 - i/365
        q *= probability
    return round(1.0 - q, 10)

'''
Mathematical approach
Less intuitive for me
'''
def pbirthday(n):
    if n < 2:
        return 0.0
    q = (364/365) ** (fact(n)/(2*fact(n-2)))
    return round(1.0 - q, 10)


PEOPLE = 23
result1 = sim_probability_of_birthday(PEOPLE, epochs=10000)
result2 = probability_of_birthday(PEOPLE)
result3 = pbirthday(PEOPLE)

print(f'Result-1: Probability of same birthday: {result1}')
print(f'Result-2: Probability of same birthday: {result2}')
print(f'Result-3: Probability of same birthday: {result3}')
