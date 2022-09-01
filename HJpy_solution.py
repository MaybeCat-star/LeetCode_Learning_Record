def HJ2():
    str1 = input()
    char = input()

    count = 0

    for _ in str1:
        if _.lower() == char.lower():
            count += 1

    print(str1.count(char))
    print(count)

def HJ3():
    num1 = input()
    List = []
    for i in range(int(num1)):
        List.append(int(input()))
    for _ in sorted(set(List)):
        print(_)


