def load():
    with open('input.txt') as f:
        return [int(code) for code in f.readline().split(',')]


class Computer():
    def __init__(self, input):
        self.program = input
        self.pointer = 0
        self.steps = 4

    def modify(self, noun, verb):
        self.program[1] = noun
        self.program[2] = verb

    def value_at(self, location):
        return self.program[self.program[location]]

    def add(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]

        self.program[self.program[self.pointer + 3]] = value1 + value2
        self.steps = 4

    def multiply(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]

        self.program[self.program[self.pointer + 3]] = value1 * value2
        self.steps = 4

    def set_value(self):
        self.program[self.program[self.pointer + 1]] = 5  # hack for now
        self.steps = 2

    def output(self):
        if self.modes[0] == '0':
            value = self.value_at(self.pointer + 1)
        else:
            value = self.program[self.pointer + 1]
        print(value)
        self.steps = 2

    def jump_if_true(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]
        if value1 != 0:
            self.pointer = value2
            self.steps = 0
        else:
            self.steps = 3

    def jump_if_false(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]
        if value1 == 0:
            self.pointer = value2
            self.steps = 0
        else:
            self.steps = 3

    def less_than(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]
        if value1 < value2:
            self.program[self.program[self.pointer + 3]] = 1
        else:
            self.program[self.program[self.pointer + 3]] = 0
        self.steps = 4

    def equals(self):
        if self.modes[0] == '0':
            value1 = self.value_at(self.pointer + 1)
        else:
            value1 = self.program[self.pointer + 1]
        if self.modes[1] == '0':
            value2 = self.value_at(self.pointer + 2)
        else:
            value2 = self.program[self.pointer + 2]
        if value1 == value2:
            self.program[self.program[self.pointer + 3]] = 1
        else:
            self.program[self.program[self.pointer + 3]] = 0
        self.steps = 4

    def run_step(self):
        instruction = int(str(self.program[self.pointer])[-2:])
        self.modes = str(self.program[self.pointer])[:-2][::-1]
        self.modes = (self.modes + '000')[:3]
        if instruction == 1:
            self.add()
        elif instruction == 2:
            self.multiply()
        elif instruction == 3:
            self.set_value()
        elif instruction == 4:
            self.output()
        elif instruction == 5:
            self.jump_if_true()
        elif instruction == 6:
            self.jump_if_false()
        elif instruction == 7:
            self.less_than()
        elif instruction == 8:
            self.equals()
        else:
            print(f'Invalid code: {instruction} at {self.pointer}')

        self.pointer += self.steps

    def run(self):
        while self.program[self.pointer] != 99:
            self.run_step()

        return self.program[0]


def solve_part_1():
    computer = Computer(load())
    print(f'Part 1: {computer.run()}')

def solve_part_2():
    computer = Computer(load())
    print(f'Part 2: {computer.run()}')

solve_part_2()
