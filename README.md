# python-typing-tutorial

A sample Python project to demonstrate basic type checking concepts and best practices.

The four sample projects included correspond to each section of the PyCon 2022 "Python Types for Fun and Profit" tutorial.

1. `introduction_exercises`: Annotating examples of basic data structures.
2. `demo_project`: Getting-started demo for setting up Pyre locally in a new project.
3. `gradual_typing_project`: Example project for applying type checking modes and other approaches to gradually increasing type coverage.
4. `typing_pattern_exercises`: More detailed and advanced Python patterns to practice expressing dynamic behavior in the type system

## Setting up

You'll want a python 3.10 environment and `watchman`, along with the
latest version of the `pyre-check` package

### Installing watchman

#### On MacOS

```bash
brew install watchman
```

#### On Ubuntu

```bash
sudo apt-get -y watchman
```


### Installing Pyenv

How exactly to get the latest Python release varies system to system,
and you may already use a solution such as `conda`.

We have instructions for using `pyenv` for this, but you're welcome
to use any other approach you know.

#### On MacOS

```bash
brew install pyenv
```

#### On Ubuntu

```bash
sudo apt-get -y watchman\
    git make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev \
    
# clone pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

#### On windows:

We recommend using the Windows Subsystem for Linux:
- Open a windows console in administrator mode
- Run `wsl --install -d Ubuntu-20.04`
- Restart your computer
- When it restarts, the `Ubuntu-20.04` application should open
  - Create a user. We recommend reusing the user from your
    windows install, but you could create a user just for pycon
  - Now, follow the `Ubuntu` instructions
  
From this point forward, to work with pyre you can:
- Open the `Ubuntu-20.04` application
- Do any terminal actions (like running `pyre`) you want from
  that terminal session.
- In order to use native tools, like your (VSCode editor) with
  files here, run `explorer.exe <name_of_a_directory>`
  - This will open up the directory in windows explorer.
  - From there you can do things like open files in VSCode.

### Configuring Pyenv and installing Python 3.10

In your `~/.profile`, write

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
export PATH="$PYENV_ROOT/shims:$PATH"
eval "$(pyenv init -)"
```

Then in a new shell:
```
pyenv install 3.10.4
```

### Clonning the tutorial repository and installing pyre-check


You can clone this repo in one of two ways:
- First fork it to your user using the "Fork" button, and then
  clone from that repository
- Or, if you don't care about playing with github, just clone directly:
  `git clone https://fbsamples/python-typing-tutorial.git`
  
Then, set it up to use Python 3.10.4:
```
cd python-typing-tutorial
pyenv local 3.10.4
```

Finally, install the latest release pyre:
```
pip install pyre-check
```

You can make sure it works by running
```
cd gradual_typing_project
pyre init <<< '
'
pyre
```
which should spit out:
```
ƛ No type errors found
```

## Contributing

See the [CONTRIBUTING](CONTRIBUTING.md) file for how to help out.

## License

python-typing-tutorial is MIT licensed, as found in the LICENSE file.
