from collections import namedtuple

Point = namedtuple('Point', 'x y')
Segment = namedtuple('Segment', 'start end stepsUntil stepsAt')
Intersection = namedtuple('Intersection', 'x y steps')

def load():
    with open("input.txt") as f:
        return [line.strip().split(",") for line in f.readlines()]

def segmentize(wire):
    prev_point = Point(0, 0)
    steps = 0
    segments = []
    for instruction in wire:
        direction = instruction[0]
        magnitude = int(instruction[1:])
        if direction == 'L':
            point = Point(prev_point.x - magnitude, prev_point.y)
        elif direction == 'R':
            point = Point(prev_point.x + magnitude, prev_point.y)
        elif direction == 'D':
            point = Point(prev_point.x, prev_point.y - magnitude)
        elif direction == 'U':
            point = Point(prev_point.x, prev_point.y + magnitude)
        else:
            print(f'Invalid direction: {direction}')
            assert False

        segments.append(Segment(prev_point, point, steps, steps + magnitude))
        prev_point = point
        steps += magnitude

    return segments

def horizontal(segment):
    return segment.start.y == segment.end.y

def vertical(segment):
    return segment.start.x == segment.end.x

def intersect(s1, s2):
    if horizontal(s1) and horizontal(s2):
        return Intersection(None, None, None)
    if vertical(s1) and vertical(s2):
        return Intersection(None, None, None)
    if vertical(s2) and \
            (min(s2.start.y, s2.end.y) < s1.start.y < max(s2.start.y, s2.end.y)) and \
            (min(s1.start.x, s1.end.x) < s2.start.x < max(s1.start.x, s1.end.x)):
        return Intersection(s2.start.x, s1.start.y, s1.stepsUntil + s2.stepsUntil + abs(s2.start.x - s1.start.x) + abs(s2.start.y - s1.start.y))
    if vertical(s1) and \
            (min(s1.start.y, s1.end.y) < s2.start.y < max(s1.start.y, s1.end.y)) and \
            (min(s2.start.x, s2.end.x) < s1.start.x < max(s2.start.x, s2.end.x)):
        return Intersection(s1.start.x, s2.start.y, s1.stepsUntil + s2.stepsUntil + abs(s2.start.x - s1.start.x) + abs(s2.start.y - s1.start.y))
    return Intersection(None, None, None)

wires = load()
segments = [segmentize(wire) for wire in wires]
intersections = []
for s1 in segments[0]:
    for s2 in segments[1]:
        i = intersect(s1, s2)
        if i.x is not None:
            intersections.append(i)

distances = [abs(point.x) + abs(point.y) for point in intersections]
steps = [intersection.steps for intersection in intersections]
print(f'Part 1: {min(distances)}')
print(f'Part 2: {min(steps)}')
