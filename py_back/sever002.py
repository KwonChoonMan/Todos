from flask import Flask , request , render_template

app = Flask(__name__)

#사용자가 입력한 값을 html로 출력
@app.route("/sample")
def sample():
    val = request.args['val']
    return render_template("sample.html" , result=val)
 

#덧셈을 입력할 화면을 출력한다
@app.route("/add_view")
def sample2_view():
    return render_template("sample2_view.html")

# /add val1=100 val2=100  # val1= 값 & val2=값
@app.route("/sample2")
def sample2():
    val1 = int(request.args['val1'])
    val2 = int(request.args['val2'])
    result = val1 + val2
    return render_template("sample2.html", result=result)


app.run()
