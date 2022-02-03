import operator
dict_1 = {1 : "n", 2 : "num", 3 : "number", 4 : "integer"}
s = dict(sorted(dict_1.items(),key = operator.itemgetter(1)))
print(s)
r = dict(sorted(s.items(), key = operator.itemgetter(1), reverse = True))
print(r)
