# What I learned from this project  
At the end of this project you are expected to be able to explain to anyone, without the help of Google:  
---   

**?**  
*.*  


**?**  
*.*  


**?**  
*.*  


**?**  
*.*  


## Each scripts and their output  
* Script 0 - .    
* Script 1 - .  
* Script 2 - .  
* Script 3 - .  
* Script 4 - .  
* Script 5 - .  
* Script 6 - .  
* Script 7 - .  
* Script 8 - .  
* Script 9 - .  
* Script 10 - .  
* Script 11 - .  
* Script 12 - .  
* Script 13 - .  
* Script 14 - .  
* Script 15 - .  
* Script 16 - .  
* Script 17 - .  
* Script 18 - .  
* Script 19 - .  
* Script 20 - .  
* Script 21 - .  
* Script 100 - .    
* Script 101 - .    
* Script 102 - .    
* Script 103 - .    



How to import functions from another file
type in import FILENAME
the file is prb called FILENAME.py but we can exclude the .py when importing

How to use imported functions
FILENAME.nameOfDefinedFunction(parametersOfFunction)

How to create a module
just create a py file.

How to use the built-in function dir()
the built-in function dir() is used to find out which names a module defines.
It returns a sorted list of strings. 

How to prevent code in your script from being executed when imported
# stuff to run always here such as class/def
def main():
    pass

    if __name__ == "__main__":
       # stuff only to run when not called via 'import' here
          main()

          if __name__ == "__main__":
              import sys
                  fib(int(sys.argv[1]))






                  How to use command line arguments with your Python programs
                  >>> import sys
                  >>> print(sys.argv)
                  ['demo.py', 'one', 'two', 'three']



