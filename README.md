# EAI-Manufacture-Finance

## Usage
1. Clone this repository: ```$ git clone https://github.com/sonadztux/EAI-Manufacture-Finance.git```
2. Go to the repository folder
3. Create python3 virtual environment: ```$ python3 -m venv env```
4. Activate the virtual environment: ```$ source env/bin/activate```
5. Run the following command to install dependencies:
    ```$(env) pip install -U pip
    $(env) pip install -r requirements.txt
6. Edit .env file configuration
8. Run the following command to initiate and migrate the database models:
    ```$(env) flask db init
    $(env) flask db migrate
    $(env) flask db upgrade
9. Run the application: ```$(env) flask run```