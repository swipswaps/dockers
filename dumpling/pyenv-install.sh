#!/bin/bash
git clone https://github.com/pyenv/pyenv.git /usr/local/pyenv
export PYENV_ROOT="/usr/local/pyenv"
export PATH="$PYENV_ROOT/shims:$PATH"
export PYENV_SHELL=bash
/usr/local/pyenv/bin/pyenv rehash 2>/dev/null
/usr/local/pyenv/bin/pyenv install 3.8.1
export PYENV_VERSION=3.8.1
pip install black
export PYENV_VERSION=system
