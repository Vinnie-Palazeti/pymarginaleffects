from marginaleffects import *
import statsmodels.formula.api as smf
import polars as pl

mtcars = pl.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv")

def test_FUN_numeric():
    d = datagrid(newdata = mtcars, FUN_numeric = lambda x: x.median())
    assert d["cyl"][0] == mtcars["cyl"].median()
    assert d["hp"][0] == mtcars["hp"].median()
    assert d["carb"][0] == mtcars["carb"].median()

def test_simple_grid():
    d = datagrid(mpg = 24, newdata = mtcars)
    assert d.shape == (1, 12)
    d = datagrid(mpg = [23, 24], hp = [120, 130], newdata = mtcars)
    assert d.shape == (4, 12)


