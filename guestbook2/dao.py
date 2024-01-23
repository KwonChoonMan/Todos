import datetime
# 웹프로그래밍을 이렇게 만들자 : MVC
# Model: 데이터 -> model의 조작을 담당하는 파일(Dao)
# View : 화면 
# Controller : 모델과 뷰를 연결한다 
guestbook= []
gb = dict(gno=1, nickname='관리자', content='욕설,비방은 경고없이 삭제합니다',writeday='2024-01-23')
guestbook.append(gb)
# 일련번호는 보통 key로 사용된다
# 문자열은 오타 위험이 있어도 보통 key는 숫자 
gno = 2

#crd
def save(nickname : str, content:str)-> bool:
    global gno 
    writeday= datetime.datetime.now().date()
    gb = dict(gno=gno, nickname=nickname, content=content, writeday=writeday)
    guestbook.append(gb)
    gno+=1
    return True


def findall()->list:
    return guestbook

# return : 함수를 종료하고 결과 값을 남겨라 
def delete(gno:int)->bool:
    for gb in guestbook:
        if gb['gno']==gno:
         guestbook.remove(gb)
         return True
    return False