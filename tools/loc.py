import os
os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

def get_loc(path):
    loc = 0
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".c") or file.endswith(".h"):
                loc += len(open(os.path.join(root, file)).readlines())
    return loc

for d in os.listdir():
    if os.path.isdir(d):
        print(d, get_loc(d))