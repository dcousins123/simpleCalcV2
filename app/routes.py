from flask import render_template, request
from app import app, db
from app.forms import CalculatePaint
from app.models import calculation


@app.route('/')
def main():
    form = CalculatePaint()
    return render_template("index.html", form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/calculations')
def calculations():
    Calculations = calculation.query.all()
    return render_template('calculations.html', title='Calculations', rows=Calculations)

@app.route('/calculate', methods=['POST'])
def calculate():
    form = CalculatePaint()
    num1 = request.form['num1']
    num2 = request.form['num2']
    result = float(num1) * float(num2)
    Calculation = calculation(num1=int(num1), num2=int(num2), result=int(result))
    if form.validate_on_submit():
        form.populate_obj(Calculation)
        db.session.add(Calculation)
        db.session.commit()
        flash(result)
        flash('Congratulations, calculation added to database!')

    return render_template('index.html', result=result, title='Home', form=form)
   
