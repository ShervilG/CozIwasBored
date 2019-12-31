from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def main_page():
	return "working !"

@app.route('/api/put_data(<name>,<loc>)',methods=['POST','GET'])
def put_data(name,loc):
	try:
		connection = sqlite3.connect("data.db")
		cursor = connection.cursor()
		cursor.execute('select max(id) from user')
		x = cursor.fetchall()
		json_data = {}
		id1 = x[0][0] + 1
		cursor.execute('insert into user values(?,?,?)',(id1,name,loc))
		connection.commit()
		return "successfully added !"
	except:
		return "error occured while adding !"

@app.route('/api/get_data(<name>)',methods=['POST','GET'])
def get_data(name):
	connection = sqlite3.connect("data.db")
	cursor = connection.cursor()
	cursor.execute('select * from user where name = ?',(name,))
	x = cursor.fetchall()
	json_data = {}
	i = x[0]
	json_data['id'] = i[0]
	json_data['name'] = i[1]
	json_data['location'] = i[2]
	return jsonify(json_data)

if __name__ == '__main__':
	app.run(debug = True)