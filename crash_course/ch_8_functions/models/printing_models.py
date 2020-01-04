#import printing_function
#import printing_function as p

#from printing_function import print_models
#from printing_function import show_completed_models

#from printing_function import print_models as pm
#from printing_function import show_completed_models as scm

from printing_function import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
