def recurr(vis, ans):
    if (len(ans) > 0):
        if (ans in se):
            return
        se[ans] = 1
    for i in range(len(tiles)):
        if (vis[i]):
            continue
        vis[i] = True

        recurr(vis, ans + tiles[i])
        vis[i] = False

tiles = "AAABBC"
curr = ""

se = dict()
vis = [False] * (len(tiles))
recurr(vis, curr)
print(len(se))