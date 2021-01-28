from random import sample

def lotto():
    while True:
        try:
            lotto = sample(range(1, 46), 6)
            lotto.sort()
            print('1~45까지 수 중 6개,')
            a=input('쉼표로 구분해 입력하세요> ').split(',')
            a.sort()
            sum=0
            print('-' * 35)
            if len(a)>6 or len(a)<6:
                print('★6개의 번호를 입력하세요★')
                print('-'*35)
            else:
                for x in range(6):
                    b=int(a[x])
                    if b in lotto:
                        sum+=1
                print('!!축하합니다. ',sum,'개 맞췄습니다!!',sep='')
                print('로또 번호: ',lotto)
                break
        except ValueError:
            print('★잘못 입력하셨습니다★')
            print('-' * 35)
        except IndexError:
            print('★잘못 입력하셨습니다★')
            print('-' * 35)


