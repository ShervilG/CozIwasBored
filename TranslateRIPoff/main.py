from flask import *
from googletrans import *
import pytesseract as pp

app = Flask(__name__)

@app.route('/')
def main_activity():
	return render_template('main.html')

@app.route('/convert',methods = ['POST','GET',])
def show_time():
	text = "text"
	up = request.files['pic']
	up.save(up.filename)
	text = pp.image_to_string(up.filename)
	if text.strip() == "":
		return "Scan again !!"
	else:
		translator = Translator()
		translated = translator.translate(text,dest='hi')
		return render_template('converted.html',tt = text,tt2 = translated.text)

if __name__ == '__main__':
	app.run(debug = True)