print("--- Import helpers ---")

from . import scrapping

#to assure that reload(helpers) reloads everything in the folder.
from importlib import reload
reload(scrapping)

#to not have to import each file separetly.
from .scrapping import *