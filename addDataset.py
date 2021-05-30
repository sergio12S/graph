from envconnect import RemoteGremlin


def load_graph():
    rg = RemoteGremlin("172.17.0.2")
    rg.open()
    # change to your shared path
    rg.sharepoint("/home/serg/projects/Bigdata/graph/data", "/data/")
    g = rg.g
    graphmlFile = "data/air-routes-small.xml"
    shared = rg.share(graphmlFile)
    # drop the existing content of the graph
    g.V().drop().iterate()
    # read the content from the air routes example
    g.io(shared).read().iterate()
    vCount = g.V().count().next()
    print("%s has %d vertices" % (shared, vCount))
    assert vCount == 47


load_graph()
