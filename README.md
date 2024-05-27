# Smart-Application-tracking-System
This Smart ATS helps to find the similarity between the given Job description and gives smart yet informative data about the sibmitted resume

# Smart ATS System

This project is a Smart Applicant Tracking System (ATS) that leverages Large Language Models (LLM) and the Google Gemini API to provide advanced features for managing and analyzing job applications.

## Features

- **Resume Parsing:** Automatically extracts key information from resumes.
- **Job Matching:** Matches applicants to the most suitable job openings.
- **Application Tracking:** Keeps track of the status of each application.
- **Reporting and Analytics:** Generates insightful reports on the hiring process.

## Setup Instructions
Activating the Environment
Activate the newly created environment using:

conda activate ./venv

Installing Dependencies
Install the required Python packages using pip:

pip install -r requirement.txt

Configuration:

1.Environment Variables: Create a .env file in the root directory of the project. This file should contain your configuration details such as API keys. Example:

  GOOGLE_API_KEY=your_google_gemini_api_key_here

2.Update Configuration File: Ensure your app.py or other configuration files reference these environment variables as needed.

Running the Application
To start the application, run the following command:

 python app.py

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html)
- Python 3.10

### Creating the Environment

To create a conda environment for this project, run the following command:

```bash
conda create -p venv python==3.10 -y

 

