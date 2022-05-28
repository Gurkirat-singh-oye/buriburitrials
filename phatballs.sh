#!/bin/bash
cd workdir
git init
git pull --no-rebase --allow-unrelated-histories https://github.com/Gurkirat-singh-oye/Charlie-the-bot
python3 kanjar.py
