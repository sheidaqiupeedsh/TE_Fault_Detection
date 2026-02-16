"""
Tennessee Eastman Process (TEP) Data Schema
-------------------------------------------
This file defines the official data schema for the whole Project.
All preprocessing, windowing and modeling must follow this schema.

Author : Sheida
"""

METADATA_COLUMNS = [
    "row",
    "fault_number",
    "simulationRUN",
    "samples"
]

# --------------------------
# sensor measured variables
# --------------------------

XMEAS_COLUMNS = [
    f"xmeas_{i}" for i in range(1, 42)
]

# ----------------------------
# sensor manipulated variables
# ----------------------------

XMV_COLUMNS = [
    f"xmv_{i}" for i in range(1, 12)
]

# ---------------------
# model input features
# ---------------------

FEATURE_COLUMNS = XMEAS_COLUMNS + XMV_COLUMNS

# -------------------
# FAULT DEFINITION
# -------------------

NORMAL_FAULT_ID = 0
FAULT_IDS = list(range(1, 21))

# ---------------
# time definition
# ---------------

SAMPLING_PERIOD_MIN = 3

# --------------------------------------------------------
# Fault introduction times (based on dataset description)
# Training fault starts at sample >= 20
# Testing fault starts at sample >= 160
# --------------------------------------------------------

FAULT_ONSET_TRAIN_SAMPLES = 20  # 1 hour = 20 samples
FAULT_ONSET_TEST_SAMPLES = 160  # 8 hours = 160 samples



if __name__ == "__main__":
    print("Number of features:", len(FEATURE_COLUMNS))
    print("First 5 features:", FEATURE_COLUMNS[:5])
    print("Last 5 features:", FEATURE_COLUMNS[-5:])
