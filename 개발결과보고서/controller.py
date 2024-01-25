import flask as f
import dao
app = f.Flask(__name__)

@app.route("/")
def list() :
  board_list = dao.findall()
  return f.render_template("list.html", list=board_list)

@app.route('/write')
def view_write():
  return f.render_template("write.html")

@app.route("/write", methods=['post'])
def write():
  nickname = f.request.form.get("nickname", type=str)
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  dao.save(nickname=nickname, title=title, content=content)
  return f.redirect("/")


@app.route("/read")
def read():
  bno = f.request.args.get('bno', type=int)
  board = dao.findone(bno)
  return f.render_template("read.html", board=board)


@app.route("/update", methods=['post'])
def update():
  bno = f.request.form.get("bno", type=int)
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  dao.update(bno=bno, title=title, content=content)
  return f.redirect("/")


@app.route("/delete", methods=['post'])
def delete():
  bno = f.request.form.get("bno", type=int)
  dao.delete(bno=bno)
  return f.redirect("/")

app.run(debug=True)