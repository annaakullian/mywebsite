import os

from flask import Flask, render_template

#lol

app =  Flask(__name__)
app.secret_key="annabanana"
app.config.from_object(__name__)

@app.route('/', methods=['GET'])	
def allimages():
	return render_template("index.html")

@app.route('/research', methods=['GET'])
def research():
	return render_template("research.html")

@app.route('/educator', methods=['GET'])
def educator():
	return render_template("educator.html")

@app.route('/softwareengineer', methods=['GET'])
def softwareengineer():
	return render_template("softwareengineer.html")

@app.route('/play', methods=['GET'])
def play():
	return render_template("play.html")

if __name__ == '__main__':
	PORT = int(os.environ.get("PORT", 5000))
	app.run(debug=True, host="0.0.0.0", port=PORT)

	
