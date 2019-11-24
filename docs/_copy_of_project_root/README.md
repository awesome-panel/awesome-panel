# Awesome Panel

A repository for sharing knowledge and resources on Awesome (Pyviz Panel

I've started this project because I think Panel could be awesome and I wan't to share knowledge and lower the friction of using it.

## Getting Started with this Repository

### Prerequisites

- An Operating System like Windows, OsX or Linux
- A working [Python](https://www.python.org/) installation.
  - We recommend using 64bit Python 3.7.4.
- a Shell
  - We recommend [Git Bash](https://git-scm.com/downloads) for Windows 8.1
  - We recommend [wsl](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) for For Windows 10
- an Editor
  - We recommend [VS Code](https://code.visualstudio.com/) (Preferred) or [PyCharm](https://www.jetbrains.com/pycharm/).
- The [Git cli](https://git-scm.com/downloads)

### Installation

Clone the repo

```bash
git clone https://github.com/MarcSkovMadsen/awesome-panel.git
```

cd into the project root folder

```bash
cd awesome-panel
```

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment.

On Linux, OsX or in a Windows Git Bash terminal it's

```bash
source .venv/Scripts/activate
```

or alternatively

```bash
source .venv/bin/activate
```

In a Windows terminal it's

```bash
.venv/Scripts/activate.bat
```

Then you should install the local requirements

```bash
pip install -r requirements_local.txt
```

### Build and run the Pages Locally

```bash
panel serve app.py
```

### Run all tests

```bash
invoke test.all
```

If all tests pass successfully you will see

```bash
All Tests Passed Successfully
=============================
```

### Command Line Interface

We use [Invoke](http://www.pyinvoke.org/) to build our command line interface. You can see the list of available commands using

```bash
$ invoke --list
Available tasks:

  docker.build                            Build Docker image
  docker.push                             Push the Docker container
  docker.remove-unused                    Removes all unused containers to free up space
  docker.run                              Run the Docker container bash terminal interactively.
  docker.run-server                       Run the Docker image with the Streamlit server.
  docker.run-server-with-ping             Run the docker image with Streamlit server and
  docker.system-prune                     The docker system prune command will free up space
  sphinx.build                            Build local version of site and open in a browser
  sphinx.copy-from-project-root           We need to copy files like README.md into docs/_copy_of_project_root
  sphinx.livereload                       Start autobild documentation server and open in browser.
  sphinx.test                             Checks for broken internal and external links and
  package.build                           Builds the awesome-streamlit package)
  test.all (test.pre-commit, test.test)   Runs isort, autoflake, black, pylint, mypy and pytest
  test.autoflake                          Runs autoflake to remove unused imports on all .py files recursively
  test.bandit                             Runs Bandit the security linter from PyCQA.
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
```

and help on a specific command using

```bash
$ invoke test.pytest --help
Usage: inv[oke] [--core-opts] test.pytest [--options] [other tasks here ...]

Docstring:
  Runs pytest to identify failing tests

  Arguments:
      command {[type]} -- Invoke command object

  Keyword Arguments:
      root_dir {str} -- The directory from which to run the tests
      test_files {str} -- A space separated list of folders and files to test. (default: {'tests})
      integrationtest {bool} -- If True tests marked integrationtest or
          functionaltest will be run. Otherwise not. (default: {False})
          These tests requires the test backend server running.
      test_results {string} -- If not None test reports will be generated in the
          test_results folder

  # Print running pytest

Options:
  -e STRING, --test-results=STRING
  -t STRING, --test-files=STRING
```
