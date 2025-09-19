import pandas as pd
import numpy as np

def data_profiling_report(df: pd.DataFrame, df_name: str = "", unique_value_threshold: int = 15) -> pd.DataFrame:
    """
    Generates a definitive data profiling report.

    This report provides a comprehensive overview of a DataFrame, including:
    1.  Standard descriptive statistics for all data types.
    2.  Data type, percentage of missing values, and unique value counts.
    3.  Coefficient of Variation for numerical columns to flag high volatility/skew.
    4.  A list of unique values for low-cardinality categorical columns.
    
    Args:
        df (pd.DataFrame): The DataFrame to be profiled.
        df_name (str, optional): The name of the DataFrame for display purposes.
        unique_value_threshold (int, optional): The maximum number of unique values to display.

    Returns:
        pd.DataFrame: A comprehensive and sorted data profiling report.
    """
    if df_name:
        print(f"--- Definitive Data Profiling Report for: {df_name} ---")
        print(f"Shape of DataFrame: {df.shape}\n")
    
    # STEP 1: Get the comprehensive summary for ALL columns
    summary_stats = df.describe(include='all').T
    
    # STEP 2: Get core non-statistical info
    info_df = pd.DataFrame({
        'Data Type': df.dtypes,
        '% Missing': df.isnull().sum() / len(df) * 100,
        '# Unique': df.nunique() # <-- FIX 1: Added this back for consistency
    })
    
    # STEP 3: Combine them
    final_report = summary_stats.join(info_df)

    # Add Coefficient of Variation (std/mean) for numeric columns
    final_report['Coeff of Var'] = final_report.apply(
        lambda row: abs(row['std'] / row['mean']) if pd.notnull(row['mean']) and row['mean'] != 0 else np.nan,
        axis=1
    )

    # Add Unique Categorical Entries
    unique_entries = {}
    for col in df.columns:
        if isinstance(df[col].dtype, pd.CategoricalDtype) or df[col].dtype == 'object':
            # Use the consistent '# Unique' column for the check
            if final_report.loc[col, '# Unique'] <= unique_value_threshold:
                unique_entries[col] = df[col].unique().tolist()
            else:
                unique_entries[col] = "[High Cardinality]"
        else:
            unique_entries[col] = np.nan
            
    final_report['Unique Values'] = pd.Series(unique_entries)
    
    # Final cleanup and reordering
    if '50%' in final_report.columns:
        final_report.rename(columns={'50%': 'Median (50%)'}, inplace=True)
    
    # FIX 2: Removed the inconsistent fillna loop. The function will now consistently
    # return NaN for all missing values, preserving numeric dtypes.
    
    # Define the final column order
    core_cols = ['Data Type', '% Missing', '# Unique']
    
    stat_cols = ['count', 'mean', 'std', 'Coeff of Var', 'min', '25%', 'Median (50%)', '75%', 'max', 'top', 'freq']
    # Filter only for columns that actually exist to handle pure numeric/categorical cases
    existing_stat_cols = [c for c in stat_cols if c in final_report.columns]
    
    final_report = final_report[core_cols + existing_stat_cols + ['Unique Values']]
    
    # Sort by the most critical metric
    return final_report.sort_values(by='% Missing', ascending=False)