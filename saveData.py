from envconnect import RemoteGremlin
import os

rg = RemoteGremlin("172.17.0.2")
rg.open()


def save_graph():
    graphmlPath = "data/A-Fish-Named-Wanda.xml"
    g = rg.g
    # drop the existing content of the graph
    g.V().drop().iterate()
    g.addV("Fish").property("name", "Wanda").iterate()
    g.io(graphmlPath).write().iterate()
    print("wrote graph to %s" % (graphmlPath))
    # check that the graphml file exists
    assert os.path.isfile(graphmlPath)


if __name__ == "__main__":
    save_graph()
