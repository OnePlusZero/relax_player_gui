import sys, os
if sys.executable.endswith('pythonw.exe'):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.path.join(os.getenv('TEMP'), 'stderr-{}'.format(os.path.basename(sys.argv[0]))), "w")
    
from flask import Flask  
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app, width=800, height=520) # add app and parameters


@app.route("/")
def hello():  
    return render_template('index.html')




if __name__ == "__main__":
    # app.run() for debug
    ui.run()