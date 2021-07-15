while True:
    value = input("Integer, please [q to quit]: ")

    # exit
    if value == 'q':
        break
    number = int(value)

    if number % 2 == 0:
        continue
    print(number, f'squared is, {number*number}')
