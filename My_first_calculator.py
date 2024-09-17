###My first calculator

# 숫자를 입력하는 칸
first_number = int(input("숫자를 입력하세요 :  "))
work = input(("원하는 작업을 선택하세요 '+', '-', '*', '/'"))
second_number = int(input("숫자를 입력하세요 : "))

# 더하기
if work == "+":
    print("결과입니다 : ", first_number+second_number)
# 빼기
elif work == "-":
    print("결과입니다 : ", first_number-second_number)
# 곱하기
elif work == "*":
    print("결과입니다 : ", first_number*second_number)
# 나누기
elif work == "/":
    if second_number == 0:
        print("0으로는 나눌 수 없습니다.")
        # '0' 을 분자로 사용할 떄는 나눗셈이 가능하다. 
        # 0/5는 0이 결과로 나오기 떄문에 문제가 되지 않는다.
    else :
        print("결과입니다 : ", first_number/second_number)
else : 
    print("올바른 연산자를 입력하세요")