numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print(f'Found a even number {number}')
        break
    position += 1

else:
    print("No even numbers found")