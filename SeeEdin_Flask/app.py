from flask import Flask, request, flash, url_for, redirect, render_template

app = Flask(__name__)

@app.route('/')
def welcome(name=None):
    return render_template('Base.html', name=name)


@app.route('/about')
def about(name=None):
    return render_template('about.html', name=name)

if __name__ == '__main__':
	app.run()
