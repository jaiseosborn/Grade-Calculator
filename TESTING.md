# Grade Calculator — Verification and Testing

## Known expected results

| Test | Inputs | Expected result |
| --- | --- | --- |
| Equal weights | Scores: 90, 85, 95, 88, 92; weights: 20, 20, 20, 20, 20 | 90.00%, A |
| Unequal weights | Scores: 100, 80, 70, 90, 85; weights: 30, 20, 10, 20, 20 | 88.00%, B |
| Invalid weights | Scores: all 90; weights: 20, 20, 20, 20, 15 | Error: weights must total 100% |
| Invalid score | Try to enter 105 | UI will not accept a score above 100 |
| Boundary | Scores: all 60; weights: all 20 | 60.00%, D |
| Zero scores | Scores: all 0; weights: all 20 | 0.00%, F |
| Reset | Enter any scores, click Reset | Scores become 0 and weights become 20; result disappears |

**Note:** The provided guide's unequal-weight example lists 87%, but the arithmetic actually equals **88%** (30 + 16 + 7 + 18 + 17). The correct result is used here.

## Manual results to complete after running/deploying

| Test | Expected | Actual | Pass/Fail |
| --- | --- | --- | --- |
| Equal weights | 90.00%, A | | |
| Unequal weights | 88.00%, B | | |
| Weights total 95% | Error message | | |
| Score out of range | Input blocked | | |
| Reset button | Defaults restored | | |
| Public deployment | App opens and calculates | | |

## Code review checklist
- [ ] I understand the weighted-average formula.
- [ ] I reviewed input validation and error handling.
- [ ] I checked grade boundaries.
- [ ] I ran automated tests.
- [ ] I tested the running app manually.
- [ ] I checked the deployed public app again.

## Bugs and fixes
Record any issues here: what happened, steps to reproduce, and what was changed.
