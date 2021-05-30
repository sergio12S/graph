from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import\
    DriverRemoteConnection
import json


to_string = json.dumps


def main():
    remoteConn = DriverRemoteConnection('ws://172.17.0.2:8182/gremlin', 'g')
    g = traversal().withRemote(remoteConn)

    # Count
    print(
        "Count: " + to_string(
            g
            .V()
            .count()
            .next()
        )
    )
    # Check values
    print(
        g.V().both().name.toList()
    )

    # Map and Return array dictionary nested
    print(g.V().valueMap().toList())

    # Group by
    # print(g.V().group().by('name').toList())
    remoteConn.close()


if __name__ == "__main__":
    main()
