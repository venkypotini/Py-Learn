def max_of_three(*args):
    print(max(args))

#max_of_three(1,2,3,5,7)


def len_of_string(strg):
    count = 0
    for each in strg:
        count+=1
    print("length of string is {}".format(count))

#len_of_string("Hallo")
#

def is_vowel(stg):
    vowel_list = ['a','e','i','o','u']
    if stg in vowel_list:
        print("The word is vowel")
    else:
        print("The word is not vowel")

#is_vowel('z')


def translate(stg):
    vowel_list = ['a','e','i','o','u']
    new_stg=""
    for each in stg.lower():
        if each not in vowel_list:
            each = each+"o"+each
            new_stg+=each
        else:
            new_stg+=each
    print(new_stg)

##translate("Hallo")
