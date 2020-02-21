class Student(object):
    def __init__(self, height=65, weight=130):
        self.height = height
        self.weight = weight
    def grow(self, change=1):
        self.height += change

'''The following code can be executed in the IPython session:
In[]:   alex = Student(height=72)   # Creates a Student object called alex with a height of 72.
In[]:   print alex.weight           # Prints the weight attribute of the alex object.
Out[]:  130                         # The output will be 130 becuase that is the default weight and was not changed.
In[]:   alex.grow(2)                # Calls the grow method on the object alex
In[]:   print alex.height           # Prints the current height of the alex object.
'''