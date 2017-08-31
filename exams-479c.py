def exams():
    n, last = int(input()), 0
    exams = sorted([map(int, input().split()) for _ in range(0, n)])
    for exam in exams:
        if exam[1] >= last:
            last = exam[1]
        else:
            last = exam[0]
    return last
print(exams()) 
