#-*- coding:utf-8 -*-

def intinput(): # a에 숫자를 담는다
    global a
    a = input("정수를 입력해주세요. \n")
    
    try :
        int(a)
        
    except :
        print("Warning!! 정수만 입력해주세요. \n")
        intinput()

    return a


def SumIt():
    intinput()
    obj = 0

    for b in range(len(a)):
        obj = obj + int(a[b])

    return print('''\n"%s"의 각 자릿수 합은 "%s" 입니다 ''' %(a,obj))

SumIt()
