
test_list = [1, 2, 3]

print(test_list[2])

test_tuple = ('hoge', 'fuga')

print(test_tuple[1])

test_dict = {'name': 'darai', 'num': 5566, 'mail': 'xxx@gmail.com'}


del test_dict['num']

# test_dict['other'] = 'hogefuga'

print(test_dict.items())

print(test_dict.get('num'))
print(test_dict.get('mail'))

test_set = set(['555', '666', '777', '555', '888'])

print(test_set)

test_list1 = [1, 2, 3]
test_list1.append(5)
print(test_list1)

test_list1.insert(2, 8)
print(test_list1)


test_list2 = [1, 2, 3, 4, 4, 5, 4]
del test_list2[2]
print(test_list2)

test_list2.remove(4)
print(test_list2)


a = (1,)
print(type(a))
# <class 'tuple'>

b = (1)
print(type(b))
# <class 'int'>

c = ('test')
print(type(c))
# <class 'str'>

d = {}
print(type(d))
# <class 'dict'>

e = set()
print(type(e))
# <class 'set'>

f = {'hoge': 'fuga', 'type': 'test'}
print(type(f))
# <class 'dict'>

g = {'hoge', 'fuga'}
print(type(g))
# <class 'set'>