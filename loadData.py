from envconnect import RemoteGremlin

rg = RemoteGremlin("172.17.0.2")
rg.open()


def load_graph():

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


if __name__ == "__main__":
    load_graph()
