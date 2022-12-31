# Below is a command that randomly chooses day of theweek from a list

import random as rn
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('This week, my favorite day is: ' + Days[rn.randrange(0,7)])
