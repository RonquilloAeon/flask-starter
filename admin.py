from app.sample import blueprint as sample_blueprint
from app.sample import views
from flask import Flask
from flask_admin import Admin
import config

app = Flask(__name__)


# Blueprints
app.register_blueprint(sample_blueprint)


# Admin
admin = Admin(app, name='admin', template_mode='bootstrap3')


# Add views
admin.add_view(views.SampleView(name='Sample', endpoint='sample'))


# Let's go!
app.debug = config.DEBUG
app.run()
