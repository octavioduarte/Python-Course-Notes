1. Standard Import
The standard import statement is used to import an entire module or specific attributes or functions from a module.

~~~python
import module_name
~~~

Example:

~~~python
import math
~~~



2. Import with Alias
You can import a module with an alias to make the code more readable or to avoid naming conflicts.

~~~python
import module_name as alias
~~~

Example:

~~~python
import numpy as np
~~~


3. Import Specific Attributes
Instead of importing the entire module, you can import specific attributes or functions from a module.

~~~python
from module_name import attribute1, attribute2
~~~

Example:


~~~python
from math import sqrt, sin
~~~


4. Import All Attributes
You can import all attributes from a module using the * wildcard. However, it's generally discouraged due to potential name clashes and decreased readability.

~~~python
from module_name import *
~~~

Example:

~~~python
from math import *
~~~

5. Conditional Import
You can conditionally import modules based on certain conditions using the import statement within a block of code.

~~~python
if condition:
    import module_name
~~~

Example:

~~~python
if os.name == 'posix':
    import posix
~~~

6. Dynamic Import
Modules can be imported dynamically at runtime using the importlib module.

~~~python
import importlib
module = importlib.import_module('module_name')
~~~

Example:

~~~python
import importlib
module_name = 'numpy'
np = importlib.import_module(module_name)
~~~
