def gravity_flip():
    n = int(input("Enter number of columns: "))
    c = input("Enter int numbers: ")
    list1 = [c[i] for i in range(len(c)) if c[i].isdigit()]
    a = sorted(list1)
    b = ' '.join(a)
    return b
print(gravity_flip())    
