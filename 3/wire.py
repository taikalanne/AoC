class Wire:
    route = []

    def __init__(self):
        self.route = [(0, 0)]

    def current_pos(self):
        return self.route[-1]

    def up_once(self):
        cache = self.route[-1]
        self.route.append((cache[0], cache[1]+1))

    def down_once(self):
        cache = self.route[-1]
        self.route.append((cache[0], cache[1]-1))

    def right_once(self):
        cache = self.route[-1]
        self.route.append((cache[0]+1, cache[1]))

    def left_once(self):
        cache = self.route[-1]
        self.route.append((cache[0]-1, cache[1]))

    def up(self, lkm):
        cache = self.route[-1]
        for i in range(1, lkm+1):
            self.route.append((cache[0], cache[1]+i))

    def down(self, lkm):
        cache = self.route[-1]
        for i in range(1, lkm+1):
            self.route.append((cache[0], cache[1]-i))

    def right(self, lkm):
        cache = self.route[-1]
        for i in range(1, lkm+1):
            self.route.append((cache[0]+i, cache[1]))

    def left(self, lkm):
        cache = self.route[-1]
        for i in range(1, lkm+1):
            self.route.append((cache[0]-i, cache[1]))
