maximetro
=========

maximetro is a traffic game inspired by Mini Metro(*). It is writen in Python
using Pygame. Should be multi user some day.

Stil in early pre-alpha. I plan to make a more strategical game than Mini Metro
is.

Gameplay 
--------

Just click around to get a feeling for the game. You should build lines. Than
railcars run on them and transport passengers to ther destinations. You gain
points for delivered passengers. The buttons at the right delete or add tracks
to existing lines.

But keep in mind: The game is stil in very early development and far from beeing
an interesting game.

Installation 
------------

You need python and pygame. Under Debian/Ubuntu and similar systems the
following should work:

	apt-get install python python-pygame 
	git git clone https://github.com/bennibaermann/maximetro.git 
	maximetro/maximetro.py 

I have no idea how to install under other systems. But in general you need
python and pygame and than clone the git repository. The underlying technologies
(SDL, Pygame, Python) are all very portable, so it should be possible to run it
more or less on any system.

Have fun.

(*) http://dinopoloclub.com/minimetro/
