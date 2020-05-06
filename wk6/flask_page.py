# flask_page.py
"""A website using flask and HTML and css templates"""
from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

posts = [
    {
        'title': 'Why does the corsair stutter?',
        'author': 'First-Mate Timmy',
        'color': 'blue',
        'post': "Prow scuttle parrel provost Sail ho "
                "shrouds spirits boom mizzenmast yardarm."
                " Pinnace holystone mizzenmast quarter crow's "
                "nest nipperkin grog yardarm hempen halter furl. "
                "Swab barque interloper chantey doubloon starboard "
                "grog black jack gangway rutters"
    }, {
        'title': 'Nipperkin bilge rat',
        'author': 'Brik, the Depraved',
        'color': 'orange',
        'post': "Hogshead bilge rat rutters Nelsons folly lee "
                "mizzenmast Brethren of the Coast bring a spring "
                "upon her cable doubloon belaying pin. Gold Road "
                "Jack Ketch cackle fruit gibbet gangway belaying "
                "pin Blimey Jack Tar gangplank handsomely. Lass "
                "coxswain overhaul heave down long clothes Blimey "
                "squiffy blow the man down coffer plunder."
    }, {
        'title': 'Round capstan transom ho belay',
        'author': 'Davy Jones',
        'color': 'cyan',
        'post': "Hands jack tender dead men tell no tales tack code"
                " of conduct me maroon avast grapple. List lanyard "
                "boom come about aye American Main spyglass crow's "
                "nest sloop blow the man down. Jury mast red ensign "
                "crack Jennys tea cup matey chandler yard capstan "
                "lanyard prow Spanish Main."
    }
]

leader_board = ['Davy Jones', 'John Largeparrot', 'Admiral John']


@app.route('/')
def index():
    return render_template('index.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"), posts=posts,
                           leader_board=leader_board)


@app.route('/about')
def about():
    return render_template('about.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"))


@app.route('/makepost', methods=['POST'])
def make_post():
    new_post = {
        'title': request.form['PostTitle'],
        'author': request.form['UserName'],
        'color': request.form['Color'],
        'post': request.form['PostBody']
    }
    posts.append(new_post)
    export_data(posts)
    return redirect('/')


def export_data(object_list):
    with open('../wk6/output.txt', 'w') as output:
        for dicts in object_list:
            output.write('Title: ' + str(dicts.get('title')) + '\n')
            output.write('Author: ' + str(dicts.get('author')) + '\n')
            output.write('Post: ' + str(dicts.get('post')) + '\n\n')


@app.route('/login')
def login():
    return render_template('login.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"))


def get_user_pass():   # either pass a string as an argument
    with open('../wk6/users.txt', 'r' ) as user_file:
        pass  # or hou can return the dictionary from within the file


if __name__ == '__main__':
    app.run(debug=True)
