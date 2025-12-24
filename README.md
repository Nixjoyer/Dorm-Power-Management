
# Dormitory Energy Consumption Calculator

This Python-based project provides a practical solution for university students residing in dormitories to track and manage their individual energy consumption and associated costs. The script collects details such as the student's name, appliance information, average daily usage, duration of operation, and the local kilowatt-hour (kWh) rate. It then calculates the total energy consumed and the cost incurred for each student. All collected data and calculated results are stored, presented in a clear, sortable table, and ultimately ranked from the highest to the lowest energy cost, helping students identify and potentially reduce their energy footprint.

## Features

*   **Individualized Data Input:** Gathers student name, appliance name, average daily usage (hours), number of days in operation, and kilowatt-hour (kWh) rate.
*   **Energy Consumption & Cost Calculation:** Automatically computes total energy consumed and the corresponding financial cost per student.
*   **Data Persistence:** Stores calculated results for multiple individuals within the current session.
*   **Tabular Display:** Presents all stored data in a well-structured, easy-to-read table.
*   **Cost-Based Ranking:** Ranks students from highest to lowest energy cost, providing clear insights into consumption patterns.
*   **Python-based:** Developed entirely in Python for ease of use and extensibility.

## Installation

To get a copy of the project up and running on your local machine, follow these simple steps.

### Prerequisites

*   Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

1.  Open your terminal or command prompt.
2.  Navigate to the directory where you want to store the project.
3.  Clone the repository using Git:

    ```bash
    git clone https://github.com/your-username/dormitory-energy-calculator.git
    cd dormitory-energy-calculator
    ```

### Install Dependencies (Optional)

This project primarily uses standard Python libraries. If future enhancements introduce external libraries (e.g., `pandas` or `tabulate` for advanced table formatting), they would be listed here. For now, assume a minimal setup.

```bash
# If a requirements.txt file exists:
# pip install -r requirements.txt
```

## Usage

Follow these instructions to run the energy consumption calculator.

1.  **Run the Script:**
    Execute the main Python script from your terminal within the `dormitory-energy-calculator` directory:

    ```bash
    python main.py # Replace main.py with the actual name of your primary script if different
    ```

2.  **Follow On-Screen Prompts:**
    The script will interactively ask you for the following information for each student:
    *   `Your Name:` (e.g., John Doe)
    *   `Appliance Name:` (e.g., Laptop, Mini-fridge, Desk Lamp)
    *   `Average Daily Usage (in hours):` (e.g., 8, 24, 5)
    *   `Number of Days in Operation:` (e.g., 30 for a month)
    *   `Kilowatt-Hour (kWh) Rate:` (e.g., 0.12 for $0.12/kWh, 0.25 for $0.25/kWh)

    You can input data for multiple students consecutively. The script will guide you through adding more entries or finishing the input process.

3.  **View Results:**
    After all inputs are provided, the script will display a clear table summarizing all entries, ranked by their total energy cost from highest to lowest.

## Contributing

We welcome contributions to improve this project! If you have suggestions for new features, bug fixes, or improvements, please follow these steps:

1.  **Fork the Repository:** Click the 'Fork' button at the top right of this page on GitHub.
2.  **Clone Your Fork:**

    ```bash
    git clone https://github.com/your-username/dormitory-energy-calculator.git
    cd dormitory-energy-calculator
    ```

3.  **Create a New Branch:**
    For features or significant changes, create a new branch:

    ```bash
    git checkout -b feature/your-feature-name
    # Or for bug fixes:
    git checkout -b bugfix/issue-description
    ```

4.  **Make Your Changes:** Implement your feature, fix the bug, or make improvements.
5.  **Commit Your Changes:**
    Write a clear and concise commit message.

    ```bash
    git commit -m "feat: Add [your feature description]"
    # Or:
    git commit -m "fix: Resolve [bug description]"
    ```

6.  **Push to Your Branch:**

    ```bash
    git push origin feature/your-feature-name
    ```

7.  **Open a Pull Request:** Go to the original repository on GitHub and open a new pull request, describing your changes in detail.
