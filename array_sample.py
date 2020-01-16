
test_list = [1, 2, 3]

print(test_list[2])

test_tuple = ('hoge', 'fuga')

print(test_tuple[1])

test_dict = {'name': 'darai', 'num': 5566, 'mail': 'xxx@gmail.com'}

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
