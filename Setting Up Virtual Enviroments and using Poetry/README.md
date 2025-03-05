This is a guide to help you install poetry and virtual environment which is required for poetry to run on any system. For the Windows portion of this guide to work you need to activate Scripts using windows Powershell and use Windows Powershell. You also need to globally install poetry and venv in your system. We will discuss these steps in detail below.

You can download and install latest version of Powershell from [here](https://github.com/powershell/powershell/releases), make sure you select the correct version i.e. `x64`, `msi` or `exe` which ever you prefer. 
# What is a virtual environment in Python?

### What is a package and what are package managers?

Before understanding what a virtual environment is, we must first know what a package and a package manager are in the context of Python. In Python, a package is essentially another term for a library or framework. Python packages are collections of modules that bundle together code to provide specific functionality, making it easier to organize and reuse code across different projects. Each package in Python can have specific versions and a package can he have dependencies meaning that package will not run without those packages. 

A package manager is a tool that helps us download packages from Python Package Index (PyPi) which is like a software repository but instead of GitHub the code is available on this website: https://pypi.org/. The default package manager used by Python Developers is called pip, but before using a package manager Python Documentation suggests that we create a virtual environment. 

A virtual environment in Python provides an isolated space where you can install and manage Python packages independently of the global Python installation. This allows you to create a self-contained directory for each specific project, ensuring that the dependencies and libraries utilized in one project do not conflict with those in another. In essence, it helps maintain a clean and organized development setup, promoting seamless collaboration and project management. Also some packages in Python can be really heavy so it's best to install them in a separate virtual environment rather than installing system wide and then after we are done with developing or running that specific project we can delete that environment.

### Looking for Packages and their specific versions

Whenever we search for any package such as Numpy or Fastapi any search engine such as Brave Search Engine or Google will bring in results from the PyPi website which again in Python Package Index. For example if we search something like install fastapi we will be redirected to this page:

https://pypi.org/project/fastapi/ and we will see something like:

![](https://i.imgur.com/YZr4zDO.png)

Let's say we want to use an older version of fastapi as it can be a project requirement we visit the Release History portion of this page and select the version we require i.e.

![](https://i.imgur.com/q4GuV89.png)

If we select version 0.113 and click on it PyPi will suggest us to run this command: <code>pip install fastapi==0.113.0</code>
# How to create a virtual environment? 

#### Activating Scripts on Windows PowerShell

First we need to ensure that powershell allows us to activate scripts which can be python specific scripts we need to run on our system. First check if Default Execution Policy on your Windows is unrestricted or restricted by running:

Run PowerShell as administrator and then run:
<code>Get-ExecutionPolicy</code>

If returns returns Restricted it means that we need to unrestrict the default execution policy but if it returns Unrestricted than your powershell already allows us to run python scripts as we wish. However if it returns AllSigned, Bypass, Default, RemoteSigned, Restricted, Undefined it's best to follow this step:

If execution policy is restricted we need to run Powershell as administrator and then run this command:

<code>Set-ExecutionPolicy unrestricted</code>

When we run this command we will be prompted to enter y, type y and then press enter key.

![](https://i.imgur.com/W2gydio.png)

#### How to create and activate a virtual environment on Windows?

First we need to open the folder where our Python Code exists, if we don't have a folder we can create that folder and then open it using VS Code or any other IDE such as Pycharm. You can also right-click inside that folder and click on the option Open with Code. 

Now we need to run the terminal of whichever IDE we are using and we will see a path of the root directory. A root directory is the main folder of our python project i.e. 

To open the terminal in Visual Studio Code, click on the **View** tab in the top menu and select **Terminal** from the dropdown options. By default, the integrated terminal in VS Code is configured to use PowerShell as its default shell. This allows you to execute commands and scripts directly within the editor without needing to switch to an external terminal application.

We will a path like this:

![](https://i.imgur.com/g7ZzR2Q.png)
The PS we see at the beginning means PowerShell. 

So our root directory is called **`exp`** and the absolute path of the folder exp is :

```C:\Users\box_9\Desktop\exp>```

An **absolute path** specifies the full path starting from the root of the file system (in Windows, the root is typically a drive like `C:\`).

**To create a virtual environment using virtualenv or poetry we need to install these packages globally**

<code>pip install virtualenv</code>
<code>pip install poetry</code>

**If any problem comes while installing poetry on windows you can check this gist: https://gist.github.com/Isfhan/b8b104c8095d8475eb377230300de9b0**

**`virtualenv`** is a Python package used to create and activate isolated virtual environments. Additionally, the **Poetry** package also relies on `virtualenv` to create and manage its virtual environments, ensuring efficient dependency isolation and project management.

After installing virtualenv globally we need to run this command inside vs code's terminal:

<code>python -m venv myenv</code>

Here myenv is the name of the virtual environment but we can also change the name of this environment, let's say i name it fastapi-code

<code>python -m venv fastapi-code</code>

When we run any of these commands we will see that a folder will be created in our root directory which will have the name of the environment. and our IDE might ask if we want to change the environment (We need to press Yes) i.e.

![](https://i.imgur.com/yGRXnAW.png)

Now we need to activate the created environment, to activate we need to run:

<code>fastapi-code\Scripts\activate.ps1</code>

You can modify this command if your virtual environment has a different name. After running the command, you'll notice that the terminal in your IDE displays the name of the activated environment instead of the default `PS` prompt. For example:

![](https://i.imgur.com/mjoUDhK.png)

##### Installing and Uninstalling Packages inside `virtualenv` using pip. 

We can run `pip freeze` command to see if the current environment has any packages installed or not, you will not get any output as we have not installed any package onto this newly created environment. Let's say we install numpy inside this virtual environment.

We just need to type `pip install numpy` and the latest version of this package will be downloaded from PyPi and get installed into the current environment. 

Let's say for some reason we need to uninstall numpy we can run: `pip uninstall numpy`

This is what we will see in the terminal:

![](https://i.imgur.com/nJYcpbd.png)

### Mac/Linux Based Operating Systems

#### How to create and activate a virtual environment on Mac/Linux? Using virtualenv package

The commands for setting up a virtual environment using virtualenv package are pretty much the same for Mac/Linux.

First we need to globally install virtualenv and poetry package on our Linux distro, just open terminal and then paste these and press enter:

<code>pip install virtualenv</code>
<code>pip install poetry</code>

Note: On some Linux Distributions we might need to run this to install Poetry:
<pre>
    curl -sSL https://install.python-poetry.org | python3 -
</pre>

##### Then to create and activate a virtualenv on Linux/Mac we can type:

<code>python -m venv env-name</code>

Let's say i run this:

<code>python -m venv venv</code>

Now when we run the above command we will see that a new folder called venv will be created this folder contains files we need to activate the environment, we must be in root/python project directory and we need to run:

<code>source venv/bin/activate</code>

For Fish Shell this command is a bit different:

<code>. venv/bin/activate.fish</code>

Now when the environment will be activated we will see the name of the environment at start of the path being shown in terminal. i.e.

Packages can be installed/uninstalled just by using:

<pre>
pip install numpy

pip uninstall numpy
</pre>

![](https://i.imgur.com/M1pHEL7.png)
# How to create a poetry virtual environment? 

### Windows Operating System

Since Our instructor suggested that we use Poetry for creating and using virtual environments let's see how to create and activate virtual environments using poetry. Poetry needs virtualenv package as a dependency so make sure to <code>pip install virtualenv</code> before trying to use poetry package. 
#### Create and Activate a poetry environment

We need to run this command:
<code>poetry new name-of-environment</code>

You can replace **`name-of-environment`** with any name you wish to assign to your Poetry environment. In the context of Poetry, the environment's folder is referred to as a **Poetry project**, while in the context of a virtual environment, it is simply called an **environment**.

Let's say i run this:

<code>poetry new poetry-env</code>

As soon as we run this command we will see that a folder called `poetry-env` will be created and this directory is the folder of the virtual environment we have created using poetry.

![](https://i.imgur.com/egQs4bu.png)

#### Changing Poetry Path and Activating Poetry environment

Now there are two options by default Poetry will place all the environments in a directory like this: `"C:\\user-name\box_9\AppData\Local\pypoetry\Cache"`

You can check the default cache path for your system using this command:

<code>poetry config --list</code>

This means that all your environments will be stored in a separate directory, distinct from the directory we our project exists. You can either leave it as is or configure Poetry to always move environment files into the root directory of your Python projects. The second approach is preferable.

Here's how to set poetry to always move environment files into root directory, just run:

<code>poetry config virtualenvs.in-project true</code>

If we `cd` into the folder of our environment i.e. poetry-env in this case we will see a structure like this:

![](https://i.imgur.com/DUSPK0b.png)

Make sure your IDE terminal is in the environment folder i.e. 

`poetry-env`. After we are in a path like this: Documents/Fastapi/Connecting FastAPI with Mongodb/poetry-env

We need to run `poetry install` command to create further environment files so we can later activate the environment. 

Now if we see the structure/directories present in our environment folder we can see something like:

![](https://i.imgur.com/w86sd4S.png)

Here we can see that when we ran `poetry install` a folder called .venv was created, it is very similar to to how a virtualenv works as it also places environment activation files in the environment folder. 

To activate environment we can again go 1 step back using `cd ..` our goal here is to be in the root directory or the python project directory. The path shown in IDE's terminal should be like:

`/Documents/Fastapi/Connecting FastAPI with Mongodb`

See that we our outside the environment folder now. To activate from here we can run:

<code>./poetry-env/.venv/bin/Scripts/activate</code>

![](https://i.imgur.com/5t0h2Fp.png)

If you are not in root directory you will need to set correct directory. 

### Linux/Mac OS

The commands to create a poetry environment are similar Windows and Linux Based Operating Systems such as GNU Linux and Mac OS. The only difference is how we activate a poetry environment i.e.

<code>source poetry-env/.venv/bin/activate</code>

For Fish Shell:

<code>source poetry-env/.venv/bin/activate.fish</code>

#### Installing Packages onto poetry environment and checking their versions

To install any package using poetry we can run pip install commands but we should stick poetry's own [documentation](https://python-poetry.org/docs/managing-environments/#powershell) which suggests we use:

<code>poetry add name-of-package</code>
i.e. <code>poetry add fastapi</code>

To check if the package and all it's dependencies have successfully installed we can run:

<code>poetry show</code> we will see an output like this:

![](https://i.imgur.com/8Yil9Ag.png)

## Running a fastapi server using both virtualenv and poetry (Any Operating System)

##### virtualenv

In case of virtualenv we can use pip to install uvicorn and fastapi i.e. 

```python3
pip install fastapi
pip install uvicorn
```

##### poetry

```python3
poetry add fastapi
poetry add uvicorn
```

Now to run a fast api server in virtualenv or poetry environment we need to paste this code into any python file in my case the file is called randomcode.py 

```python3
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a root route
@app.get("/")
async def read_root():
    return {"message": "hello, world!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

To simply run this code for fast api we need to run this command in IDE's terminal:

<code>uvicorn main:app --reload</code>

As soon as we run this our fastapi server will be up and running at 127.0.0.1 IP which is also known as localhost and the port will be 8000. 
For a more detailed approach to understand this code we can check out [KDNuggets](https://www.kdnuggets.com/beginners-guide-to-fastapi) and it is a better approach to follow fastapi's official [documentation](https://fastapi.tiangolo.com/tutorial/first-steps/) as fastapi is well-known for having a good documentation.  
