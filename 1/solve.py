def load_input():
    with open("input.txt") as input:
        return input.readlines()


def fuel(mass):
    return (mass // 3) - 2


def fuel_with_extras(mass):
    res = 0
    while mass > 0:
        mass = fuel(mass)
        if mass > 0:
            res += mass

    return res


modules = [int(module) for module in load_input()]

total_fuel = sum(fuel(module) for module in modules)
print(f"Fuel needed: {total_fuel}")

actually_total_fuel = sum(fuel_with_extras(module) for module in modules)
print(f"Including fuel for fuel: {actually_total_fuel}")
