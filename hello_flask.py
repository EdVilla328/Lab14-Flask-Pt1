from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '''
<p>Kevin: AFK (Away From Keyboard)</p>
<p>Joshua: FPS (Frames Per Second)</p>
<p>Zack: OWCA (Organization Without a Cool Acronym)</p>
'''

@app.route('/eduardo')
def eduardo():
    acronym = 'DPS (Damage Per Second)'
    return render_template('template.html', acronym=acronym)