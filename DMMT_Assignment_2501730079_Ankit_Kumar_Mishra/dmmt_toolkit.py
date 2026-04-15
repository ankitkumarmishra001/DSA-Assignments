# Data Management Mini Toolkit (DMMT)
# Made by BTech 1st year student (simple version)

# BST

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root


    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)
        else:
            return self.search(root.right, data)

   
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

   
    def find_min(self, node):
        while node.left:
            node = node.left
        return node

   
    def delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)

        elif data > root.data:
            root.right = self.delete(root.right, data)

        else:
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# GRAPH 

class Graph:
    def __init__(self):
        self.graph = {}

   
    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, w))

 
    def show(self):
        for i in self.graph:
            print(i, self.graph[i])

   
    def bfs(self, start):
        vis = []
        q = [start]

        print("BFS from", start, ":", end=" ")

        while q:
            node = q.pop(0)

            if node not in vis:
                print(node, end=" ")
                vis.append(node)

                for n, w in self.graph.get(node, []):
                    q.append(n)
        print()

 
    def dfs(self, node, vis=None):
        if vis is None:
            vis = []

        print(node, end=" ")
        vis.append(node)

        for n, w in self.graph.get(node, []):
            if n not in vis:
                self.dfs(n, vis)


# HASH TABLE 

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    
    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash(key)
        self.table[idx].append((key, value)) 

    def get(self, key):
        idx = self.hash(key)

        for k, v in self.table[idx]:
            if k == key:
                return v

        return "Not Found"

    def delete(self, key):
        idx = self.hash(key)

        for i in range(len(self.table[idx])):
            if self.table[idx][i][0] == key:
                self.table[idx].pop(i)
                break

    def show(self):
        for i in range(self.size):
            print(i, ":", self.table[i])


# MAIN OPERATIONS

def main():
    # BST OPERATIONS
    print(" BST OPERATIONS ")

    b = BST()
    root = None

    arr = [50, 30, 70, 20, 40, 60, 80]
    for i in arr:
        root = b.insert(root, i)

    print("Inorder traversal:")
    b.inorder(root)
    print()

    print("Search 20:", b.search(root, 20))
    print("Search 90:", b.search(root, 90))

    print("\nDelete leaf node (20)")
    root = b.delete(root, 20)
    print("Inorder after deleting 20:")
    b.inorder(root)
    print()

    print("\nInsert 65 (to create one child case)")
    root = b.insert(root, 65)

    print("Delete node with one child (60)")
    root = b.delete(root, 60)
    print("Inorder after deleting 60:")
    b.inorder(root)
    print()

    print("\nDelete node with two children (30)")
    root = b.delete(root, 30)
    print("Inorder after deleting 30:")
    b.inorder(root)
    print()


    # GRAPH OPERATIONS
    print("\n GRAPH OPERATIONS ")

    g = Graph()

    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 7)
    g.add_edge('B', 'E', 3)
    g.add_edge('C', 'E', 1)
    g.add_edge('D', 'F', 5)
    g.add_edge('E', 'D', 2)
    g.add_edge('E', 'F', 6)
    g.add_edge('C', 'F', 8)

    print("Adjacency List:")
    g.show()

    g.bfs('A')

    print("DFS from A:", end=" ")
    g.dfs('A')
    print()


    # HASH TABLE 
    print("\n HASH TABLE ")

    h = HashTable(5)

    # inserting values (collision will happen)
    h.insert(10, "A")
    h.insert(15, "B")
    h.insert(20, "C")
    h.insert(7, "D")
    h.insert(12, "E")

    print("Hash Table:")
    h.show()

    print("\nGet 10:", h.get(10))
    print("Get 15:", h.get(15))
    print("Get 7:", h.get(7))

    print("\nDelete key 15 (collision case)")
    h.delete(15)

    print("Hash Table after deletion:")
    h.show()


if __name__ == "__main__":
    main()