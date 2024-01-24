n = int(input("Zeilenanzahl Pascalsche Dreieck"))

triangle = []
# Erzeugung des Pascalschen Dreiecks
for i in range(n):
    row = []
    for j in range(i + 1):
        if j == 0 or j == i:
            # Erstes und Letztes Element einer Reihe sind 1
            row.append(1)
        else:
            previous_row = triangle[i - 1]
            row.append(previous_row[j - 1] + previous_row[j])
    triangle.append(row)

# Ausgabe Pascal'sches Dreieck
for row in triangle:
    print(" ".join(map(str, row)).center(n * 3))
        