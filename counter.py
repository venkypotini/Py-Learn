from collections import Counter
from collections import OrderedDict
s = "Hallo how are you, can you hear me hallo"
w = Counter(s.lower().split())
print(w)
print(w.most_common(3))
print(sum(w.values()))
print(list(w))
print(set(w))
print(dict(w))
print(w.items())
print(dict(w.items()))

d = {'one': 1,'two':2,'three':3,'four':4,'five':5}
print(d.items())
print(list(d.items()))

d = OrderedDict()

d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

for each in d:
    print(each)
for k,v in d.items():
    print(k,v)
