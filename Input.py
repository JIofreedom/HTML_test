from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def default_page():
	return render_template('index.html')

@app.route("/login",methods=['get','post'])
def login_page():
	id = str(request.values['id'])
	idnum = int(request.values['id'][1:])
	def check_id(id):
		if len(id) != 10:
			return 0
		if not (id[0].isupper()):
			return 0
		else:
			return 1
	def check_id_num(idnum):
		if not (id[1] in "12"):
			return 0
		for x in id[2:]:
			if not x.isdigit():
				return 0
		else:
			return 1
	check_id(id)
	check_id_num(idnum)
	if check_id(id) == 1 & check_id_num(idnum) == 1:
		return render_template('result_success.html',id=request.values['id'], name=request.values['name'])
	else:
		return render_template('result_fail.html')

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)
