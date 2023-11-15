#ЧЕРЕПАШКА
import turtle

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.parents = []
        self.children = []
        self.x = x
        self.y = y

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)  # переместим черепаху в координаты узла
        turtle.pendown()
        turtle.circle(10)  # нарисуем узел в виде маленького круга

        # напишем значение узла рядом с ним
        turtle.penup()
        turtle.goto(self.x+10, self.y)
        turtle.pendown()
        turtle.write(self.value)
        
    def connect(self, other_node):
        # перемещаем черепаху на узел
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

        # проводим линию к другому узлу
        turtle.goto(other_node.x, other_node.y)

def simplify(node, previous):
    global graph
    if len(node.parents) == 2:
        other_parent = [parent for parent in node.parents if parent != previous][0]
        other_parent.children.remove(node)
        for child in node.children:
            other_parent.children.append(child)
            child.parents.remove(node)
            child.parents.append(other_parent)

        graph.remove_node(node.value)
        del node

# Создаем узлы с соответствующими координатами
node_a = Node("A", -100, 0)
node_b = Node("B", -50, 50)
node_c = Node("C", -50, -50)
node_d = Node("D", 0, 0)
node_e = Node("E", 50, 0)

# Соединим
node_a.children = [node_b, node_c]
node_b.parents = [node_a]
node_c.parents = [node_a]

node_b.children = [node_d, node_e]
node_d.parents = [node_b]
node_e.parents = [node_b]

node_c.children = [node_d]
node_d.parents.append(node_c)

# Упростим дерево, как в коде
simplify(node_a, None)

# Построим узлы и соединения
for node in [node_a, node_b, node_c, node_d, node_e]:
    node.draw()
    for child in node.children:
        node.connect(child)

turtle.done()
