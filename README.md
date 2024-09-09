# Azure Pipeline for a Simple Python Application

## Repository Content:
1. <b>app.py:</b>
This is the main Python script, a simple function that adds two numbers.
2. <b>test_app.py: </b>
This is a test script for app.py that uses pytest to check if the add function works correctly.
3. <b>requirements.txt:</b>
This file lists the required dependencies for the project. For this example, we need pytest for running the tests.
4. <b>setup.py (optional for packaging):</b>
If you want to package the Python project, you can create a setup.py file. This file is useful if you are distributing your code as a Python package.
5. <b>azure-pipelines.yml:</b>
This is the starter pipeline created using the pre-built template in the Azure DevOps portal.
6. <b>azure-pipelines-ci.yml:</b>
This is the pipeline configured to build, test, and package the python application.