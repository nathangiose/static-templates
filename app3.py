'''from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)
if __name__ == '__main__':
    app.debug = True
    app.run()
'''


from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>')
def home(name):
    return render_template('homepage.html', name=name)



'''@app.route('/looping/<int:number>')
def looping(number):
    render_template('loopy.html', number=number)'''


'''@app.route('/mtable/<int:number>')
def looping(number):
    render_template('timestable.html', number=number)'''

'''@app.route('/timestsble/<int:number>')
def looping(num):
    render_template('loopy.html', num=num)'''

if __name__ == '__main__':
    app.debug = True
    app.run()
