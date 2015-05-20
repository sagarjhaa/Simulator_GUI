from nodebox.graphics import *
from nodebox.graphics.physics import Node, Edge, Graph

# Create a graph with randomly connected nodes.
# Nodes and edges can be styled with fill, stroke, strokewidth parameters.
# Each node displays its id as a text label, stored as a Text object in Node.text.
# To hide the node label, set the text parameter to None.
g = Graph()
# Random nodes.

def create_graph(d_nodes,d_links):

    d_links.append(d_nodes)
    
    for i in range(len(d_links)):#100
        g.add_node(id=str(d_links[i]), 
            radius = 5,
            stroke = color(1), 
              text = color(1))
##    g.add_node(id=str(d_nodes), 
##            radius = 5,
##            stroke = color(1), 
##              text = color(1))
    # Random edges.
    for i in range(len(d_links)-1):#1,100
        node1 = str(d_links[-1])#choice(g.nodes)
        node2 = str(d_links[i])#choice(g.nodes)
        g.add_edge(node1, node2, 
            length = 200.0, 
            weight = random(), 
            stroke = color(1, 0, 0.25, 0.75))

    # Two handy tricks to prettify the layout:
    # 1) Nodes with a higher weight (i.e. incoming traffic) appear bigger.
    for node in g.nodes:
        node.radius = node.radius + node.radius*node.weight
    # 2) Nodes with only one connection ("leaf" nodes) have a shorter connection.
    for node in g.nodes:
        if len(node.edges) == 1:
            node.edges[0].length *= 0.5

    g.prune(depth=0)          # Remove orphaned nodes with no connections.
    g.distance         = 15   # Overall spacing between nodes.
    g.layout.force     = 0.01 # Strength of the attractive & repulsive force.
    g.layout.repulsion = 10   # Repulsion radius.

    dragged = None

def draw(canvas):
    
    canvas.clear()
    background(0)
    translate(600, 600)
    
    # With directed=True, edges have an arrowhead indicating the direction of the connection.
    # With weighted=True, Node.centrality is indicated by a shadow under high-traffic nodes.
    # With weighted=0.0-1.0, indicates nodes whose centrality > the given threshold.
    # This requires some extra calculations.
    g.draw(weighted=0.5, directed=True)
    g.update(iterations=10)
    
    # Make it interactive!
    # When the mouse is pressed, remember on which node.
    # Drag this node around when the mouse is moved.
    dx = canvas.mouse.x - 600 # Undo translate().
    dy = canvas.mouse.y - 600
    global dragged
    if canvas.mouse.pressed and not dragged:
        dragged = g.node_at(dx, dy)
    if not canvas.mouse.pressed:
        dragged = None
    if dragged:
        #dragged.x = dx
        #dragged.y = dy
        if dx < 1000:
            dragged.x = dx
        if dy < 1000:
            dragged.y = dy
        
#canvas.size = 500, 500
##canvas.fullscreen = True            
##canvas.run(draw)
