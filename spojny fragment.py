alphabet = [chr(number) for number in range(65,91)]

rows = []
while rows == []:
    path = input("> Please enter the path to your file [.txt]: ")
    if path.endswith(".txt") == False: path += ".txt"
    try: rows = open(path).read().split("\n")
    except: print("> Couldn't open the file! Please write the correct file path: ")
rows = [row for row in rows if row]

for row in rows:
    for character in row:
        if character.upper() not in alphabet: row = row.replace(character, '')
    splitRow = []
    n = 0
    for x in range(len(row)):
        if x != 0 and row[x] != row[x-1]:
            splitRow.append(str(row[n:x]))
            n = x
        if x == len(row) - 1: splitRow.append(str(row[n:]))
        else: pass
    longestString = max(splitRow, key=len)
    print(longestString, len(longestString))
input()
