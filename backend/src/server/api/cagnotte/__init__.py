
from flask_restx import Namespace

ns = Namespace('cagnotte', description='Cagnotte description')

# Okay, this is ugly.
# But ! ... Well no time for hardcore stuff
# Will kaizen later if needed


def load():
    from .cagnotte_item import CagnotteItem

ns.load = load
