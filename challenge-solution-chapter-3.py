# Chapter 3

# 3.1

names = ['Fariha', 'Andrew', 'Karen', 'Gelle', 'Mahdi']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[-4])

# 3.2

message_for_names = "Hey " + names[0] + " I just wanted to tell you that you are beautiful"
print(message_for_names.title())


# 3.3

my_fav_transportation = ['Tesla', 'Train', 'Bus', 'plane', 'Bicycle']
message_for_transportation = " One day I am going to buy a " + my_fav_transportation[0] + " and I'll cruise around with my Mom and give her a taste of what it feels like to be in an expensive car( Inshallah)"
print(message_for_transportation.lstrip().title())

# 3.4

my_guests = ['Michael Sayman', 'Tim Cook', 'Anthony D. Mays', 'Sundar Pichai', 'shuo-from-intel' ]


message_to_guest0 = "Hello " + my_guests[0] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"

message_to_guest1 = "Hello " + my_guests[1] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"

message_to_guest2 = "Hello " + my_guests[2] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"



print(message_to_guest0.title())
print(message_to_guest1.title())
print(message_to_guest2.title())


# 3.5

my_guests = ['Michael Sayman', 'Tim Cook', 'Anthony D. Mays', 'Sundar Pichai', 'shuo-from-intel' ]

my_guests.pop(0)
my_guests.insert(0, 'Fariha')

message_to_guest0 = "Hello " + my_guests[0] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"

message_to_guest1 = "Hello " + my_guests[1] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"

message_to_guest2 = "Hello " + my_guests[2] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"



print(message_to_guest0.title())
print(message_to_guest1.title())
print(message_to_guest2.title())

# 3.6

my_guests = ['Michael Sayman', 'Tim Cook', 'Anthony D. Mays', 'Sundar Pichai', 'shuo-from-intel' ]

my_guests.pop(0)
my_guests.insert(0, 'Fariha')
my_guests.insert(3, 'Tamim')
my_guests.append('Google')

message_to_guest0 = "Hello " + my_guests[0] + "I am inviting you to have a dinner with me so I'd get to know you a bit more and may be a get a bit of advice from you"

print(message_to_guest0.title())
print(my_guests)

# 3.7
# Still gotta do this tomorrow!
