from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import create_app, db

""" STEP-BY-STEP
1. Initializes migration support for the application.
 - python3 manage.py db init
2. The migration script is populated with changes detected automatically.
 - python3 manage.py db migrate
3. Upgrades the database.
 - python3 manage.py db upgrade
"""

app = create_app()
app.config.from_object("config.DevConfig")

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
