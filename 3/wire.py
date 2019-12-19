class Wire:
    route = [(0, 0)]

    def up(lkm):
        for i in lkm:
            cache = route[-1]
            route.append(cache)
