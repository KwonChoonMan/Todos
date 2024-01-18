from flask import Flask , request
# class -> 사용자 정의 자료함을 만드는 방법 파이썬은 모든 타입은 클래스
# _name_은 현재 파일의 이름 -> Flask 웹서버 객채를 생성
# 서버는 사용자 요청을 기다리다가 요청이 들어오면 처리해주는 프로그램이다
# Flask 웹서버는 5000번 포트로 사용자 요청을 대기한다


# decorator라고함
# 자바에선 annotation이라고함  낙인찍는거다 annotation
app = Flask(__name__)

@app.route("/hello")    # /hello 는 바깥에 보여주는 이름
def hello():      
    return "hello flask"

@app.route("/insa")
def insa():
    return "안녕하세요"
@app.route("/hello3")

def add():
 # request로 전달받은 값은 무조건 글자
 val= request.args['val']
 return val

@app.route("/hello4")
def 제곱():
   val = int(request.args ["val"])
   result = val * val
   return f'제곱 결과 : {result}입니다'



@app.route("/hello5")
def 적정체중():
   ki = int(request.args['val'])
   result = ki - 105
   return f'적정체중:{result}입니다'
 
app.run()

