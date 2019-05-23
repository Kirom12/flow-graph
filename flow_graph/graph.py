import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

import datetime
import os
from flow_graph.database import db_session
from flow_graph.models import FlowForm

bp = Blueprint('graph', __name__)

@bp.route('/')
def index():
    data = FlowForm.query.all()

    return render_template('graph/index.html', datas=data)


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
        form = FlowForm(
            request.form['activity'],
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
        db_session.add(form)
        db_session.commit()

    return render_template('graph/form-validation.html')