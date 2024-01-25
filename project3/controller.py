import flask as f  
import dao
#create get-post
#read   get
#update  get(/read)-post
#delete  get(/read)-post

# get html을 보내준다
# post 처리 후 이동한다
# 컨트롤러 구성
# 1. 주소 지정
# 2. request에서 값을 꺼낸다
# 3. dao를 부른다
# 4. html 또는 redirect한다
app = f.Flask(__name__)

@app.route("/")
def list():
    board_list= dao.findall()
    return f.render_template("list.html", list=board_list)

@app.route("/write")
def view_write():
    return f.render_template("write.html")


@app.route("/write", methods=['post'])
def write():
    nickname = f.request.form.get('nickname', type=int)
    title = f.request.form.get('title', type=str)
    content = f.request.form.get('content',type=str)
    dao.save(nickname=nickname, title=title, content=content)
    return f.redirect("/")

# /read?bno=111
@app.route("/read")
def read():
    bno = f.request.form.get('bno', type=int)
    board = dao.findone(bno)
    return f.render_template("read.html", board=board)

# /read에서 내용을 바꾸고 변경버튼 클릭
@app.route("/update", methods=['post'])
def update():
    bno = f.request.form.get('bno', type=int)
    title = f.request.form.get('title', type=str)
    content = f.request.form.get('content',type=str)
    dao.update(bno=bno, title=title, content=content)
    return f.redirect("/")

@app.route("/delete", methods=['post'])
def delete():
    bno = f.request.form.get("bno", type=int)
    dao.delete(bno=bno)
    return f.redirect("/")

app.run(debug=True)