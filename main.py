from base.common import *
from base.game1 import *
from base.game2 import *
from base.game3 import *


print('~' * 35)
print('게임모음 관리v0.1')
while True:
    print('~' * 35)
    print('1. 복불복 게임')
    print('2. 가위바위보 게임')
    print('3. 로또 맞추기')
    print('q. 종료')
    print('~' * 35)

    a=input('입력> ')
    print('~'*35)
    if a=='q':
        break
    elif a=='1':
        start('복불복 게임')
        shuffle()
        restart(shuffle)
    elif a=='2':
        start('가위바위보 게임')
        choice()
        restart(choice)
    elif a=='3':
        start('로또 맞추기')
        lotto()
        restart(lotto)
    else:
        print('★잘못 입력하셨습니다★')




