# Constructionist - A Static Site Generator in Python

## Prerequisites
Constructionist requires a Python 3.x installation

## How to install

Constructionist can be currently installed as follows:

```bash
$ git clone git@github.com:mrstanb/constructionist.git
$ python3 -m pip install -r requirements.txt
```

## Usage
For now, rather simplistic:

* Constructionist assumes Markdown content to be in the `/content` folder
* It then goes on to generate HTML content in the `/public` folder
* You can simply call it from the terminal as follows:

```bash
$ ./constructionist.py
```

In case this doesn't work, you might wanna try the following before running Constructionist:

```bash
$ chmod +x constructionist.py
```
