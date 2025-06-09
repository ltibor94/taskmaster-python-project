# Task Master Python Project – Phase1

[![Task Master Demo](/docs/demos/Demo_Phase1.gif)](/docs/demos/Demo_Phase1.gif)

## Task Listing
Displays all tasks in a responsive Bootstrap table. Each row shows the task’s content, completion status (open or finished), creation date, and action buttons. The table is styled for clarity and adapts to different screen sizes for optimal usability.

## Filtering
Navigation links for "All Tasks," "Finished Tasks," and "Open Tasks" allow users to filter the task list. This feature helps users focus on specific subsets of tasks, improving task management and organization.

## Adding New Task
A form below the task table allows users to add new tasks. The form validates input to prevent empty submissions. Upon successful addition, the new task appears instantly in the list, streamlining the task creation process.

## Deleting Task
Each task row includes a "Delete" button. Clicking it removes the task from the database and updates the list immediately, enabling users to efficiently manage and clean up their tasks.

## Updating Task
The "Update" button opens a form to edit a task’s content and completion status. After editing, changes are saved to the database and reflected in the task list, supporting easy and quick task modifications.

## Marking Tasks as Complete
A "Complete" button is provided for each task. Clicking it marks the task as finished, updates its status badge, and disables the button, allowing users to track progress and completed work visually.

## Bootstrap UI
The interface uses Bootstrap for a modern, mobile-friendly design. The navigation bar and table are styled for accessibility, with navigation links aligned to the right for intuitive filtering and navigation.

## Error Handling
Custom error pages display informative messages if task retrieval, creation, updating, or deletion fails. This improves user experience and helps with debugging by providing clear feedback on what went wrong.

## Modular Architecture
The application is built using a modular architecture that leverages Flask Blueprints for organizing routes, a dedicated service layer for business logic, and Data Transfer Objects (DTOs) for structured data exchange. This separation of concerns enhances maintainability and scalability, making it easier to add new features or modify existing ones. By isolating different responsibilities, the codebase remains clean, testable, and adaptable to future requirements, supporting efficient development and long-term project growth.

## Logging
A logger records key actions and errors throughout the application. This aids in monitoring, troubleshooting, and maintaining a reliable record of application behavior for developers and administrators.