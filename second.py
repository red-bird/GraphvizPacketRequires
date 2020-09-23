import requests
from graphviz import Digraph

def getRequires(package_name_value):
    url = 'https://pypi.python.org/pypi/' + str(package_name_value) + '/json'
    try:
        data = requests.get(url).json()
        tmp = data['info']['requires_dist']
        return tmp
    except Exception:
        return None


package_name = input("Enter package name ")
dot = Digraph(comment='Usual search')
requires = getRequires(package_name)
dot.node(package_name, package_name)
for i in range(len(requires)):
    dot.node(str(i), str(requires[i]))
    dot.edge(str(i), package_name)
print(dot.source)