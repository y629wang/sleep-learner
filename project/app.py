from flask import Flask
from flask import render_template

from controllers.player import player_app

app = Flask(__name__)
app.register_blueprint(player_app)


@app.route('/')
def hello():
  return render_template('hello.html')


if __name__ == '__main__':
  app.run(debug=True)
