import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from backend.src.api import app
from backend.src.database.models import db

MIGRATION_DIR = os.path.join('backend', 'src', 'migrations')

migrate = Migrate(app, db, directory=MIGRATION_DIR)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
