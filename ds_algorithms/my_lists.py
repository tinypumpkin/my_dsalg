class Node(object):
    def __init__(self,data):
        self._next=None
        self._date=data
    
    @property
    def date(self):
        return self._date
    @property
    def next(self):
        return self._next
    @date.setter
    def date(self,date):
        self._date=date
    @next.setter
    def next(self,ne):
        self._next=ne 

class linklist(object):
    def __init__(self):
        self._head=None
    def get_tail(self,flag=None):
        tail=None
        if flag==None:
            head=self._head
        else:
            head=flag
        while head!=None:
            tail=head
            head=head.next
        return tail
    def size(self,flag=None):
        head=None
        if flag==None:
            head=self._head
        else:
            head=flag
        num=0
        while head!=None:
            head=head.next
            num+=1
        return num

    #头插法
    def add_by_head(self,val):
        tem=Node(val)
        tem.next=self._head
        self._head=tem
    
    #显示所有
    def show_links(self):
        head=self._head
        while head!=None:
            print("链表的值是==>",head.date)
            head=head.next
    
    def show_links_in(self,val):
        head=val
        while head!=None:
            print("链表的值是==>",head.date)
            head=head.next
    #反转链表
    def revers(self):
        head=self._head
        pri=None
        tem=head
        while head!=None:
            head=head.next
            tem.next=pri
            pri=tem
            tem=head
        self._head=pri
        return pri

    def revers_in(self,links):
        head=links
        pri=None
        tem=head
        while head!=None:
            head=head.next
            tem.next=pri
            pri=tem
            tem=head
        return pri
    
    #查找按值
    def find_val(self,val):
        head=self._head
        while head!=None:
            if head.date==val:
                return head
            head=head.next
        return Node(None)

    def find_in_val(self,links,val):
        head=links
        while head!=None:
            if head.date==val:
                return head
            head=head.next
        return Node(None) 
    #查找按id
    def find_ind(self,index):
        head=self._head
        num=self.size()
        tem=0
        if index==0:
            return head
        if index>num or index<0:
            return None
        while head!=None and tem<=num:
            if tem==index:
                return head
            tem+=1 
            head=head.next
        return None

    def find_in_ind(self,links,index):
        head=links
        num=self.size()
        tem=0
        if index==0:
            return head
        if index>num or index<0:
            return None
        while head!=None and tem<=num:
            if tem==index:
                return head
            tem+=1 
            head=head.next
        return None
    #插入左插（Node前）
    def insert_node(self,node,val):
        head=self._head
        tail=self.get_tail()
        pri=head
        begin=head
        if head==node:
            pri=Node(val)
            pri.next=head
            self._head=pri
            return
        while head!=None:
            if head==node:
                r_node=Node(val)
                r_node.next=head
                pri.next=r_node
                return begin
            pri=head
            head=head.next
        if pri==tail:
                r_node=Node(val)
                r_node.next=None
                pri.next=r_node    
        self._head=begin

    #插入左插(按index)
    def insert_left(self,index,val):
        head=self._head
        num=self.size()
        pri=head
        begin=head
        tem=0
        if index==0:
            pri=Node(val)
            pri.next=head
            self._head=pri
            return
        if index>num or index<0:
            print("输入index超范围")
            return None
        while head!=None and tem<=num:
            if tem==index:
                node=Node(val)
                node.next=head
                pri.next=node
                return begin
            tem+=1
            pri=head
            head=head.next
        if index==tem:
                node=Node(val)
                node.next=None
                pri.next=node    
        self._head=begin
        
    #删除(按node)
    def del_node(self,node):
        head=self._head
        tail=self.get_tail()
        pri=head
        begin=head
        if head==node:
            pri=head.next
            head=pri
            self._head=pri
            return
        while head!=None:
            if head==node:
                pri.next=node.next
                return begin
            pri=head
            head=head.next
        if pri==tail:
                pri.next=None    
        self._head=begin
    #判定是否有环

if __name__ == "__main__":
    lin=linklist()
    lin.add_by_head(1)
    lin.add_by_head(2)
    lin.add_by_head(3)
    lin.add_by_head(4)
    #lin.show_links()
    #lin.find_val(2).next.date
    #print(lin.find_ind(0).date)
    #inl=lin.revers()
    #lin.show_links_in(inl)
    #print(lin.find_in_val(inl,2).next.date)
    #print(lin.find_in_ind(inl,0).date)
    #lin.insert_left(4,7)
    node=lin.find_val(0)
    #lin.insert_node(node,7)
    lin.del_node(node)
    lin.show_links()