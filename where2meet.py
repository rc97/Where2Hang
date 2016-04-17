from flask import Flask,request,render_template,url_for,jsonify
# from flask_sqlalchemy import SQLAlchemy
import simplejson


app = Flask(__name__)

location = 'somewhere'
sound = 0 
light = 0 
temperature = 0 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


# class Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)

#     location = db.Column(db.String(128))
#     sound = db.Column(db.Numeric)
#     light = db.Column(db.Numeric)
#     temperature = db.Column(db.Integer)

#     def __init__(self, location, sound, brightness, light, temperature):
#         self.location = location
#         self.sound = sound
#         self.brightness = brightness
#         self.light = light
#         self.temperature = temperature

#     def __repr__(self):
#         return '<Data %r>' % self.location

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sensorData', methods=['POST','GET'])
def data():
	if request.method=='POST':
		global location,sound,light,temperature
		data = simplejson.parse(request.data)
		location = data.location
		sound = data.sound
		light = data.light
		temperature = data.temperature
	elif request.method=='GET':
		# send the sensor data in a response to the website
		return jsonify(sound=sound,light=light,temperature=temperature)


if __name__ == '__main__':
    app.run(debug=True)