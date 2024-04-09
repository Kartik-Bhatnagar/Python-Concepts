# Organizing Modules

**Package** : A package is a collection of modules in a folder. The name of the package is the name of the folder. 
We need to tell Python that a
folder is a package to distinguish it from other folders in the directory. To do this, place a (normally empty) file in the folder named __init__.py. 

### Example
Let's put our modules inside an ecommerce package in our working folder, which will also
contain a main.py file to start the program. Let's additionally add another package inside
the ecommerce package for various payment options. The folder hierarchy will look like
this:
parent_directory/
 main.py
 ecommerce/
    __init__.py
    database.py
    products.py
    payments/
        __init__.py
        square.py
        stripe.py
        paypal.py

 There are two ways of importing modules: absolute imports and relative imports.

 ### Absolute imports
 Absolute imports specify the complete path to the module, function, or class we want to import. If we need access to the Product class inside the products module, we could use any of these syntaxes to perform an absolute import:
 
`import ecommerce.products`
`product = ecommerce.products.Product()`

//or
`from ecommerce.products import Product`
`product = Product()`

//or
`from ecommerce import products`
`product = products.Product()`

The import statements use the period operator to separate packages or modules.

These statements will work from any module. We could instantiate a Product class using this syntax in main.py, in the database module, or in either of the two payment modules.
The packages can also be installed in the Python site packages folder, or the PYTHONPATH environment variable could be customized to dynamically tell Python which folders to search for packages and modules it is going to import.
In Python, when you install packages using tools like pip, they are typically installed in a directory called site-packages.
However, there might be cases where you want to install packages in a different location or organize them in a custom way. This is where the PYTHONPATH environment variable comes into play.
#### PYTHONPATH
The PYTHONPATH variable is a list of directories that Python will search when trying to import modules or packages. By default, it includes the current directory and the site-packages directory.
In the Environment Variables window, you can either set the PYTHONPATH variable under User variables (for your user account only) or System variables (for all users on the system). Click "New" and add the variable name (PYTHONPATH) and its value (the path to the directory containing your Python packages).add the paths to the directories you want to include, separated by semicolons.   
When you set the PYTHONPATH environment variable to include a directory containing Python packages, those packages become accessible from anywhere in the machine, as long as Python can recognize the PYTHONPATH variable.

### Relative imports 
When working with related modules inside a package, it seems kind of redundant to specify the full path; 
 Relative imports are basically a way of saying find a class, function, or module as it is positioned relative to the current module. 
For example, if we are working in the products module and we want to import the Database class from the database module next to it, we could use a relative import:

`from .database import Database`

The period in front of database says use the database module inside the current package. In this case, the current package is the package containing the products.py file we are currently editing, that is, the ecommerce package.

If we were editing the paypal module inside the ecommerce.payments package, we would want, for example, to use the database package inside the parent package instead. This is easily done with two periods, as shown here:

`from ..database import Database`

#### init
The __init__.py file that defines a directory as a package? This file can contain any variable or class declarations we like, and they will be available as part of the package.
In our example, if the ecommerce/__init__.py file contained the following line:

`from .database import db` 

We could then access the db attribute from main.py or any other file using the following import:

`from ecommerce import db` insted of ` import ecommerce.database.db`

It might help to think of the __init__.py file as if it were an ecommerce.py file, if that file were a module instead of a package. 
