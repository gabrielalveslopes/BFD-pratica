def palindromo(palavra):
    return palavra == palavra[::-1]

print(palindromo("arara"))
print(palindromo("banana"))
print(palindromo("civic"))
print(palindromo("deified"))
print(palindromo("hello"))