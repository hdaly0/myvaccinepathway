import pandas as pd
from constants import DOSE_1, ASTRAZENECA, SYMPTOMATIC, HOSPITALISATION, DEATH, PFIZER, MODERNA, DOSE_2, \
    PFIZER_BOOSTER, MODERNA_BOOSTER, INDEX, COLUMNS, ALLOWED_DOSE_NUMBERS, ALLOWED_PRIMARY_VACCINE_TYPES,\
    ALLOWED_IMMUNITY_TYPES, DELTA, OMICRON, ALLOWED_VARIANT_TYPES

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

    PFIZER_BOOSTER: {
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
# Booster
# HOSPITALISATION: [
#     # (days_since_jab, immunity(lower, median, upper))
#     # Source - Table 1
#     (30, (82.6, 85.5, 87.9)),
#     (60, (76.3, 80.1, 83.2)),
#     (90, (68.6, 73.2, 77.3)),
#     # Source - Figure 1 - data read from graph, at 6month+ looks like it declines to similar value as dose2
#     # Use dose2 180 day data, but note values continue to decline in graph (i.e. don't plateau here)
#     (180, (30.0, 35.2, 41.7)),
# ],
#
# DEATH: [
#     # (days_since_jab, immunity(lower, median, upper))
#     (30, (89.9, 91.7, 93.2)),
#     (60, (85.8, 88.3, 90.3)),
#     (90, (80.4, 83.7, 86.5)),
# ],
ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION = [
    # (days_since_jab, immunity(lower, median, upper))
    # Source - Table 1
    # Data is very granular, quoted "2-24 weeks" as 1 time point. Usually this gets converted to the middle date
    #   but because of the large range, this data was put in at 2 weeks and 13 weeks (the half way point)
    (14, (54, 64, 71)),
    (91, (54, 64, 71)),
    (175, (30, 44, 54)),
]
ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH = [
    # TODO Doesn't exist
]
ALL_3_VACCINE_TYPES_AVG_DOSE_3_HOSPITALISATION = [
    # (days_since_jab, immunity(lower, median, upper))
    # Source - Table 1
    (21, (89, 92, 94)),
    (29, (84, 88, 91)),
    (70, (78, 83, 87)),
]
ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH = [
    #TODO Doesn't exist
]

IMMUNITY[OMICRON] = {
    # Source - UK Gov aggregated from various studies: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1049160/Vaccine-surveillance-report-week-3-2022.pdf
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
                # Source - Figure 1a - data read from graphs
                (21, (32, 45, 55)),
                (49, (21, 32, 42)),
                (84, (17, 26, 35)),
                (119, (12, 16, 22)),
                (154, (1, 4, 7)),
                (175, (0, 0, 2)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        PFIZER: {
            # Source - Table 1
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (21, (61, 64, 67)),
                (49, (44, 47, 50)),
                (84, (25, 28, 31)),
                (119, (12, 15, 18)),
                (154, (8, 11, 14)),
                (175, (9, 12, 15)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (21, (67, 73, 78)),
                (49, (47, 52, 57)),
                (84, (31, 34, 38)),
                (119, (23, 26, 29)),
                (154, (11, 15, 19)),
                (175, (0, 10, 24)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },
    },

    PFIZER_BOOSTER: {
        # Data here is for various vaccine type primary doses + pfizer booster
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1a
                (7, (54, 57, 60)),
                (21, (60, 63, 66)),
                (49, (52, 54, 57)),
                (70, (41, 44, 47)),
                # TODO - add plateau value??
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (7, (64, 67, 70)),
                (21, (65, 68, 71)),
                (49, (54, 57, 60)),
                (70, (47, 50, 53)),
                # TODO - add plateau value??
                # Source - Figure 1 - data read from graph, at 6month+ looks like it plateaus to similar value as dose2
                # Use dose2 180 day data
                # (180, (6.4, 7.9, 10.2)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (7, (63, 66, 69)),
                (21, (63, 67, 71)),
                # No further omicron moderna booster data available
                # Use pfizer primary pfizer booster data from same timeframe as lower bound
                # Source - Figure 1b BNT162b2 booster
                (49, (54, 57, 60)),
                (70, (47, 50, 53)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },
    },

    MODERNA_BOOSTER: {
        # Data here is for various vaccine type primary doses + moderna booster
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1a
                (7, (64, 67, 69)),
                (21, (67, 70, 73)),
                (49, (58, 61, 64)),
                # No further omicron moderna booster data available
                # Use astrazeneca primary pfizer booster data from same timeframe as lower bound
                # Source - Figure 1a BNT162b2 booster
                (70, (41, 44, 47)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        PFIZER: {  # Pfizer primary, Moderna booster
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (7, (71, 74, 77)),
                (21, (72, 75, 78)),
                (49, (62, 65, 68)),
                # No further omicron moderna booster data available
                # Use pfizer primary pfizer booster data from same timeframe as lower bound
                # Source - Figure 1b BNT162b2 booster
                (70, (47, 50, 53)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (7, (67, 70, 73)),
                (21, (64, 68, 72)),
                # No further omicron moderna booster data available
                # Use pfizer primary pfizer booster data from same timeframe as lower bound
                # Source - Figure 1b BNT162b2 booster
                (49, (54, 57, 60)),
                (70, (47, 50, 53)),
            ],

            HOSPITALISATION: ALL_3_VACCINE_TYPES_AVG_DOSE_2_HOSPITALISATION,

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH
        },
    }
}
# No Dose 1 omicron data - assume values are half that of dose 2.
for vaccine_type in [ASTRAZENECA, PFIZER]:
    for immunity_type in ALLOWED_IMMUNITY_TYPES:
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

    if vaccine_type not in ALLOWED_PRIMARY_VACCINE_TYPES:
        raise ValueError(f"{vaccine_type} not in allowed list: {ALLOWED_PRIMARY_VACCINE_TYPES}")

    if immunity_type not in ALLOWED_IMMUNITY_TYPES:
        raise ValueError(f"{immunity_type} not in allowed list: {ALLOWED_IMMUNITY_TYPES}")

    immunity_datapoints = IMMUNITY[variant_type][dose_number][vaccine_type][immunity_type]

    immunity_df = _get_interpolated_df_from_raw_data(immunity_datapoints)

    return immunity_df


def get_immunity_raw(dose_number, vaccine_type):
    immunity = {}
    for variant_type in ALLOWED_VARIANT_TYPES:
        immunity[variant_type] = {}
        for immunity_type in ALLOWED_IMMUNITY_TYPES:
            immunity[variant_type][immunity_type] = get_immunity_specific_immunity_type(variant_type, dose_number, vaccine_type, immunity_type)

    return immunity
