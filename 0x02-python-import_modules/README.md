
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



