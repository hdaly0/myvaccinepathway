import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

AZ_IMMUNITY_POST_JAB_2 = [
    # (day_since_jab_2, immunity pair)
    # (7, 94),
    # (10, 94),
    (11, 94), # Dose date should be day 0 not day 1
    # (13, 94),

    # (14, 95),
    (41, 95),
    # (69, 95),

    # (70, 92),
    (87, 92),
    # (104, 92),

    # (105, 88),
    (122, 88),
    # (139, 88),

    (140, 77),

]

az_immunity_series = pd.Series([np.NAN] * 200)

for day, immunity in AZ_IMMUNITY_POST_JAB_2:
    az_immunity_series[day] = immunity

az_immunity_series = az_immunity_series.interpolate()
# print(az_immunity_series)
# az_immunity_series.plot()
# plt.show()
