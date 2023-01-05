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

