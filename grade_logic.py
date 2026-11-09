"""Calculation and validation helpers for the Grade Calculator app."""


def letter_grade(average):
    """Return the standard A-F letter grade for a percentage."""
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def calculate_grade(scores, weights):
    """Return (weighted average, contributions) after validating input.

    Scores and weights must each contain exactly five finite numeric values.
    Scores must be 0..100, weights 0..100, and weights must total 100.
    """
    import math

    if len(scores) != 5 or len(weights) != 5:
        raise ValueError("Enter exactly five assignment scores and weights.")
    for score in scores:
        if isinstance(score, bool) or not isinstance(score, (int, float)) or not math.isfinite(score) or not 0 <= score <= 100:
            raise ValueError("Each assignment score must be between 0 and 100.")
    for weight in weights:
        if isinstance(weight, bool) or not isinstance(weight, (int, float)) or not math.isfinite(weight) or not 0 <= weight <= 100:
            raise ValueError("Each weight must be between 0 and 100%.")
    if not math.isclose(sum(weights), 100.0, rel_tol=0, abs_tol=1e-7):
        raise ValueError(f"Assignment weights must total 100% (currently {sum(weights):g}%).")

    contributions = [score * weight / 100 for score, weight in zip(scores, weights)]
    return sum(contributions), contributions
