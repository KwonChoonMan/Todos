from flask import Flask, request, render_template
import datetime
app = Flask(__name__)
# 태어난 년도를 입력받아 나이를 출력
# 년도를 입력하는 화면 
@app.route("/nai_view")
def nai_view():
    return render_template("nai_view.html")

# 결과를 출력하는 화면 
@app.route("/nai_result")
def nai_result():
 this_year = datetime.datetime.now().year
 birth_year = int(request.args['birth_year'])
 nai = this_year - birth_year
 return render_template('nai_result.html', nai=nai)
app.run()

# http 상대코드
# 200 - 연결 성공
# 400 - 잘못된 요청(작업시작X)
# 403 - 권한이 없음
# 404 - 파일이 없음(not found)
# 405 - 매소드가 오류
# 500 - 작업중 오류 