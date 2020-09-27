l=[1,2,3,4,5]
l[0] = '1'
print(l)
l.append('6')
print(l)
l.insert(0,1)
print(l)
l.insert(2,3)
print(l)
del l[6]
print(l)

m=[6,7,8,9,10]
l += m
print(l)


# l再定義
l = [1,2,3,4,5]
if 5 in l:
  print('exist')

l.sort()
print(l)
l.sort()
print(l)

a='My name is fukui'
print(a.split(' '))
print(a)

# 参照渡し
i=[1,2,3,4,5]
j=i
j[0] = 100
print(f'i={i}, j={j}')
print(f'idi={id(i)}, j={id(j)}')

# 値わたし
i= [1,2,3,4,5]
j=i.copy()
j[0] = 100
print(f'i={i}, j={j}')
print(f'i={id(i)}, j={id(j)}')
