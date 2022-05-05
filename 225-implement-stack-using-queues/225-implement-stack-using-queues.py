#TWO QUEUES, push =o(1), pop = o(n) | somethigns to keep in mind for optimization during push, make sure to update peek variable as we will be returning peek or top in 0(1), so ok one operation done. now also keep a lenght variable ++, -- for push pop. so lenght and empty will be done. Now pop, so for this we ll pop all elements from q1 till one left the last one, and push all to q2. last one will be removed then withouyt pushing to q2, now since we need to reverse the operation of copying everything to q1 back, better swap the reference to avoid copying, q1,q2=q2,q1

class MyStack:
    def __init__(self):
        self.q1, self.q2 = deque([]), deque([])
        self.topp = None
        self.len = 0

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.topp = x                #stacks perspective
        self.len += 1

    def pop(self) -> int:
        for _ in range(len(self.q1)-1):
            x = self.q1.popleft()
            self.q2.append(x)
            self.topp = x           #top will take the last value
            
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.len -= 1
        return popped

    def top(self) -> int:
        return self.topp

    def empty(self) -> bool:
        return self.len == 0

#ONE QUEUE: nothing just one less queue else push is N and pop is 1 only. so idea is to push element but after pushing in stack same end is used to pop, what a dirty filthy bastard. kher, so revert the elements thats all.
#pop etc is same

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.topp = None
        self.len = 0

    def push(self, x: int) -> None: #reversing chal rhi hai
        self.q1.append(x)
        size = len(self.q1) #size var alag lena pdega len(q) kabhi kam nhi hnna
        while size > 1:
            self.q1.append(self.q1.popleft())
            size -= 1
        self.len += 1

    def pop(self) -> int:
        self.len -= 1
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return self.len == 0