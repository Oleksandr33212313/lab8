all_words = []
print("Вводьте рядки. Порожній рядок — завершення вводу.")
while True:
    line = input()
    if line == "":
        break
    words = line.split()       
    all_words.extend(words)     
unique_words = []
for w in all_words:
    if w not in unique_words:
        unique_words.append(w)
result = " ".join(unique_words)
print("Результат:", result)