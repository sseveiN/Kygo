from sys import exit
from random import randint
import time


class Scene(object):

	def enter(self):
		print "Scene not configured yet."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		print "Engine has scene map.", scene_map
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "------------------------------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class RunOver(Scene):

	car = ["Lamborghini Aventador", "Jaguar F-Type",
			"Corvette Stingray", "Mazda Miata",
			"Porshe 911 RS", "Tesla Roadster",
			"Ford Mustang GT", "Chevy Camaro",
			]
	def enter(self):
		print "You forget about what just happened and decide to " \
		      "cross the street."

		print "You get runover by a", \
		      RunOver.car[randint(0, len(self.car)-1)] + "."

		exit(1)

class Walking(Scene):

	def enter(self):
		print "KYGO"
		print "ITS A TRIP"
		print "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-"
		print "You're walking down the street, when you see a kitten."
		print "It's small, grey, and wandering about ahead " \
		      "of you on the sidewalk."
		print "As you get closer, it eyes you."
		print "You stop in front of it, locking eyes. " \
		      "(Should I say hi or ignore it?)"

		response = raw_input("> ")

		if 'hi' in response:
			print "Hey buddy, whatcha up to?"
			print "Well let's see who you're owner is."
			print '"KYGO" - Cat'
			print "Doesn't seem you have an owner, " \
			      "I'll take you to the shelter, don't worry about it."
			sleep()
			return 'stolen'

		elif 'ignore' in response:
			print "You ignore the cat."
			sleep()
			return 'run_over'

		else:
			print "DOES NOT COMPUTE!"
			sleep()
			return 'walking'

class Stolen(Scene):

	def enter(self):
		print "As you walk down the street, someone comes from" \
		      " behind and takes Kygo!"
		print "He'll get away in a couple of seconds if you don't do anything!" \
		      "(Should I run or wait?)"

		now = time.time()
		get_away = now + 10
		response = raw_input("> ")

		while time.time() < get_away:

			if 'run' in response:
				print "You start chasing after the man and Kygo!"
				print "He's gone into a crowd full of people!"
				sleep()
				return 'catch_up'

			elif 'wait' in response:
				print "You see Kygo being taken away in the distance."
				sleep()
				return 'run_over'

			else:
				print "DOES NOT COMPUTE"
				sleep()
				return 'run_over'

		print 'He got away with Kygo!'
		return 'run_over'

class Catch(Scene):

	def enter(self):
		print 'As you push your way through people, you start getting closer.'
		print 'Kygo is meowing at you.'
		print 'You finally catch up and get a hold of the robber.'
		print 'He drops Kygo and puts his hands up.'
		print 'Do you want to fight or run?'

		response = raw_input('> ')

		if 'fight' in response:
			your_hp = 20
			robber_hp = 20
			robber = True

			print "GET READY TO RUMBLE!!!!!"

			while your_hp > 0 and robber:
				your_attack = randint(4,10)
				robber_attack = randint(4,10)

				robber_hp -= your_attack

				attacks = [
				    'LEFT-CROSS', 'RIGHT-JAB',
				    'UPPERCUT', 'FALCO PUNCH!!!!!!!'
				]

				raw_input('> ')

				print 'YOU HIT HIM WITH A', attacks\
				[randint(0, len(attacks)-1)] + '!!!'

				if robber_hp < 0:
					print '\n911YOU KNOCKED HIM OUT!'
					robber = False

				your_hp -= robber_attack

				if robber:
					raw_input('> ')
					print 'HE HIT YOU WITH A', attacks\
					[randint(0, len(attacks)-1)] + '!!!'

					if your_hp < 0:
						print '\nYOU GOT KNOCKED OUT!'
						return 'run_over'

			print 'You pick up the scared Kygo.'
			print 'You take out your phone to call the police.'
			return 'call'

		elif run in response:
			print 'You run and run and run.'
			return 'run_over'

class Call(Scene):

	def enter(self):
		print "What's the number for the police again?"
		number = int(raw_input('> '))

		if number == 911:
			print "You call 911."
			print "'What's the emergency?'"
			print "Ok, an officer will be there in just a second."
			return 'the_end'

		else:
			print "I don't think that's it put lets try it."
			print 'Nope.'
			return 'call'

class TheEnd(Scene):

	def enter(self):
		print "The officer arrives and takes the man away."
		print "Kygo sits there looking at you."
		print "Kygo knows what you did for him."
		print "You adopt Kygo."
		print "You live life with Kygo, and have fun with him."
		print "The End."
		exit(1)

class Map(object):
	scenes = {
	'run_over': RunOver(),
	'walking': Walking(),
	'stolen': Stolen(),
	'catch_up': Catch(),
	'call': Call(),
	'the_end': TheEnd()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene
		print "start_scene in __init__", self.start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


def sleep():
	time.sleep(5)


a_map = Map('walking')
a_game = Engine(a_map)
a_game.play()