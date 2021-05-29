from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import\
    DriverRemoteConnection
import json


to_string = json.dumps


def main():

    g = traversal().withRemote(DriverRemoteConnection(
        'ws://172.17.0.2:8182/gremlin', 'g'))

    g.addV('person').property('name', 'serg').as_('m'). \
        addV('person').property('name', 'alex').as_('v'). \
        addE('knows').from_('m').to('v').iterate()

    print(
        "marko: " + to_string(g.V().has('person', 'name', 'serg')
                              .valueMap().
                              next())
    )

    print(
        "who marko knows: " + to_string(g.V().has('person', 'name', 'serg')
                                        .out('knows')
                                        .valueMap()
                                        .next())
    )


if __name__ == "__main__":
    main()
