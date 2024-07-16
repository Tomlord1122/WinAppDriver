# Windows Application Driver Test Suite

This repository contains a set of automated tests for Windows applications using the Windows Application Driver (WinAppDriver). The tests are written in Python and utilize the `unittest` framework along with the `appium` library for interacting with the applications.

## Files Overview

### Install Dependencies

```
pip install -r requirements.txt
```

### Compress to one executable file

```
python -m PyInstaller --onefile --add-data "windowStore.py;." --add-data "windowsUpdate.py;." --add-data "Edge.py;." run_spec.py
```

### run_spec.py
This file is the main entry point for running the test suite. It includes the following key functions:
- `create_test_suite()`: Creates a test suite by adding test cases from `EdgeTests`, `WindowsStoreUpdateTests`, and `windowsUpdate`.
- `main()`: Sets up the environment, runs the test suite, and restarts the computer after the tests are complete.

### windowStore.py
This file contains the `WindowsStoreUpdateTests` class, which includes tests for updating applications from the Microsoft Store. Key methods include:
- `setUpClass()`: Sets up the Appium driver for the Microsoft Store application.
- `tearDownClass()`: Quits the Appium driver.
- `test_update_apps()`: Checks for updates in the Microsoft Store and verifies if the updates are complete.

### windowsUpdate.py
This file contains the `windowsUpdate` class, which includes tests for checking and installing Windows updates. Key methods include:
- `setUpClass()`: Sets up the Appium driver for the Windows update process.
- `tearDownClass()`: Quits the Appium driver.
- `test_open_edge()`: Opens the Windows update window, checks for updates, and installs them if available.

### Edge.py
This file contains the `EdgeTests` class, which includes tests for the Microsoft Edge browser. Key methods include:
- `setUpClass()`: Sets up the Appium driver for the Microsoft Edge browser.
- `tearDownClass()`: Quits the Appium driver.
- `test_open_edge()`: Opens Microsoft Edge using the search functionality.
- `test_update_edge()`: Checks for updates in Microsoft Edge and installs them if available.

## Running the Tests

To run the tests, execute the `run_spec.py` script. This will:
1. Change the directory to the location of the Windows Application Driver.
2. Start the Windows Application Driver.
3. Create and run the test suite.
4. Restart the computer after the tests are complete.
