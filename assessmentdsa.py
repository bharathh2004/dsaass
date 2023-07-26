# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def findPair(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
    print('Pair not found')
 
if __name__ == '__main__':
 
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
    findPair(nums, target)

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# Q3. Write a program to check if two strings are a rotation of each other?
str1 = "abcde";  
str2 = "deabc";  
   
if(len(str1) != len(str2)):  
    print("Second string is not a rotation of first string")  
else:  
    try:  
        str1 = str1 + str1;    
        if(str1.index(str2)):  
            print("Second string is a rotation of first string")
    except ValueError:  
            print("Second string is not a rotation of first string")

# Q4. Write a program to print the first non-repeated character from a string?

string = "geeksforgeeks"
index = -1
fnc = ""
 
if len(string) == 0 :
  print("EMTPY STRING");
 
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is", fnc)

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it

def tower_of_hanoi(disks, source, auxiliary, target):  
    if(disks == 1):  
        print('Move disk 1 from rod {} to rod {}.'.format(source, target))  
        return  
 
    tower_of_hanoi(disks - 1, source, target, auxiliary)  
    print('Move disk {} from rod {} to rod {}.'.format(disks, source, target))  
    tower_of_hanoi(disks - 1, auxiliary, source, target)  
  
  
disks = int(input('Enter the number of disks: '))    
tower_of_hanoi(disks, 'A', 'B', 'C')




# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
def postToPre(post_exp):
    s = []
    length = len(post_exp)
 
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
 
if __name__ == "__main__":
    post_exp = "AB+CD-"
    print("Prefix : ", postToPre(post_exp))



#  Q7. Write a program to convert prefix expression to infix expression   

def prefixToInfix(prefix):  
    symbols = []  
    l = len(prefix) - 1  
    while l >= 0:  
        if not Operator(prefix[l]):    
            symbols.append(prefix[l])  
            l -= 1  
        else:   
            string = "(" + symbols.pop() + prefix[l] + symbols.pop() + ")"  
            symbols.append(string)  
            l -= 1  
       
    return symbols.pop()  
  
def Operator(symbols):  
    if symbols == "*" or symbols == "+" or symbols == "-" or symbols == "/" or symbols == "^" or symbols == "(" or symbols == ")":  
        return True  
    else:  
        return False  

string = "*+P/QR-/STU"  
print("The infix string is: ", prefixToInfix(string))



# Q8. Write a program to check if all the brackets are closed in a given code snippet.


Python3 program to check for
balanced brackets.
 
function to check if
brackets are balanced
 
 
def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
 
if __name__ == "__main__":
    expr = "{()}[]"
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")

# Q9. Write a program to reverse a stack        


class Stack:
 

    def __init__(self):
        self.Elements = []
       
    def push(self, value):
        self.Elements.append(value)
       
    def pop(self):
        return self.Elements.pop()
     
    def empty(self):
        return self.Elements == []
     
    def show(self):
        for value in reversed(self.Elements):
            print(value)
 
def BottomInsert(s, value):
    if s.empty():
        s.push(value)
         
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
 
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
 
stk = Stack()
 
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
 
print("Original Stack")
stk.show()
 
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# Q10. Write a program to find the smallest number using a stack

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Smallest element is:", list1[0])