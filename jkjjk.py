"""number = 1
while number <= 20:
    print(number)
    number += 1"""

odd_sum = 0
for number in range(1,21):
    if number % 2!= 0:
        odd_sum += number
print("The sum of odd numbers between  between 1 and 20 is:", odd_sum)