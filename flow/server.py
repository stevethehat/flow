import imp
import sys
import app.config as installation_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from server_base import ServerBase

class App(ServerBase):
	pass

def app_start():
	print "starting app..."

	app = App(installation_config)
	app.start()

