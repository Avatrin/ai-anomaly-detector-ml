import pandas as ps

df = pd.read_csv(project_root_dir/"cleaned_data2"/"drive1_torque.csv", skiprows=range(1,15), parse_dates=['key'], index_col=['key'])

def show_bollinger_bands(df):
  df.index = pd.to_datetime(df.index, unit="s")
  df["filt_value"] = savgol_filter(df["value"], 99, 3) # window size (1001 or 99), polynomial order 3
  df["sma"] = df["value"].rolling(50).mean()
  df["std"] = df["value"].rolling(50).std()
  df["bollinger_upper"] = df["sma"] + df["std"] * 2   # calculate upper band
  df["bollinger_lower"] = df["sma"] - df["std"] * 2   # calculate lower band

  plt.figure(figsize=(8,6))
  # plt.plot(df)
  plt.plot(df[["value", "sma", "bollinger_upper", "bollinger_lower"]].loc["1978-07-01 00:00:00":"1979-07-01 00:00:00"])

if __name__ == "__main__":
  df = pd.read_csv(project_root_dir/"cleaned_data2"/"drive1_torque.csv", skiprows=range(1,15), parse_dates=['key'], index_col=['key'])
  show_bollinger_bands(df)
