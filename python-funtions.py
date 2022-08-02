# CHALLENGE #1
def sum_to(num):

  sum = 0

  for n in range(1, num + 1):
    sum += n

  return sum

# CHALLENGE #2
def largest(nums):

  largest = 0

  for num in nums:
    if num > largest:
      largest = num

  return largest

# CHALLENGE #3

def occurences(string, substr):
  
  stripped_string = string.replace(substr, '')

  return (len(string) - len(stripped_string) // len(substr))

# CHALLENGE #4 

def product(args):

  product = 1

  for arg in args:
    product *= arg
    
  return product


