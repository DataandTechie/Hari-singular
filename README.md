Job Postings Dashboard

This project is a Streamlit-based web application designed to visualize job postings data. 
The application allows users to filter job postings by various parameters such as date range, vendor, and job title. 
The filtered data is then presented in both tabular and graphical formats, providing insightful visualizations.

Features
Date Filtering: Select a date range to filter job postings based on when they were posted.
Vendor and Job Title Filtering: Use the sidebar to filter job postings by vendor and job title.

Interactive Visualizations:
Bar charts and pie charts display the distribution of job postings by vendor and job title.
Dynamic and responsive plots created with Plotly.
Installation
Clone the repository:

bash
Copy code
git clone <repository-url>
cd <repository-directory>
Install dependencies:
Ensure you have Python installed. Then install the required Python packages:

bash
Copy code
pip install streamlit pandas plotly numerize
Run the application:

bash
Copy code
streamlit run <script_name>.py
Usage
After launching the app, a table displaying all job postings will appear.
Use the date selectors to filter postings by the "posted_on" date.
Utilize the sidebar to filter by vendor and job title.
Visualizations in the form of bar charts and pie charts will update based on your filters.
Code Structure
query.py: Contains the view_all_data() function, which retrieves the job postings data.
Streamlit app:
Data is loaded and displayed in a table using st.dataframe().
Filters are applied to narrow down the data based on user input.
Plotly is used to create and display bar and pie charts to visualize the data distribution.

Dependencies
Streamlit: An app framework for Machine Learning and Data Science teams.
Pandas: A powerful data analysis and manipulation library for Python.
Plotly: A graphing library that makes interactive, publication-quality graphs.
Numerize: A Python library to convert numbers to readable formats.

Contribution
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

