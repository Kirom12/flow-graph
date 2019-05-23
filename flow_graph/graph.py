import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

import datetime
import os
from flow_graph.db import get_db

bp = Blueprint('graph', __name__)

@bp.route('/')
def index():
    print(datetime.datetime.now())

    db = get_db()

    data = db.execute(
        'SELECT * FROM form_data ORDER BY id DESC'
    ).fetchall()

    format_data = []

    for i, row in enumerate(data):
        format_data.append({})
        for key in row.keys():
            format_data[i][key] = row[key]

        format_data[i]['want'] = 'Oui' if format_data[i]['want'] == 1 else 'Non'

        format_data[i]['theoretical_flow'] = theoretical_flow_calculation(row['difficulty'], row['skill'])
        format_data[i]['flow_indication'] =  round((row['skill_feel'] + row['immersed'] + row['objective'] + row['control'] + row['other'] + row['time'] + row['fail'] + row['learn'])/8,1)

    return render_template('graph/index.html', datas=format_data)


def theoretical_flow_calculation(difficulty, skill_level):
    """
    Calculation of theoretical flow due of difficulty and skill level
    @TODO Calculation with average of difficulty and skill level
    :param difficulty:
    :param skill_level:
    :return:
    """
    if difficulty > 3:
        if skill_level > 3:
            return "flow"
        if skill_level < 3:
            return "angoisse"
        if skill_level == 3:
            return "stimulé"
    if difficulty == 3:
        if skill_level > 3:
            return "contrôle"
        if skill_level < 3:
            return "inquetude"
        if skill_level == 3:
            return "neutre"
    if difficulty < 3:
        if skill_level > 3:
            return "relaxation"
        if skill_level < 3:
            return "apathie"
        if skill_level == 3:
            return "ennui"

@bp.route('/form')
def flow_form():
    return render_template('graph/form.html')

@bp.route('/form-validation', methods=['POST'])
def flow_form_validation():
    print(request.form['activity'])

    if request.method == 'POST':
        db = get_db()

        db.execute(
            'INSERT INTO form_data (date, activity, category, difficulty, skill, skill_feel, immersed, objective, control, other, time, fail, learn, want, happiness, social) VALUES (datetime("now", "localtime"),?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (request.form['activity'],
             request.form['category'],
             request.form['difficulty'],
             request.form['skill'],
             request.form['skill-feel'],
             request.form['immersed'],
             request.form['objective'],
             request.form['control'],
             request.form['other'],
             request.form['time'],
             request.form['fail'],
             request.form['learn'],
             request.form['want'],
             request.form['happiness'],
             request.form['social'])
        )

        db.commit()

    return render_template('graph/form-validation.html')