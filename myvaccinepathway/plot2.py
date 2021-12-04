import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import date, timedelta

INITIAL_IMMUNITY = 0
start_date = date(2021, 1, 1)
end_date = date(2022, 12, 31)

daterange_index = pd.date_range(start_date, end_date)

immunity_series = pd.Series(np.NAN, index=daterange_index)

print(immunity_series)


class Dose:
    def __init__(self, date, type, dose_number):
        self.dose_date = date
        self.type = type
        self.dose_number = dose_number
        self.peak_immunity_level = Dose.get_peak_immunity_level(self.type, self.dose_number)
        self.peak_immunity_date = Dose.get_peak_immunity_date(self.type, self.dose_number, self.dose_date)

    @staticmethod
    def get_peak_immunity_level(type, dose_number):
        # AZ
        if dose_number <= 0:
            return 0
        if dose_number == 1:
            return 0.45
        return 0.65

    @staticmethod
    def get_peak_immunity_date(type, dose_number, dose_date):
        # AZ
        if dose_number <= 0:
            return dose_date
        if dose_number == 1:
            return dose_date + timedelta(7)
        return dose_date + timedelta(14)

    @staticmethod
    def create_doses(dose_type_pairs):
        doses = []
        for dose_type_pair in dose_type_pairs:
            dose_date, dose_type = dose_type_pair
            doses.append(Dose(dose_date, dose_type, len(doses) + 1))
        return doses


doses = Dose.create_doses([
    (date(2021, 1, 15), "az"),
    (date(2022, 4, 14), "az"),
    (date(2022, 7, 22), "pf"),
])


for i, dose in enumerate(doses):
    if dose.dose_number == 1:
        immunity_series[str(dose.dose_date)] = INITIAL_IMMUNITY
    else:
        immunity_series[str(dose.dose_date)] = doses[i - 1].peak_immunity_level

    immunity_series[str(dose.peak_immunity_date)] = dose.peak_immunity_level

immunity_series = immunity_series.interpolate(method="spline", order=3)

print(immunity_series)
immunity_series.plot()
plt.show()



#
# class VaccineImmunity:
#     def __init__(self, immunity_levels, immunity_delay):
#         self.immunity_level = [0.0] + immunity_levels
#         self.peak_immunity_delay = [0] + immunity_delay
#
#     def __getitem__(self, item: int):
#         if item < 0:
#             return self.immunity_level[0]
#
#         if item > len(self.immunity_level):
#             return self.immunity_level[-1]
#
#         return self.immunity_level[item]
#
#     def immunity_delay(self, dose):
#         if dose < 0:
#             return self.peak_immunity_delay[0]
#
#         if dose > len(self.peak_immunity_delay):
#             return self.peak_immunity_delay[-1]
#
#         return self.peak_immunity_delay[dose]
#
#
# AZ_IMMUNITY = VaccineImmunity(
#     immunity_levels=[0.45, 0.6],
#     immunity_delay=[7, 7],
# )

