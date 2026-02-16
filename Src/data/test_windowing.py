import pandas as pd
from Src.data.windowing import create_windows

df = pd.read_csv("data/raw/faulty_training.csv")
x, y = create_windows(
    df=df,
    window_size=50,
    step_size=5,
    is_training=True
)
