DiPlanner
DiPlanner is a lightweight task planner application designed to help you organize and manage your daily tasks. It features an intuitive interface for adding, editing, and tracking tasks for specific days, with automatic data saving for seamless user experience.

Features
Calendar Navigation

Select specific days using the built-in calendar.
Navigate months with the "Next Month" button.
Daily Task Management

View a horizontal timeline of hours for the selected day.
Add tasks with a title and a short description for any hour.
Mark tasks as completed (tasks will be crossed out).
Edit or delete existing tasks.
Persistent Storage

Tasks are automatically saved to a tasks.json file.
All tasks are restored when the application is reopened.
User-Friendly Interface

Designed with a light theme and styled buttons in orange and blue tones.
Requirements
Python: Version 3.8 or higher.
Required Libraries:
PyQt6
json (part of the Python standard library).
Installation
Clone or download the repository:


git clone https://github.com/fikkic/DiPlaner
cd diplanner
Install dependencies:

pip install PyQt6
Ensure the dipla.ui file is located in the project folder.

Running the Application
Open a terminal or command prompt.

Navigate to the project directory.

Run the main script:

bash
Копировать код
python dipla.py
The application window will open, and you can start planning your day.

Project Structure
plaintext
Копировать код
diplanner/
├── dipla.py          # Main application logic
├── dipla.ui          # UI design file created with Qt Designer
├── tasks.json        # File for storing task data
└── README.md         # Project description
How to Edit the UI
Install and open Qt Designer (part of Qt Tools).
Open the dipla.ui file:

designer dipla.ui
Modify the interface as needed and save the file.
Restart the application to see the changes.
Future Enhancements
Add notifications for task reminders.
Allow viewing tasks for multiple days at once.
Integrate cloud synchronization for tasks.
Support for recurring tasks.
Contact Information
If you have any questions or suggestions, feel free to reach out:

Email: radyukdiana@icloud.com
GitHub: fikkic
Start organizing your day efficiently with DiPlanner! 🎯
