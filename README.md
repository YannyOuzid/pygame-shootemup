### Pygame shoot'em up project

### Libraries
```
pygame : python -m pip install pygame
pymongo : python3 -m pip install pymongo
```

### Controls
```
Arrows: Move your player
Space: Use one bomb
Left Shift: `Change your player gameplay to risk mode (the touch must stay pushed)
P : Pause your game and see the highscores (top 10)
```

### Interface
```
Highscore: The highest score in the game
Score: Your actual score
Weapon: The gameplay type of your player
Power: Define the size of your bullet (the maximum is 3)
Speed: Define your shooting speed (the maximum is 3)
Bomb: Number of bombs (You have only 5 bombs)
Lives: Number of lives 
Multiplier: The score multiplier
```

### Rules
```
This game is an infinite shootem up.
Every five enemies killed without being touched, your multiplier and the enemies's 
spawning speed will increase.
When you are touched by an enemy or an enemy bullet, you lose one life, one power level and one speed level,
the enemy's spawning speed and the multiplier are reset.
When you have zero life the game is over.
```

### Risk reward mechanic
```
When you are in risk mode gameplay (keep the Left Shift pressed), 
you can win some points by staying close to the enemiy bullets without being touched
```