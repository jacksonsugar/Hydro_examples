Raspberry Pi compile from source.

$ sudo apt-get update
$ sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev pkg-config libgl1-mesa-dev libgles2-mesa-dev python-setuptools libgstreamer1.0-dev git-core gstreamer1.0-plugins-{bad,base,good,ugly} gstreamer1.0-{omx,alsa} python-dev libmtdev-dev xclip xsel python-pip

$ sudo pip install pygame cython

%%%
Quick install
sudo pip install git+https://github.com/kivy/kivy.git@stable-1.10


%%%%
Build from source
~/Documents/ $ git clone https://github.com/kivy/kivy

~/Documents/ $ cd kivy

~/Documents/kivy/ $ make
~/Documents/kivy/ $ echo "export PYTHONPATH=$(pwd):\$PYTHONPATH" >> ~/.profile
~/Documents/kivy/ $ source ~/.profile

