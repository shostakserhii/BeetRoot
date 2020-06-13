import sys
import os
print(sys.path)
print()
print(os.getcwd())
prev = os.path.join(os.getcwd(), '..' , '')
print(f"Prev = {prev}")
print(os.path.abspath(prev))
prev = os.path.join(os.getcwd(), '..', '..')
print("Pringting Prev after '..', '..' ")
print(prev)
print("Printing abstract path for Prev:")
print(os.path.abspath(prev))
print("\nRelative path for Prev:")
print(os.path.relpath(prev))
print(len(sys.path))
sys.path.insert((len(sys.path)),prev)
print(sys.path)
a = 'D:\Game'
sys.path.insert(0,a)
print(sys.path)
for i in sys.path:
    print(i)
sys.path.remove(a)
print("-"*100)
for i in sys.path:
    print(i)