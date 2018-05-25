from flask import Flask,request, render_template, url_for
from linkDB import *

app = Flask(__name__)

from views import *

# home page
#app.add_url_rule('/', 'homePage', home)
@app.route('/')
def home():
	print('Home page request  ')
	return render_template('index.html', cities=cityObject, states=state)

# for starting the weather app
#app.add_url_rule('/startWeatherProcess', methods=['post'], 'startApp', startApp)

@app.route('/startWeatherProcess', methods=['GET','POST'])
def startApp():
	if request.method == 'POST' :
		user = request.form['name']
		key = request.form['password']
		if (user == 'harkishen' or user == 'harkishen singh' or user == 'pratik' or user=='pratik srichandan') and \
		key == 'socialyticsCompany' :

			print('User authonticated as ' + user)

			print('User '+user+' Requested to start the Application')
			obj = Links_to_Database()
			for i in state :
			    for j in cityObject :

			        obj.asking(j,i)
			        obj.further_info()
			        obj.displaying()
			        obj.object_creation_apending()

			print('\n\n\n\nSuper array of all weathers...\n\n')
			print(objArr)
			print('\nperforming all checks...\n')
			checks()

			return '<h3>Your Web Weather Application has been Completed Successfully. All Good.!</h3>'
		else :
			print('User Authontication Failed.! Inputed User : '+user)


if __name__ == '__main__' :
	app.debug = True
	app.run('0.0.0.0', '8888')
