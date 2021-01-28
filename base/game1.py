import random
import time

def shuffle():
    while True:
        try:
            data = ['꽝', '피자', '치킨', '사탕']
            random.shuffle(data)
            g1=int(input('1~4 중 입력하세요> '))
            print('-' * 35)
            for x in range(1, 4):
                print(x)
                time.sleep(1)
            print('!!축하합니다. ','*',data[g1],'*','이(가) 당첨되셨습니다!!', sep='')
            break
        except ValueError:
            print('-' * 35)
            print('★잘못 입력하셨습니다★')
            print('-' * 35)
