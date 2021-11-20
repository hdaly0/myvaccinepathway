"""
Constants and vaccine immunity level data
"""

PFIZER = "pfizer"
AZ = "astrazeneca"
MODERNA = "moderna"

INITIAL_IMMUNITY_LEVEL = 0

DOSE_1_PEAK_IMMUNITY_LEVEL = {
    PFIZER: 0.3,
    AZ: 0.33,  # Dummy value
    MODERNA: 0.3,  # Dummy value
}
DOSE_2_PEAK_IMMUNITY_LEVEL = {
    PFIZER: 0.95,
    AZ: 0.7,  # Dummy value
    MODERNA: 0.95,  # Dummy value
}
DOSE_PEAK_IMMUNITY_LEVEL = [DOSE_1_PEAK_IMMUNITY_LEVEL, DOSE_2_PEAK_IMMUNITY_LEVEL]


DOSE_1_PEAK_IMMUNITY_DAY = {
    PFIZER: 12,
    AZ: 12,  # Dummy value
    MODERNA: 12,  # Dummy value
}
DOSE_2_PEAK_IMMUNITY_DAY = {
    PFIZER: 7,
    AZ: 7,  # Dummy value
    MODERNA: 7,  # Dummy value
}
DOSE_PEAK_IMMUNITY_DAY = [DOSE_1_PEAK_IMMUNITY_DAY, DOSE_2_PEAK_IMMUNITY_DAY]


DOSE_1_IMMUNITY_WANING_RATE = {
    PFIZER: -0.001,  # Dummy value
    AZ: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_2_IMMUNITY_WANING_RATE = {
    PFIZER: -0.001,  # Dummy value
    AZ: -0.001,  # Dummy value
    MODERNA: -0.001,  # Dummy value
}
DOSE_IMMUNITY_WANING_RATE = [DOSE_1_IMMUNITY_WANING_RATE, DOSE_2_IMMUNITY_WANING_RATE]

DEFAULT_JAB_DATE_OFFSET = {
    1: 120,
    2: 30
}
