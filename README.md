Tools Used : Django web framework, Django Rest Framework

## Installation
1. Download the zip file of this repository.
2. Install the requirements.txt file.
  ```bash
  pip install -r requirements.txt
  ```
3. Run the migrations
  ```bash
  python manage.py makemigrations 
  ```    
  ```bash
  python manage.py migrate
  ```
4. Run server in your localhost
  ```bash
  python manage.py runserver
   ```


## Working
1. To **register** http://localhost:8000/register

    Input format :
    ```json
        "username": "new",
        "email" : "new@mail.com",
        "password" : "pwd"
    ```

2. To login http://localhost:8000/login
      Input format must be
     ``` json
        "username": "new",
        "password" : "pwd"
    ```
3. To retrieve notes - http://localhost:8000/api/notes/
    Output will look something like this:
    ```json
    [
    {
        "id": 1,
        "note": "fds",
        "file": "http://localhost:8000/files/files/download_4.jpg",
        "owner": 1,
        "recipent": [
            2
        ]
    },
    {
        "id": 2,
        "note": null,
        "file": null,
        "owner": 1,
        "recipent": [
            2
        ]
    },
    ]
    ```

4. To create and send notes - http://localhost:8000/api/notes/
    - fill the form and select recipents
    
5. To retrive your inbox - http://localhost:8000/inbox