# ❤️ Developer Guide

Welcome. We are so happy that you want to contribute.

Please note that this project is released with a [Contributor Code of Conduct](code-of-conduct.md).
By participating in this project you agree to abide by its terms.

## 🧳 Prerequisites

- A working [Python](https://www.python.org/downloads/) environment.
- [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## 📙 How to

Below we describe how to install and use this project for development.

### 💻 Install for Development

To install for development you will need to create a new environment

Then run

```bash
git clone https://github.com/awesome-panel/awesome-panel.git
cd awesome-panel
pip install pip -U
pip install -e .[dev,docs,examples]
```

Then you can see the available commands via

```bash
pn --help
```

You can run all tests via

```bash
pn test all
```

Please run this command and fix any failing tests if possible before you `git push`.

### Serve the site

```bash
mkdir -p apps/dev/www
mkdir -p apps/prod/www
panel serve examples/*.py examples/*.ipynb --glob --num-procs 4 --num-threads 0 --index home.py --static-dirs apps-dev=apps/dev/www apps=apps/prod/www
```

### 🚢 Release a new package on Pypi

Update the version in the [__init__.py](src/awesome_panel/__init__.py).

Then run

```bash
pn test all
```

Then you can build

```bash
pn build package
```

and upload

```bash
pn release package <VERSION>
```

to release the package 📦. To upload to *Test Pypi* first, you can add the `--test` flag.
