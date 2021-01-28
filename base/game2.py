import random

def choice():
    while True:
        try:
            d={'가위바위':'컴퓨터','가위보':'내',
               '바위가위':'내','바위보':'컴퓨터',
               '보가위':'컴퓨터','보바위':'내'}
            b = random.choice(['가위', '바위', '보'])
            a=input('가위바위보 중 입력하세요> ')
            print('-' * 35)
            if a==b:
                print('!!무승부입니다!!')
            elif d[a+b]=='내':
                print('!!축하합니다. ',d[a+b],'가 컴퓨터를 이겼습니다!!',sep='')
            elif d[a+b]=='컴퓨터':
                print('!!아쉽네요..', d[a + b],'가 나를 이겼습니다!!', sep='')
            print('나:', a, '/','컴퓨터:', b)
            break
        except KeyError:
            print('*잘못 입력하셨습니다*')
            print('-' * 35)