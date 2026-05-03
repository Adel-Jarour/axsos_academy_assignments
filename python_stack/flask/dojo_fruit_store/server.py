from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)  
app.secret_key = 'ThisIsASecretKey'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberrys = int(request.form['strawberry'])
    raspberries = int(request.form['raspberry'])
    apples = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    sum_total = strawberrys + raspberries + apples
    print(f"Charging {first_name} {last_name} for {sum_total} fruits.")

    session['strawberrys'] = strawberrys
    session['raspberries'] = raspberries
    session['apples'] = apples
    session['first_name'] = first_name
    session['last_name'] = last_name
    session['student_id'] = student_id
    session['sum_total'] = sum_total
    
    return redirect(url_for('checkout_results'))

@app.route('/checkout_results')
def checkout_results():
        return render_template(
        "checkout.html",
        strawberrys=session.get('strawberrys'),
        raspberries=session.get('raspberries'),
        apples=session.get('apples'),
        first_name=session.get('first_name'),
        last_name=session.get('last_name'),
        student_id=session.get('student_id'),
        sum_total=session.get('sum_total')
    )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    