import statsmodels.api as sm


def run(add_constant: bool, prepend: bool) -> None:
    print("Starting: discrete_choice_example.run()")

    # load example data
    spector_data = sm.datasets.spector.load()

    # optionally add a constant
    if add_constant:
        spector_data.exog = sm.add_constant(spector_data.exog, prepend=prepend)

    # print some info to screen
    print(spector_data.exog[:5, :])
    print(spector_data.endog[:5])

    rand_data = sm.datasets.randhie.load()
    rand_exog = rand_data.exog.view(float).reshape(len(rand_data.exog), -1)
    rand_exog = sm.add_constant(rand_exog, prepend=False)

    poisson_mod = sm.Poisson(rand_data.endog, rand_exog)
    poisson_res = poisson_mod.fit(method="newton")
    print(poisson_res.summary())

    print("Exiting: discrete_choice_example.run()")