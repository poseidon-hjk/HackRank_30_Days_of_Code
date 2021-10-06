"""""
input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
"""


num = int(input())

name_number = []
for _ in range(num) :
    name_number += [input().split()]

phone_book = {}
for x,y in name_number:
    phone_book[x] = y

while True:
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except:
            break

