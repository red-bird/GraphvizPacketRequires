import requests
from graphviz import Digraph
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz 2.44.1/bin/'


checker = list()

def getRequires(package_name_value):
    url = 'https://pypi.python.org/pypi/' + str(package_name_value) + '/json'
    data = requests.get(url).json()
    tmp = data['info']['requires_dist']
    return tmp


def getName(name):
    return str(name).split(' ')[0]


def addRequires(requires, dot_ref, parent_name):
    if requires is not None:
        for i in range(len(requires)):
            tmp_name = str(requires[i])
            dot_ref.node(tmp_name, tmp_name)
            dot_ref.edge(tmp_name, parent_name)
            #print(getName(requires[i]))
            tmp_name_noversion = getName(requires[i])
            global checker
            if tmp_name_noversion not in checker:
                checker.append(tmp_name_noversion)
                addRequires(getRequires(tmp_name_noversion), dot_ref, tmp_name)



package_name = input("Enter package name ")
dot = Digraph(comment='The Round Table')
addRequires(getRequires(package_name), dot, package_name)

print(dot.source)
dot.render('graph.gv', view=True, cleanup=True)
