import requests
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

import os

bp = Blueprint('graph', __name__)

@bp.route('/')
def index():
    headers = {
        "Authorization" : "Bearer " + current_app.config.get("PERSONAL_TOKEN")
    }
    r = requests.get(current_app.config.get("TYPEFORM_API_URL"), headers=headers)
    data = r.json()


    #with open("tests/files/api_request.json") as f:
    #    data = json.load(f)

    clean_data = []

    for x in data['items']:
        if 'answers' in x:

            # Theoretical flow calculation
            theoretical_flow = theoretical_flow_calculation(x['answers'][2]['number'], x['answers'][3]['number'])
            flow_indication = round((x['answers'][4]['number'] + x['answers'][5]['number'] + x['answers'][6]['number'] + x['answers'][7]['number'] + x['answers'][8]['number'] + x['answers'][9]['number'] + x['answers'][10]['number'] + x['answers'][11]['number']) / 8, 1)

            # Save all data in a clean dict
            clean_data.append({
                'date': x['submitted_at'],
                'activity': x['answers'][0]['text'],
                'category': x['answers'][1]['choice']['label'],
                'difficulty': x['answers'][2]['number'],
                'skill': x['answers'][3]['number'],
                'skill_feel': x['answers'][4]['number'],
                'immersed': x['answers'][5]['number'],
                'objective': x['answers'][6]['number'],
                'control': x['answers'][7]['number'],
                'other': x['answers'][8]['number'],
                'time': x['answers'][9]['number'],
                'fail': x['answers'][10]['number'],
                'learn': x['answers'][11]['number'],
                'want': x['answers'][12]['boolean'],
                'happiness': x['answers'][13]['number'],
                'social': x['answers'][14]['choice']['label'],
                'theoretical_flow': theoretical_flow,
                'flow_indication': flow_indication
            })

    return render_template('graph/index.html', datas=clean_data)


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

    return render_template('graph/form-validation.html')