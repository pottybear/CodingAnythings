#-*- coding:utf-8 -*-

def SumIt(n):
    
    try :
        print('''\n"%s"의 각 자릿수 합은 "%s" 입니다. '''  %(n, sum(list(map(int,list(n))))) )
    
    except:
        print("Warning!! 정수만을 입력해주세요. \n")
        SumIt(input("정수를 입력해주세요. \n"))

    

SumIt(input("정수를 입력해주세요. \n"))
