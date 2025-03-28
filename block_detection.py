from functools import lru_cache
reactions = [(2, 1, 0, 2), (1, 1, 1, 1),  (0, 0, 2, 1),  (0, 3, 0, 0), (1, 0, 0, 1)]
@lru_cache(maxsize=None)
def is_winning(a, b, c, d):
    for reaction in reactions:
        aa, bb, cc, dd = reaction
        if a >= aa and b >= bb and c >= cc and d >= dd:
            if not is_winning(a - aa, b - bb, c - cc, d - dd):
                return True
    return False

n = int(input())
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if is_winning(a, b, c, d):
        print("Patrick")
    else:
        print("Roland")