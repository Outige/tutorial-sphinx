This is the simplest way I've got sphinx to work for my projects. It's probably not 100% but it seems to work for most of what sphinx can do. I will put caviots bellow, for what I feel is lacking with this approach.

# Install:
Manually install all requirements:

```bash
$ pip3 install sphinx
```

Or you can use the `requirements.txt` in this repo. Not that sphinx is a versioned documentation tool. That means that this tutorial might only work for the older requirements used in the `requirements.txt` file. To use my requirements:

```bash
$ pip3 install -r requirements.txt
```

# Sphinx quickstart:

`sphinx-quickstart` is a command line setup wizard that will prompt you with various questions. Depending on your answers to the questions, sphinx will set up your docs differnetly.

Initiate the sphinx quickstart command from inside the `docs/` dir:

```
$ sphinx-quickstart .
```

We will then be greeted with some questions. This is how I answered them:

```
> Separate source and build directories (y/n) [n]: y
```

This one is quite important. Docs can be done using y/n. But they will be slightly different. At this stage sphinx is deciding if it will write the necessary sphinx files to `docs/`(n) or `docs/source`(y). I say yes because it is a bit cleaner.

```
> Project name: Style Checks
```

This isn't that relevant. What ever you want to title of the docs to be.

```
> Author name(s): Tieg O'Sullivan
```

Your name goes here.

```
> Project release []: 0.0.1
```

Not that important.

```
> Project language [en]: e
```

English please.

### Directory before sphinx quick start
```
.
├── README.md
└── requirements.txt
```

### Directory after sphinx quick start
```
.
├── build
├── make.bat
├── Makefile
├── README.md
├── requirements.txt
└── source
    ├── conf.py
    ├── index.rst
    ├── _static
    └── _templates
```

The most important files are `source/conf.py` and `source/index.rst`. 

`source/conf.py` is a config that sphinx will use to make your documentation.

`source/index.rst` will be converted into `build/html/index.html` when you make your html (will get to that soon).

# Generating html

I'm using linux so I will run the following:

```
$ make html
```

I get this output:

```
build succeeded.

The HTML pages are in build/html.
```

Now open `build/html`. I usally make and launch in one step like:

```
$ make html && xdg-open build/html/index.html
```

You should be greeted with a home page with some links like:
* Index
* Module Index
* Search Page

# Autodoc

Note: To generate html doc from docstrings, you have to have the docstrings formatted correctly. This is an easy google search.

So now we have the base for docs. Lets get some content. One of the best features of sphinx is that you can generate doc html from docstrings in your python code. Howver to get this working we have to do a bit of tinkering.


## Generating rst from docstrings

This is the main part in getting your docstrings to html. To generate the rsts:

```
$ sphinx-apidoc -o <path to the dir of your index.rst> <path to your code>
```

In or example:

```
$ sphinx-apidoc -o source/ ../style/
```

I get this output:
```
Creating file source/style.rst.
Creating file source/modules.rst.
```

My directory now looks like this:

```
.
├── build
├── make.bat
├── Makefile
├── README.md
├── requirements.txt
└── source
    ├── conf.py
    ├── style.rst
    ├── modules.rst
    ├── index.rst
    ├── _static
    └── _templates
```

## updating conf.py to allow autodoc

We have to edit the `conf.py` to allow autodoc.

Update `conf.py` to be able to locate the code.

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

`../..` because we first have to cd out of the `source/` directory then we cd out of the `docs/` directory. Finaly we are at the level where we can cd into our code.

Run the sphinx comand line tool for automatically generating `.rst` from your python files.

In config.py update `extenstions` as such:
```python
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
]
```
`sphinx.ext.autodoc` is the extension that allows for automatic documentation. `sphinx.ext.napoleon` is an extension that allows you to use differnt formats of docstrings (without it you have to use the standard sphinx docstring format). I'm not sure what `sphinx.ext.coverage` is.

I think you could get away with just using `sphinx.ext.autodoc` and following the sphinx docstring format to the letter.

## Link modules.rst from index.rst

Update the tocree in index.rst from:

```
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```

To:

```
.. toctree::
   :maxdepth: 3
   :caption: Contents:

   modules
```

changing `:maxdepth: 2` -> `:maxdepth: 3` just indicates how 'deep' the table of contents will be displayed. Adding `modules` linkes to the `modules.rst` that we just generated.

Now you can make html again and you have docs!