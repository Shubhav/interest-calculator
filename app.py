from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/aboutus')
def aboutus():
	return render_template('aboutus.html')
	
@app.route('/si')
def si():
	return render_template('si.html')
	
@app.route('/ci')
def ci():
	return render_template('ci.html')

@app.route('/sip')
def sip():
	return render_template('sip.html')

@app.route('/calculatesi',methods = ['POST'])
def calculatesi():
	p=int(request.form['amount'])
	t=int(request.form['years'])
	r=int(request.form['rate'])
	si = int((p*t*r)/100)
	amount = int(p+si)
	return render_template('siresult.html',p=p,t=t,r=r,si=si,amount=amount)
	
@app.route('/calculateci',methods = ['POST'])
def calculateci():
	p=int(request.form['amount'])
	t=int(request.form['years'])
	r=int(request.form['rate'])
	n=int(request.form['compounded'])
	amount=int(p*(pow((1+(r/(100*n))),n*t)))
	ci=int(amount-p)
	return render_template('ciresult.html',p=p,t=t,r=r,n=n,ci=ci,amount=amount)

if __name__ == "__main__":
	app.run(debug=True)

'''	
if __name__ == '__main__':
	app.run(port=5000, host='localhost', debug=True)
'''
