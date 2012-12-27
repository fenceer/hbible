import os

for f in os.listdir(os.path.split(__file__)[0]):
    module_name, ext = os.path.splitext(f)
    if not module_name.startswith('__') and ext == '.py':
        __import__(__name__ + '.' + module_name, fromlist=module_name)
        
