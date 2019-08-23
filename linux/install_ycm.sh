#!/bin/bash

cp -r ./.vim ~/.vim
cp ./.vimrc ~
cd ~/.vim/bundle/YouCompleteMe

py2_installed=$(dpkg -s python2.7 | grep "install ok installed")
py3_installed=$(dpkg -s python3 | grep "install ok installed")

if [ "$py2_installed" == "" && "$py3_installed" == ""];
then
    sudo apt-get install python2.7
fi

sudo apt-get install python-dev python3-dev

sudo apt-get install llvm-3.9 clang-7 libclang-7-dev libboost-all-dev

# sudo python ./install.py --all
sudo python ./install.py --clang-completer

mkdir ~/.ycm_build
cd ~/.ycm_build

cmake -G "Unix Makefiles" -DUSE_SYSTEM_BOOST=ON -DUSE_SYSTEM_LIBCLANG=ON . ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp

cmake --build . --target ycm_core --config Release

cp ~/.vim/bundle/YouCompleteMe/third_party/ycmd/examples/.ycm_extra_conf.py ~/.vim/

vi ~/.vim/.ycm_extra_conf.py
