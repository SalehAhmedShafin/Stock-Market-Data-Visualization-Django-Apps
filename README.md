# Django Stock Market Data Web Application

## Project Overview

This Django learning project involves building a basic web application with data visualization and CRUD functionality. The project is divided into three main steps:

1. **Initial Web App with JSON Data:**
   - Creation of a basic web app using Python and Django.
   - Utilization of JSON data to generate a table visualization on the home page.

2. **Integration with SQL Server and CRUD Functionality:**
   - Loading the data into an SQL server for improved data management.
   - Implementation of CRUD operations for the table, allowing users to edit rows dynamically.
   - Creation of separate branches in the Git repository for each model version: `jsonModel` and `sqlModel`.

3. **Enhanced Data Visualization:**
   - Addition of a line chart above the table visualization.
   - Plotting the "close" column on the y-axis and "sorted date" on the x-axis in the line chart.
   - Incorporation of the "volume" column as a bar chart on a secondary y-axis.
   - Accommodate the line and bar chart together by making it a multi axis chart.
   - Implementation of a dropdown feature to switch between different "trade_code" columns, dynamically updating the all charts.

## Getting Started

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SalehAhmedShafin/Stock-Market-Data-Visualization-Django-Apps
# Django Learning Project

## Getting Started

1. **Navigate to the project directory:**
    ```bash
    cd Webapps/Janata
    ```

2. **Apply migrations to set up the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

4. **Open your browser and go to [http://localhost:8000/](http://localhost:8000/) to view the web app.**

## Challenges Faced

### Transition from JSON to SQL
- Adapting the codebase to switch between JSON and SQL models posed challenges.
- Ensuring data consistency and integrity during the migration process.

### Implementing CRUD Operations
- Integrating frontend and backend components to support editable rows in the table.
- Handling user input and updating the SQL database accordingly.

### Multi-Axis Chart Integration
- Implementing a multi-axis chart with dynamic data based on user selections.
- Coordinating the line and bar charts for a cohesive visualization.
- 
### Chart.js integration issue
- After integrating Chart.js into the project, the chart is not displaying as expected on the webpage.

## Key Learnings

### Django and Backend Development
- Gained proficiency in using Django for web application development.
- Learned the intricacies of integrating backend functionality with frontend interfaces.

### Data Visualization with Chart.js
- Acquired skills in implementing interactive charts using Chart.js.
- Explored the nuances of creating multi-axis charts for diverse data representation.

### Database Management
- Applied principles of maintaining data integrity and consistency in a dynamic web environment.

### Version Control and Collaboration
- Collaborated on a project involving frontend and backend development, enhancing coordination and communication skills.

This project provided valuable insights into full-stack web development, data visualization, and database management, enhancing skills in Python, Django, Chart.js, and version control.
