#!/bin/bash
# mkdir ~/.vim/bundle
# cp ~/GitProj/vim/YouCompleteMe.zip ~/.vim/bundle
cd ~/.vim/bundle
unzip YouCompleteMe.zip
cd YouCompleteMe
sudo python ./install.py --clang-completer

