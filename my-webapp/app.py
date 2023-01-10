import os
from flask import Flask

def create_app():
	app = Flask(__name__)

	#define what happens when domain is access
	@app.route("/")
	def main():
		return "You've just setup your first flask app in Docker!"
		return app

	@app.route("/how are you?")
	def hello():
		return "I am good, how are you?"
		return app

#if __name__ == "__main__":
#	app.run()

