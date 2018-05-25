from flask import render_template, request
from linkDB import *

def home(request):
	return render_template('index.html', cities=cityObject, states=state)



