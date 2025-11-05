s = input("Введіть рядок зі словами, розділеними комами і пробілами: ")
words = s.split(", ")
result = words[0] + " " + words[-1]
print("Результат:", result)