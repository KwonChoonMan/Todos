# 사용자의 요청에 응답하는 서버 : 백엔드 + 화면
# 프레임워크 . 필요한 기능들을 부품화해서 조합하는 방식 
# templates - html, static - css, jk

from flask import Flask , request, render_template

app = Flask(__name__)  # _name_는 현재 타입이다.

# 배포서술자(deployment descriptor : 함수와 주소의 쌍)

@app.route("/hello")
def aaa():
  # 플라스크 함수의 리턴은 반드시 문자열 
    return render_template("index.html")

# 현재 서버의 모든 url을 출력해라
print(app.url_map)

# 실행되는 url : 127.0.0.1:5000
# debug란 개발 모드 

# 어떤 작업을 하려면 화면을 보여준다(get) + 결과를 출력한다 (post)
# 이름을 입력받아 출력
@app.route('/name', methods=['get'])
def name_input():
    return render_template("name.html")

@app.route('/name', methods=['post'])
def name_print():
    nai = request.form['nai']
    name = request.form['irum']
    return render_template("name_result.html",name=name,nai=nai)
 #get 형식 요청 데이터 : request.args
 #post 형식 요청 데이터 : request.form



app.run(debug=True)