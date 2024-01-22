import datetime

# 리스트 : 번호,작성자,내용,날짜
guestbook = []
gno = 1

# 추가
def save(writer:str, content:str):
    global gno
    writeday = datetime.datetime.now().date()
    gb= dict(gno=gno, writer=writer, content=content, writeday=writeday)
    guestbook.append(gb)
    gno+=1

# 목록
def list():
    return guestbook


# 삭제
def delete(gno:int):
    for gb in guestbook:
     if gb['gno']==gno:
        guestbook.remove(gb)

# 변경 : 번호 내용
def update(gno:int, content:str):
   for gb in guestbook:
      if gb['gno']==gno:
         gb['content']=content