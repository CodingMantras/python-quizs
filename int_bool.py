my_List = [True, 1, "python", 5, False, {}, True]
integers_found = 0
bools_found = 0

for item in my_List:
    if isinstance(item, bool):
        integers_found += 1
    elif isinstance(item, int):
        bools_found += 1

print(f"{integers_found = } {bools_found = }")
