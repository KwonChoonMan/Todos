def samplel():
    return 10 

# 나이를 입력받아 생년/미성년을 판단
def is_major(nai:int)-> bool:
    return nai>=18

def get_free(nai:int)->int:
    if nai>24 and nai<65:
        return 3000
    return 0

def get_frees(personnel:int)->int:
    if personnel<10:
        return personnel*3000
    return personnel *2400
