# Programming for Data Analytics - Assignments

This repository contains the project for the "Programming for Data Analytics" course. It includes solutions to the programming tasks, as well as supporting data files used in the project.

## Table of Contents

- [About](#about)
- [Project description](#project-description)
- [Files and Structure](#files-and-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Running the code](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)

## About

This project analyses and predicts currency trends for USD, GBP, BTC about EUR. By employing a systematic methodology, the analysis includes exploring trends, measuring volatility, smoothing data, decomposing time series, forecasting, and creating interactive visualizations. The insights from this project can assist in understanding currency behaviours and making data-driven decisions.


---

### Project Description

#### Overview:

This project analyses and predicts currency trends for USD, GBP, Bitcoin in relation to EUR. By following a systematic approach, the analysis will include trend exploration, volatility measurement, data smoothing, time-series decomposition, and forecasting.

---

#### Rules and Strategies

1. **Data Collection**

   - **Rule**: Use reliable and consistent data sources (e.g., Yahoo Finance, CoinGecko) to ensure data accuracy and completeness.
   - **Strategy**:
     - Focus on historical data spanning at least 5 years to identify long-term trends and patterns.
     - Save raw data in CSV format for reusability and shareability.
     - Consider using a database (e.g., SQLite) for efficient data management.

2. **Data Cleaning**

   - **Rule**: Ensure the dataset is free from errors, missing values, and inconsistencies.
   - **Strategy**:
     - Use forward-filling or interpolation techniques to handle missing values.
     - Standardise date formats to YYYY-MM-DD.
     - Normalize Bitcoin exchange rates or other data points to enable meaningful comparisons with traditional currencies.

3. **Exploratory Data Analysis (EDA)**

   - **Rule**: Begin with basic statistical summaries and visualizations to understand the data.
   - **Strategy**:
     - Use line charts to visualise historical trends.
     - Compute descriptive statistics such as each currency's mean, median, standard deviation, and range.
     - Explore relationships between currencies using correlation matrices and heatmaps.

4. **Advanced Analysis**

   - **Rolling Averages (Smoothing Trends)**

     - **Rule**: Highlight long-term trends by smoothing out short-term fluctuations.
     - **Strategy**: Use rolling averages with appropriate window sizes (e.g., 7-day, 30-day) to observe medium and long-term patterns.

   - **Time-Series Decomposition**

     - **Rule**: Decompose the data into trend, seasonality, and residual components for deeper insights.
     - **Strategy**:
       - Focus on yearly and monthly seasonality to identify recurring patterns.
       - Analyse residuals for irregularities or unexpected events.

   - **Volatility Analysis**

     - **Rule**: Measure and compare volatility across currencies.
     - **Strategy**:
       - Calculate standard deviations for monthly or yearly periods.
       - Use bar plots to compare the volatility of each currency over time.

5. **Forecasting**

   - **Rule**: Use simple predictive models to estimate future trends.
   - **Strategy**:
     - Use historical data to focus on short-term forecasting (e.g., 30 days).
     - Use linear regression for basic forecasting, keeping the approach interpretable and transparent.
     - Evaluate the accuracy of predictions by splitting the data into training and test sets.

**Tips for Effectively Achieving Your Project Goals**

1. **Visualization**

   - **Rule**: Use clear and visually appealing plots to communicate findings effectively.
   - **Strategy**:
     - Create interactive visualisations to allow dynamic exploration of trends (e.g., with dropdown menus for selecting currencies).
     - Label axes, add titles, and use consistent colour schemes for clarity.
    
2. **Documentation**

   - **Rule**: Maintain comprehensive and clear documentation for the project.
   - **Strategy**:
     - Write a README file that includes the project objectives, data sources, and instructions for running the analysis.
     - Clearly outline each step in markdown or explanatory text within the project notebook.
     - Summarise key findings and insights at the end of the analysis.

3. **Deliverables**

   - **Clean Data Files**:
     - Provide the cleaned and processed dataset in CSV format.
     - Database File: Store all processed data in an SQLite database for quick querying.

   - **Visualizations**:
     - Trend lines for each currency.
     - Volatility comparison charts.
     - Interactive visualisations for exploring data dynamically (Bonus Features).

   - **Final Report**: Include insights, observations, and potential real-world implications of the trends analysed.

4. **Best Practices**

   - Always validate your data sources to avoid bias or inaccuracies.
   - Break down complex tasks into smaller, manageable steps.
   - Keep visualisations simple and intuitive, ensuring they convey the intended message.
   - Regularly save progress and version-control your work using platforms like GitHub.

5. **Bonus Features**

    - Explore the impact of external factors (e.g., inflation, major global events) on currency trends.

---

## Files and Structure

The repository includes the following files and structure:

- `data/`: A folder containing subdirectories: 
    * `csv/`: A folder that stores CSV files.
      * `raw/`: A folder that stored raw CSV files.
      * `allcurrencies/`: A folder that stores merged, cleaned CSV files.
    * `db/`: A folder stores a database.
- `analysingCurrencyTrends`: A Jupyter Notebook that analyzes and predicts currency trends.
- `functions.py`: A file that contains functions used in the project.
- `.gitignore`: A file to specify which files and directories should not be tracked by Git.
- `README.md`: This file, which provides an overview of the repository.
- `requirements.tx`t`: Dependencies needed to run the Jupyter Notebook.

## Getting Started

To get started with this project, clone the repository to your local machine.

## Prerequisites

Ensure that you have Python installed on your system. The assignments may require specific Python libraries, which can be installed using the `requirements.txt` file if available.

You may also need a tool like [Jupyter Notebook](https://jupyter.org/) or a Python IDE (e.g., VSCode, PyCharm) to run the code.

## Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/TomUszyn/PFDA-project.git
   
2. Navigate to the project directory:
   ```bash
   cd PFDA-project

3. Install any necessary dependencies (if a requirements.txt file exists):
   ```bash
   pip install -r requirements.txt

## Running the Code

### Option 1: Running the Notebook in Jupyter

Since the code is implemented in Jupyter Notebooks (.ipynb files), you can run them using Jupyter Notebook or JupyterLab. Follow these instructions to get started:

1. Install Jupyter: If you don't already have Jupyter installed, you can install it using pip:
   ```bash
   pip install notebook

2. Open the Jupyter Notebook:
    * Navigate to the directory where the notebook file is located.
    * Run the following command to start Jupyter Notebook:
      ```bash
      jupyter notebook
3. Launch the notebook:
    * A browser window will open. Click on the desired `analysingCurrencyTrends.ipynb` file.
    * You can now execute the code cells interactively by selecting a cell and clicking the "Run" button or pressing Shift + Enter.

### Option 2: Running the Code in VS Code

You can also run Jupyter Notebooks in **Visual Studio Code (VS Code)**, which is a powerful code editor with great support for Python and Jupyter notebooks.

### Step 1: Install Visual Studio Code
If you don't have VS Code installed, you can download and install it from [here](https://code.visualstudio.com/).

### Step 2: Install the Python Extension
After installing VS Code, you need to install the Python extension and the Jupyter extension to enable notebook support:

1. Open **VS Code**.
2. Go to the **Extensions** view by clicking on the Extensions icon in the sidebar (or press `Ctrl+Shift+X`).
3. Search for **Python** and install it.
4. Search for **Jupyter** and install it as well.

### Step 3: Open the Jupyter Notebook in VS Code
1. Open VS Code and navigate to the folder where your notebook is located.
2. You can open the notebook directly from the **File Explorer** in VS Code. Simply click on the `analysingCurrencyTrends.ipynb` file, and it will open in a Jupyter Notebook interface within VS Code.

### Step 4: Running the Notebook
Once your notebook is open, you can run it just like in Jupyter Notebooks:

- You’ll see a **toolbar** above the notebook cells with a "Run" button. You can use this to run individual cells.
- To run a cell, select it and press `Shift + Enter` or click the "Run" button.

### Step 5: Working with Virtual Environments (Optional)
If your project uses a specific virtual environment (for example, `conda`), you can set it up in VS Code:

1. Make sure the virtual environment is activated.
2. Select your environment by clicking on the **Python version** in the bottom left corner of the VS Code window and selecting the appropriate interpreter.

## License

This repository is licensed under the MIT License - see the LICENSE file for more details.

## Acknowledgments

Thanks to the module lecturer and materials for providing the assignment context and datasets.
Inspiration from various programming tutorials and resources that helped solve the tasks.

## Author

I am a student at Atlantic Technical University in Ireland, currently pursuing a Higher Diploma in Science in Computing (Data Analytics). I have a strong foundation in computing with a particular focus on data analysis. My technical skills include:

* Operating Systems: Proficient in the Windows family and Linux (especially Ubuntu).
* Programming: Python programming with a focus on data analysis.
* Databases: Basic knowledge of MySQL for data storage and management.
* Web Technologies: Familiar with Apache for web server management.
* Scripting: Experience with Bash scripting and YAML for automation and configuration.

I am enthusiastic and hardworking. I am passionate about analysing real-world and virtual datasets, and I enjoy working on data-driven projects that provide insights and drive decisions.