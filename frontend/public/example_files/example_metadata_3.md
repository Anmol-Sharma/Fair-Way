# Customer Churn Dataset

## Metadata

- **Creator**: Jane Doe
- **Date Created**: 2023-10-05
- **Version**: 1.0

## Description

This dataset contains information about customers of a telecommunications company, including demographic data and service usage metrics. The goal is to predict whether a customer will churn (cancel their subscription) based on various features.

## Data Dictionary

| Column Name       | Data Type | Description                                                      |
| ----------------- | --------- | ---------------------------------------------------------------- |
| customer_id       | integer   | Unique identifier for each customer                              |
| age               | integer   | Age of the customer                                              |
| gender            | string    | Gender of the customer (Male/Female)                             |
| subscription_type | string    | Type of subscription plan (Basic/Standard/Premium)               |
| monthly_charges   | float     | Monthly charges in USD                                           |
| total_usage       | integer   | Total data usage in GB over the past month                       |
| churn             | boolean   | Indicates whether the customer churned (1 = Churn, 0 = Retained) |

## File Structure

```

customer_churn_dataset/
├── README.md # This file
├── data/ # Directory containing the dataset files
│ └── customer_churn.csv # Main dataset file in CSV format
└── documentation/ # Additional documentation and analysis
└── data_description.pdf # Detailed description of the dataset

```

## Usage Instructions

1. **Loading the Data**:
   The dataset is provided in CSV format and can be loaded using standard data analysis tools like Python's `pandas` library.
   Example in Python:

   ```python
   import pandas as pd

   df = pd.read_csv('data/customer_churn.csv')
   print(df.head())
   ```

2. **Preprocessing**:

   - Handle missing values if any (none in this dataset).
   - Encode categorical variables if necessary.

3. **Analysis**:
   Use the dataset to build predictive models for customer churn, perform exploratory data analysis, or generate insights about customer behavior.

## License

This dataset is released under the [MIT License](LICENSE). You are free to use, modify, and distribute this dataset for any purpose, provided you include the appropriate attribution.

## Contact

For questions or feedback, please contact:

- **Email**: jane.doe@example.com
- **GitHub**: [jane-doe](https://github.com/jane-doe)
