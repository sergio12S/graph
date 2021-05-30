# How to use janusgraph

## Run

1. Run docker

    * Simple container
    `docker run --name janusgraph-default janusgraph/janusgraph:latest`

    * Container with settings
    `docker run --name janusgraph-default \
        -e janusgraph.storage.berkeleyje.cache-percentage=80 \
        -e gremlinserver.threadPoolWorker=2 \
        -e gremlinserver.channelizer=org.apache.tinkerpop.gremlin.server.channel.WsAndHttpChannelizer \
        -p 8182:8182 \
        --mount src=/home/serg/projects/Bigdata/graph/data,target=/data,type=bind \
        janusgraph/janusgraph:latest`

2. Connecting with Gremlin Console
`docker run --rm --link janusgraph-default:janusgraph -e GREMLIN_REMOTE_HOSTS=janusgraph \
    -it janusgraph/janusgraph:latest ./bin/gremlin.sh`

3. Remote connection

    * Add connection
    `:remote connect tinkerpop.server conf/remote.yaml`
    * Close connection
    `:remote close`

## Information

* Check remote connetction
`:remote console`

## Working with console

### Create example graph

`graph = TinkerFactory.createModern()`
`g = traversal().withGraph(TinkerFactory.createModern())`

### Check count data in graph

`g.V().count()`
`g.V(1).values('name')`
`g.V(1).outE('knows')`
`g.V(1).outE('knows').inV().values('name')`
`g.V(1).out('knows').values('name')`
`g.V(1).out('knows').has('age', gt(30)).values('name')`

### Add data

`g = traversal().withGraph(TinkerGraph.open())`
`v1 = g.addV("person").property(id, 1).property("name", "marko").property("age", 29).next()`
`v2 = g.addV("software").property(id, 3).property("name", "lop").property("lang", "java").next()`
`g.addE("created").from(v1).to(v2).property(id, 9).property("weight", 0.4)`

### Calculate mean by age

`g.V().has('person','name',within('vadas','marko')).values('age').mean()`

### Group by

`g.V().group().by(label).by('name')`
