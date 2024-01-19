from flask import Flask , request , render_template

app =Flask(__name__)

# 이름과 사는 도시를 입력받아 출력하는 웹을 작성하시오

@app.route("/name1",methods=['get'])
def name1_input():
    return render_template('name1.html')

@app.route('/name1', methods=['post'])
def name1_print():
    name= request.form['irum']
    city= request.form['city']
    return render_template("name_result.html", name=name,city=city)

app.run(debug=True)