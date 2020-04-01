from py2neo import Graph,Node,Relationship
import time

# http端口
graph = Graph("http://192.168.18.201:7474", username="neo4j", password="kOzGX7J8Sm8F1nisqIYv")

g = graph.run("MATCH (n:stock) RETURN n LIMIT 25").data()
g = graph.run("MATCH p=()-[r:stock2plate]->() RETURN p LIMIT 25").data()

print(g)