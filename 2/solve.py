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
        self.program[self.program[self.pointer + 3]] = \
            self.value_at(self.pointer + 1) + self.value_at(self.pointer + 2)
        self.steps = 4

    def multiply(self):
        self.program[self.program[self.pointer + 3]] = \
            self.value_at(self.pointer + 1) * self.value_at(self.pointer + 2)
        self.steps = 4

    def run_step(self):
        if self.program[self.pointer] == 1:
            self.add()
        elif self.program[self.pointer] == 2:
            self.multiply()
        else:
            print(f'Invalid code: {self.program[self.pointer]} at {self.pointer}')

        self.pointer += self.steps

    def run(self):
        while self.program[self.pointer] != 99:
            self.run_step()

        return self.program[0]


def solve_part_1():
    computer = Computer(load())
    computer.modify(12, 2)
    print(f'Part 1: {computer.run()}')


def solve_part_2():
    TARGET = 19690720
    for noun in range(100):
        for verb in range(100):
            computer = Computer(load())
            computer.modify(noun, verb)
            result = computer.run()
            if result == TARGET:
                print(f'Part 2: Noun {noun}, verb {verb}, answer {100 * noun + verb}')
                break


solve_part_1()
solve_part_2()
