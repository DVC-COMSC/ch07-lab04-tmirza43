
# ******************************
# Make your Code
# ******************************
import random

numbers = []
numbers2 = []
total = []

for i in range(10):
  numbers.append(random.randint(0,10))
  numbers2.append(random.randint(0,10))

for j in range(10):
  total.append(numbers[j] + numbers2[j])

print(numbers)
print(numbers2)
print(total)
