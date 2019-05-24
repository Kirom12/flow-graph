
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

from flow_graph.database import db_session
from flow_graph.models import FlowForm
from sqlalchemy import desc

bp = Blueprint('graph', __name__)

@bp.route('/')
def index():
    data = FlowForm.query.order_by(desc(FlowForm.id)).all()

    return render_template('graph/index.html', datas=data)

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
            request.form['anxiety'],
            request.form['social'])
        db_session.add(form)
        db_session.commit()

    return render_template('graph/form-validation.html')