import os
import sys

working_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, working_directory)
from app import app as application
