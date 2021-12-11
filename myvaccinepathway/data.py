import pandas as pd
from constants import DOSE_1, ASTRAZENECA, SYMPTOMATIC, HOSPITALISATION, DEATH, PFIZER, MODERNA, DOSE_2, BOOSTER, INDEX, \
    COLUMNS, ALLOWED_DOSE_NUMBERS, ALLOWED_VACCINE_TYPES, ALLWED_IMMUNITY_TYPES

""" Store all real world immunity data """
INITIAL_IMMUNITY = 0

IMMUNITY = {
    DOSE_1: {
        ASTRAZENECA: {
            # Source - immunity values: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1029794/S1411_VEEP_Vaccine_Effectiveness_Table_.pdf
            # Source - time to first immunity: https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (40, 45, 50)),

                # TODO: Plateau to 44 after 3 months - this is a guess given dose 2, day 3, has 44% immunity
                (90, (41, 44, 46)),
            ],

            HOSPITALISATION: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),


                # TODO: 14 days is a guess. Need evidence/reference
                (14, (75, 80, 85)),
            ],

            DEATH: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (75, 80, 85)),
            ],
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (50, 55, 65)),
            ],

            HOSPITALISATION: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (75, 80, 85)),
            ],

            DEATH: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (75, 80, 85)),
            ],
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (60, 75, 90)),
            ],

            HOSPITALISATION: [
                # TODO: "Insufficient Data" in source above.
                # Using Symptomatic data above as this will be a lower bound

                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (60, 75, 90)),
            ],

            DEATH: [
                # TODO: "Insufficient Data" in source above.
                # Using Symptomatic data above as this will be a lower bound
                # (day_since_jab, immunity pair)
                (11, (0, 0, 0)),

                # TODO: 14 days is a guess. Need evidence/reference
                (14, (60, 75, 90)),
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
                (2, (42, 44, 46)),

                # 4 - 6 days -> choose day 5
                (5, (42, 44, 47)),

                # 7 - 13 days -> choose day 10
                (10, (59, 61, 63)),

                # 14 - 69 days -> choose day 42
                (42, (64, 66, 68)),

                # 70 - 104 days -> choose 87
                (87, (59, 61, 63)),

                # 105 - 139 days -> choose 122
                (122, (55, 57, 59)),

                # 140 + -> choose 140
                (140, (48, 53, 56)),
            ],

            HOSPITALISATION: [
                # (day_since_jab_2, immunity pair)
                # TODO: Check these 4 values??
                # (7, 92),
                # (10, 94),
                (11, (92, 94, 96)),  # Dose date should be day 0 not day 1
                # (13, 94),

                # (14, 95),
                (41, (93, 95, 97)),
                # (69, 95),

                # (70, 92),
                (87, (90, 92, 94)),
                # (104, 92),

                # (105, 88),
                (122, (86, 88, 90)),
                # (139, 88),

                # (140, 77),
                (140, (75, 77, 79)),
                # (140, 77),
            ],

            DEATH: [
                # 14 - 69 days -> choose day 42
                (42, (91, 93, 96)),

                # 70 - 104 days -> choose 87
                (87, (88, 92, 95)),

                # 105 - 139 days -> choose 122
                (122, (80, 87, 92)),

            ],
        },

        PFIZER: {
            # Source: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1017309/S1362_PHE_duration_of_protection_of_COVID-19_vaccines_against_clinical_disease.pdf
            SYMPTOMATIC: [
                # (day_since_jab_2, immunity pair)

                # 0 - 3 days -> choose day 2
                (2, (52, 54, 56)),

                # 4 - 6 days -> choose day 5
                (5, (66, 68, 70)),

                # 7 - 13 days -> choose day 10
                (10, (90, 92, 94)),

                # 14 - 69 days -> choose day 42
                (42, (87, 89, 91)),

                # 70 - 104 days -> choose 87
                (87, (78, 80, 82)),

                # 105 - 139 days -> choose 122
                (122, (73, 75, 77)),

                # 140 + -> choose 140
                (140, (71, 73, 75)),
            ],

            HOSPITALISATION: [
                # (day_since_jab_2, immunity pair)
                (11, (90, 100, 100)),

                (41, (96, 98, 100)),

                (87, (94, 96, 98)),

                (122, (93, 95, 97)),

                (140, (88, 94, 97)),

            ],

            DEATH: [
                # (day_since_jab_2, immunity pair)
                (42, (95, 98, 100)),

                (87, (92, 95, 97)),

                (122, (90, 94, 97)),

                (140, (87, 93, 97)),
            ],
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (day_since_jab_2, immunity pair)

                # 0 - 3 days -> choose day 2
                (2, (71, 74, 77)),

                # 4 - 6 days -> choose day 5
                (5, (77, 80, 83)),

                # 7 - 13 days -> choose day 10
                (10, (93, 95, 97)),

                # 14 - 69 days -> choose day 42
                (42, (93, 95, 97)),

                # 70 - 104 days -> choose 87
                # TODO: Not enough data yet

                # 105 - 139 days -> choose 122
                # TODO: Not enough data yet

                # 140 + -> choose 140
                # TODO: Not enough data yet
            ],

            HOSPITALISATION: [
                # TODO: Not enough data yet
                # Use pfizer data as similar vaccine and pfizer seems to be lower bound in all research
            ],

            DEATH: [
                # TODO: Not enough data yet
                # Using pfizer data as similar vaccine and pfizer seems to be lower bound in all research

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
# Use Pfizer dose 2 hospitalisation and death data for Moderna dose 2 as no moderna data available
IMMUNITY[DOSE_2][MODERNA][HOSPITALISATION] = IMMUNITY[DOSE_2][PFIZER][HOSPITALISATION]
IMMUNITY[DOSE_2][MODERNA][DEATH] = IMMUNITY[DOSE_2][PFIZER][DEATH]


DAY_INDEX = 0
IMMUNITY_INDEX = 1


def _create_immunity_by_day_series(immunity_at_given_points):
    flattened_immunity_at_given_points = [(delay_day, lower, average, upper) for (delay_day, (lower, average, upper)) in immunity_at_given_points]
    immunity_df = pd.DataFrame(flattened_immunity_at_given_points, columns=[INDEX] + COLUMNS).set_index(INDEX)
    immunity_df = immunity_df.reindex(index=range(0, immunity_df.index.max() + 1))

    # immunity_series = pd.Series([np.NAN] * (immunity_at_given_points[-1][DAY_INDEX] + 1))
    #
    # for day, immunity in immunity_at_given_points:
    #     immunity_series[day] = immunity

    immunity_df = immunity_df.interpolate()

    return immunity_df


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
