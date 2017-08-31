def helpful_maths():
    string = input("Enter the sum: ")
    num = [string[i] for i in range(len(string))]
    new_list = []
    for i in range(len(num)):
        if num[i].isdigit():
            new_list.append(num[i])
    a = sorted(new_list)
    list1 = []
    for i in range(len(a)):
        list1.append(a[i])
        list1.append("+")
    if list1[-1] == "+":
        list1.pop()
    b = ''.join(list1)
    return b
print(helpful_maths())
