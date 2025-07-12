## Using UV Virtual Environments

This guide is made using these two resources:

1. [UV's official guide](https://docs.astral.sh/uv/getting-started/)
2. [Corey Schafer's UV Tutorial](https://www.youtube.com/watch?v=AMdG7IjgSPM) 

	Corey's tutorial is pretty detailed and this guide aims to complement his tutorial in an easier way. Watch Corey's tutorial along with this guide.

### For MacOS/Linux

Open any terminal and the execute these commands and enter password if prompted.

###### Use `curl` to download the script and execute it with `sh`:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If your system doesn't have `curl`, you can use `wget`:
```
wget -qO- https://astral.sh/uv/install.sh | sh
```

Request a specific version by including it in the URL:
```
curl -LsSf https://astral.sh/uv/0.7.16/install.sh | sh
```

###  Windows

##### Activating Scripts on Windows PowerShell

First we need to ensure that powershell allows us to activate scripts which can be python specific scripts we need to run on our system. First check if Default Execution Policy on your Windows is unrestricted or restricted by running:

Run PowerShell as administrator and then run: `Get-ExecutionPolicy`

If returns returns Restricted it means that we need to unrestrict the default execution policy but if it returns Unrestricted than your powershell already allows us to run python scripts as we wish. However if it returns AllSigned, Bypass, Default, RemoteSigned, Restricted, Undefined it's best to follow this step:

If execution policy is restricted we need to run Powershell as administrator and then run this command:

`Set-ExecutionPolicy unrestricted`

When we run this command we will be prompted to enter y, type y and then press enter key.

![](https://i.ibb.co/XZ402XzZ/image.png)
##### Using Windows Powershell to install UV

Open Windows Powershell with Administrator Access and the run:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

To Install Specific Version of uv use:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.7.16/install.ps1 | iex"
```

### You can also use Pip to install UV (On both windows and Unix Based OS)

```
pip install uv
```
### Using UV to manage virtual environments in a directory

#### Using Terminal to create Project and use UV

Let's say we want to create a python project folder called fastapi-project using uv we need to first `cd`  (change directory) to where we want to create our project and then write:

<pre> uv init fastapi-project </pre>
This will create a project called fastapi-project and will create files required by uv including a .gitignore file and a main.py file. Now if we again cd into `fastapi-project` we can see these files:

![](https://i.ibb.co/wZHRXDTn/image.png)

Here we can see that a virtual environment has still not been created.
#### Creating and Opening Project in any IDE

Let's say we already have a folder and we want to use uv for virtual environments we can open that folder in any IDE. Open any terminal (powershell for windows) and write:

<pre> uv init </pre>
Here uv-stack is the name of of our python project we already had, and when we used uv init it created all these files inside uv-stack directory, including a main.py file.

![](https://i.ibb.co/VpxTvnNd/image.png)

Here we can see that a virtual environment has still not been created.

### What is the meaning of the files the uv creates?

![](https://i.ibb.co/Q7VyfH5m/image.png)

###### `.git` File

The `.git` file is created to track changes in a project using Git. With Git, we can upload files and code to platforms like GitHub, monitor changes, and revert any modifications that may cause issues. Git also keeps a record of which user made each change.

###### `.gitignore` File

The `.gitignore` file specifies folders and file paths that Git should ignore. It tells Git not to track the files and directories listed in this file.

###### `.python` version File

This file contains the reference of the python version being used across the python project. We can change the version of python as well using this file. 

###### `main.py` Python File

UV assumes that by default we might want to create a `main.py` file because generally IDEs pickup this file to run if not set. 

###### `pyproject.toml` File

Typically these are the contents inside a `pyproject.toml` file: 
![](https://i.ibb.co/3YW3bRbs/image.png)

On line 7 we can dependencies these are the packages a uv virtual environment might have. It's empty because haven't installed any packages, but if we add any packages the are added to dependencies list. 

###### `README.md` File

This file typically contains documentation for the project. The text you're currently reading exists because it was written in Markdown format within the `README.md` file.

### Adding Packages to a project and creating a virtual environment and uv lock

To add packages to a uv environment run this:

<pre> uv add package-name </pre>

For example we are installing flask and requests packages we can run:

<pre> uv add flask requests </pre>

As soon as we add both these packages first a .venv directory is created and then if we open `pyproject.toml` file this is what we will see:

![](https://i.ibb.co/6R5DtmJ5/image.png)

This means uv itself creates a virtual environment, activates it and add packages to it, these are many steps for a beginner especially if we used pip to do so. `Pip` is also an environment and package manager like uv.

Another thing that happens as soon as we run uv add **(for the first time)** we will see a .lock file get created. 

![](https://i.ibb.co/wFPh2QcV/image.png)

The lock file contains version numbers of packages including sub dependencies so environment can easily be reproduced perfectly. 

Now whenever we open a project with any IDE i.e. Vs Code or Pycharm they will automatically select the environment created by uv. 

#### Seeing Which Packages need which smaller packages or dependencies using tree

We can also see sub dependencies in uv using `uv tree`.
### If we want to create a virtual environment without adding packages we can simply run

<pre> uv venv </pre>
### Uv handles virtual environments for us

As mentioned before UV automatically creates a `.venv` folder to establish and manage your Python environment, and you can specify custom names for environments as needed. If your virtual environment folder gets deleted or you're working with a freshly cloned repository without an existing `.venv` folder, UV seamlessly handles the situation. When you run `uv run something.py`, UV intelligently detects the missing environment and creates a new `.venv` folder on the fly, then rapidly installs all required packages based on your `pyproject.toml` configuration.

This automatic environment reconstruction eliminates the manual setup steps typically required with other Python package managers, making UV particularly valuable for team collaboration and deployment scenarios where environments need to be quickly recreated from scratch.

### How to share uv environment projects and how a user can replicate the uv environment on his/her system?

As discussed earlier, UV stores project dependencies in the `pyproject.toml` file while maintaining exact version specifications and dependency trees in the lock file. This creates a robust, reproducible environment setup.

Consider a GitHub repository structured like this:

A github repository is like a folder but online where developers can share and contribute to the code simultaneously. 

![](https://i.ibb.co/zhTLVqz0/image.png)

When someone clones(downloads) this repository (to their system), they'll find the standard project files (directories, `.dockerignore`, `.gitignore`, `Dockerfile`, and `LICENSE`) alongside three key files: `README.md`, `pyproject.toml`, and `uv.lock`.

Creating an identical development environment becomes remarkably simple. The person cloning the repository only needs to run:

<pre>uv sync</pre>
This single command automatically:

- Creates a virtual environment on their local system
- Fetches the exact package versions specified in `uv.lock`
- Installs all dependencies with their complete dependency trees (packages and the sub packages those depend on)
- Ensures perfect environment replication across different machines

This streamlined approach eliminates the multi-step process typically required with pip and virtualenv, where users must manually create environments, activate them, and install requirements—often leading to version conflicts and "works on my machine" issues. With UV, environment reproduction becomes a one-command operation.

See how in easy it is:

![](https://i.ibb.co/4Z691313/image.png)

You can clone this repo to try this: 

https://github.com/shery7310/Using-UV

### If you used pip before you can easily use those same commands with uv aswell:

This is a good [guide](https://pydevtools.com/handbook/how-to/how-to-use-pip-in-a-uv-virtual-environment/) regarding that.
