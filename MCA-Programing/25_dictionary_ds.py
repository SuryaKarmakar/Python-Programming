# create dictionary
dict1 = {}
dict2 = {
    1: 10,
    2: 20,
    3: 30
}
dict3 = {
    "a": "A",
    "b": "B",
    "C": "C"
}
dict4 = {
    1: 100,
    "a": "aaa",
    1.11: 10.11,
    (1, 2, 3): (1, 2, 3)
}
dict5 = {
    "name": "john",
    "age": 24,
    "height": 5.11,
    "hobbie": ["playing", "cooking", "ridding"]
}

# accessing values

# using []
print("name:", dict5["name"])

# using get()
print("age:", dict5.get("age"))

# adding values
dict5["country"] = "US"
print(dict5) 

# updating existing value
dict5["age"] = 30
print(dict5)

# deleting items
del dict5["age"]
print(dict5)

# deleting and return deleted item value using pop
print(dict5.pop("country"))

# deleting and return deleted item key and value using popitem
print(dict5.popitem()) # its delete last item on the dictionary

# deleting all items
dict5.clear()
print(dict5)

# iteration
for x in dict2:
    # print("key:", x, "and value:", dict2[x])
    print("key: {0} and value: {0}".format(x, dict2[x]))

# all()
d_all_1 = {1: 1, 2: 1}
print(all(d_all_1))

d_all_0 = {0: 1, 1: 1}
print(all(d_all_0))

# any()
d_any_1 = {0: 1, 1: 1}
print(any(d_any_1))

# len()
print(len(dict2))

# sorted()
print(sorted(dict2))
print(sorted(dict2, reverse = True))

# items()
print(dict3.items())

# keys()
print(dict3.keys())

# values()
print(dict3.values())