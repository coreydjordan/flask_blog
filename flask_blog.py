from random import lognormvariate
from django.shortcuts import render
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.secret_key = '59NX6KyE4DXcXeqSdGgX'

posts = [
    {
    'author':'corey jordan',
    'title' : 'blog 1',
    'content': 'first blog post',
    'date_posted':'May 5, 2022'
},
    {
    'author':'jonah jordan',
    'title' : 'blog 2',
    'content': 'second blog posted',
    'date_posted':'May 5, 2022'
        
}]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in', 'success')
            return redirect(url_for('index'))
        else:
            flash('login unsuccessful', 'danger')
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 