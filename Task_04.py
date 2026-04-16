
# 1. Even number and odd number
num=int(input("Enter the Number:"))

if num%2==0:
     print("Even Number")
else:
     print("Odd Number")

# 2. Count of all the Prime Number

number=[10,501,22,37,100,999,87,351]
prime_number=[]
for num in number:
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if (num % i)==0:
                break
        else:
            prime_number.append(num)

print("Prime Numbers List:", prime_number)
print("Count of Prime Number:",len(prime_number))

# 3. Happy Numbers

def is_happy(n):
    seen=set()
    while n !=1 and n not in seen:
        seen.add(n)
        n=sum(int(digit)**2 for digit in str(n))
    return n==1
numbers=[10,501,22,37,100,999,87,351]
happy_numbers=[num for num in numbers if is_happy(num)]
print(f"Happy Numbers: {happy_numbers}")
print (f"Total Count : {len(happy_numbers)}")

# 4. the dum of the first and last digit of an integer

number_str= input("Enter an integer: ").strip().lstrip('-')
first_digit=int(number_str[0])
last_digit=int(number_str[-1])
total_sum = first_digit+last_digit
print(f"The Sum of the first and last digit is : {total_sum}")


# 5. To find the ways to make Rs.10 using Rs.1, Rs.2, Rs.5, Rs.10 coins

def find_combination(target,coins,current_combination,index):
    if target==0:
        print(current_combination)
        return
    for i in range(index,len(coins)):
        coin = coins[i]
        if target - coin >=0:
            find_combination(target - coin,coins,current_combination + [coin], i)
target_amount =10
available_coins=[1,2,5,10]
print(f" Ways to make Rs.{target_amount}:")
find_combination(target_amount,available_coins,[],0)



# 6. Find the duplicates in the three lists

list1=[10,20,30,40,50]
list2=[30,40,50,60,70]
list3=[50,40,80,90,100]
duplicates=list(set(list1) & set(list2) & set(list3))
print(f"List1: {list1}")
print(f"List2: {list2}")
print(f"List3: {list3}")
print(f"Common elements in all three lists: {duplicates}")

# 7. to find the non-repeating elements in a given list of integers

def first_non_repeating(num):
    counts={}
    for x in num:
        counts[x] = counts.get(x,0)+1
    for x in num:
        if counts[x] ==1:
            return x
    return none
numbers=[9,4,9,6,7,4]
result=first_non_repeating(numbers)
print(f"The first non-repeating elements is : {result}")


# 8. To find the minimum element in a rated and sorted list

def find_minimum(num):
    minimum=num[0]
    for x in num:
        if x < minimum:
            minimum=x
    return minimum
my_list=[30,40,50,10,20]
print("Minimum: ", find_minimum(my_list))


# 9. To find the triplet in the lists

numbers=[10,20,30,9]
target = 59
n = len(numbers)
for i in range(n):
    for j in range(i+1,n):
        for k in range (j+1,n):
            if numbers[i] + numbers[j] +numbers[k] ==target:
                print(f" Triplet Found: {numbers[i]}, {numbers[j]}, {numbers[k]}")










