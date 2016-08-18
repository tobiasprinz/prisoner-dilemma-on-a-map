from maps import HexMap
import prisoners


class Context(object):

    def __init__(self):
        self.treatment_history = {}


class GameMaster(object):

    def __init__(self, number_of_turns, number_of_rows, number_of_columns):
        self.number_of_turns = number_of_turns

        max_x, max_y = (number_of_rows, number_of_columns)
        self.prison_map = HexMap(max_x, max_y)
        for x in range(max_x):
            for y in range(max_y):
                prisoner = prisoners.CooperativePrisoner()
                self.prison_map.put(prisoner, x, y)
