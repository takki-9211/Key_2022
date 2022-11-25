from flask import Flask
from flask import render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#アプリケーション作成
app = Flask(__name__) #アプリケーションのインスタンス化・実体化


@app.route("/")
def quest():
    return render_template('quest.html')

@app.route("/logger")
def logger():
    return render_template('logger.html')

#習熟度の分類結果の表示ページを新しく作るか迷い中
@app.route('/result')
def result():
    return render_template('result.html')
