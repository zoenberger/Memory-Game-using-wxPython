# Memory-Game-using-wxPython

REQUIRES: wxPython. So go install that first. 

Background: I was doing some wxPython tutorials, but I just wasn't getting it, so I gave myself a mini project: this game! It's just a basic memory game with cards you click looking for pairs. Very ruidimentary on initial commit, but works great-ish!


IMAGES:
All the images in the Images folder are so you can run out of box. You can actually populate that folder with your own JPEGs and it will work fine. Though make sure all the JPEGs are same size or something will happen probably. You can also change the function that reads the Images folder to read PNG files or other supported types by wxPython. I just left it .jpg files for now. 
Sleep Function:
Ugh. When the user clicks on the second card and it is NOT a match, the program wiaths 1.5 seconds so the user can look at the cards before they're hidden again. Standard SOP for memory games. However, the Sleep timer I used doesn't halt wxPython event handling, so if you click during the time, it executes it immediately after timer. Need to make that better.


Hippie Score Keeping:
Aka, no score keeping. I would like to add a timer for the game and number of succesful attempts and total attempts. That's why there is a blank space to right. 

Skill Levels:
As of now, one skill level: 24 cards with 12 pairs. Though I tried to make some built-in flexibility for added functionality later. 

wxPython:
I don't know why I find it so difficult, but I'm trying. And if you see bad practices in my code (which I'm sure it's riddled with), be sure to let me know. 
