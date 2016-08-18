class HexMap(object):

    def __init__(self, number_of_rows, number_of_columns, members=None):
        self.x_height = number_of_rows
        self.y_height = number_of_columns
        number_of_members = number_of_columns * number_of_rows

        if not members:
            members = [None for x in range(number_of_members)]

        if len(members) < number_of_members:
            members = members * int(number_of_members * len(members) + 0.5)

        the_map = list()
        i = 0
        for x in range(number_of_rows):
            row = list()
            for y in range(number_of_columns):
                row.append(members[i])
                i += 1
            the_map.append(row)
        self.the_map = the_map

    def get_neighbours(self, x_pos, y_pos):
        top_left = self.get(x_pos, y_pos - 1)
        top_right = self.get(x_pos - 1, y_pos - 1)
        middle_left = self.get(x_pos - 1, y_pos)
        middle_right = self.get(x_pos + 1, y_pos)
        bottom_left = self.get(x_pos, y_pos + 1)
        bottom_right = self.get(x_pos - 1, y_pos + 1)

        return [
            top_left, top_right,
            middle_left, middle_right,
            bottom_left, bottom_right,
        ]

    def put(self, prisoner, x_pos, y_pos):
        self.the_map[x_pos][y_pos] = prisoner

    def get(self, x_pos, y_pos):
        if x_pos >= self.x_height:
            x_pos = 0
        if x_pos < 0:
            x_pos = self.x_height - 1
        if y_pos >= self.y_height:
            y_pos = 0
        if y_pos < 0:
            y_pos = self.y_height - 1
        try:
            return self.the_map[x_pos][y_pos]
        except IndexError:
            raise Exception('Could not access (%s, %s) in %s' % (x_pos, y_pos, self.the_map))

    def all(self):
        return reduce(lambda x, y: x + y, self.the_map)
