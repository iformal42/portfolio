# TODO:- Design Good Proto folio Website
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from allprojects import Projects
from project_card import Card

app = Flask(__name__)
Bootstrap5(app)


@app.route('/')
def home():
    card = Card()
    return render_template('index.html', proj=card.detail)


@app.route('/project/<int:num>')
def project(num):
    p = Projects()
    return render_template('project.html', proj=p.location.get(num))


@app.route('/all_projects')
def all_projects():
    card = Card()
    return render_template('show_case.html', proj=card.detail)


if __name__ == '__main__':
    app.run(debug=True)
