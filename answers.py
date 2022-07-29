
def string_times(str, n):
  return str * n
  
def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[:3] * n

def string_bits(str):
  result = ''
  for n in range(0, len(str)):
    if n%2 == 0:
      result += str[n]
  return result

def string_splosion(str):
  result = ''
  for n in range(0,len(str)+1):
    result += str[:n]
  return result

def last2(str):    
  count = 0
  for i in range(len(str)-2):
    if str[i:i+2] == str[-2:]:
      count += 1  
  return count

def array_count9(nums):
  count = 0
  for element in nums:
    if element == 9:
      count += 1
  return count

def array_front9(nums):
  for element in nums[:4]:
    if element == 9:
      return True
  return False

def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False

def string_match(a, b):
  min_length = min(len(a), len(b))
  count = 0 
  for i in range(min_length-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count
