# Mouse Movement Program

This Python script leverages the `tkinter` library for creating a graphical user interface (GUI) and `pyautogui` for controlling the mouse cursor. The program allows users to schedule random mouse movements within a specified time range, preventing the computer from going into sleep mode during certain hours.

## How it Works

The program consists of the following components:

- **move_mouse(start_hour, end_hour):**
  - A function that continuously moves the mouse cursor to random coordinates on the screen.
  - The mouse movements occur only within the specified time range, determined by the `start_hour` and `end_hour` parameters.

- **run_program():**
  - Retrieves the starting and ending hours entered by the user from the GUI.
  - Initiates a new thread to run the `move_mouse` function with the provided time range.

- **stop_program():**
  - Stops the mouse movement program by triggering a mouse click using `pyautogui`.
  - Enables the `FAILSAFE` feature in `pyautogui` to ensure a failsafe exit mechanism.

- **GUI Components:**
  - Entry fields for entering the starting and ending hours in 24-hour format.
  - "Run" button to start the mouse movement program based on the specified time range.
  - "Stop" button to halt the program.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/mouse-movement-program.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mouse-movement-program
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the program:

    ```bash
    python mouse_movement_program.py
    ```

5. Enter the starting and ending hours in 24-hour format in the respective entry fields.
6. Click the "Run" button to start the mouse movement program.
7. Click the "Stop" button to halt the program.

## Dependencies

- **tkinter**: GUI library for Python.
- **pyautogui**: Library for programmatically controlling the mouse and keyboard.

## Notes

- The program runs in a separate thread to prevent GUI freezing during mouse movement.
- Ensure correct input format for starting and ending hours (24-hour).


## Authors

- [@galudSla](https://github.com/galudSla)
- email: tedgiann@gmail.com
