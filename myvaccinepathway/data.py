import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dose number
DOSE_1 = "dose_1"
DOSE_2 = "dose_2"
# DOSE_3_PLUS = DOSE_2  # Use immunity data from dose 2 for all future doses
BOOSTER = "booster"
ALLOWED_DOSE_NUMBERS = [DOSE_1, DOSE_2, BOOSTER]

# Vaccine type
ASTRAZENECA = "astrazeneca"
PFIZER = "pfizer"
MODERNA = "moderna"
ALLOWED_VACCINE_TYPES = [ASTRAZENECA, PFIZER, MODERNA]

# Immunity type
SYMPTOMATIC = "symptomatic"
HOSPITALISATION = "hospitalisation"
DEATH = "death"
ALLWED_IMMUNITY_TYPES = [SYMPTOMATIC, HOSPITALISATION, DEATH]

""" Store all real world immunity data """
IMMUNITY = {
    DOSE_1: {
        ASTRAZENECA: {
            # Source - immunity values: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1029794/S1411_VEEP_Vaccine_Effectiveness_Table_.pdf
            # Source - time to first immunity: https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 30),
                (14, 45),
                # (14, 50),
            ],

            HOSPITALISATION: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 75),
                (14, 80),
                # (14, 85),
            ],

            DEATH: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 75),
                (14, 80),
                # (14, 85),
            ],
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 50),
                (14, 55),
                # (14, 65),
            ],

            HOSPITALISATION: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 75),
                (14, 80),
                # (14, 85),
            ],

            DEATH: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 75),
                (14, 80),
                # (14, 85),
            ],
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, 0),

                # TODO: 14 days is a guess. Need evidence/reference
                # (14, 60),
                (14, 75),
                # (14, 90),
            ],

            HOSPITALISATION: [
                # TODO: "Insufficient Data" in source above.
            ],

            DEATH: [
                # TODO: "Insufficient Data" in source above.
            ],
        },
    },

    DOSE_2: {
        # Source: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1017309/S1362_PHE_duration_of_protection_of_COVID-19_vaccines_against_clinical_disease.pdf
        # Where no error bars were present, errors of +-2% were used for the lower and upper bounds as this is the width of the markers on the plots provided
        # Whenever values are unclear or could be rounded, they are always rounded to give the largest possible range to err on the side of caution
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (day_since_jab_2, immunity pair)

                # 0 - 3 days -> choose day 2
                # (2, 42),
                (2, 44),
                # (2, 46),

                # 4 - 6 days -> choose day 5
                # (5, 42),
                (5, 44),
                # (5, 47),

                # 7 - 13 days -> choose day 10
                # (10, 61),
                (10, 61),
                # (10, 61),

                # 14 - 69 days -> choose day 42
                # (42, 66),
                (42, 66),
                # (42, 66),

                # 70 - 104 days -> choose 87
                # (87, 61),
                (87, 61),
                # (87, 61),

                # 105 - 139 days -> choose 122
                # (122, 57),
                (122, 57),
                # (122, 57),

                # 140 + -> choose 140
                # (140, 48),
                (140, 53),
                # (140, 56),
            ],

            HOSPITALISATION: [
                # (day_since_jab_2, immunity pair)
                # (7, 94),
                # (10, 94),
                (11, 94),  # Dose date should be day 0 not day 1
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
            ],

            DEATH: [
                # TODO
            ],
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (day_since_jab_2, immunity pair)

                # 0 - 3 days -> choose day 2
                # (2, 52),
                (2, 54),
                # (2, 56),

                # 4 - 6 days -> choose day 5
                # (5, 66),
                (5, 68),
                # (5, 70),

                # 7 - 13 days -> choose day 10
                # (10, 90),
                (10, 92),
                # (10, 94),

                # 14 - 69 days -> choose day 42
                # (42, 91),
                (42, 89),
                # (42, 87),

                # 70 - 104 days -> choose 87
                # (87, 78),
                (87, 80),
                # (87, 82),

                # 105 - 139 days -> choose 122
                # (122, 77),
                (122, 75),
                # (122, 73),

                # 140 + -> choose 140
                # (140, 71),
                (140, 73),
                # (140, 75),
            ],

            HOSPITALISATION: [
                # TODO
            ],

            DEATH: [
                # TODO
            ],
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (day_since_jab_2, immunity pair)

                # 0 - 3 days -> choose day 2
                # (2, 71),
                (2, 74),
                # (2, 77),

                # 4 - 6 days -> choose day 5
                # (5, 83),
                (5, 80),
                # (5, 77),

                # 7 - 13 days -> choose day 10
                # (10, 93),
                (10, 95),
                # (10, 97),

                # 14 - 69 days -> choose day 42
                # (42, 93),
                (42, 95),
                # (42, 97),

                # 70 - 104 days -> choose 87
                # TODO: Not enough data yet

                # 105 - 139 days -> choose 122
                # TODO: Not enough data yet

                # 140 + -> choose 140
                # TODO: Not enough data yet
            ],

            HOSPITALISATION: [
                # TODO
            ],

            DEATH: [
                # TODO
            ],
        },
    },

    BOOSTER: {
        PFIZER: {
            SYMPTOMATIC: [

            ],

            HOSPITALISATION: [

            ],

            DEATH: [

            ],
        },
    },
}


DAY_INDEX = 0
IMMUNITY_INDEX = 1


def _create_immunity_by_day_series(immunity_at_given_points):
    immunity_series = pd.Series([np.NAN] * (immunity_at_given_points[-1][DAY_INDEX] + 1))

    for day, immunity in immunity_at_given_points:
        immunity_series[day] = immunity

    immunity_series = immunity_series.interpolate()

    return immunity_series


def get_immunity_specific_immunity_type(dose_number, vaccine_type, immunity_type):
    if dose_number not in ALLOWED_DOSE_NUMBERS:
        raise ValueError(f"{dose_number} not in allowed list: {ALLOWED_DOSE_NUMBERS}")

    if vaccine_type not in ALLOWED_VACCINE_TYPES:
        raise ValueError(f"{vaccine_type} not in allowed list: {ALLOWED_VACCINE_TYPES}")

    if immunity_type not in ALLWED_IMMUNITY_TYPES:
        raise ValueError(f"{immunity_type} not in allowed list: {ALLWED_IMMUNITY_TYPES}")

    immunity_datapoints = IMMUNITY[dose_number][vaccine_type][immunity_type]

    immunity_series = _create_immunity_by_day_series(immunity_datapoints)

    return immunity_series


def get_immunity(dose_number, vaccine_type):
    return {immunity_type: get_immunity_specific_immunity_type(dose_number, vaccine_type, immunity_type) for immunity_type in ALLWED_IMMUNITY_TYPES}


# print(az_immunity_series)
# az_immunity_series.plot()
# plt.show()
