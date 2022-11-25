from flask import Flask
from flask import render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#アプリケーション作成
app = Flask(__name__)#アプリケーションのインスタンス化・実体化

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///key.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)#自動生成
    age = db.Column(db.String(30), nullable=False)
    job = db.Column(db.String(30), nullable=False)
    job_d = db.Column(db.String(30), nullable=True)
    exp = db.Column(db.String(30), nullable=False)
    confi = db.Column(db.String(30), nullable=False)
    lang = db.Column(db.String(30), nullable=True)


#編集中
@app.route("/", methods=['GET', 'POST'])
def quest():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('quest.html', posts=posts)

    else:
        age = request.form.get('age')
        job = request.form.get('job')
        job_d = request.form.get('job_d')
        exp = request.form.get('exp')
        confi = request.form.get('confi')
        lang = request.form.get('lang')

        id = datetime.datetime.now()
        
        new_post = Post(id=id, age=age, job=job, joB_d=job_d, exp=exp, confi=confi, lang=lang)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')


@app.route("/logger")
def logger():
    return render_template('logger.html')


#習熟度の分類結果の表示ページを新しく作るか迷い中
@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)