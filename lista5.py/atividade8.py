
def primo(n):
    if n % 2 == 0 and n != 2:
        return False
    else:
        return True

print(primo(7))
print(primo(4))
print(primo(2))
print(primo(11))
print(primo(15))