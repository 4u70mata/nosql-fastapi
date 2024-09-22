
### Endpoints

#### 1. Get Users
- **Endpoint:** `/users`
- **Method:** `GET`
- **Description:** Retrieve a list of users.
- **Response:**
  - **200 OK**: Returns a JSON array of user objects.

#### 2. Create User
- **Endpoint:** `/users`
- **Method:** `POST`
- **Description:** Create a new user.
- **Request Body:**
  ```json
  {
    "name": "string",
    "email": "user@example.com",
    "age": 18,
    "tweets": [
      {
        "content": "string",
        "hashtags": ["string"]
      }
    ]
  }
  ```
- **Response:**
  - **200 OK**: Returns the created user object.
  - **422 Unprocessable Entity**: Validation error if input is invalid.

#### 3. Get User by ID
- **Endpoint:** `/user/{user_id}`
- **Method:** `GET`
- **Description:** Retrieve a user by their ID.
- **Path Parameter:**
  - `user_id`: The ID of the user to retrieve.
- **Response:**
  - **200 OK**: Returns the user object.
  - **422 Unprocessable Entity**: Validation error if the ID is invalid.

## Example Requests

### Get Users
```bash
curl -X 'GET' 'http://127.0.0.1:8000/users' -H 'accept: application/json'
```

### Create User
```bash
curl -X 'POST' 'http://127.0.0.1:8000/users' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "name": "Hamid",
  "email": "Skitiwi@example.com",
  "age": 99,
  "tweets": [
    {
      "content": "Ok",
      "hashtags": [
        "I said Nothing tbh."
      ]
    }
  ]
}'
```

### Get User by ID
```bash
curl -X 'GET' 'http://127.0.0.1:8000/user/66f074351a848bb256c73bf9' -H 'accept: application/json'
```
To add a comprehensive Docker section in your README file, you can break it down into several subsections, including building, running, and using the application with Docker. Here’s an example of how you might structure that section:

### Docker


###### Building the Docker Image
To build the Docker image for the application, run the following command in the root directory of the project:

```bash
docker-compose build
```
###### Running the Application
  
```bash
docker-compose up
```  
This command will start both the web application and the MongoDB service. The application will be accessible at `http://localhost:8000`.
To stop the running services, use:  
```bash  
docker-compose down  
```
The application uses the following environment variable:    
- `MONGO_URI`: Specifies the connection string for the MongoDB service.  
You can customize this in the `docker-compose.yml` file as u wish.  
The application defines several Docker volumes for persistent data storage:  
    
- **mongo-data**: Stores MongoDB data.  
- **app_data**: Stores application data.  
- **app_logs**: Stores application logs.  
  
These volumes ensure that your data persists even when the containers are stopped or removed.  
- The web application runs on port `8000`, which is mapped to port `8000` on your host.
- MongoDB runs on port `27017`, mapped to the same port on your host.