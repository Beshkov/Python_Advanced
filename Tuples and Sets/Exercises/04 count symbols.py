read_ln = input()

uniques = set()
for el in read_ln:
    count = read_ln.count(el)
    uniques.add(f"{el}: {read_ln.count(el)} time/s")

uniques = sorted(uniques)
[print(el) for el in uniques]