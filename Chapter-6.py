# A simple Dictionary

# alien_0 = {'color': 'Green', 'point':5}
#
# print(alien_0['color'])
# print(alien_0['point'])

#Alien Shoot down

# alien_1 = {'color': 'green', 'points': 5}
# new_points = alien_1['points']
# print("You just earned " + str(new_points)+ " points.")


# Adding a new Key-Value pairs

# alien_2 = {'color': 'green', 'points': 5}
# print(alien_2)
#
# alien_2['X-position'] = 0
# alien_2['y-position'] = 25
# print(alien_2)


# Starting with an empty Dictionary
# Modifying Values in a Dictionary

# alien_3 = {}
# alien_3['color'] = 'Blue'
# alien_3['points'] = 233
# print(alien_3)
#
# alien_3['color'] = 'Yellow'
# print(alien_3)


# Tracking Alien's Movement
alien_4 = {'x-position':0, 'y-position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_4['x-position']))


# Move the Alien to the right
#Determine how far to move the alien based on it's current speed'

if alien_4['speed']=='slow':
    x_increment = 1
elif alien_4['speed']=='medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus the increment.
alien_4['x_position'] = alien_4['x_position'] + x_increment

print("New x-position: " + str(alien_4['x_position']))
