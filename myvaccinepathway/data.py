import pandas as pd
from constants import DOSE_1, ASTRAZENECA, SYMPTOMATIC, HOSPITALISATION, DEATH, PFIZER, MODERNA, DOSE_2, BOOSTER, INDEX, \
    COLUMNS, ALLOWED_DOSE_NUMBERS, ALLOWED_VACCINE_TYPES, ALLWED_IMMUNITY_TYPES, DELTA, OMICRON, ALLOWED_VARIANT_TYPES

""" Store all real world immunity data """
INITIAL_IMMUNITY = 0

IMMUNITY = {}

"""===DELTA=========================================================================================================="""
IMMUNITY[DELTA] = {
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
IMMUNITY[DELTA][DOSE_2][MODERNA][HOSPITALISATION] = IMMUNITY[DELTA][DOSE_2][PFIZER][HOSPITALISATION]
IMMUNITY[DELTA][DOSE_2][MODERNA][DEATH] = IMMUNITY[DELTA][DOSE_2][PFIZER][DEATH]

"""===OMICRON========================================================================================================"""
IMMUNITY[OMICRON] = {
    # Source - Imperial/WHO modelling: https://spiral.imperial.ac.uk/bitstream/10044/1/93034/13/2021-12-16%20COVID19%20Report%2048.pdf
    DOSE_1: {
        # TODO: Not enough data
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))

            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))

            ],
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))

            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))

            ],
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))

            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))

            ],
        },
    },

    DOSE_2: {
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1 - data read from graphs, don't have same ranges as table data
                # Using ~max table data range above and below median value from graph
                (14, (22, 24, 26)),
                # Source - Table 1
                (90, (7.1, 8.6, 10.6)),
                (180, (2.7, 3.3, 4.4)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1 - data read from graphs, don't have same ranges as table data
                # Using ~max table data range above and below median value from graph
                (14, (64, 68, 72)),
                # Source - Table 1
                (90, (32.3, 37.3, 42.9)),
                (180, (14.8, 17.8, 22.4)),
            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))
                # This value was extrapolated. The ratio of dose2:booster for hospitalisation was used
                # to extrapolate and approximate this value. I.e. (68.0/85.5)*91.7 - rounded and using largest range
                # from table data
                (14, (67, 73, 79)),
                # Source - Table 1
                (90, (47.1, 52.6, 58.4)),
                (180, (24.5, 28.9, 35.1)),
            ],
        },

        PFIZER: {
            # Source - Table 1
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1 - data read from graphs, don't have same ranges as table data
                # Using ~max table data range above and below median value from graph
                (14, (36, 40, 44)),
                # Source - Table 1
                (90, (15.9, 19.1, 22.7)),
                (180, (6.4, 7.9, 10.2)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1 - data read from graphs, don't have same ranges as table data
                # Using ~max table data range above and below median value from graph
                (14, (76, 81, 86)),
                # Source - Table 1
                (90, (54.3, 59.8, 65.1)),
                (180, (30.0, 35.2, 41.7)),
            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))
                # This value was extrapolated. The ratio of dose2:booster for hospitalisation was used
                # to extrapolate and approximate this value. I.e. (81.0/85.5)*91.7 - rounded and using largest range
                # from table data
                (14, (80, 87, 94)),
                # Source - Table 1
                (90, (68.9, 73.6, 77.7)),
                (180, (44.6, 50.4, 57.4)),
            ],
        },

        MODERNA: {
            # TODO: Not enough data
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))

            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))

            ],
        },
    },

    BOOSTER: {
        # All data here is for pfizer booster given the following primary doses
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Table 1
                (30, (43.1, 48.4, 53.3)),
                (60, (33.9, 38.9, 44.0)),
                (90, (25.8, 30.2, 35.0)),
                # Source - Figure 1 - data read from graph, at 6month+ looks like it plateaus to similar value as dose2
                # Use dose2 180 day data
                (180, (2.7, 3.3, 4.4)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Table 1
                (30, (82.6, 85.5, 87.9)),
                (60, (76.3, 80.1, 83.2)),
                (90, (68.6, 73.2, 77.3)),
                # Source - Figure 1 - data read from graph, at 6month+ looks like it plateaus to similar value as dose2
                # Use dose2 180 day data
                (180, (14.8, 17.8, 22.4)),
            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Table 1
                (30, (89.9, 91.7, 93.2)),
                (60, (85.8, 88.3, 90.3)),
                (90, (80.4, 83.7, 86.5)),

            ],
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Table 1
                (30, (43.1, 48.4, 53.5)),
                (60, (33.9, 38.9, 44.0)),
                (90, (25.8, 30.2, 35.0)),
                # Source - Figure 1 - data read from graph, at 6month+ looks like it plateaus to similar value as dose2
                # Use dose2 180 day data
                (180, (6.4, 7.9, 10.2)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Table 1
                (30, (82.6, 85.5, 87.9)),
                (60, (76.3, 80.1, 83.2)),
                (90, (68.6, 73.2, 77.3)),
                # Source - Figure 1 - data read from graph, at 6month+ looks like it declines to similar value as dose2
                # Use dose2 180 day data, but note values continue to decline in graph (i.e. don't plateau here)
                (180, (30.0, 35.2, 41.7)),
            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))
                (30, (89.9, 91.7, 93.2)),
                (60, (85.8, 88.3, 90.3)),
                (90, (80.4, 83.7, 86.5)),
            ],
        },

        MODERNA: {
            # TODO: Not enough data
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))

            ],

            DEATH: [
                # (days_since_jab, immunity(lower, median, upper))

            ],
        },
    }
}
# No Dose 1 omicron data - assume values are half that of dose 2.
for vaccine_type in [ASTRAZENECA, PFIZER]:
    for immunity_type in ALLWED_IMMUNITY_TYPES:
        IMMUNITY[OMICRON][DOSE_1][vaccine_type][immunity_type] = [(day, (lower / 2, average / 2, upper / 2))
                                                                 for (day, (lower, average, upper)) in
                                                                 IMMUNITY[OMICRON][DOSE_2][vaccine_type][immunity_type]]
# No Moderna omicron data. Use pfizer
for dose_number in ALLOWED_DOSE_NUMBERS:
    IMMUNITY[OMICRON][dose_number][MODERNA] = IMMUNITY[OMICRON][dose_number][PFIZER]


DAY_INDEX = 0
IMMUNITY_INDEX = 1


def _get_interpolated_df_from_raw_data(immunity_at_given_points):
    flattened_immunity_at_given_points = [(delay_day, lower, average, upper) for (delay_day, (lower, average, upper)) in
                                          immunity_at_given_points]
    immunity_df = pd.DataFrame(flattened_immunity_at_given_points, columns=[INDEX] + COLUMNS).set_index(INDEX)
    immunity_df = immunity_df.reindex(index=range(0, immunity_df.index.max() + 1))

    # Linear interpolation to fill NANs
    immunity_df = immunity_df.interpolate()

    return immunity_df


def get_immunity_specific_immunity_type(variant_type, dose_number, vaccine_type, immunity_type):
    if dose_number not in ALLOWED_DOSE_NUMBERS:
        raise ValueError(f"{dose_number} not in allowed list: {ALLOWED_DOSE_NUMBERS}")

    if vaccine_type not in ALLOWED_VACCINE_TYPES:
        raise ValueError(f"{vaccine_type} not in allowed list: {ALLOWED_VACCINE_TYPES}")

    if immunity_type not in ALLWED_IMMUNITY_TYPES:
        raise ValueError(f"{immunity_type} not in allowed list: {ALLWED_IMMUNITY_TYPES}")

    immunity_datapoints = IMMUNITY[variant_type][dose_number][vaccine_type][immunity_type]

    immunity_df = _get_interpolated_df_from_raw_data(immunity_datapoints)

    return immunity_df


def get_immunity_raw(dose_number, vaccine_type):
    immunity = {}
    for variant_type in ALLOWED_VARIANT_TYPES:
        immunity[variant_type] = {}
        for immunity_type in ALLWED_IMMUNITY_TYPES:
            immunity[variant_type][immunity_type] = get_immunity_specific_immunity_type(variant_type, dose_number, vaccine_type, immunity_type)

    return immunity
