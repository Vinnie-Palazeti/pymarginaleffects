from .comparisons import comparisons


def slopes(
    model,
    variables=None,
    newdata=None,
    slope="dydx",
    vcov=True,
    conf_int=0.95,
    by=False,
    hypothesis=None,
    equivalence=None,
    wts=None,
    eps=1e-4,
):
    assert isinstance(eps, float)

    if slope not in ["dydx", "eyex", "eydx", "dyex"]:
        raise ValueError("slope must be one of 'dydx', 'eyex', 'eydx', 'dyex'")

    out = comparisons(
        model=model,
        variables=variables,
        newdata=newdata,
        comparison=slope,
        vcov=vcov,
        conf_int=conf_int,
        by=by,
        hypothesis=hypothesis,
        equivalence=equivalence,
        wts=wts,
        eps=eps,
    )
    return out


def avg_slopes(
    model,
    variables=None,
    newdata=None,
    slope="dydx",
    vcov=True,
    conf_int=0.95,
    by=True,
    wts=None,
    hypothesis=None,
    equivalence=None,
    eps=1e-4,
):
    if slope not in ["dydx", "eyex", "eydx", "dyex"]:
        raise ValueError("slope must be one of 'dydx', 'eyex', 'eydx', 'dyex'")
    out = slopes(
        model=model,
        variables=variables,
        newdata=newdata,
        slope=slope,
        vcov=vcov,
        conf_int=conf_int,
        by=by,
        wts=wts,
        hypothesis=hypothesis,
        equivalence=equivalence,
        eps=eps,
    )

    return out
