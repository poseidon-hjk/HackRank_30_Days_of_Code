'''
    My solve
'''

if __name__ == '__main__':
    n = int(input().strip())

    result = ""
    floor = n
    cnt = 0
    max_cnt = 0

    while floor > 0:
        modulus = floor % 2
        floor //= 2

        if modulus == 1:
            cnt += 1
        elif modulus == 0:
            if cnt > max_cnt:
                max_cnt = cnt
                cnt = 0

        if floor == 1:
            cnt += 1

    if floor == 1:
        # result += str(floor)
        max_cnt += 1
        # print(result)
    else:
        while floor > 1:
            # print(floor)
            if floor == 0:
                break

            modulus = floor % 2
            # result += str(modulus)
            cnt += modulus

            if modulus == 0:
                max_cnt = cnt
                cnt = 0

            if (floor // 2) == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                break
            else:
                floor //= 2

    print(max_cnt)

