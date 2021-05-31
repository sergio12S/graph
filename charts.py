from graphviz import Digraph
import os.path
from gremlin_python.process.traversal import T
from envconnect import RemoteGremlin


rg = RemoteGremlin("172.17.0.2")
rg.open()
rg.sharepoint("/home/serg/projects/Bigdata/graph/data", "/data/")
g = rg.g


def test_createGraphvizGraph():
    graphmlFile = "data/tinerpop-modern.xml"
    shared = rg.share(graphmlFile)
    g.V().drop().iterate()
    g.io(shared).read().iterate()

    dot = Digraph(comment='Modern')

    # get vertice properties including id and label as dicts
    for vDict in g.V().valueMap(True).toList():
        vId = vDict[T.id]
        vLabel = vDict[T.label]
        gvLabel = r"%s\n%s\nname=%s" % (vId, vLabel, vDict["name"][0])
        if "age" in vDict:
            gvLabel = gvLabel+r"\nage=%s" % (vDict["age"][0])
        dot.node("node%d" % (vId), gvLabel)
    # loop over all edges
    for e in g.E():
        eDict = g.E(e.id).valueMap(True).next()
        geLabel = r"%s\n%s\nweight=%s" % (e.id, e.label, eDict["weight"])
        # add a graphviz edge
        dot.edge("node%d" % (e.outV.id), "node%d" % (e.inV.id), label=geLabel)
    # modify the styling see http://www.graphviz.org/doc/info/attrs.html
    dot.edge_attr.update(arrowsize='2', penwidth='2')
    dot.node_attr.update(style='filled', fillcolor="#A8D0E4")
    # print the source code
    # render without viewing - default is creating a pdf file
    dot.render('/tmp/modern.gv', view=False)
    # check that the pdf file exists
    assert os.path.isfile('/data/modern.gv.pdf')


# call the test
test_createGraphvizGraph()
