#!/usr/bin/env python
# coding: utf-8

# In[7]:


## 1.1  Write a Python Program to implement your own myreduce() function which works exactly like 
##/nPython's built-in function reduce() 


# In[8]:


from functools import reduce
def myreduce(x1, x2):
    return x1 + x2
reduce(myreduce, [1, 2, 3, 4])


# In[ ]:


##1.2  
 
Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter(


# In[9]:


lst=[1,2,3,4]
def myreduce(num):
    if num%2==0:
        return True
list(filter(myreduce,lst))


# In[ ]:


## Implement List comprehensions to produce the following lists. 
 
Write List comprehensions to produce the following Lists 
 
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’] 
 
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz'] 
 
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz'] 
 
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
 
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
 
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 


# In[10]:


word="ACADGILD"
list(word)


# In[13]:


word2=[i*n for i in list('xyz') for n in range(1,5)]
print(word2)


# In[14]:


word3=[x*n for n in range(1,5) for x in list('xyz')]
print(word3)


# In[15]:


number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)


# In[17]:


number=[2,3,4,5]
number=[[x+n for n in range(0,4)] for x in number ]
print(number)


# In[19]:


number=[1,2,3]
number= [(b,a) for a in number for b in number]
print(number)


# In[22]:


def longestWord(word_list):
    wordlen=[]
    for w in word_list:
        wordlen.append((len(w),w))
    wordlen.sort()
    return wordlen[-1][-1]

#Input
print("Input:")
word_list=input("Please enter your word: ")
word_list=word_list.split(",")
#function execution
longest_word=longestWord(word_list)
print("Output:")
print(longest_word)


# In[23]:


'''Write a Python Program(with class concepts) to find the area of the triangle using the below formula. 
 
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
 
Function to take the length of the sides of triangle from user should be defined in the parent class and function to calculate the area should be defined in subclass'''
class Polygon:

    def __init__(self, n):
        self.number_of_sides = n

class Triangle(Polygon):

    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  # list of three numbers

    def get_area(self):
        '''return the area of the triangle using the semi-perimeter method'''
        a, b, c = self.lengths_of_sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5


# In[24]:


tri = Triangle([3, 4, 5])
print(tri.get_area())


# In[25]:


'''Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n'''

def filter_long_words(words, n):
    print(n)
    return [word for word in words if len(word) > n]
    
print (filter_long_words(['a', 'avg', 'abcde', 'zxcw', 'b'], 3))


# In[26]:


'''Write a Python program using function concept that maps  list of words into a list of integers representing the lengths of the corresponding words​. 
 Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4] 
 Here 2,3 and 4 are the lengths of the words in the list'''

def maptoword(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
words = ['ab','cde','erty']
print (maptoword(words))


# In[27]:


'''Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. 
'''
def is_vowel(char):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if char not in vowels:
        return False
    return True

print (is_vowel(input("enter the character ")))


# In[ ]:




