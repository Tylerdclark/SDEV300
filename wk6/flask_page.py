# my_webpage.py
"""A website using flask and HTML and css templates"""
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

posts = [
    {
        'title': 'Why does the corsair stutter?',
        'author': 'First-Mate Timmy',
        'post': "Prow scuttle parrel provost Sail ho "
                "shrouds spirits boom mizzenmast yardarm."
                " Pinnace holystone mizzenmast quarter crow's "
                "nest nipperkin grog yardarm hempen halter furl. "
                "Swab barque interloper chantey doubloon starboard "
                "grog black jack gangway rutters"
    }, {
        'title': 'Nipperkin bilge rat',
        'author': 'Brik, the Depraved',
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


if __name__ == '__main__':
    app.run(debug=True)
