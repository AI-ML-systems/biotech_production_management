import pandas as pd


def extract_final_values(
    data: pd.DataFrame,
    group_column: str,
    time_column: str = "Time",
    value_column: str = "OpticalDensity",
    final_time: float = 24.0
) -> dict[float, float]:
    final_values = {}
    unique_groups = sorted(data[group_column].unique())

    for group in unique_groups:
        group_data = data[data[group_column] == group]
        final_value = group_data[group_data[time_column] == final_time][value_column].iloc[0]
        final_values[group] = final_value
    return final_values


def calculate_coefficients(
    values: dict[float, float], reference_key: float
) -> dict[float, float]:
    reference_value = values[reference_key]
    return {key: value / reference_value for key, value in values.items()}


def format_coefficients(
    coefficients: dict[float, float], unit: str,
) -> tuple[tuple[str, float], ...]:
    return tuple((f"{key}{unit}", coeff) for key, coeff in coefficients.items())


def print_coefficient_report(formatted_coefficients: tuple[tuple[str, float], ...]):
    for label, coeff in formatted_coefficients:
        print(f"  {label}: {coeff:.6f}")
