# flask_page.py
"""A website using flask and HTML and css templates"""
from flask import Flask, render_template, request, redirect
from datetime import datetime
from ip2geotools.databases.noncommercial import DbIpCity

app = Flask(__name__)
now = datetime.now()


class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def __eq__(self, other):
        return (self.user_name == other.user_name) and (self.password == other.password)

    def __str__(self):
        return self.user_name + ', ' + self.password


class Session:
    def __init__(self, ip, location):
        self.ip = ip
        self.location = location
        self.attempts = 1

    def make_attempt(self):
        self.attempts += 1

    def __eq__(self, other):
        return self.ip == other.ip

    def __str__(self):
        return 'location: ' + self.location + ', Attempts: ' + self.attempts


users = list()
sessions = list()
logged_in = False
bad_pass = False
changed_pass = False
used_before = False
wait = False

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
    return render_template('login.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"), logged_in=logged_in,
                           wait=wait)


def get_users():  # either pass a string as an argument
    with open('../wk6/users.txt', 'r') as user_file:
        users.clear()
        for entry in user_file:
            user_name, password = entry.split(',')
            users.append(User(user_name, password))


def analyze_session(session):
    if session.attempts > 15:
        return True
    else:
        return False


@app.route('/userlogin', methods=['POST'])
def try_login():
    get_users()
    global logged_in
    temp_user = User(request.form['user'], request.form['pw'])
    for user_info in users:
        if temp_user == user_info:
            logged_in = True
    if not logged_in:
        global used_before
        used_before = False
        ip = request.environ['REMOTE_ADDR']
        print(ip)
        response = DbIpCity.get(ip, api_key='free')
        location = str(response.latitude) + ', ' + str(response.longitude)
        temp_session = Session(ip, location)
        for session in sessions:
            if session == temp_session:
                session.make_attempt(1)
                used_before = True
                global wait
                wait = analyze_session(session)
        if not used_before:
            sessions.append(Session(ip, location))

    return redirect('/login')


@app.route('/change')
def change():
    print(len(users))
    return render_template('change.html', current_time=now.strftime("%m/%d/%Y, %H:%M:%S"), bad_pass=bad_pass,
                           changed_pass=changed_pass)


@app.route('/changepass', methods=['POST'])
def change_pass():
    print(len(users))
    temp_pass = request.form['pw']
    with open('../wk6/CommonPassword.txt', 'r') as common:
        for password in common:
            password = password.rstrip()
            if temp_pass == password:
                global bad_pass
                bad_pass = True
    if not bad_pass:
        temp_user = users[-1]  # last logged in
        temp_user.set_password(temp_pass)
        global changed_pass
        changed_pass = True
    return redirect('/change')


if __name__ == '__main__':
    app.run(debug=True)
