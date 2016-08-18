from judges import Judge
from maps import HexMap
import prisoners
import unittest


class MapTest(unittest.TestCase):

    def test_get_cell_amount(self):
        prison_map = HexMap(10, 10)
        self.assertEqual(100, len(prison_map.all()))

    def test_that_get_neighbours_encounters_all_elements_equally_often(self):
        max_x = 3
        max_y = 4

        members = range(max_x * max_y)
        hex_map = HexMap(max_x, max_y, members)

        encounters = []
        for x in range(max_x):
            for y in range(max_y):
                encounters += hex_map.get_neighbours(x, y)

        encounter_count = []
        for member in members:
            encounter_count.append(encounters.count(member))

        self.assertTrue(len(set(encounter_count)) == 1)

    def test_that_neighbours_never_include_oneself(self):
        max_x = 15
        max_y = 12

        members = range(max_x * max_y)
        hex_map = HexMap(max_x, max_y, members)

        for x in range(max_x):
            for y in range(max_y):
                neighbours = hex_map.get_neighbours(x, y)
                oneself = hex_map.get(x, y)
                self.assertTrue(
                    oneself not in neighbours,
                    '%s at position (%s,%s) encountered in %s' % (
                        oneself, x, y, neighbours))


class JudgementTest(unittest.TestCase):

    def setUp(self):
        self.judge = Judge()

    def test_mutual_cooperation(self):
        prisoner1 = prisoners.CooperativePrisoner()
        prisoner2 = prisoners.CooperativePrisoner()

        penalty1, penalty2 = self.judge.sentence(prisoner1, prisoner2)

        self.assertTrue(penalty1 == penalty2)

    def test_mutual_defection(self):
        prisoner1 = prisoners.DefectingPrisoner()
        prisoner2 = prisoners.DefectingPrisoner()

        penalty1, penalty2 = self.judge.sentence(prisoner1, prisoner2)
        self.assertTrue(penalty1 == penalty2)

    def test_betrayal_by_1(self):
        prisoner1 = prisoners.DefectingPrisoner()
        prisoner2 = prisoners.CooperativePrisoner()

        penalty1, penalty2 = self.judge.sentence(prisoner1, prisoner2)

        self.assertTrue(penalty1 < penalty2)

    def test_betrayal_by_2(self):
        prisoner1 = prisoners.CooperativePrisoner()
        prisoner2 = prisoners.DefectingPrisoner()

        penalty1, penalty2 = self.judge.sentence(prisoner1, prisoner2)

        self.assertTrue(penalty1 > penalty2)


if __name__ == '__main__':
    unittest.main()
