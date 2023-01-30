'''
class bt:
    def __init__(self,data):
        self.data=data
        self.lc=None
        self.rc=None
def insert(root,newvalue):
    if root is None:
        root = bt(newvalue)
        return root
    if newvalue<root.data:
        root.lc=insert(root.lc,newvalue)
    else:
        root.rc=insert(root.rc,newvalue)
    return root
def inorder(root):
    if root == None:
        return
    inorder(root.lc)
    print(root.data)
    inorder(root.rc)
    
def postorder(root):
    if root == None:
        return
    postorder(root.lc)
    postorder(root.rc)
    print(root.data)


root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("inorder traversal of bts")
inorder(root)
print("postorder traversal of bts")
postorder(root)

'''

'''

# horizontal distance evaluation with key hashing

class Node:
    def __init__(self,key,l=None,r=None):
        self.key=key
        self.l=l
        self.r=r
def vot(node,dist,d):
    if node is None:
        return
    d.setdefault(dist,[]).append(node.key)
    vot(node.l,dist-1,d)
    vot(node.r,dist+1,d)
def pvot(root):
    d={}
    vot(root,0,d)
    for value in d.values():
        print(value)
if __name__=="__main__":
    root = Node(1)
    root.l=Node(2)
    root.r=Node(3)
    root.r.l=Node(4)
    root.r.r=Node(5)
    root.r.l.l=Node(6)
    root.r.l.r=Node(7)
    root.r.l.r.l=Node(8)
    root.r.l.r.r=Node(9)
    pvot(root)

'''


# push and pop can be used in queue, but enqueue
# and dequeue cannot be used in stack.






