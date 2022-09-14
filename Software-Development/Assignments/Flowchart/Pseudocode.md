# Pseudocode for Knight's Tour Problem
---

This is pseudocode for the (apparently overwhelmingly difficult) Knight's Tour problem, to be created from scratch in Pygame. This is supplimentary to the Flowchart included in the same file.

---

First, Import Pygame and os - for handling advanced interactions with GUI and filesystems


A graphical environment in an independant window is established using the Pygame framework


A function is created to establish a chessboard within this window. This is performed through the utilisation of Pygame to generate the dimensions of the chessboard according to user specifications. The board must record the relative x&y positions of the squares generated, along with the order in which they are drawn on the screen. This will be done through assigning each value its own generated entry within a python dictionary.


The user must be able to click on ANY square, to create a Knight chess piece on that tile. Doing so must be able to lock the knight sprite to the coordinate selected, and change the colouration of the tile selected. A button must next be pressed that algorithmically generates a path for the knight to take around the generated chess board using the data of the x & y positions within the dictionary.


Additionally, this means some kind of algorithm must be produced, to determine suitable "paths" for the knight to take. This will need to utilise the coordinates of generated squares, allowed movements of a knight-type chess piece, and the coordinates that have been visited by the knight before. A predictive model will need to be formed to ensure that no movement is repeated, and that every square is eventually reached, as shown [here.](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Knight%27s_tour.svg/1200px-Knight%27s_tour.svg.png)

