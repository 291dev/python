def say_somethin():
  print('hi')

# DocStrings

def menu(entree, drink, dessert):
  print(entree, drink, dessert)

menu(entree='entree', drink='drink', dessert='dessert')

def ng_func(x, l=[]):
  l.append(x)
  return l
x = ng_func(10)
print(x)
y = ng_func(10)
print(y)

def ok_func(x, l=None):
  if l is None:
    l = []
  l.append(x)
  return l

x = ok_func(10)
print(x)
y = ok_func(10)
print(y)


def say_something(*args):
  for arg in args:
    print(arg)

say_something('hi', 'hey', 'ho')

d = {
  'a': '1',
  'b': '2'
}

def menu(**args):
  for k,v in args.items():
    print(k, v)

menu(**d)
menu(a='a', b='b')

def tupleargs(*args):
  for v in args:
    print(v)

tupleargs('a', 'b', 'c')
tupleargs(*('a', 'b', 'c'))

def example_fanc(param1, param2):
  """Example function with types documented in the docstring.
  
  Args:
    param1 (int): The first Parameter.
    param2 (str): The second parameter.
  
  Returns:
    bool: The return value. True for success, False otherwise.
  """
  print(param1)
  print(param2)
  return True

# closure
def outer(a,b):
  def inner():
    return a + b
  return inner

# decolater
def print_info(func):
  def wrapper(*args, **kwargs):
    print('start', func.__name__) 
    result = func(*args, **kwargs)
    return result
  return wrapper

def add_num(a, b):
  return a + b

f = print_info(add_num)
r = f(10, 20)
print(r)

@print_info
def sub_num(a, b):
  return a - b

print(sub_num(4,3))

# lambda functionを引数とするときによく使う
l = [1,2,3]

def multi10(nums, func):
  for i in nums:
    print(func(i))

multi10(l, lambda num: num*10)


# generator
def greeting():
  yield 'Good morning'
  yield 'Good afternoon'
  yield 'Good evening'

for strs in greeting():
  print(strs)

g = greeting()
print(next(g))
print(next(g))
print(next(g))


t = [1,2,3,4,5]
r = [i for i in t if i%2 ==0]
print(r)

animal = 'cat'

# globsl変数を書き換える場合
def f():
  global animal 
  animal = 'dog'
  print('global:', animal)

f()


l = [1,2,3]

try:
  l[4]
except IndexError as ex:
  print("Exception occered: {}".format(ex))
finally:
  print('clean up')

class UppercaseError(Exception):
  pass

def check():
  words = ['APPLE', 'orange']
  for word in words:
    if word.isupper():
      raise UppercaseError(word)
try:
  check()
except UppercaseError as esc:
  print('This is my fault. Gonext')  
