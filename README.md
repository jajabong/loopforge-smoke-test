# loopforge-smoke-test

Smoke-test fixture for the LoopForge bug-fix SOP acceptance run on Aimax.

Bug report: `mean()` divides by `len(values) + 1` instead of `len(values)`,
so `mean([2, 4, 6])` returns 3.0 instead of 4.0. The fix is a one-line change;
`test_mean_basic` and `test_mean_single` currently fail, the median tests pass.
