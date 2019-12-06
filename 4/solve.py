def doubles(password):
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return True
    return False


def doubles_after_triples(password):
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            password = password.replace(password[i], '')
            return doubles_after_triples(password)
    return doubles(password)


def increasing(password):
    for i in range(5):
        if password[i] > password[i + 1]:
            return False
    return True


start = 136818
end = 685979
passwords = []
for password_int in range(start, end):
    password = str(password_int)
    if doubles(password) and increasing(password):
        passwords.append(password)

print(f'Part 1: {len(passwords)}')

filtered = []
for password in passwords:
    if doubles_after_triples(password):
        filtered.append(password)

print(f'Part 2: {len(filtered)}')
