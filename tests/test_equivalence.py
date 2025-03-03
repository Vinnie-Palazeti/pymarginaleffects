import polars as pl
from polars.testing import assert_series_equal
from marginaleffects import *
import statsmodels.formula.api as smf

Guerry = pl.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/HistData/Guerry.csv", null_values = "NA").drop_nulls()
mod_py = smf.ols("Literacy ~ Pop1831 * Desertion", Guerry).fit()

def test_simple_equivalence():
    cmp_py = comparisons(mod_py, comparison = "differenceavg", equivalence = [-.1, .1]).sort("term")
    cmp_r = pl.read_csv("tests/r/test_equivalence_01.csv").sort("term")
    assert_series_equal(cmp_r["statistic.nonsup"], cmp_py["statistic_nonsup"], check_names = False, rtol = 1e-4)
    assert_series_equal(cmp_r["p.value.nonsup"], cmp_py["p_value_nonsup"], check_names = False, rtol = 1e-4)
    assert_series_equal(cmp_r["statistic.noninf"], cmp_py["statistic_noninf"], check_names = False, rtol = 1e-4)
    assert_series_equal(cmp_r["p.value.noninf"], cmp_py["p_value_noninf"], check_names = False, rtol = 1e-4)