# How to use janusgraph

## Run

1. Run docker

    * Simple container
    `docker run --name janusgraph-default janusgraph/janusgraph:latest`

    * Container with settings
    `docker run --name gremlin \
        -e janusgraph.storage.berkeleyje.cache-percentage=80 \
        -e gremlinserver.threadPoolWorker=4 \
        -e gremlinserver.channelizer=org.apache.tinkerpop.gremlin.server.channel.WsAndHttpChannelizer \
        -p 8182:8182 \
        --mount type=bind,src=$(pwd),target=/home/serg/projects/Bigdata/ \
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

### Check count data in graph and check releationship

* `g.V().count()`
* `g.V(1).values('name')`
* `g.V(1).outE('knows')`
* `g.V(1).outE('knows').inV().values('name')`
* `g.V(1).out('knows').values('name')`
* `g.V(1).out('knows').has('age', gt(30)).values('name')`

### Add data

* `g = traversal().withGraph(TinkerGraph.open())`
* `v1 = g.addV("person").property(id, 1).property("name", "marko").property("age", 29).next()`
* `v2 = g.addV("software").property(id, 3).property("name", "lop").property("lang", "java").next()`
* `g.addE("created").from(v1).to(v2).property(id, 9).property("weight", 0.4)`

### Calculate mean by age

* `g.V().has('person','name',within('vadas','marko')).values('age').mean()`

### Group by

* `g.V().group().by(label).by('name')`

## Query to Neptune DB instance

1. toList()
2. toSet()
3. next() -  when you need the result (and you are expecting exactly one result)
4. nextTraverser()
5. iterate() -  when you don't need the result (typically mutation queries, that add/change properties, edges and/or vertices)

## Query to controlling the recursion

1. dedup() - Remove duplicates.
2. where(neq("u861")) -  Exclude u861.
3. repeat() - avoid combinatorial explosion!
4. emit() - modulator to “output” all the traversed vertices.
    If emit() is placed after repeat(), it will “output” all vertices leaving the repeat-traversal. If emit() is placed before repeat(), it will “output” the vertices prior to entering the repeat-traversal.
5. until() is controlling when to break out of the recursion based on a condition.
    As with emit() you can place until() before or after the repeat() step.

## Technique to control the recursive combinatory explosion is to put a limit on the depth of each explored branch

* `until(has("age", 32).or().loops().is(eq(3)))`
* `repeat(out("knows").simplePath()))`
* `g.V().has("user", "userId", "u861").until(has("age", 32)).repeat(out("knows").simplePath()).timeLimit(100).valueMap("userId", "age")`

## Query

* sideEffect - allow the traverser to proceed unchanged, but yield some computational sideEffect in the process (S ↬ S).
* store() - store all objects into a set but only store their by()-modulated values.
