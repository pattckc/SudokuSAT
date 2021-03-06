from .parse import *
import unittest
from tempfile import TemporaryFile

sudoku_line_4 = "...3..4114..3..."
sudoku_dimacs_4 = """143 0
234 0
241 0
311 0
324 0
413 0
"""
sudoku_clauses_4 = [[{'143'},{'234'},{'241'},{'311'},{'324'},{'413'}]]

sudoku_predicates_4 = {'143', '234', '241', '311', '324', '413'}

sudoku_line_9 = "52...6.........7.13...........4..8..6......5...........418.........3..2...87....."
sudoku_dimacs_9 = """115 0
122 0
166 0
277 0
291 0
313 0
444 0
478 0
516 0
585 0
724 0
731 0
748 0
853 0
882 0
938 0
947 0
"""

sudoku_line_16 = "1.D....4.A58.....E.........C...G.2.76.GBF..4....39F.1A.D7........4.6.31...B.58.C8C7E.69..F.....D...D..........2...A.G8C....7E.1426.G4....57F.A...B..........8...F.....B..3A.42E1A.4C.5...E6.7.3........3D.C5.7B2....9..1GB.63.4.C...2.........6.....8FD.3....9.E"
sudoku_dimacs_16 ="""111 0
13D 0
184 0
1AA 0
1B5 0
1C8 0
22E 0
2CC 0
2GG 0
322 0
347 0
356 0
37G 0
38B 0
39F 0
"""

generic_dimacs = """
c this is an example
p cnf 4 4
1 -2 0
2 3 0
1 3 4 0
-1 0
"""

generic_clauses = [{'1','-2'},{'2','3'},{'1','3','4'},{'-1'}]

generic_predicates = {'1','2','3','4'}

generic_dimacs_letters = """
c this is an example
p cnf 2 2
B -A 0
B 0
"""

generic_clauses_letters = [{'-A','B'},{'B'}]

generic_predicates_letters = {'A','B'}

class TestParseMethods(unittest.TestCase):

    def test_get_dimacs_string(self):
        self.assertEqual(get_dimacs_string(sudoku_line_4), sudoku_dimacs_4)
        self.assertEqual(get_dimacs_string(sudoku_line_9), sudoku_dimacs_9)
        self.maxDiff = None
        self.assertEqual(get_dimacs_string(sudoku_line_16)[:len(sudoku_dimacs_16)], sudoku_dimacs_16)

    def test_parse_puzzles(self):
        with TemporaryFile('w+') as f:
            f.write(sudoku_line_4)
            f.seek(0)
            sudoku_size, sudoku_clauses, sudoku_predicates = parse_sudoku_puzzles(f)
            self.assertEqual(sudoku_size, 4)
            self.assertEqual(sudoku_clauses, sudoku_clauses_4)
            self.assertEqual(sudoku_predicates, sudoku_predicates_4)

    def test_parse_sudoku_rules(self):
        sdk4, prd4 = parse_sudoku_rules(4);

    def test_dimacs_to_cnf(self):
        clauses, predicates = dimacs_to_cnf(generic_dimacs)
        self.assertEqual(clauses, generic_clauses)
        self.assertEqual(predicates, generic_predicates)

        clauses, predicates = dimacs_to_cnf(generic_dimacs_letters)
        self.assertEqual(clauses, generic_clauses_letters)
        self.assertEqual(predicates, generic_predicates_letters)

if __name__ == '__main__':
    unittest.main()
    print("All parser tests passed")
