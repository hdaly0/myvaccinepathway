"""
Constants and vaccine immunity level data
"""

PFIZER = "Pfizer"
AZ = "AstraZeneca"
MODERNA = "Moderna"

INITIAL_IMMUNITY_LEVEL = 0

DOSE_1_PEAK_IMMUNITY_LEVEL = {
    AZ: 0.45,
    PFIZER: 0.55,
    MODERNA: 0.75,
}
DOSE_2_PEAK_IMMUNITY_LEVEL = {
    AZ: 0.65,
    PFIZER: 0.90,
    MODERNA: 0.95,
}
DOSE_PEAK_IMMUNITY_LEVEL = [DOSE_1_PEAK_IMMUNITY_LEVEL, DOSE_2_PEAK_IMMUNITY_LEVEL]


DOSE_1_PEAK_IMMUNITY_DAY = {
    AZ: 12,  # Dummy value
    PFIZER: 12,
    MODERNA: 12,  # Dummy value
}
DOSE_2_PEAK_IMMUNITY_DAY = {
    AZ: 7,  # Dummy value
    PFIZER: 7,
    MODERNA: 7,  # Dummy value
}
DOSE_PEAK_IMMUNITY_DAY = [DOSE_1_PEAK_IMMUNITY_DAY, DOSE_2_PEAK_IMMUNITY_DAY]


DOSE_1_IMMUNITY_WANING_RATE = {
    AZ: -0.001,  # Dummy value
    PFIZER: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_2_IMMUNITY_WANING_RATE = {
    AZ: -0.001,  # Dummy value
    PFIZER: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_IMMUNITY_WANING_RATE = [DOSE_1_IMMUNITY_WANING_RATE, DOSE_2_IMMUNITY_WANING_RATE]

DEFAULT_JAB_DATE_OFFSET = {
    1: 120,
    2: 30
}
