import pandas as pd
from constants import DOSE_1, ASTRAZENECA, SYMPTOMATIC, HOSPITALISATION, DEATH, PFIZER, MODERNA, DOSE_2, \
    PFIZER_BOOSTER, MODERNA_BOOSTER, INDEX, COLUMNS, ALLOWED_DOSE_NUMBERS, ALLOWED_PRIMARY_VACCINE_TYPES,\
    ALLOWED_IMMUNITY_TYPES, DELTA, OMICRON, ALLOWED_VARIANT_TYPES

""" Store all real world immunity data """
INITIAL_IMMUNITY = 0

# IMMUNITY[covid_variant][dose][vaccine_type][immunity_type]
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
        # TODO
    },

    MODERNA_BOOSTER: {
        # TODO
    },
}
# Use Pfizer dose 2 hospitalisation and death data for Moderna dose 2 as no moderna data available
IMMUNITY[DELTA][DOSE_2][MODERNA][HOSPITALISATION] = IMMUNITY[DELTA][DOSE_2][PFIZER][HOSPITALISATION]
IMMUNITY[DELTA][DOSE_2][MODERNA][DEATH] = IMMUNITY[DELTA][DOSE_2][PFIZER][DEATH]

# Use DOSE_2 data for Delta BOOSTER values until data inserted
IMMUNITY[DELTA][PFIZER_BOOSTER] = IMMUNITY[DELTA][DOSE_2]
IMMUNITY[DELTA][MODERNA_BOOSTER] = IMMUNITY[DELTA][DOSE_2]

"""===OMICRON========================================================================================================"""

ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH = [
    # Source - UK Gov aggregated from various studies - week 4 surveillance: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1050721/Vaccine-surveillance-report-week-4.pdf
    # (days_since_jab, immunity(lower, median, upper))
    # Assuming the immunity value only goes down over time, use the later value as a lower bound for previous
    #   immunity level. Set immunity value at 14 days as this seems to be the time period often quoted for initial
    #   immunity. E.g. see: https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination
    (14, (40, 59, 70)),
    # Source - mean from Table 1, range from Table 2a
    # TODO: earlier data?
    (175, (40, 59, 70))
]
ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH = [
    # Source - UK Gov aggregated from various studies - week 4 surveillance: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1050721/Vaccine-surveillance-report-week-4.pdf
    # (days_since_jab, immunity(lower, median, upper))
    # Source - mean from Table 1, range from Table 2a
    # Table 1 quotes 2weeks+, Table 2a quotes 0-3months
    #   - put in 2 datapoints, one for 14 days (2 weeks), one for 91 days (3 months)
    (14, (85, 95, 99)),
    (91, (85, 95, 99)),
    # TODO: add later data?
]

IMMUNITY[OMICRON] = {
    # Source - UK Gov aggregated from various studies - week 4 surveillance: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1050721/Vaccine-surveillance-report-week-4.pdf
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
                (21, (41, 50, 58)),
                (49, (27, 35, 43)),
                (84, (23, 30, 37)),
                (119, (15, 18, 23)),
                (154, (2, 5, 8)),
                (175, (0, 0, 1)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Assuming the immunity value only goes down over time, use the later value as a lower bound for previous
                #   immunity level. Set immunity value at 14 days as this seems to be the time period often quoted for initial
                #   immunity. E.g. see: https://www.health.gov.au/initiatives-and-programs/covid-19-vaccines/is-it-true/is-it-true-how-long-does-it-take-to-have-immunity-after-vaccination
                (14, (34, 56, 71)),
                # Source - Figure 2a - data read from graphs
                (154, (34, 56, 71)),
                (175, (19, 33, 44)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH,
        },

        PFIZER: {
            # Source - Table 1
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (21, (63, 66, 68)),
                (49, (47, 49, 51)),
                (84, (28, 31, 33)),
                (119, (14, 17, 19)),
                (154, (11, 13, 15)),
                (175, (7, 9, 12)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 2b
                (21, (41, 74, 88)),
                (49, (49, 71, 84)),
                (84, (35, 54, 67)),
                (119, (48, 60, 69)),
                (154, (43, 57, 68)),
                (175, (18, 35, 48)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH,
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (21, (72, 76, 79)),
                (49, (49, 53, 58)),
                (84, (33, 36, 39)),
                (119, (24, 26, 28)),
                (154, (14, 17, 20)),
                (175, (3, 13, 22)),
            ],
            # TODO
            HOSPITALISATION: [],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_2_DEATH,
        },
    },

    PFIZER_BOOSTER: {
        # Data here is for various vaccine type primary doses + pfizer booster
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1a
                (7, (57, 60, 62)),
                (21, (61, 63, 66)),
                (49, (52, 54, 57)),
                (84, (37, 39, 41)),
                (105, (19, 29, 38)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 2a
                (7, (83, 90, 94)),
                (21, (83, 87, 90)),
                (49, (81, 85, 88)),
                (84, (70, 77, 84)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },

        PFIZER: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (7, (65, 67, 69)),
                (21, (65, 67, 70)),
                (49, (54, 56, 58)),
                (84, (44, 46, 48)),
                (105, (36, 39, 43)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 2b
                (7, (68, 79, 86)),
                (21, (83, 88, 92)),
                (49, (80, 84, 88)),
                (84, (70, 76, 81)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (7, (63, 65, 68)),
                (21, (63, 66, 68)),
                (49, (29, 49, 64)),
            ],
            # TODO
            HOSPITALISATION: [],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },
    },

    MODERNA_BOOSTER: {
        # Data here is for various vaccine type primary doses + moderna booster
        ASTRAZENECA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1a
                (7, (66, 68, 71)),
                (21, (68, 71, 73)),
                (49, (60, 62, 64)),
                (84, (19, 39, 54)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 2a
                (7, (81, 91, 96)),
                (21, (87, 92, 95)),
                (49, (83, 91, 96)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },

        PFIZER: {  # Pfizer primary, Moderna booster
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1b
                (7, (72, 74, 76)),
                (21, (71, 73, 76)),
                (49, (63, 65, 68)),
                (84, (50, 64, 75)),
            ],

            HOSPITALISATION: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 2b
                (7, (73, 88, 95)),
                (21, (83, 92, 96)),
                (49, (80, 94, 98)),
            ],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },

        MODERNA: {
            SYMPTOMATIC: [
                # (days_since_jab, immunity(lower, median, upper))
                # Source - Figure 1c
                (7, (66, 68, 71)),
                (21, (66, 68, 70)),
                (49, (35, 56, 71)),
            ],
            # TODO
            HOSPITALISATION: [],

            DEATH: ALL_3_VACCINE_TYPES_AVG_DOSE_3_DEATH,
        },
    }
}

# No hospitalisation data for Moderna with Omicron
for dose_number in [DOSE_2, PFIZER_BOOSTER, MODERNA_BOOSTER]:
    IMMUNITY[OMICRON][dose_number][MODERNA][HOSPITALISATION] = IMMUNITY[OMICRON][dose_number][PFIZER][HOSPITALISATION]

# No Dose 1 omicron data - assume values are half that of dose 2.
for vaccine_type in ALLOWED_PRIMARY_VACCINE_TYPES:
    for immunity_type in ALLOWED_IMMUNITY_TYPES:
        IMMUNITY[OMICRON][DOSE_1][vaccine_type][immunity_type] = [(day, (lower / 2, average / 2, upper / 2))
                                                                 for (day, (lower, average, upper)) in
                                                                 IMMUNITY[OMICRON][DOSE_2][vaccine_type][immunity_type]]


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
