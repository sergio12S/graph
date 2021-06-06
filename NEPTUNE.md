# Neptune

## Magic comands

%%sparql - Executes a SPARQL query against your configured database endpoint.
%%gremlin - Executes a Gremlin query against your database using web sockets. The results are similar to what the Gremlin console would return.
%status - Calls the Neptune status endpoint, which returns information about the health and configuration of your DB cluster, as a JSON object.
%load - Invokes the Neptune bulk loader.
%graph_notebook_config - Returns a JSON object that contains connection information for your host.
%seed - Provides a form to add data to your graph without the use of a bulk loader. both SPARQL and Gremlin have an Air routes dataset.

## Create neptune notebook

Get data from vertex:
%%gremlin
g.V().valueMap().limit(10)

Change property or add property if it doesn't exist:
%%gremlin
g.V('1').property(single, 'name', 'marko')

Build a visualization of the graph:
%%gremlin -p v,ine,outv,oute,inv,oute,inv
g.V().hasLabel('League').inE().outV().outE().inV().outE().inV().path().by('name').by(label)
