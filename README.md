The Digital IFRS 9 Playbook: A PRA-Compliant Credit Risk Framework

!\[alt text](notebooks/assets/rgk\_logo.png)

<!-- Optional: Add a logo for your project and place it in an 'assets' folder inside 'notebooks' -->

This repository contains the end-to-end development of a world-class, AI-driven IFRS 9 Expected Credit Loss (ECL) framework. It is designed to meet the rigorous standards of the UK's Prudential Regulation Authority (PRA) and serves as a portfolio for the UK Global Talent Visa.



🚀 Key Deliverables \& Highlights

This project is more than just code; it is a suite of tangible, high-impact assets that demonstrate the full lifecycle of modern risk management.

✨ The Live Interactive Dashboard: \[<!-- Link to your deployed Streamlit App will go here -->] - A multi-view dashboard for simulating risk appetite, demonstrating model explainability with SHAP, and reviewing model performance.

📖 The Definitive Whitepaper: \[<!-- Link to deliverables/whitepaper/The\_Digital\_IFRS9\_Playbook.pdf will go here -->] - A consolidated, professional report detailing the entire methodology, from regulatory design to production deployment.

📦 The Open-Source Toolkit: risk-governance-kit - A pip-installable Python library for automating model validation and governance, featuring tools for calculating PSI, WOE/IV, Gini, and generating automated validation reports.

📄 The Mock Validation Report: \[<!-- Link to the PDF in deliverables/reports/mock\_validation\_report.pdf will go here -->] - A simulated "Second Line of Defense" report, proving a 360-degree understanding of model risk management and PRA SS1/23.



✨ Live Application Demo

Below is a demonstration of the interactive Risk Appetite \& Profitability Simulator, a key feature of the deployed Streamlit application. It allows a user to adjust the PD cutoff and instantly see the impact on approvals, expected losses, and net profit.

<!-- IMPORTANT: Create a short GIF of your Streamlit app in action and place it in 'notebooks/assets/'. Tools like ScreenToGif or Kap are great for this. -->

!\[alt text](notebooks/assets/streamlit\_demo.gif)



The 10-Article Series: The Journey from Data to Deployment

This project is documented in a comprehensive 10-part series. Each notebook below is a self-contained article with detailed narrative, code, and visualizations.

Article #	Title	Link to Notebook

1	Architecting the Digital Foundation (PRA Compliance \& EDA)	01\_Regulatory\_Foundation\_and\_EDA.ipynb

2	From Raw Data to Intelligent Risk Signals (Feature Engineering)	02\_Feature\_Engineering\_360\_Profile.ipynb

3	The 'Glass Box' Champion Model (Logistic Regression \& WOE)	<!-- Link will go here -->

4	The Resilience Gauntlet (Advanced Model Validation)	<!-- Link will go here -->

5	Auditing the Algorithm (Explainable \& Fair AI with SHAP)	<!-- Link will go here -->

6	The Automated IFRS 9 Engine (SICR Calibration)	<!-- Link will go here -->

7	Future-Proofing ECL (Macroeconomic Satellite Models)	<!-- Link will go here -->

8	Governance as Code (The Open-Source Toolkit \& Vintage Analysis)	<!-- Link will go here -->

9	From Model to Market Impact (API \& Strategy Dashboard)	<!-- Link will go here -->

10	The Future of Risk Leadership (Alternative Data \& Climate Risk)	<!-- Link will go here -->



🛠 Project Structure

/app: Contains the source code for the deployed Streamlit dashboard.

/deliverables: Contains all final, non-code outputs: exported reports, charts, and the final whitepaper.

/notebooks: Contains the Jupyter Notebooks for the 10-part article series and the utils.py script.

/risk\_governance\_kit: The source code for the installable Python library.

/tests: Unit tests for the library to ensure code quality and robustness.





⚙️ Getting Started

To run this project locally, please follow these steps:

1. Clone the repository:

code

Bash

git clone https://github.com/ykbhole15/credit-risk-modelling-UK.git

cd credit-risk-modelling-UK



2\. Download the data:

The data for this project is from the Home Credit Default Risk competition. It must be downloaded from Kaggle and placed in a local data/ folder at the root of the project (this folder is included in .gitignore and will not be uploaded).



3\. Set up the environment:

It is highly recommended to use a virtual environment.

code

Bash

python -m venv venv

source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

pip install -r requirements.txt



4\. Install the toolkit:

To make the risk\_governance\_kit functions available for use in the notebooks, install it in editable mode:

code

Bash

pip install -e .



About the Author

This project was developed by Yuvaraj Bhole as a comprehensive portfolio demonstrating the end-to-end skills required of a senior risk professional in a modern, UK-regulated financial institution. The work showcases a deep expertise in IFRS 9, model governance, MLOps, and the strategic application of AI in finance.

Connect with me on LinkedIn. <!-- Add your LinkedIn profile URL here -->

