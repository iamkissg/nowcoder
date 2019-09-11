def is_huiwen(ll):

    len_ll = len(ll)

    if len_ll == 0:
        # 假定空链表是回文的
        # raise ValueError('Empty input.')
        return True
    if len_ll == 1:
        return True

    for i in range(len_ll//2+1):
        if ll[i] != ll[len_ll-1-i]:
            return False
    else:
        return True



ll = input().split()
print(is_huiwen(ll))