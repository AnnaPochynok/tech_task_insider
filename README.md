Description
---
Automated UI and API tests as tech tasks

    .
    ├── data                    # Various data files that are used for tests
    │   ├── constants           # Test data that are used in tests
    ├── src                     # Test framework source files with tests implementation
    │   ├── api                 # API tests source files
    │   └── ui                  # UI tests source files
    ├── tests                   # test files
    │   ├── api                 # API tests
    │   └── ui                  # UI tests
    ├── conftest.py             # Fixture files related to all test types
    ├── README.md               # Project description
    └── requirements.txt        # Project related packages

---
Prepare local environment
---
* Install and setup virtualenv for the project:
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```
* Install all packages required for the tests run:
```shell
pip install -r requirements.txt
```
----
Same actions you can de within PyCharm IDE via UI with hints

Running tests locally
---
Once the environment is ready the tests can be executed. Run the following command to do so:
```shell
pytest tests
```
Run tests in a Chrome:
```shell
pytest tests --browser chrome
```
Run tests in a Firefox:
```shell
pytest tests --browser firefox
```