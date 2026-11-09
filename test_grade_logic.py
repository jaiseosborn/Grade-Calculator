"""Run with: python -m unittest -v test_grade_logic.py"""
import unittest
from grade_logic import calculate_grade, letter_grade


class GradeLogicTests(unittest.TestCase):
    def test_equal_weights(self):
        avg, parts = calculate_grade([90, 85, 95, 88, 92], [20] * 5)
        self.assertAlmostEqual(avg, 90)
        self.assertAlmostEqual(sum(parts), avg)
        self.assertEqual(letter_grade(avg), "A")

    def test_unequal_weights(self):
        avg, _ = calculate_grade([100, 80, 70, 90, 85], [30, 20, 10, 20, 20])
        self.assertAlmostEqual(avg, 88)
        self.assertEqual(letter_grade(avg), "B")

    def test_wrong_weight_total(self):
        with self.assertRaisesRegex(ValueError, "total 100%"):
            calculate_grade([90] * 5, [20, 20, 20, 20, 15])

    def test_bad_score(self):
        with self.assertRaisesRegex(ValueError, "score"):
            calculate_grade([105, 90, 90, 90, 90], [20] * 5)

    def test_grade_boundaries(self):
        for score, expected in [(0, "F"), (59.99, "F"), (60, "D"), (70, "C"), (80, "B"), (90, "A"), (100, "A")]:
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), expected)

    def test_zero_and_full_scores(self):
        self.assertEqual(calculate_grade([0] * 5, [20] * 5)[0], 0)
        self.assertEqual(calculate_grade([100] * 5, [20] * 5)[0], 100)

    def test_non_numeric_and_negative(self):
        for bad in (-1, float("nan"), "hello"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    calculate_grade([bad, 80, 80, 80, 80], [20] * 5)


if __name__ == "__main__":
    unittest.main()
