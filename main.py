#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
# app.config['SECRET_KEY'] = 'super secret'

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

@app.route('/index')
def index_p():
    line_li = []
    date_r = []
    cate_r = []
    area_r = []
    with open("ueda.txt", encoding="utf-8") as f:
        for line in f:
            items = line.rstrip().split('\t')
            line_li.append(items)
    for d in line_li:
        date_r.append(d[9][:7])
        cate_r.append(d[3])
        area_r.append(d[2])
    date = sorted(list(set(date_r)), reverse=True)  # set()で集合に、要素の重複がなくなる
    cate = sorted(list(set(cate_r)))
    area = sorted(list(set(area_r)))
    return render_template('index.html', date=date, cate=cate, area=area)

@app.route('/list')
def list_p():
    para = request.args.get('para')
    line_li = []
    with open("ueda.txt", encoding="utf-8") as f:
        for line in f:
            items = line.rstrip().split('\t')
            if para == items[9][:7] or para == items[3] or para == items[2]:
                line_li.append(items)
    return render_template('list.html', line_li=line_li, para=para)

# おまじない
if __name__ == "__main__":
    app.run(debug=True)
