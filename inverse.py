def backwords(*args):
    for word in (args[::-1]):
        print(word[::-1],end = ' ')


backwords("hallo", "how", "are","you")


def mean(args):
    print('\n')
    print(args)
    print(*args)
mean((1,2,3,4))

def build_tuple(*args):
    # value = []
    # for each in args:
    #     value.append(each)
    # value = tuple(value)
    # return(value)
    return args

message_tuple = build_tuple("hello","how","are","you")
print(type(message_tuple))
print(message_tuple)

message_tuple = build_tuple(1,2,3,4)
print(type(message_tuple))
print(message_tuple)

def avg_lnt(*args):
    ln= 0
    for each in args:
        ln+=len(each)
    return(ln/len(args))

avlth = avg_lnt("hallo", "hallo","hallo","hallo")
print(avlth)

def largest(*args):
    large = 0
    for each in args:
        if each > large:
            large = each
    return(large)

print(largest(1,5,6,2))
