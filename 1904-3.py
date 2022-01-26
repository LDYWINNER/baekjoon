# for reference
from itertools import permutations


def unique_perms(series):
    return {"".join(p) for p in permutations(series)}

print(sorted(unique_perms('110')))