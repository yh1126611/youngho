numbers = []
product = 1
numbers = input().split()

for i in range(len(numbers)):
    product = product * int(numbers[i])

# print (len(numbers))
# print (numbers)
print (product)