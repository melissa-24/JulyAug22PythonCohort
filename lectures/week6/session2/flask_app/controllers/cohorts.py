from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.cohort import Cohort
from flask_app.models.trainer import Trainer
from flask_app.models.user import User

@app.route('/cohorts/')
def cohorts():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theCohorts = Cohort.getAll()
        print(theCohorts)
        theTrainers = Trainer.getAll()
        return render_template('cohorts.html', user=theUser, cohorts=theCohorts, trainers=theTrainers)
    
@app.route('/addCohort/')
def addCohort():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data = {
            'id': session['user_id']
        }
        theUser = User.getOne(data)
        theTrainers = Trainer.getAll()
        return render_template('addCohort.html', user=theUser, trainers=theTrainers)

@app.route('/createCohort/', methods=['post'])
def createCohort():
    data = {
        'name': request.form['name'],
        'topic': request.form['topic'],
        'length': request.form['length'],
        'trainer_id': request.form['trainer_id']
    }
    Cohort.save(data)
    return redirect('/cohorts/')