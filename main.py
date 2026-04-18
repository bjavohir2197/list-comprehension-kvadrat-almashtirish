kvadratlar = [x ** 2 for x in range(1, 11)]
print(f"Kvadratlar: {kvadratlar}")
juft = [x for x in range(1, 21) if x % 2 == 0]
print(f"Juft sonlar (1-20): {juft}")
sozlar = ["python", "java", "go", "javascript", "rust"]
uzunliklar = [(s, len(s)) for s in sozlar]
print(f"Uzunliklar: {uzunliklar}")
