Chat API Service
This project provides a Django-based REST API for generating and storing responses from the llama model using a background ollama subprocess. It includes functionalities for creating chat requests and storing the responses in a database.

Features
Integrates with llama3.2: Uses the ollama command-line tool to run the llama model for generating text responses.
REST API: Built using Django REST Framework, allowing easy creation of chat requests and retrieval of responses.
Database Storage: Stores request and response pairs in a database for future reference.
Filters and Permissions: Uses DjangoFilterBackend and authentication for secured API access.
Requirements
Python 3.8+
Django 4.0+
Django REST Framework
ollama command-line tool installed and accessible in the environment
Installation
Clone the repository:

git clone https://github.com/masih1999-12/django-chat-bot.git
cd django-chat-bot
Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Set up the database:

python manage.py migrate

Run the development server:

python manage.py runserver
API Endpoints
1. Create a Chat Request
Endpoint: POST /api/chats/

Request Body:

json
Copy code
{
  "request_text": "Hello, how are you?"
}
Response:

On Success (201 Created):
json
Copy code
{
  "id": 1,
  "response_text": "I'm just a model, but I'm doing great. How can I help you?"
}
On Failure (400 Bad Request):
json
Copy code
{
  "error": "request_text is required"
}
Project Structure
views.py: Contains the ChatApiView for handling API requests.
model_loader.py: Includes the run_ollama function for running the ollama subprocess.
models.py: Defines the Chat model for storing request and response text.
serializers.py: Serializes the Chat model for API interaction.
Key Files and Code
run_ollama Function
The run_ollama function uses the Python subprocess module to execute the ollama command-line tool for generating responses.

git checkout -b feature-name
Commit your changes:
git commit -m "Description of changes"
Push to the branch:
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Your Name
GitHub | Email
Notes
Ensure ollama is installed and properly configured on your system.
For production, use a WSGI server (e.g., Gunicorn) and configure a proper database backend (mysql).