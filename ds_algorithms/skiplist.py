import random

class Node:
    def __init__(self,val,next,down):
        self._val=val
        self._next=next
        self._down=down
    @property
    def val(self):
        return self._val
    @property
    def next(self):
        return self._next
    @property
    def down(self):
        return self._down
    @val.setter
    def val(self,val):
        self._val=val
    @next.setter
    def next(self,next):
        self._next=next
    @down.setter
    def down(self,down):
        self._down=down

class skiplist:
    def __init__(self):
        self.head=Node(-1,None,None)
    
    def add(self,val):
        head=self.head
        h=self.head
        down=None
        nodes=[]
        while head:
            while head.next!=None and head.val<val:
                head=head.next
            nodes.append(head)
            head=head.down
        pos=True
        while nodes and pos:
            node=nodes.pop()
            h=node
            tem=Node(val,node.next,down)
            node.next=tem
            down=tem
            pos=random.getrandbits(1)==0
        if pos:
            head=Node(-1,None,h)

    def show_all(self,sklist=None):
        if sklist==None:
            sklist=self.head
        head=sklist
        while head.down!=None:
            head=head.down
        while head:
            out=head
            yield out
            head=head.next

    def find_val(self,val,sklist_head=None):
        head=self.head
        if sklist_head!=None:
            head=sklist_head
        node=None
        while head:
            while head.next!=None and head.next.val<=val:
                head=head.next
            node=head
            head=head.down
        if node.val==val:
            return node
        else:
            return None
        
    def del_val(self,node,sklist=None):
        head=self.head
        if sklist!=None:
            head=sklist
        out=head
        nodes=[]
        while head:
            while head.next and head.next.val<node.val:
                head=head.next
            nodes.append(head)
            head=head.down
        while nodes:
            tem=nodes.pop()
            if tem.next.val==node.val:
                tem.next=tem.next.next
        return out


if __name__ == "__main__":
    sk=skiplist()
    sk.add(1)
    sk.add(2)
    sk.add(3)
    sk.add(4)
    lis=[i.val for i in sk.show_all()]
    print(lis)
    #print(sk.find_val(4).val)
    node=sk.find_val(1)
    head=sk.head
    out=sk.del_val(node,head)
    lis2=[i.val for i in sk.show_all(out)]
    print(lis2)

    