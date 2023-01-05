from manim import *

  

class BFS(Scene):


    # Create vertex
    def gnode(self, position, tname, c, width=3, radio=0.4, cname=WHITE):
        circle = Circle(radio, color = c, stroke_width = width).move_to(position)
        self.name = Text(str(tname), color=cname).scale(0.5)
        self.name.move_to(circle.get_center())
        return circle, self.name


    # Create edges
    def edges(self, u, v, width=2, color=WHITE):
        line = Line(u, v, stroke_width=width, color = color)
        return line
    

    def construct(self):
        title = Text("Breadth First Search", color=BLUE).scale(1.5)
        description = Text("Ejemplo de arbol generado por BFS", gradient=(BLUE,GREEN)).next_to(title, DOWN)
        name = Text("Ana Maritza Bello Yañez", slant=ITALIC).next_to(title, UP)
        self.add(title, description, name)
        self.play(FadeOut(title, description, name))
        self.wait(1)

        vertex = {
            'node_1' : {'coordinates' : [-3,3,0],'label': '1', 'layer': 0, 'new_coordinate': [3,3,0]},
            'node_2' : {'coordinates' : [-4,1.5,0],'label': '2', 'layer': 1, 'new_coordinate': [2,1.5,0]},
            'node_3' : {'coordinates' : [-2,1.5,0],'label': '3', 'layer': 1, 'new_coordinate': [4,1.5,0]},
            'node_4' : {'coordinates' : [-5,0,0],'label': '4', 'layer': 2, 'new_coordinate': [1,-1,0]},
            'node_5' : {'coordinates' : [-3,0,0],'label': '5', 'layer': 2, 'new_coordinate': [2.5,-1,0]},
            'node_6' : {'coordinates' : [-0.5,0.5,0],'label': '6', 'layer': 2, 'new_coordinate': [5,-1,0]},
            'node_7' : {'coordinates' : [-0.5,2.5,0],'label': '7', 'layer': 2, 'new_coordinate': [3.5,-1,0]},
            'node_8' : {'coordinates' : [-3,-2,0],'label': '8', 'layer': 3, 'new_coordinate': [2.5,-2.5,0]},  
        }

        node_list = []
        for key in vertex.keys():
            nodo, name = self.gnode(vertex[key]['coordinates'], vertex[key]['label'], GRAY)
            node_list.append(nodo)
            self.play(Create(nodo), Write(name))
        
        aristas = []
        
        arista12 = self.edges(node_list[1-1].get_left(), node_list[2-1].get_top())
        aristas.append(arista12)
        arista13 = self.edges(node_list[1-1].get_right(), node_list[3-1].get_top())
        aristas.append(arista13)
        arista24 = self.edges(node_list[2-1].get_left(), node_list[4-1].get_top())
        aristas.append(arista24)
        arista25 = self.edges(node_list[2-1].get_right(), node_list[5-1].get_top())
        aristas.append(arista25)
        arista45 = self.edges(node_list[4-1].get_right(), node_list[5-1].get_left())
        aristas.append(arista45)
        arista56 = self.edges(node_list[5-1].get_bottom(), node_list[8-1].get_top())
        aristas.append(arista56)
        arista35 = self.edges(node_list[3-1].get_left(), node_list[5-1].get_top())
        aristas.append(arista35)
        arista37 = self.edges(node_list[3-1].get_right(), node_list[7-1].get_left())
        aristas.append(arista37)
        arista38 = self.edges(node_list[3-1].get_right(), node_list[6-1].get_left())
        aristas.append(arista38)
        arista78 = self.edges(node_list[7-1].get_bottom(), node_list[6-1].get_top())
        aristas.append(arista78)
        
        for element in aristas:
            self.play(Create(element))
        
        tree_nodes = []
        for key in vertex.keys():
            nodox, namex = self.gnode(vertex[key]['new_coordinate'], vertex[key]['label'],RED)
            tree_nodes.append(nodox)
            if vertex[key]['layer'] == 0:
                nodo, name = self.gnode(vertex[key]['coordinates'], vertex[key]['label'],RED)
                nodox, namex = self.gnode(vertex[key]['new_coordinate'], vertex[key]['label'],RED)
                layer = Text('Layer 0' ).scale(0.5).next_to([5.5,3,0])
                new_node = nodo.copy()
                self.play(Create(nodo),Write(namex), Write(layer), new_node.animate.move_to(vertex[key]['new_coordinate']))
            elif vertex[key]['layer'] == 1:
                nodo, name = self.gnode(vertex[key]['coordinates'], vertex[key]['label'],BLUE)
                nodox, namex = self.gnode(vertex[key]['new_coordinate'], vertex[key]['label'],RED)
                layer = Text('Layer 1' ).scale(0.5).next_to([5.5,1.5,0])
                new_node = nodo.copy()
                self.play(Create(nodo),Write(namex), Write(layer), new_node.animate.move_to(vertex[key]['new_coordinate']))
            elif vertex[key]['layer'] == 2:
                nodo, name = self.gnode(vertex[key]['coordinates'], vertex[key]['label'],GREEN)
                nodox, namex = self.gnode(vertex[key]['new_coordinate'], vertex[key]['label'],RED)
                layer = Text('Layer 2' ).scale(0.5).next_to([5.5,-1,0])
                new_node = nodo.copy()
                self.play(Create(nodo),Write(namex), Write(layer), new_node.animate.move_to(vertex[key]['new_coordinate']))
            elif vertex[key]['layer'] == 3:
                nodo, name = self.gnode(vertex[key]['coordinates'], vertex[key]['label'],ORANGE)
                nodox, namex = self.gnode(vertex[key]['new_coordinate'], vertex[key]['label'],RED)
                layer = Text('Layer 3' ).scale(0.5).next_to([5.5,-2,0])
                new_node = nodo.copy()
                self.play(Create(nodo),Write(namex), Write(layer), new_node.animate.move_to(vertex[key]['new_coordinate']))

        all_naristas = []
        narista21 = self.edges(tree_nodes[2-1].get_top(), tree_nodes[1-1].get_bottom())
        all_naristas.append(narista21)
        narista31 = self.edges(tree_nodes[3-1].get_top(), tree_nodes[1-1].get_bottom())
        all_naristas.append(narista31)
        narista42 = self.edges(tree_nodes[4-1].get_top(), tree_nodes[2-1].get_bottom())
        all_naristas.append(narista42)
        narista52 = self.edges(tree_nodes[5-1].get_top(), tree_nodes[2-1].get_bottom())
        all_naristas.append(narista52)
        narista73 = self.edges(tree_nodes[7-1].get_top(), tree_nodes[3-1].get_bottom())
        all_naristas.append(narista73)
        narista63 = self.edges(tree_nodes[6-1].get_top(), tree_nodes[3-1].get_bottom())
        all_naristas.append(narista63)
        narista85 = self.edges(tree_nodes[8-1].get_top(), tree_nodes[5-1].get_bottom())
        all_naristas.append(narista85)

        for element in all_naristas:
            self.play(Create(element))
        
        self.wait(3)

class MST(Scene):
    

    def construct(self):

        title = Text("Minimum Spanning Tree", color=BLUE).scale(1.5)
        description = Text("Ejemplo de arbol generado por MST", gradient=(BLUE,GREEN)).next_to(title, DOWN)
        name = Text("Ana Maritza Bello Yañez", slant=ITALIC).next_to(title, UP)
        self.add(title, description, name)
        self.play(FadeOut(title, description, name))
        self.wait(1)
        
        title2 = Text("Minimum Spanning Tree", weight=BOLD, font="Arial", color=GREEN).move_to([2,-2,0])
        self.play(Write(title2))

        #---------------------------------------------Primero definir el grafo original------------------------------------------------------------------------------#
        vertices=[1,2,3,4,5,6,7,8]  #Definir vertices
        aristas=[
            (1,2),
            (1,3),
            (1,7),
            (2,3),
            (2,4),
            (2,5),
            (4,8),
            (4,5),
            (5,6),
            (5,3),
            (3,7),
            (3,6),
            (7,6),
            (8,6)
            ]
        coordenadas=[[-3,3,0], [-4,1.5,0], [-2,1.5,0],[-5,0,0],[-3,0,0],[-0.5,0.5,0],[-0.5,2.5,0],[-3,-2,0]] #Las coordenadas deben estar en formato de lista [x,y,z]
        acomodo={v:coord for (v,coord) in zip(vertices,coordenadas)}  #Crea un diccionario con las coordenadas de cada nodo, para pasarlo como argumento layout del grafo
    
        g=Graph(vertices,
                aristas,
                labels=True,
                layout=acomodo,
                edge_type=Line,
                edge_config={'color':WHITE,'stroke_width':1},
                vertex_config={'fill_color':GRAY})
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------#

        weight1 = Text("21", font_size=25).next_to([-4,2.5,0])
        weight2 = Text("14", font_size=25).next_to([-2.8,2.6,0])
        weight3 = Text("7", font_size=25).next_to([-2,3,0])
        weight4 = Text("10", font_size=25).next_to([-3.5,1.7,0])
        weight5 = Text("8", font_size=25).next_to([-4.2,0.8,0])
        weight6 = Text("16", font_size=25).next_to([-5.3,0.8,0])
        weight7 = Text("4", font_size=25).next_to([-4,-0.8,0])
        weight8 = Text("6", font_size=25).next_to([-4.5,0.2,0])
        weight9 = Text("23", font_size=25).next_to([-2.2,0.5,0])
        weight10 = Text("5", font_size=25).next_to([-3,0.8,0])
        weight11 = Text("11", font_size=25).next_to([-1.8,2.1,0])
        weight12 = Text("18", font_size=25).next_to([-1.5,1.2,0])
        weight13 = Text("9", font_size=25).next_to([-0.5,1.5,0])
        weight14 = Text("24", font_size=25).next_to([-2,-0.8,0])

        self.play(
            Write(weight1),
            Write(weight2),
            Write(weight3),
            Write(weight4),
            Write(weight5),
            Write(weight6),
            Write(weight7),
            Write(weight8),
            Write(weight9),
            Write(weight10),
            Write(weight11),
            Write(weight12),
            Write(weight13),
            Write(weight14),
        )

        self.play(Create(g))

        tree_edges = [(4,8),(5,3),(4,5),
        (7,1),(5,2),(7,6),
        (2,3),(3,7),
        (1,2),(2,4),(3,6),(5,6),(6,8)
        ]

        for element in tree_edges:
            if element in [(2,3),(1,2),(2,4),(3,6),(5,6),(6,8)]:
                self.play(
                    g.animate.add_edges(element,
                    edge_type=Line,
                    edge_config={
                        'color':RED,
                        'stroke_width':15,}
                        )
                    )
                self.wait(0.5)
                self.play(g.animate.remove_edges(element))
            else:
                self.play(
                    g.animate.add_edges(element,
                    edge_type=Line,
                    edge_config={
                        'color':BLUE,
                        'stroke_width':15}
                        )
                    )


#class Dijkstra(Scene):
#    title = Text("Dijkstra", color=BLUE).scale(1.5)
#    description = Text("Ejemplo de camino más corto", gradient=(BLUE,GREEN)).next_to(title, DOWN)
#    name = Text("Ana Maritza Bello Yañez", slant=ITALIC).next_to(title, UP)
#    self.add(title, description, name)
#    self.play(FadeOut(title, description, name))
#    self.wait(1)
#    
#    title2 = Text("Minimum Spanning Tree", weight=BOLD, font="Arial", color=GREEN).move_to([2,-2,0])
#    self.play(Write(title2))
#        #---------------------------------------------Primero definir el grafo original------------------------------------------------------------------------------#
#    vertices=[1,2,3,4,5,6,7,8]  #Definir vertices
#    aristas=[
#        (1,2),
#        (1,3),
#        (1,7),
#        (2,3),
#        (2,4),
#        (2,5),
#        (4,8),
#        (4,5),
#        (5,6),
#        (5,3),
#        (3,7),
#        (3,6),
#        (7,6),
#        (8,6)
#        ]
#    coordenadas=[[-3,3,0], [-4,1.5,0], [-2,1.5,0],[-5,0,0],[-3,0,0],[-0.5,0.5,0],[-0.5,2.5,0],[-3,-2,0]] #Las coordenadas deben estar en formato de lista [x,y,z]
#    acomodo={v:coord for (v,coord) in zip(vertices,coordenadas)}  #Crea un diccionario con las coordenadas de cada nodo, para pasarlo como argumento layout del grafo
#
#    g=Graph(vertices,
#            aristas,
#            labels=True,
#            layout=acomodo,
#            edge_type=Line,
#            edge_config={'color':WHITE,'stroke_width':1},
#            vertex_config={'fill_color':GRAY})
#    #-------------------------------------------------------------------------------------------------------------------------------------------------------------#
#
#    weight1 = Text("21", font_size=25).next_to([-4,2.5,0])
#    weight2 = Text("14", font_size=25).next_to([-2.8,2.6,0])
#    weight3 = Text("7", font_size=25).next_to([-2,3,0])
#    weight4 = Text("10", font_size=25).next_to([-3.5,1.7,0])
#    weight5 = Text("8", font_size=25).next_to([-4.2,0.8,0])
#    weight6 = Text("16", font_size=25).next_to([-5.3,0.8,0])
#    weight7 = Text("4", font_size=25).next_to([-4,-0.8,0])
#    weight8 = Text("6", font_size=25).next_to([-4.5,0.2,0])
#    weight9 = Text("23", font_size=25).next_to([-2.2,0.5,0])
#    weight10 = Text("5", font_size=25).next_to([-3,0.8,0])
#    weight11 = Text("11", font_size=25).next_to([-1.8,2.1,0])
#    weight12 = Text("18", font_size=25).next_to([-1.5,1.2,0])
#    weight13 = Text("9", font_size=25).next_to([-0.5,1.5,0])
#    weight14 = Text("24", font_size=25).next_to([-2,-0.8,0])
#
#    self.play(
#        Write(weight1),
#        Write(weight2),
#        Write(weight3),
#        Write(weight4),
#        Write(weight5),
#        Write(weight6),
#        Write(weight7),
#        Write(weight8),
#        Write(weight9),
#        Write(weight10),
#        Write(weight11),
#        Write(weight12),
#        Write(weight13),
#        Write(weight14),
#    )

