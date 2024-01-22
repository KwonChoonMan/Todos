import flask as f
import model as m 
app = f.Flask(__name__)
# 목록
@app.route("/")
def list():
    result = m.list()
    return f.render_template("/list.html",list=result)

# 추가
@app.route("/write", methods=['post'])
def write():
    writer = f.request.form.get('writer',type=str)
    content = f.request.form.get('content',type=str)
    m.save(writer=writer, content=content)
    return f.redirect("/")
#삭제
@app.route("/delete", methods=['post'])
def delete():
    gno = f.request.form.get('gno',type=int)
    m.delete(gno=gno)
    return f.redirect("/")

#변경
@app.route("/update", methods=['post'])
def update():
    gno = f.request.form.get('gno',type=int)
    content = f.request.form.get('content',type=str)
    m.update(gno=gno, content=content)
    return f.redirect("/")

app.run(debug=True)