import requests
import sys
from graphviz import Digraph

checker = list()

def getRequires(package_name_value):
    url = 'https://pypi.python.org/pypi/' + str(package_name_value) + '/json'
    try:
        data = requests.get(url).json()
        tmp = data['info']['requires_dist']
        return tmp
    except Exception:
        return None



def getName(name):
    return str(name).split(' ')[0]


def addRequires(requires, dot_ref, parent_name):
    if requires is not None:
        for i in range(len(requires)):
            tmp_name = getName(requires[i])
            global checker
            if tmp_name not in checker:
                dot_ref.node(tmp_name, tmp_name)
                checker.append(tmp_name)
                addRequires(getRequires(tmp_name), dot_ref, tmp_name)
            dot_ref.edge(tmp_name, parent_name)



package_name = str(sys.argv[1])
dot = Digraph(comment='Deep search')
addRequires(getRequires(package_name), dot, package_name)

print(dot.source)