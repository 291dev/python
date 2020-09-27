x = -10

if x < 0:
  print('negative')
elif x == 10:
  print('10')
else:
  print('positive')



a = 5
b = 10

if a > 0:
  print('a is positive')
  if a < b:
    print('a is smaller than b')

y = [1,2,3]
x = 1
if x in y:
  print('in')

if 100 not in y:
  print('not in')

is_ok = 0

if is_ok:
  print('ok')
else:
  print('ng')

  is_none = None
  
  if is_none is None:
    print('None')

# true
print(1 == True) 
# false
print(1 is True)

count = 0
while count < 5:
  print(count)
  if count == 1:
    count += 1
    continue
  if count == 2:
    break
  count += 1

while count < 5:
  count += 1
else:
  print('done')


some_list = [1,2,3,4,5]
i = 0
for i in some_list:
  print(i)

for i in range(2,10):
  print(i)

for _ in range(10):
  print('hello')

for i, fruit in enumerate(['a', 'b' , 'c']):
  print(i, fruit)

days = ['mon', 'tue']
fruits = ['a', 'b']
for i,v in zip(days, fruits):
  print(i, v)

d = { 'a': 'ok' , 'b': 'ng'}
for k, v in d.items():
  print(k,v)


while True:
  word = input('Enter: ')
  if word == 'ok':
      break
  print('next')