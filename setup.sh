# Local
brew install pyenv pyenv-virtualenv
pyenv install 3.7.9
pyenv virtualenv 3.7.9 JableTVDownload
pyenv local JableTVDownload
pip install -U pip
pip install --upgrade setuptools
pip install -r requirements.txt


# Multipass
multipass launch
multipass find
multipass ls
multipass launch lts -c 2 -d 20G -m 8G -n ubuntu --mount ~/Temp:/home/ubuntu/Temp
# Install GUI
multipass shell ubuntu
sudo apt update
sudo apt install ubuntu-desktop xrdp

multipass mount ~/Temp ubuntu:/home/ubuntu/Temp
sudo apt install python3-pip
cd ~/Temp/JableTVDownload/
pip3 install -r requirements.txt
./batch.sh

multipass restart ubuntu