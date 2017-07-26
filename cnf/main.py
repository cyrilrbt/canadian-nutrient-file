import warnings
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_script import Server, Manager

import cnf.settings
import cnf.scripts


# pymongo has issues...
warnings.filterwarnings("ignore", category=DeprecationWarning, module='mongoengine')


def setup_app():
    app = Flask(
        __name__,
        template_folder=cnf.settings.TEMPLATE_FOLDER,
    )
    app.config.from_object(cnf.settings)
    with app.app_context():
        app.db = MongoEngine(app)

        app.manager = Manager(app)
        app.manager.add_command(
            'runserver',
            Server(
                host=app.config['FLASK_BIND'],
                port=app.config['FLASK_PORT']
            )
        )
        app.manager.add_command('import', cnf.scripts.Import())

    return app


def main():  # pragma: no cover
    app = setup_app()

    # Import your views!
    with app.app_context():
        import cnf.views

    app.manager.run()
