from flask import Flask, request, render_template, redirect, url_for,os

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))
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
	si = (p*t*r)/100
	amount = p+si
	print(amount)
	return render_template('siresult.html',p=p,t=t,r=r,si=si,amount=amount)
	
@app.route('/calculateci',methods = ['POST'])
def calculateci():
	p=int(request.form['amount'])
	t=int(request.form['years'])
	r=int(request.form['rate'])
	n=int(request.form['compounded'])
	amount = p*(pow((1+(r/(100*n))),n*t))
	ci=amount-p
	return render_template('ciresult.html',p=p,t=t,r=r,ci=ci,amount=amount,n=n)
	
if __name__ == "__main__":
	app.run(debug=True)

'''	
if __name__ == '__main__':
	app.run(port=5000, host='localhost', debug=True)
	
'''