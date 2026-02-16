import numpy as np
import pandas as pd

from Src.data.te_schema import (
    FEATURE_COLUMNS,
    NORMAL_FAULT_ID,
    FAULT_ONSET_TRAIN_SAMPLES,
    FAULT_ONSET_TEST_SAMPLES
)


def create_window_from_RUN(run_df: pd.DataFrame, window_size: int, step_size: int, fault_onset_sample: int):
    x_windows = []
    y_labels = []
    values = run_df[FEATURE_COLUMNS].values
    samples = run_df["sample"].values
    fault_number = run_df["faultNumber"].iloc[0]
    num_steps = len(run_df)

    for start in range(0, num_steps - step_size + 1, step_size):
        end = start + window_size

        window_samples = samples[start:end]
        window_x = values[start, end]
        window_samples = samples[start:end]

        # Labeling logic
        if fault_number == NORMAL_FAULT_ID:
            label = 0
        else:
            label = int(window_samples.max() >= fault_onset_sample)

        x_windows.append(window_x)
        y_labels.append(label)

    return np.array(x_windows), np.array(y_labels)


def create_windows(df: pd.DataFrame, window_size: int, step_size: int, is_training: bool = True):
    """
        Create windows for ALL simulation runs.

        Returns
        -------
        X : np.ndarray (N, window_size, 52)
        y : np.ndarray (N,)
        """
    x_all = []
    y_all = []
    fault_onset = (
        FAULT_ONSET_TRAIN_SAMPLES
        if is_training
        else FAULT_ONSET_TEST_SAMPLES
    )
    for run_id, run_df in df.groupby("simulationRun"):
        x_run, y_run = create_window_from_RUN(
            run_df=run_df,
            window_size=window_size,
            step_size=step_size,
            fault_onset_sample=fault_onset
        )
        x_all.append(x_run)
        y_all.append(y_run)
    return np.vstack(x_all), np.concatenate(y_all)
