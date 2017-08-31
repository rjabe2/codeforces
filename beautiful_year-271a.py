def calculate_next(year):
    while True:
        year = str(int(year)+1)
        if len(set(year)) == 4:
            return year

if __name__ == "__main__":
    print(calculate_next(input()))
