def sleep_in(weekday, vacation):
  if weekday is True:
    if vacation is True:
      return True
    else:
      return False
  elif vacation is True:
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b

def diff21(n):
  if n < 21:
    return n-21
  else:
    return (21-n)*2

def parrot_trouble(talking, hour):
  if talking is True and hour < 7 or talking is True and hour > 20:
    return True
  else:
    return False

def makes10(a, b):
  return(a==10 or b==10 or(a+b)==10)

def near_hundred(n):
  return(n > 90 and n < 110 or n > 190 and n < 210)

def pos_neg(a, b, negative):
    if negative is True:
        return a < 0 and b < 0
    else:
        if a > 0 and b < 0 or b > 0 and a < 0:
            return True
        else:
            return False

def not_string(str):
  if 'not' in str[:3]:
    return str
  else:
    return 'not ' + str

def missing_char(str, n):
    return str.replace(str[n], '')
#print(missing_char('Hello', 2)) #removed both lls?

def front_back(str):
  str = str[-1] + str[1:len(str)] + str[0]
  return str

def string_splosion(str):
  n = len(str)
  return [str[i:i+n] for i in range(len(str)-n+1)]

def array123(nums):
  for i in range(len(nums)):
    print(i)
    print(i+1)
    print(i+2)
    return i == 1 and i+1 == 2 and i+2 == 3
print(array123([1, 1, 2, 4, 1]))




def same_first_last(nums):
    if nums[0] == nums[-1] and len(nums) > 1:
      return True
    else:
      return False

def lone_sum(a, b, c):
  if a == b and a == c:
    return 0
  elif a == b:
    return c
  elif b == c:
    return a
  elif c == a:
    return b
  if a == b and a == c:
    return 0
  else:
    return a+b+c



def round10(num):
  if num[-1] >= 5:
    num = (num[1]-10) + num
  elif num[-1] < 5:
    num = num-num[-1]
  return num

def round_sum(a, b, c):
    x = round10(a)+round10(b)+round10(c)
    return x



def mean_av(nums):
  sum = 0
  div = len(nums)
  for i in range(len(nums)):
    sum = sum + nums[i]
  mean = sum / div
  return mean

def centered_average(nums):
  x = mean_av(nums)
  return x


def cat_dog(str):
  c_cnt = 0
  d_cnt = 0
  for i in range(len(str)-2):
    if str[i] == 'c' and str[i]+1 == 'a' and str[i]+2 == 't':
      c_cnt +=1
    if str[i] == 'd' and str[i]+1 == 'o' and str[i]+2 == 'g':
      d_cnt +=1
  return c_cnt == d_cnt
