# A Toy Browser Fingerprinting Tool

## Project Description
This project is a toy web browser fingerprinting tool that helps understand the basic concepts of web browser fingerprinting. It collects a small number of attributes from the user's browser and generates a unique fingerprint using sha-256.

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/OmarDayili/A-Toy-Browser-Fingerprinting-Tool.git
    cd A-Toy-Browser-Fingerprinting-Tool
    ```


2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Run the Flask application:
    ```bash
    python app.py
    ```
    or

   ```bash
   flask run
   ```

3. Open your web browser and navigate to `http://127.0.0.1:5000`.

4. Click on "Get Fingerprint" to see the generated unique fingerprint and the browser attributes used.

## Explanation
- `app.py`: The main Flask application file.
- `templates/index.html`: The homepage with a button to trigger fingerprinting.
- `templates/result.html`: The result page displaying the fingerprint and browser attributes.
- `static/styles.css`: Basic CSS styling for the HTML pages.
- `requirements.txt`: List of Python packages required for the project.

## License
This project is licensed under the MIT License.
