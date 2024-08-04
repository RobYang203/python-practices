list_a = [1, 2, 3, 4, 5, 6]
list_range = list(range(6))

print("----- print List -----")
print("create by []:", list_a, len(list_a))
print("create by list function :", list_range, len(list_range))
print("is 2 in a", 2 in list_a)
print("is 10 not in a", 10 not in list_a)
print("a + range :", list_a + list_range)
print("a * 2 :", list_a * 2)
print("get index 2 in a:", list_a[2])
print("start index 2 and get 2 element :", list_a[2:len(list_range)-2])
print("start index 1 and step 2 and get all element :",
      list_a[1:len(list_range):2])
print("get min in a :", min(list_a))
print("get max in a :", max(list_a))
print("search 2 index in a :", list_a.index(2))
print("count 2 in a :", list_a.count(2))

del list_a[0]
print("del index 0 in a :", list_a)

list_a.append(10)
print("append 10 to a:", list_a)

print("copy a: ", list_a.copy())

list_a.clear()

print("clear all element in a:", list_a)

list_range.insert(5, 50)

print("insert 50 to index 5 of range :", list_range)

print("pop range:", list_range.pop())

print("pop index 2 in range:", list_range.pop(2))
print(list_range)
print("remove 0 in range:", list_range.remove(0))
print(list_range)
print("reverse range:", list_range.reverse())
print(list_range)

tuple_a = (1, 2, 3, 4, 1, 1, 1, 1)
print(tuple_a)
tuple_b = tuple(range(10))
print(tuple_b)

print("count 1 in a:", tuple_a.count(1))


set_a = {1, 1, 2, 3, 4, 5}
print("set a:", set_a)
set_b = set(range(5, 10))
print("set b:", set_b)

print("1 is in a:", 1 in set_a)
print("10 is not in a:", 10 not in set_a)
print("b different from a:", set_a.difference(set_b))
print("b intersection from a:", set_a.intersection(set_b))

set_a.add(200)
print("a add 200 :", set_a)

set_a.remove(200)
print("a remove 200:", set_a)

set_union = set_a.union(set_b)
print("a union b:", set_union)


dict_a = {"a": 1, "b": 2}
print(dict_a)

dict_dict = dict(a=1, b=2, c=3)
print(dict_dict)

dict_zip = dict(zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 0]))
print(dict_zip)

dict_tuple = dict([(6, 7), (1, 2)])
print(dict_tuple)

dict_a["c"] = 10
print("add key c in a:", dict_a)

del dict_a["a"]
print("delete key a in a", dict_a)

dict_copy = dict_a.copy()
print("copy to a:", dict_copy)

pop_item = dict_a.popitem()
print("pop item in a: ", pop_item, type(pop_item))
