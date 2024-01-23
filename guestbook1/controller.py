import flask as f 
import model as m

# 플라스크 앱을 생성 인자는 현재 파일의 이해
# 플라스크의 앱(백엔드 서버)을 실행
app = f.Flask(__name__)

# 방명록을 출력 : 127.0.0.1:5000
@app.route("/name")
def list():
     guestbook = m.findall()
     # list.html에  list라 이름으로  guestbook을 넘겨준다 
     return f.render_template("list.html",list=guestbook)
    

@app.route("/write", method=['post'])
def write():
    content = f.request.form.get("content",type=str)
    m.save(content=content)
    return f.redirect("/name")


@app.route("/delete" , method=['post'])
def delete():
     gno =f.request.args.get("gno", type=int)
     m.delete(gno)
     return f.redirect("/name")





# 서버를 개발자 모드(변경하면 자동 재실행)로 실행
app.run(debug=True)