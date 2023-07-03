import numpy as np
import polars as pl
import statsmodels.formula.api as smf
import statsmodels.api as sm
from marginaleffects import *
from polars.testing import assert_series_equal


dat = pl.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/geepack/dietox.csv")
mod = smf.mixedlm(formula = "Weight ~ Time * Litter", data = dat, groups=dat["Pig"]).fit()


def test_predictions_01():
    unknown = predictions(mod)
    known = pl.read_csv("tests/r/test_statsmodels_mixedlm_predictions_01.csv")
    assert_series_equal(known["estimate"], unknown["estimate"], check_names = False)
    assert_series_equal(known["std.error"], unknown["std_error"], check_names = False)


def test_predictions_02():
    unknown = predictions(mod, by = "Cu")
    known = pl.read_csv("tests/r/test_statsmodels_mixedlm_predictions_02.csv")
    assert_series_equal(known["estimate"], unknown["estimate"], check_names = False)
    assert_series_equal(known["std.error"], unknown["std_error"], check_names = False)


def test_comparisons_01():
    unknown = comparisons(mod)
    known = pl.read_csv("tests/r/test_statsmodels_mixedlm_comparisons_01.csv", ignore_errors=True)
    assert_series_equal(known["estimate"], unknown["estimate"], rtol = 3e-2, check_names = False)
    assert_series_equal(known["std.error"], unknown["std_error"], check_names = False)


def test_comparisons_02():
    unknown = comparisons(mod, by = "Cu").sort(["term", "Cu"])
    known = pl.read_csv("tests/r/test_statsmodels_mixedlm_comparisons_02.csv").sort(["term", "Cu"])
    assert_series_equal(known["estimate"], unknown["estimate"], check_names = False)
    assert_series_equal(known["std.error"], unknown["std_error"], check_names = False)