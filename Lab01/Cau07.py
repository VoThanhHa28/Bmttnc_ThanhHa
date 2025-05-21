print("Input writting line (input 'done' to finish): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
for line in lines:
    line.upper()
print(lines)

    