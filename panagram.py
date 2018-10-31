def panagram(strg):
    alpha = list(map(chr, range(97,123)))
    flag = True
    for each in alpha:
        if each not in strg.lower():
            flag = False
    return flag

print(panagram("The quick brown fox jumps over the lazy dog"))
