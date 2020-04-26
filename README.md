Vanguard kit
==========================

[![PyPI version](https://badge.fury.io/py/vanguardkit.svg)](https://badge.fury.io/py/vanguardkit)
[![Tests](https://github.com/BentoBox-Project/vanguard-kit/workflows/CI/badge.svg)](https://github.com/BentoBox-Project/vanguard-kit/actions?workflow=CI)

> A convenient way to calculate the edit distance between html files to scrape with confidence

Sometimes, scraping becomes a hard task, because the web sites are in continous changing.
What about if there was a way to prevent those changes before scrape a site?
Vanguard is a tool kit that provides a way to calculate the edit distance between
two html files by the Zhang-Shasha algorithm.
This package is based on [zss](https://github.com/timtadh/zhang-shasha).

## Installation

OS X & Linux:

From PYPI

```sh
$ pip3 install vanguardkit
```

from the source

```sh
$ git clone https://github.com/dany2691/vanguard-kit.git
$ cd vanguard-kit
$ python3 setup.py install
```

## Usage example

With vanguard, it is possible to convert html content into a tree (graph) of nodes.
The create_html_tree function is the responsible to do that, it returns an instance of the VanguardNode class that inherits from the zss.Node class:

```python
from vanguardkit import create_html_tree

with open("target_website.html") as target_website:
    thml_tree = create_html_tree(target_website)
```

It is possible to segment specific parts of an html file.

By tag:
```python
with open("target_website.html") as target_website:
    html_tree = create_html_tree(
        html_file=target_website,
        specific_tag="footer"
    )
```

By tag and class:
```python
with open("target_website.html") as target_website:
    html_tree = create_html_tree(
        html_file=target_website,
        specific_tag="div",
        class_="main-div"
    )
```

By tag and id:
```python
with open("target_website.html") as target_website:
    html_tree = create_html_tree(
        html_file=target_website,
        specific_tag="div",
        id="super-div"
    )
```

## Calculating distance

As previously said, the used algorithm is the Zhang-Shasha, that computes the edit distance between the two given trees. Ths is possible with the zss package behind the scenes; vanguard only provides a way to convert html files into trees.

```python
from vanguard_kit import create_html_tree, calcuate_html_tree_distance

with open("stored_target_website.html") as stored_file:
    with open("current_target_website.html") as current_file:
        previous_tree = create_html_tree(stored_file)
        current_tree = create_html_tree(current_file)
        print(calcuate_html_tree_distance(previous_tree, current_tree))
        # Rrints 1
```

Due to the VanguardNode class implements the __sub__ dunder method, the next way to calculate the edit distance is possible:

```python
from vanguard_kit import create_html_tree, calcuate_html_tree_distance

with open("stored_target_website.html") as stored_file:
    with open("current_target_website.html") as current_file:
        previous_tree = create_html_tree(stored_file)
        current_tree = create_html_tree(current_file)
        print(previous_tree - current_tree)
        # Rrints 1
```

Then, the next statement returns True:

```python
calcuate_html_tree_distance(previous_tree, current_tree) == previous_tree - current_tree
```

# Development setup

This project uses _pipenv_ for dependecy resolution. It's a kind of mix between
pip and virtualenv. Follow the next instructions to setup the development enviroment.

```sh
$ git clone https://github.com/dany2691/vanguard-kit.git
$ cd vanguard_kit
$ pipenv shell
$ pipenv install -e .
```

To run the test-suite, inside the pybundler directory:

```shell
$ pytest tests/ -vv
```

## Meta

Daniel Omar Vergara Pérez – [@dan1_net](https://twitter.com/dan1_net) – daniel.omar.vergara@gmail.com

[https://github.com/dany2691](https://github.com/dany2691)

## Contributing

1. Fork it (<https://github.com/dany2691/vanguard-kit>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
