"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    res = ''
    head = cur
    for c in s:
        if c == '0':
            head = head.left
        else:
            head = head.right
        if head.left == head.right == None:
            head = root
            res += head.data
    return res