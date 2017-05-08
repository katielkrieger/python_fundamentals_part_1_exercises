#[Debugging and Modules Exercises](https://www.rithmschool.com/courses/python-fundamentals-part-1/python-debugging-and-modules-exercises)

Katie Krieger

5/8/17

1. A module is Python file that we want to import into other files.
2. Three ways to import a module in Python:

	* `import math` - importing everything
	* `from math import pow` - importing a single function
	* `import random as r` - aliasing the module
3. The purpose of importing a module is to add additional functionality to your code. If you want to use the same function across multiple files, you can put it in a module and import that module in multiple files. It keeps you from having to write the same code in multiple places, and it lets you organize your code more cleanly, only importing what you need in each file.
4. An `ImportError` is thrown when you try to import a module or a function therein that cannot be found.
5. An OrderedDict remembers the order in which key-value pairs were added. It might be helpful if you want to know the last item added to a dictionary.
6. Defaultdict could be helpful when you don't want to throw a KeyError, and instead want to execute some other code, if you try to find a key that does not exist in the dictionary.
7. The purpose of the following code:
```py
if __name__ == '__main__':
	pass
```
is to create a placeholder for code in a module that you don't want to run when that module is imported into another .py file, but that you do want to run when the module is executed directly.