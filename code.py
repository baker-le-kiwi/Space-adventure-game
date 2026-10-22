import random
import time
dice_roll = random.randint(1, 6)
oxygen = 100
inventory = []
c1 = 0
c12 = 0
c22 = 0
c13 = 0
c23 = 0
c33 = 0
c41 = 0
print("=" * 27)
print("Welcome to space adventure")
print("=" * 27)
time.sleep(5)
print("""
You are stranded on an asteroid
Astr382805043
You must escape before your oxygen runs out
""")
time.sleep(5)
c1 = input("""
you are in the middle of a large crater,
the wreckage of your ruined ship lays behind you,

[1]: Look around the wreckage of the ship
[2]: Attempt to exit the crater 
what is your first decision: 
""")
if c1 == "2":
    c12 = input("""
You wander foreward for what seems like hours, 
stumbling over rocks and more rock, and more rocks.
So many rocks, and so much dust, you make it to the edge
and see miles of dust and rock, however, something catches your eye, 
aha, some sort of tower, off to the left
[1]: Go left
[2]: Go right
""")
elif c1 == "1":
    c22 = input("""
You scrounge through the wreckage 
and come across many curious objects,
a kiwi stuffed animal,
a small laser blaster,
and a can full of rotten sardines.
[1]: Take the kiwi
[2]: Take the blaster
[3]: Take the expired sardines
""")
else:
    print("Invalid choice")
if c22 == "1":
    print("you take the kiwi, good choice")
    inventory.append("Kiwi stuffed animal")
if c22 == "2":
    print("You take the laser blaster, sensible choice")
    inventory.append("Laser blaster")
if c22 == "3":
    print("You take the sardines, for some reason")
    inventory.append("Expired sardines")
else:
    print("")
if c22 == "1" or "2" or "3":
    c12 = input("""
You wander foreward for what seems like hours, 
stumbling over rocks and more rock, and more rocks.
So many rocks, and so much dust, you make it to the edge
and see miles of dust and rock, however, something catches your eye, 
aha, some sort of tower, off to the left
[1]: Go left
[2]: Go right
""")
else:
    print("")
if c12 == "1":
    print("You go left, following the distant outline of the tower")
    c13 = input("""
You continue wandering for a long time, and find,
a rock, a blue rock, a blue shiny rock, a shiny blue cyrstal
[1]: Pick up rock
[2]: Continue on
""")

    if c13 == "1":
        print("""
You reach out to pick up the rock, even through your spacesuit, you can feel the heat pouring off of it.
Luckily you pack is rated for space, unfortunatly, glass is not,
as your reach around to put it in your bag, the glass on your helmet begins to melt.
As it does, your radiation alarm begins to blare in your helmet.
The crystal must be pouring gamma rays to penetrate  your suit.
you collapse onto the ground, suddently weak, then everything goes black. """)
        print("")
        print("""You do not wake up, Game over""")
    if c13 == 2:
        print("")
    else:
        print("")
    if c12 == "2":
        print("You go right, ignoring the possibly creepy, disturbing alien tower")
        c23 = input("""
You walk along the ridge of the crater for a while, 
until, 
no,
is that?
it is!
Mr.Beast appears infront of you,
would you like to take part in my 100 day asteroid survival video?
[1]: Say yes and show him you are subscribed
[2]: Throw sardines at him (requires sardines)
[3]: Say 'NO!' and run away
""")

        if c23 == "1":
            print("""Mr.Beast sees you are subscribed and you join the video, 
            you are the only competator and by default, win a million dollars
            """)
            time.sleep(3)
            print("""As you are distracted, celebrating you win, Mr.Beast cuts your oxygen hose
            You die. 
            But hey, million dollars!""")
        if c23 == "2" and "Expired Sardines" in inventory:
            print("""
Mr.Beast staggers backwards, the sardine fumes penetrating his helmet,
he begins to cough, then he keels over, seemingly dead
You rush foreward, but it is too late,
Karl has already taken the prize pool away""")
            c33 = input("""
[1]: Chase after karl
[2]: Mourn Jimmy
[3]: Do fortnite emotes over dead body 
""")
        else:
            print("")
        if c23 == "3":
            print("""
As you run away screaming, Jimmy yells the words, 'Duo, sic him',
duolingo owl appears out of nowhere,
then, he rushes after you, pursuing at terrifying speeds,
holding a fillet knife""")
            c41 = input("""
[1]: Continue to run from duo
[2]: Hold out your streak sheild
""")


# if c33 == "1":
#    print("")
# if c33 == "2":
#    print("")
# if c33 == "3":
#    print("")
# if c41 == "1":
#    print("")
# if c41 == "2":
#    print("")