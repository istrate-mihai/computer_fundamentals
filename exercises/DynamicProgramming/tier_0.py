# Exercise 1 — Top-Down

# You have n tiles to place. Each tile is either 1 unit wide or 2 units wide. How many ways can you tile a board of length n ?

def place_tiles(n):
    if n <= 2:
        return n

    