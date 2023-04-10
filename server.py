from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "poggers"


@app.route('/')
def visit_counter():
    
    
    if 'visits' in session:
        session['visits'] +=1
    else:
        session['visits'] = 0
    return render_template('index.html')


@app.route('/+_two')
def visit_counter2():
    if 'visits' in session:
        session['visits'] +=2
    else:
        session['num_visits'] = 2
    return render_template('index.html')



@app.route('/take_visits', methods=["POST"])
def take_visits ():
    num_visits =  int(request.form['v_number'])
    if 'visits' in session:
        session['visits'] += num_visits
    else:
        session['visits'] = num_visits
    
    return render_template('index.html')

@app.route('/reset_session')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
