borad_list=[]
bno=1

def write(title:str, content:str,nickname:str):
    global bno
    b=dict(bno=bno,title=title,content=content,nickname=nickname,readcnt=0)
    borad_list.append(b)
    bno+=1
    return True


# 작업을 2개 -조회수 증가
def findone(bno:int):
    for board in borad_list:
        if board['bno']==bno:
            board['readcnt']=board['readcnt']+1
            return None