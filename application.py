""" https://github.com/techwithtim/Flask-Web-App-Tutorial/tree/main/website will be used as an starting point for the project
"""
from email.mime import application
from website import create_app

app = create_app()
application = app

if __name__ == '__main__':
    app.run(debug=True)
