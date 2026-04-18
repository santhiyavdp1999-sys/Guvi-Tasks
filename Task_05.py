# 1. to filter out people under 18 and then map the remaining peoples names to a list


people=[{"name": "sanju","age" : 25},{"name": "Akira","age": 16},{"name": "dheeran","age": 30},{"name": "priya","age": 17}]
filtered_people= filter(lambda p: p['age']>=18, people)
names_list= list(map(lambda p: p['name'], filtered_people))
print(names_list)

# 2. To calculate the product of all the number in the list.

from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, numbers)
print(f"The Product is: {product}")

# 3. List comprehension that creates a new list of squares of even number (lambda function)

numbers =[1,2,3,4,5,6,7,8,9,10]
is_even = lambda x: x%2==0
square_of_evens = [x**2 for x in numbers if is_even(x)]
  
print(square_of_evens)


# 4. 


