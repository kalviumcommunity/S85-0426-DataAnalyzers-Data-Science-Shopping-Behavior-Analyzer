### 1. Problem Statement

Retail chains want to send personalized offers to customers, but it's a tough challenge. Imagine a store with millions of customers; you can't manually figure out what each person likes. Most stores have a lot of data about what people buy, but they struggle to turn that data into smart decisions. They often end up sending the same generic offers to everyone, which most people ignore. Personalization is difficult because they lack clear insights into what different groups, or "segments," of customers actually prefer.   

### 2. Objective

The main goal of this project is to solve the personalization puzzle using **behavioural clustering**. The system aims to automatically group customers based on their shopping habits. By creating these groups, the retail chain can understand the unique preferences of each segment and send them offers that are far more relevant and appealing.

### 3. Approach / Methodology

*   **What is behavioural clustering?** It’s a technique used to group customers based on how they act—in this case, their shopping behaviour. Instead of looking at demographics like age or location, we focus on actions like what they buy, how often they shop, and how much they spend.

*   **What type of data is used?** We use transaction data, which includes:
    *   **Purchase History:** What products a customer buys.
    *   **Frequency:** How often they visit the store.
    *   **Monetary Value:** How much money they spend per visit or over time.

*   **How are customers grouped?** We use a clustering algorithm, like **K-Means**, to do the grouping. This algorithm takes all the customer data and finds natural clusters, or groups, of customers who behave similarly.

*   **How are clusters are interpreted?** After the groups are formed, we analyze them to give them meaningful labels. For example, we might find clusters like:
    *   **Premium Buyers:** Customers who buy expensive items frequently.
    *   **Discount Seekers:** Customers who mostly buy items on sale.
    *   **Occasional Shoppers:** Customers who visit rarely but spend a lot when they do.

### 4. System Workflow

The project follows a step-by-step pipeline:

1.  **Data Collection:** Gather raw purchase data from the store’s database.
2.  **Preprocessing:** Clean the data to handle missing values and format it for the clustering model.
3.  **Clustering:** Run the K-Means algorithm to segment customers into distinct groups.
4.  **Insight Generation:** Analyze each cluster to understand its unique characteristics and preferences.
5.  **Recommendations:** Create targeted marketing strategies and personalized offers for each cluster.

### 5. Recommendation Logic

The logic is simple: send different offers to different clusters.

*   **Example 1 (Premium Buyers):** A customer in this cluster might receive early access to new high-end products or exclusive invitations to special events.
*   **Example 2 (Discount Seekers):** A customer in this cluster would get notifications about "buy one, get one free" deals, clearance sales, or digital coupons for their favorite brands.

This way, each customer receives offers that align with their shopping style, making them more likely to make a purchase.

### 6. Assumptions & Limitations

*   **Assumptions:**
    *   We assume that a customer's past behaviour is a good predictor of their future behaviour.
    *   We assume that the clusters we create are stable over time.

*   **Limitations:**
    *   **Data Bias:** If the data is mostly from one type of customer (e.g., weekend shoppers), the clusters might not represent the entire customer base.
    *   **Cold Start Problem:** The system can't make good recommendations for new customers because they have no purchase history.
    *   **Changing Behaviours:** Customer preferences can change, and the model might not adapt quickly enough.

### 7. Improvements

This system can be made even better:

*   **Real-time Data:** Instead of analyzing data weekly or monthly, use real-time data to adapt to a customer's most recent actions.
*   **Hybrid Models:** Combine clustering with other recommendation techniques (like "customers who bought this also bought...") to provide even more accurate suggestions.
*   **Feedback Loop:** Incorporate a system to track whether customers are using the offers they receive, and use that feedback to improve the model over time.

### 8. Final Summary

This project helps retail chains move from generic marketing to smart personalization. By using behavioural clustering, it groups customers based on their shopping habits, like what they buy and how often. These groups then receive tailored offers that match their preferences, such as luxury deals for big spenders and discounts for bargain hunters. This approach makes marketing more effective and helps build stronger customer loyalty.

### 9. Milestone 4.5: Local Data Science Environment Setup Proof

This section documents the local setup required for the Data Science sprint and provides terminal proof that the environment is ready for notebooks, scripts, ML workflows, and Streamlit-based development.

#### Operating System

- Windows

#### Installed Versions

- Python (system): `3.13.5`
- Anaconda (conda): `25.11.1`
- Conda environment for sprint: `ds-sprint` with Python `3.11.15`

#### Setup Steps Performed

1. Verified existing Python installation from terminal.
2. Installed Anaconda using `winget`.
3. Verified Conda installation and base path.
4. Accepted required Conda Terms of Service channels.
5. Created a dedicated environment `ds-sprint` with Python 3.11.
6. Installed starter Data Science packages in `ds-sprint`:
    - `numpy`
    - `pandas`
    - `scikit-learn`
    - `jupyter`
7. Validated environment by running Python and importing the installed packages.

#### Verification Commands and Outputs

```powershell
python --version
# Python 3.13.5

where.exe python
# C:\Users\iamsh\AppData\Local\Programs\Python\Python313\python.exe
# C:\Users\iamsh\AppData\Local\Microsoft\WindowsApps\python.exe

python -c "import sys; print('executable:', sys.executable); print('version:', sys.version.split()[0]); print('ok')"
# executable: C:\Users\iamsh\AppData\Local\Programs\Python\Python313\python.exe
# version: 3.13.5
# ok
```

```powershell
winget install -e --id Anaconda.Anaconda3 --accept-source-agreements --accept-package-agreements
# Successfully installed Anaconda3 (2025.12-2)

C:\Users\iamsh\anaconda3\Scripts\conda.exe --version
# conda 25.11.1

C:\Users\iamsh\anaconda3\Scripts\conda.exe info --base
# C:\Users\iamsh\anaconda3

C:\Users\iamsh\anaconda3\Scripts\conda.exe tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
C:\Users\iamsh\anaconda3\Scripts\conda.exe tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
C:\Users\iamsh\anaconda3\Scripts\conda.exe tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
# accepted Terms of Service for all required channels

C:\Users\iamsh\anaconda3\Scripts\conda.exe create -y -n ds-sprint python=3.11
# environment location: C:\Users\iamsh\anaconda3\envs\ds-sprint

C:\Users\iamsh\anaconda3\Scripts\conda.exe env list
# base                     C:\Users\iamsh\anaconda3
# ds-sprint                C:\Users\iamsh\anaconda3\envs\ds-sprint

C:\Users\iamsh\anaconda3\Scripts\conda.exe run -n ds-sprint python --version
# Python 3.11.15

C:\Users\iamsh\anaconda3\Scripts\conda.exe install -y -n ds-sprint numpy pandas scikit-learn jupyter
C:\Users\iamsh\anaconda3\Scripts\conda.exe run -n ds-sprint python -c "import numpy, pandas, sklearn, jupyter; print('packages-ok')"
# packages-ok

C:\Users\iamsh\anaconda3\Scripts\conda.exe run -n ds-sprint python -c "print('hello from ds-sprint')"
# hello from ds-sprint
```

#### Notes

- If `conda` is not immediately available in a new terminal, use the full path above or reopen terminal after running Anaconda installation.
- Preferred sprint environment command:

```powershell
conda activate ds-sprint
```

### 10. Milestone 4.10: Writing Markdown for Headings, Lists, and Code Blocks in Notebooks

This milestone demonstrates clear documentation inside a Jupyter Notebook. The goal is to show how Markdown can structure a notebook so that the flow is easy to follow for reviewers and teammates.

#### Notebook Artifact

- [Markdown_Notebook_Milestone.ipynb](notebooks/Markdown_Notebook_Milestone.ipynb)

#### What the Notebook Demonstrates

1. Headings for organizing notebook sections.
2. Ordered and unordered lists for structured explanations.
3. Inline code such as `customer_id` and `summarize_items()`.
4. A fenced code block inside a Markdown cell.
5. A clean alternation between Markdown cells and code cells.

#### Why This Matters

- Markdown explains the purpose of the code, not just the output.
- Clear structure makes the notebook easier to review and reuse.
- Good documentation helps teammates understand why each step exists.

#### Submission Notes

- The notebook is focused on communication rather than analysis.
- A short screen recording should show the Markdown cells, code cells, and the explanation of why documentation improves readability.

### 11. Milestone 4.11: Creating a Project Folder Structure for Data Science Work

This milestone demonstrates a clean and predictable project layout for Data Science work. The goal is to separate notebooks, raw data, processed data, and outputs so the repository stays easy to understand and maintain.

#### Recommended Folder Structure

```text
S85-0426-DataAnalyzers-Data-Science-Shopping-Behavior-Analyzer/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── outputs/
│   ├── figures/
│   └── reports/
└── scripts/
```

#### Why This Structure Helps

- `data/raw` keeps original files untouched.
- `data/processed` stores cleaned or transformed data.
- `notebooks` keeps exploratory or documentation-focused work separate.
- `outputs` holds generated results, charts, and exported reports.
- `scripts` keeps reusable Python code isolated from notebooks.

#### Organization Principles

1. Use simple, lowercase folder names.
2. Keep raw data separate from generated artifacts.
3. Avoid mixing notebooks, scripts, and outputs in the same folder.
4. Use predictable paths so collaborators can find files quickly.

#### Submission Notes

- The repository is being structured to support clarity and reuse.
- A short walkthrough video should show the root project folder, explain each subfolder, and describe why the structure makes collaboration easier.

### 12. Milestone 4.12: Organizing Raw Data, Processed Data, and Output Artifacts

This milestone demonstrates clean separation across the data lifecycle. Raw data, processed data, and output artifacts are kept in different locations so the project remains reproducible, auditable, and easy to maintain.

#### Data Lifecycle Layout

```text
S85-0426-DataAnalyzers-Data-Science-Shopping-Behavior-Analyzer/
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── figures/
│   └── reports/
└── notebooks/
```

#### Folder Purpose

- `data/raw` stores original input files exactly as received.
- `data/processed` stores cleaned or transformed datasets derived from raw inputs.
- `outputs/figures` stores generated plots and visual artifacts.
- `outputs/reports` stores exported summaries or written reports.
- `notebooks` stores analysis or documentation notebooks that read from data and write to outputs when needed.

#### Data Discipline Principles

1. Never edit raw data directly.
2. Save derived datasets in `data/processed` with clear names.
3. Keep output artifacts separate from input data.
4. Use one-directional flow from raw to processed to outputs.

#### Submission Notes

- The repository now contains separate folders for the required data stages.
- A short video should show the raw, processed, and output folders and explain why this separation protects data integrity and reproducibility.

### 13. Milestone 4.13: Creating and Running a First Python Script for Data Analysis

This milestone demonstrates a standalone Python script that runs outside Jupyter Notebook. The script uses simple numeric and string values to show how analysis code can be executed in a repeatable, command-line-friendly way.

#### Script Artifact

- [scripts/first_data_analysis.py](scripts/first_data_analysis.py)

#### What the Script Demonstrates

1. Defining simple variables with numbers and text.
2. Performing basic calculations such as totals and averages.
3. Printing results to the console with clear labels.
4. Using a proper script entry point with `if __name__ == "__main__":`.

#### How to Run It

```powershell
python scripts/first_data_analysis.py
```

#### Why Scripts Matter

- Scripts run from top to bottom and are easier to automate than notebooks.
- They do not depend on notebook state or manually run cells.
- They are better for repeatable workflows and simple data tasks.

#### Submission Notes

- The script is intentionally small and focused on execution flow.
- A short screen recording should show the script file, the terminal run, and the printed output.

### 14. Milestone 4.14: Reviewing Raw Data Columns and Types

This milestone documents the first structured inspection of the transaction dataset. The goal is to confirm which columns exist, what types they use, and which fields will need cleanup before analysis begins.

#### What It Demonstrates

1. Loading the raw dataset into a notebook or script.
2. Checking column names, data types, and missing values.
3. Identifying fields that need renaming or type conversion.

#### Why This Matters

- Early inspection prevents avoidable errors later in the pipeline.
- Knowing the schema helps define a clean preprocessing plan.
- A quick review makes it easier to explain the dataset during presentation.

#### Submission Notes

- The focus is on understanding the raw inputs before any transformations happen.
- A short walkthrough should show the dataset preview and the schema summary.

### 15. Milestone 4.15: Cleaning Missing Values and Duplicates

This milestone documents the first cleanup pass on the raw dataset. The goal is to remove obvious noise so the clustering inputs are reliable.

#### What It Demonstrates

1. Identifying missing values.
1. Dropping duplicate rows when appropriate.
1. Deciding which records need further review.

#### Why This Matters

- Clean inputs make patterns easier to trust.
- Basic cleanup reduces the risk of misleading clusters.

#### Submission Notes

- A short walkthrough should show the before-and-after row counts and missing-value summary.

### 16. Milestone 4.16: Standardizing Customer Identifiers

This milestone documents a small normalization step for customer identifiers so records can be grouped consistently across files and analysis steps.

#### What It Demonstrates

1. Checking identifier formats.
1. Removing inconsistent spacing or casing.
1. Confirming each customer maps to a stable key.

#### Why This Matters

- Consistent IDs prevent duplicate customer records.
- Stable keys make joins and summaries more dependable.

#### Submission Notes

- A short walkthrough should show the original and cleaned identifier examples.

### 17. Milestone 4.17: Building Customer-Level Aggregates

This milestone documents how raw transactions are turned into one row per customer. The goal is to build the features needed for clustering.

#### What It Demonstrates

1. Grouping transactions by customer.
1. Calculating purchase frequency and spend totals.
1. Creating a compact analysis table.

#### Why This Matters

- Clustering works better on customer-level features.
- Aggregates make behavior patterns easier to compare.

#### Submission Notes

- A short walkthrough should show the source table and the aggregated output.
