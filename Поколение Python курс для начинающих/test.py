class MyError(Exception):
    def __init__(self, text):
        self.txt = text
    
def numerics(n):
    if n < 1001:
        raise MyError(f'Ошибка! На вход подано число {n}')
    elif len(set([int(i) for i in str(n)])) == 1:
        raise MyError(f'Ошибка! На вход подано число {n} - все цифры одинаковые')
    else:
        return [int(i) for i in str(n)]

def kaprekar_step(L):
    n1 = int(''.join(str(i) for i in sorted(L)))
    n2 = int(''.join(str(i) for i in sorted(L, reverse=True)))
    return abs(n1 - n2)

def kaprekar_loop(n):
    try:
        numerics(n)
    except MyError as mr:
        print(mr.args[0])
    else:
        new_n = n
        while new_n != 6174:
            print(new_n)
            new_n = kaprekar_step(numerics(new_n))
        print('6174')
    
#kaprekar_loop(8654)
#kaprekar_loop(6174)
kaprekar_loop(int(input()))
#kaprekar_loop(1111)