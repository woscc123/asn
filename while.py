# while

print('10개의 쿠폰을 모으면 치킨1마리가 공짜!')

client='한유빈'
count=1
while 10>count>=1:
    count+=1
    print('{0}님 쿠폰 {1}개를 모았습니다.'.format(client,count))
    # 등호조심
    if count==10: 
        print('{0}님 치킨 한마리 드립니다.'.format(client))

#등호하나는 오류
#expected an indented block :
#들여쓰기 빈공간 잘못쓰면 발생하는 오류



    # 아니다 !=
    # 아니면 계속출력
    # 내가맡긴물건찾기

client='한유빈'
notme='asdf'
while notme!=client:
    print('{0}님이 아닙니다.'.format(client))
    notme=input('누구세요?')    

    # 꺨 때 까지 계속 울리는 알람
client='한유빈'
count=1

while True:
    count+=1
    print('{0}님 기상시간입니다.(호출{1}회)'.format(client,count))

    