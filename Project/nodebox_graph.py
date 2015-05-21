from nodebox.graphics import *
from nodebox.graphics.physics import Node, Edge, Graph

import random as rd

# Create a graph with randomly connected nodes.
# Nodes and edges can be styled with fill, stroke, strokewidth parameters.
# Each node displays its id as a text label, stored as a Text object in Node.text.
# To hide the node label, set the text parameter to None.
g = Graph()
# Random nodes.

def create_graph(p_node,s):
    p = p_node
    
    temp = s.pAll[p_node].follower

    g.add_node(id=str(p_node),radius = 5,stroke = color(1),text = color(1))

    
    for i in range(len(temp)):#100
        g.add_node(id=str(temp[i]), 
            radius = 5,
            stroke = color(1), 
              text = color(1))
    
    # Random edges.
    p_links = s.pAll[p_node].follower
    for i in range(len(p_links)):
        node1 = str(p_node)#choice(g.nodes)
        node2 = str(p_links[i])#choice(g.nodes)
        g.add_edge(node1, node2,
                   length = 500.0,
                   weight = random(),
                   stroke = color(1, 0, 0.25, 0.75))


    #New Round
    for I in range(3):
        
        p_node = s.pAll[p].follower[I] #0
        p_links = s.pAll[p_node].follower

        r     = rd.choice([0,51,255])#rd.randint(10,200)
        green = rd.choice([255,128,255]) #rd.randint(0,100)
        b     = rd.choice([128,0,255])#rd.randint(0,200)

        print r,green,b
        
        for i in range(len(p_links)):
            node1 = str(p_node)#choice(g.nodes)

            bul = True
            if p_links[i] not in s.pAll[p].follower:  #Not a parent follower
                
                for j in range (I):                  #Loop to check another sibling's follower
                    
                    sibling = s.pAll[p].follower[j]
                    
                    if p_links[i] in s.pAll[sibling].follower:

                        bul = False

                if bul:
                    g.add_node(id=str(p_links[i]),radius = 5,stroke = color(1),text = color(1))
                    node2 = str(p_links[i])#choice(g.nodes)
                    g.add_edge(node1, node2,
                               length = 50.0,
                               weight = random(),
                               stroke = color(r, green, b, 0.75))
                    

    
    

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
        if dx < 500 or dx > 10:
            dragged.x = dx
        if dy < 500 or dy > 10:
            dragged.y = dy
