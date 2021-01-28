from base.game1 import *

def start(name):
    print(name,'을(를) 시작합니다!', sep='')
def restart(name):
        while True:
            print('~'*35)
            print('1. 다시 시작')
            print('q. 메인메뉴')
            print('~' * 35)
            a=input('입력> ')
            if a=='q':
                break
            elif a=='1':
                name()
            else:
                print('★잘못 입력하셨습니다★')

