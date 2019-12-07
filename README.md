# Awesome Panel [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-panel)

[<img src="https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/panel-logo.png?raw=true" align="right" height="75" width="75">](https://panel.pyviz.org/)

> A high-level app and dashboarding solution for **Python**!

A repository for sharing knowledge on the use of [Panel](https://panel.pyviz.org/) for developing **awesome analytics apps** in Python.

Panel is part of the [HoloViz](https://holoviz.org/) maintained libraries and the effort to make browser-based data visualization in Python easier to use, easier to learn, and more powerful.

[<img class="pvlogo" src="https://holoviz.org/assets/panel.png" height="75">](https://panel.pyviz.org)
[<img class="pvlogo" src="https://holoviz.org/assets/hvplot.png" height="75">](https://hvplot.pyviz.org)
[<img class="pvlogo" src="https://holoviz.org/assets/holoviews.png" height="75">](https://holoviews.org)
[<img class="pvlogo" src="https://holoviz.org/assets/geoviews.png" height="75">](http://geoviews.org)
[<img class="pvlogo" src="https://holoviz.org/assets/datashader.png" height="75">](http://datashader.org)
[<img class="pvlogo" src="https://holoviz.org/assets/param.png" height="75">](https://param.pyviz.org)
[<img class="pvlogo" src="https://holoviz.org/assets/colorcet.png" height="75">](https://colorcet.pyviz.org)

This project provides

- A curated [list](https://github.com/MarcSkovMadsen/awesome-panel#awesome-resources) of Awesome Panel **resources**. See below.
- An [**awesome Panel application**](https://awesome-panel.org) with a **gallery** of Awesome Panel Apps.
    - Feel free to add your awesome app to the gallery via a [Pull request](https://github.com/MarcSkovMadsen/awesome-panel/pulls). It's easy (see below).
- A **best practices** example and **starter template** of an awesome, multipage app with an automated CI/ CD pipeline, deployed to the cloud and running in a Docker container.

Visit the app at [awesome-panel.org](https://awesome-panel.org)!

![Awesome Panel Org Animation](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/awesome-panel-full-branded.gif?raw=true)

## The Power of Panel

The only way to truly understand how powerfull Panel is to play around with it. But if you need to be convinced first, then here is the **30 minute introduction** to Panel!

Afterwards you can go to the [Panel Getting Started Guide](http://panel.pyviz.org/getting_started/index.html) or visit the [Panel Gallery](http://panel.pyviz.org/gallery/index.html).

[![Introduction to Panel](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/youtube-introduction-to-panel.png?raw=true)](https://www.youtube.com/watch?v=L91rd1D6XTA&t=1133s "Introduction to panel")

## Governance

This repo is maintained by me :-)

I'm Marc, Skov, Madsen, PhD, CFA®, Lead Data Scientist Developer at [Ørsted](https://orsted.com)

You can learn more about me at [datamodelsanalytics.com](https://datamodelsanalytics.com)

I try my best to govern and maintain this project in the spirit of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

But **i'm not an experienced open source maintainer** so helpfull suggestions are appreciated.

Thanks

### LICENSE

Apache 2.0 License

## Getting Started with the Awesome Panel Repository

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

#### Create virtual environment

##### via python

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

##### or via anaconda

Create virtual environment named awesome-panel

```bash
conda create -n awesome-panel python=3.7.4
```

and activate environment.

```bash
activate awesome-panel
```

Then you should install the local requirements

```bash
pip install -r requirements_local.txt
```

### Build and run the Application Locally

```bash
panel serve app.py
```

or in a jupyter notebook

```bash
jupyter notebook app.ipynb
```

or as a Docker container via

```bash
invoke docker.build --rebuild
invoke docker.run-server
```

### Run the Application using the image on Dockerhub

If you don't wan't to clone the repo and build the docker container you can just use `docker run` to run the image from [Dockerhub](https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-panel)

To run the panel interactively on port 80

```bash
docker run -it -p 80:80 marcskovmadsen/awesome-panel:latest
```

To run bash interactively

```bash
docker run -it -p 80:80 --entrypoint "/bin/bash" marcskovmadsen/awesome-panel:latest
```

### Code quality and Tests

We use

- [isort](https://pypi.org/project/isort/) for sorting import statements
- [autoflake](https://github.com/myint/autoflake) to remove unused imports and unused variables
- [black](https://pypi.org/project/black/) the opinionated code formatter
- [pylint](https://www.pylint.org/) for static analysis
- [mypy](https://github.com/python/mypy) for static type checking
- [pytest](https://github.com/pytest-dev/pytest) for unit to functional tests

to ensure a high quality of our code and application.

You can run all tests using

```bash
invoke test.all
```

### Workflow

We use the power of [Invoke](http://www.pyinvoke.org/) to semi-automate the local workflow. You can see the list of available commands using

```bash
$ invoke --list
Available tasks:

  docker.build                            Build Docker image
  docker.push                             Push the Docker container
  docker.remove-unused                    Removes all unused containers to free up space
  docker.run                              Run the Docker container bash terminal interactively.
  docker.run-server                       Run the Docker image with the Panel server.
  docker.run-server-with-ping             Run the docker image with Panel server and
  docker.system-prune                     The docker system prune command will free up space
  jupyter.notebook                        Run jupyter notebook
  package.build                           Builds the awesome-panel package)
  panel.bootstrap-dashboard               Starts the Panel Server and serves the Bootstrap Dashboard App
  sphinx.build                            Build local version of site and open in a browser
  sphinx.copy-from-project-root           We need to copy files like README.md into docs/_copy_of_project_root
  sphinx.livereload                       Start autobild documentation server and open in browser.
  sphinx.test                             Checks for broken internal and external links and
  test.all (test.pre-commit, test.test)   Runs isort, autoflake, black, pylint, mypy and pytest
  test.autoflake                          Runs autoflake to remove unused imports on all .py files recursively
  test.bandit                             Runs Bandit the security linter from PyCQA.
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
```

### Project Layout

The basic layout of a application is as simple as

```bash
.
└── app.py
```

As our application grows we would refactor our app.py file into multiple folders and files.

- *assets* here we keep our css and images assets.
- *models* - Defines the layout of our data in the form of
  - Classes: Name, attribute names, types
  - DataFrame Schemas: column and index names, dtypes
  - SQLAlchemy Tables: columns names, types
- *pages* - Defines the different pages of the Panel app
- *services* - Organizes and shares business logic, models, data and functions with different pages of the Panel App.
  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations

and end up with a project structure like

```bash
.
├── app.py
└── src
    └── assets
    |    └── css
    |    |   ├── app.css
    |    |   ├── component1.css
    |    |   ├── component2.css
    |    |   ├── page1.css
    |    |   └── page2.css
    |    └── images
    |    |   ├── image1.png
    |    |   └── image2.png
    ├── core
    |   └── services
    |       ├── service1.py
    |       └── service2.py
    └── pages
    |   └── pages
    |       ├── page1.py
    |       └── page2.py
    └── shared
        └── models
        |   ├── model1.py
        |   └── model2.py
        └── components
            ├── component1.py
            └── component2.py
```

Further refactoring is guided by by [this](https://itnext.io/choosing-a-highly-scalable-folder-structure-in-angular-d987de65ec7) blog post and the [Angular Style Guide](https://angular.io/guide/styleguide).

We place our tests in a `test` folder in the root folder organized with folders similar to the `app` folder and file names with a `test_` prefix.

```bash
.
└── test
    ├── test_app.py
    ├── core
    |   └── services
    |       ├── test_service1.py
    |       └── test_service2.py
    └── pages
    |   └── pages
    |       ├── page1
    |       |   └── test_page1.py
    |       └── page2
    └── shared
        └── models
        |   ├── test_model1.py
        |   └── test_model2.py
        └── components
            ├── test_component1.py
            └── test_component2.py
```