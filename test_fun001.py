from fun001 import samplel , is_major,get_free,get_frees

# unit test(단위 테스트)
# 테스트하는 함수를 작성
# 테스트하는 함수는 pytest로 실행이 가능
# def test_sample():
#     assert samplel()==10

# def text_round():
#     assert round(2.5)==2

# def test_sample():
#    assert is_major(20) is True
#    assert is_major(18) is True
#    assert is_major(15) is False

# 나이를 입력받아 입장료를 리턴하는 함수
# 25-64세면 3000원 기타는 무료
# def test_get_free():
#     assert get_free(70)==0
#     assert get_free(50)==3000
#     assert get_free(15)==0

# 입장료는 3000원이다 10명이면 1인당 2400원이다
#  인원수를 입력받아 요금을 출력
def test_get_frees():
    assert get_frees(10)==24000
    assert get_frees(9)==27000
    assert get_frees(5)==15000