################################################################## Built in
import sys
class String:
    def __init__(self, string):
        self.string = string

    def all_caps(self):
        string = self.string
        print(string.upper().strip() , end="")

    def reverse(self):
        string = self.string
        print(string[::-1] , end="")

    def sort(self):
        string = self.string
        print(''.join(sorted(string, key=str.casefold)))

    def is_digit(self):
        string = self.string
        print(string.isdigit())

    def find(self, inp):
        string = self.string
        print(string.find(inp))

# List


class List:
    def __init__(self, list):
        self.list = list

    def append(self, data):
        l = self.list
        l.append(data)
        print(l.strip())

    def reverse(self):
        l = self.list
        l.reverse()
        print(l.strip())

    def sort(self):
        l = self.list
        l.sort()
        print(l.strip())

    def separate(self, chr):
        l = self.list
        # l.split(chr)
        print(l.split(chr).strip())

    def insert(self, num, index):
        l = self.list
        l.insert(num, index)
        print(l.strip())


t = sys.stdin.readline().strip()
string = sys.stdin.readline()
i1 = sys.stdin.readline()
i2 = sys.stdin.readline()
i3 = sys.stdin.readline()
i4 = sys.stdin.readline()
i5 = sys.stdin.readline()

if t is not 'list':
    s = String(string)
    s.all_caps()
    s.reverse()
    s.sort()
    s.is_digit()
    
    i5 = i5.strip().split(" ")
    s.find(str(i5[1]))
else:
    s = List(list(string))
    
    i1 = i1.strip().split(" ")
    s.append(i1[1])
    
    s.reverse()
    
    s.sort()
    
    i4 = i4.strip().split(" ")
    s.separate(i4[2])
    
    i5 = i5.strip().split(" ")
    s.insert(i5[1] , i5[2])


################################################################## Library

import sys
def check_condition(mid, array, n, K): 
	count = 0
	sum = 0
	for i in range(n): 

		if (array[i] > mid): 
			return False

		sum += array[i] 

		if (sum > mid): 
			count += 1
			sum = array[i] 
	count += 1

	if (count <= K): 
		return True
	return False

def find(array, n, K): 
	start = 1
	end = 0

	for i in range(n): 
		end += array[i] 

	x = 0
	while (start <= end): 
		mid = (start + end) // 2

		if check_condition(mid, array, n, K): 
			x = mid 
			end = mid - 1
		else: 
			start = mid + 1

	return x 

inp1 = list(map(int, sys.stdin.readline().strip().split(' ')))
inp2 = int(sys.stdin.readline())

a = inp1
k = inp2
n = len(a) 

print(find(a, n, k)) 

############################################################# Multiply Numbers
import sys

# Linked List Node


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):

        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

# Multiply  linked list


def multiply(list1, list2):
    num1 = 0
    num2 = 0

    curr = list1.head
    while curr:
        num1 = (num1 * 10 + curr.data)
        curr = curr.next

    curr = list2.head
    while curr:
        num2 = (num2 * 10 + curr.data)

        curr = curr.next

    return num1 * num2

def populate(string):
    l = LinkedList()
    curr_node = None
    for i in string.strip():
        node = Node(int(i))
        if l.head is None:
            l.head = node
            curr_node = l.head
        else:
            curr_node.next = node
            curr_node = curr_node.next
            curr_node.prev = curr_node
    return l


arr = sys.stdin.readline().split(" ")
num1 = arr[0]
num2 = arr[1]

len1 = len(num1)
len2 = len(num2)

# Populate Doubly Linked List
l_list1 = populate(num1)
l_list2 = populate(num2)

print(multiply(l_list1, l_list2))


############################################################## Remove Duplicates
import sys

class LinkedList:
    def __init__(self):
        self.head = None
        
    def removeDuplicates(self): 
        curr = self.head 
        if curr is None: 
            return
        while curr.next is not None: 
            if curr.data == curr.next.data: 
                new = curr.next.next
                curr.next = None
                curr.next = new 
            else: 
                curr = curr.next
        return self.head 

    def printList(self):  
        curr = self.head  
        while(curr):  
            print(curr.data , end = ' ') 
            curr = curr.next
        
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
def populate(string):
    l = LinkedList()
    curr_node = None
    for i in string.split(" "):
        i = int(i)
        node = Node(i)
        if l.head is None:
            l.head = node
            curr_node = l.head
        else:
            curr_node.next = node
            curr_node = curr_node.next
    return l

lis = populate(sys.stdin.readline().strip())
lis.removeDuplicates()
lis.printList()

############################################################### Thanos vs Tony Stark
import sys

test_cases = int(sys.stdin.readline())

inp = []

while len(inp) is not test_cases:
    D, P = sys.stdin.readline().strip().split(" ")
    inp.append([D, P])


def swap(string):
    string = list(string)

    string.reverse()

    for i in range(len(string)-1):
        if string[i] is 'S' and string[i+1] is 'C':
            string[i+1] = 'S'
            string[i] = 'C'
            break

    string.reverse()

    return ''.join(string)


count = 0
prev_dmg = 0

def beam(string, d):
    global count
    global prev_dmg
    C = 1
    dmg = 0
    for j in string:
        if j is 'C':
            C *= 2
        elif j is 'S':
            dmg += C

    if prev_dmg is dmg:
        prev_dmg = 0
        print('IMPOSSIBLE')
        return

    prev_dmg = dmg

    if dmg > d:
        count += 1
        s = swap(string)
        beam(s, d)
    else:
        print(count)
        count = 0

# Best possible solution is putting all S infront
for i in inp:
    C = 1
    string = i[1].strip()
    dmg = int(i[0])
    beam(string, dmg)

####################################################################### World War
import sys

inp = [int(i) for i in sys.stdin.readline().split()]

area = 600

lis = []

list_len = []

for i in inp:
    l = [j for j in range(1, i+1)]
    list_len.append(len(l))
    lis.append(l)

max = 0 

for i in list_len:
    count = 0
    for j in lis:
        if i in j:
            count += 1
        elif count > 0:
            break
    
    if count*i > max:
        max = count*i

print(max*area)