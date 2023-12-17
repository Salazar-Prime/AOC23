with open("day14/day14-1.txt") as file:
    map = [list(line.replace("\n", "")) for line in file]
    results = []
    for _ in range(1000_000_000):
        for _ in range(4):
            for r in range(len(map)):
                for c in range(len(map[0])):
                    if map[r][c] in ["#", "O"]:
                        continue
                    r2 = r + 1
                    while r2 < len(map) and map[r2][c] != "#":
                        if map[r2][c] == "O":
                            map[r][c] = "O"
                            map[r2][c] = "."
                            break
                        r2 += 1
            map = [[r[col] for r in map][::-1] for col in range(len(map[0]))]
        results.append(sum(l.count("O") * (len(map) - il) for il, l in enumerate(map)))

        for i in range(int(len(results) / 2)):
            for ir in range(2, int(len(results))):
                if results[i : i + ir] == results[i + ir : i + ir + ir]:
                    pattern = results[i : i + ir]
                    print(pattern[(1_000_000_000 - i - 1) % len(pattern)])
                    exit(0)
