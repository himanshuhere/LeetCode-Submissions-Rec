class MyQueue:
#push 0(n) and pop 0(n)
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
            
        self.s1.append(x)
        
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1

#push o(1) pop amortized o(1)
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        self.peek()
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]        

    def empty(self):
        return not self.s1 and not self.s2
    
    #Amorized o(1) means one operation may take n time but for overall cals it might give you o(1) result. think like if we do all 5 push then 4 pop, since on first pop, we have put s1 data to s2 and return s2.top, now for second third so on calls POP we ll direct return s2.pop, thats y first called peek. Peek returns the last element not pop, thus second line to pop that element.
    #On long time span that can be ref as constant time thus amortized o(1). Then again for all push we do in s1 and will use s2 until it is empty then again fill s2 with s1 bruh.
    #THIS IS A BEAUTIFUL ALGO AND EXPLANATION FOR AMORTIMZED CONSTANT