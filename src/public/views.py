"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template, request, jsonify
from .forms import vstupkarty
from ..data.database import db
from ..data.models import LogUser, karty
from sqlalchemy import func
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = vstupkarty()
    if form.validate_on_submit():
        karty.create(**form.data)
    return render_template("public/karty.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/vystup',methods=['GET'])
def vystup():
    pole = db.session.query(karty.CISLO_KARTY.label("CISLO_KARTY"),func.strftime('%Y-%m-%d %H:%M', karty.TIME).label("time")).group_by(func.strftime('%Y-%m', karty.TIME)).all()
    return render_template("public/vystup.tmpl",data = pole)


@blueprint.route('/_add_numbers', methods=['GET','PUT'])
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@blueprint.route('/jquery', methods=['GET','PUT'])
def jquery_ukazka():
    return render_template('public/jquery.tmpl')