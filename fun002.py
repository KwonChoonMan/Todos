# 숫자를 제곱하는 함수
def  asd(num:int)->int:
    # int가 아니면 실패 -> int 어떻게? 실패는 뭐지>
    if isinstance(num, int)==False:
     return 0
    return num*num

# 파이썬, jv은 동적타임
# 자바는 정적타입  