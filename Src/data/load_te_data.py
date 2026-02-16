from contextlib import redirect_stdout

import pandas as pd
from pathlib import Path

data_raw_dirs = Path("C:/Users/Sheidaqiupeedsh/TE_Fault_Detection/Fault_detection_project/data/raw")


def load_csv(file_name):
    file_path = data_raw_dirs / file_name
    df = pd.read_csv(file_path)
    return df


def inspect_dataframe(df, name="Dataset", txt_path="inspect_log.txt"):
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"\nname = {name}\n")
        f.write(f"Shape = {df.shape}\n")
        f.write(f"columns:, {df.columns.tolist()}\n")
        f.write("\nHead:\n")
        f.write(df.head().to_string() + "\n")
        f.write("\nInfo:\n")
        with redirect_stdout(f):
            df.info()


if __name__ == "__main__":
    df = load_csv("fault_free_training.csv")
    inspect_dataframe(df, name="Dataset",
                      txt_path="C:/Users/Sheidaqiupeedsh/TE_Fault_Detection/Fault_detection_project/notebooks/logs/fault_free_training_inspect_log.txt")
