"""
sock sorter
original version by Kyle Douglas
"""
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

i = 0
laundry = []
while i < 100:
    laundry.append(random.choice(sock_types))
    i += 1
print(laundry)

sorted_laundry = {}
lone_rangers = {}
for sock in laundry:
    if sock not in sorted_laundry:
        sorted_laundry[sock] = 1
    else:
        sorted_laundry[sock] += 1


for sock_type in sorted_laundry:
    if sorted_laundry[sock_type]%2 == 1:
        lone_rangers[sock_type] = 1




print(sorted_laundry)
print(lone_rangers)


