from flask import Blueprint

blueprint = Blueprint('simple_page', __name__, template_folder='templates')
