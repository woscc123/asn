print('5분내에 불을끄자')
print('1분마다 알려줌')
print(5)
print(4)
print(3)
print(2)
print(1)

for timer in [5,4,3,2,1]:
    print("{0}".format(timer))
    #timer 변수 후 포맷

for stopwatch in range(5,1):
    print("{0}".format(stopwatch))

# 위아래 동일문

# 목표수익이 10프로인 주식의 알림을 만들자. 1프로 오를때마다 알림
for profit in range(1,11):
    print("{0}".format(profit))

# 손절가격이 -10프로인 주식의 알림을 만들자. -1프로 내릴때마다 알림

for loss in range(-1,-11,-1):
    print("{0}".format(loss))
    # 인터넷 참고 3개를 하면된다 음수는  마지막은 증가하는 difference