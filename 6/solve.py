from collections import namedtuple

Orbit = namedtuple('Orbit', 'centre satellite')

class Body:
    def __init__(self, name):
        self.name = name
        self.centre = None
        self.satellites = []

    def __repr__(self):
        return self.name

def make_orbit(orbit_line):
    orbit_line = orbit_line.strip()
    orbit_bodies = orbit_line.split(')')
    return Orbit(orbit_bodies[0], orbit_bodies[1])

def load():
    with open('input.txt') as f:
        return [make_orbit(orbit_line) for orbit_line in f.readlines()]

bodies = {}
for orbit in load():
    centre = bodies.get(orbit.centre, Body(orbit.centre))
    satellite = bodies.get(orbit.satellite, Body(orbit.satellite))
    centre.satellites.append(satellite)
    satellite.centre = centre
    bodies[centre.name] = centre
    bodies[satellite.name] = satellite

def count_orbits(body):
    if body.centre is not None:
        return count_orbits(body.centre) + 1
    else:
        return 0

# Part 1
orbits = 0
for body in bodies:
    orbits += count_orbits(bodies[body])

print(f'Part 1: {orbits}')

# Part 2
you = bodies['YOU']
san = bodies['SAN']

you_centres = []
while you.centre is not None:
    you_centres.append(you.centre)
    you = you.centre

san_centres = []
while san.centre is not None:
    san_centres.append(san.centre)
    san = san.centre

for centre in you_centres:
    if centre in san_centres:
        distance = you_centres.index(centre) + san_centres.index(centre)
        print(f'Part 2: {distance}')
        break
