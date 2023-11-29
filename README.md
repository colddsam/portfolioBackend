
# FastAPI Inttegration for Backend

This is a simple FastAPI project for managing achievements, projects, skills, and events. It provides endpoints to upload and retrieve data related to these categories. The data is stored in a JSON file `website.json`.

## Tech Stack

**Client:** HTML, SCSS, JAVASCRIPT

**Server:** FASTAPI, PYTHON


## Features

### FastAPI App Creation:

- Creates a FastAPI app instance using FastAPI().
### CORS Middleware:

- Adds Cross-Origin Resource Sharing (CORS) middleware to the app using `add_middleware`.
- Allows all origins, credentials, methods, and headers for simplicity.
### JSON File Loading:

- Defines an asynchronous function `load_json()` to load data from a JSON file `(website.json)`.
### Endpoints:

#### Welcome Page:

- Endpoint: ``/
- Method: `POST`
- Returns a welcome message.
#### Achievements:

- Endpoint: `/achievements/`
- Method: `POST`
- Parameters: `header`, `description`, `image`, `url (form parameters)`
- Uploads achievement data to `website.json`.
#### Projects:

- Endpoint: `/projects/`
- Method: `POST`
- Parameters: `header`, `description`, `image`, `url (form parameters)`
- Uploads project data to `website.json`.
#### Skills:

- Endpoint: `/skills/`
- Method: `POST`
- Parameters: `percentage`, `name`, `image`, `url (form parameters)`
- Uploads skill data to `website.json`.
#### Events:

- Endpoint: `/events/`
- Method: `POST`
- Parameters: `description`, `organization`, `image`, `url(form parameters)`
- Uploads event data to `website.json`.
#### Content Retrieval:

- Endpoint: `/content/{prompt}`
- Method: `GET`
- Parameters: `prompt` (path parameter)
- Retrieves content from `website.json` based on the specified category `prompt`.
#### Content Deletion:

- Endpoint: `/delete/{prompt}/{id}`
- Method: `GET`
- Parameters: `prompt`, `id` (path parameters)
- Deletes content from `website.json` based on the specified category prompt and content ID.
### Content Retrieval and Deletion (Commented Out):

- Includes commented-out code for retrieving images and deleting content. The code seems to be using os and FileResponse, but these parts are commented.


## API Reference

#### Upload Achievements

```http
  POST apikey/achievements/
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/achievements/` | `POST` | **header :** Achievement header (string, form) |
||||**description :** Achievement description (string, form)|
||||**image :** Image file for the achievement (string, form)|
||||**url :** URL for additional information (string, form)|

**Description :** Uploads achievement data and saves it to website.json. Returns the updated JSON data.

#### Upload Projects

```http
  POST apikey/projects/
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/skills/` | `POST` | **header :** Project header (string, form) |
||||**description :** Project description (string, form)|
||||**image :** Image file for the Project (string, form)|
||||**url :** URL for additional information (string, form)|

**Description :** Uploads Project data and saves it to website.json. Returns the updated JSON data.

#### Upload Skills

```http
  POST apikey/skills/
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/skills/` | `POST` | **percentage :** Skill proficiency percentage (float, form) |
||||**name :** Skills description (string, form)|
||||**image :** Image file for the skills (string, form)|
||||**url :** URL for additional information (string, form)|

**Description :** Uploads skills data and saves it to website.json. Returns the updated JSON data.

#### Upload Events

```http
  POST apikey/events/
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/events/` | `POST` | **description :** Event description (string, form) |
||||**organization :** Event organization (string, form)|
||||**image :** Image file for the event (string, form)|
||||**url :** URL for additional information (string, form)|

**Description :** Uploads events data and saves it to website.json. Returns the updated JSON data.

#### Get Content

```http
  GET apikey/content/{prompt}
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/content/{prompt}` | `GET` | **prompt :** Category prompt (string, path) |

**Description :** Retrieves content from website.json based on the specified category prompt.

#### Delete Content

```http
  GET apikey/delete/{prompt}/{id}
```

| Endpoint | Method| Parameters|
| :-------- | :------- | :---- |
| `/achievements/` | `GET` | **prompt :** Category prompt (string, path) |
||||**id :** Content ID to be deleted (integer, path)|

**Description :** Deletes content from website.json based on the specified category prompt and content ID. Returns a status message.
## Running Tests

Install the required dependencies using the following command:

```bash
  pip install fastapi[all] uvicorn
```

Run the application using the following command:

```bash
  uvicorn your_app_name:app --reload
```
Replace **your_app_name** with the name of the Python file containing your FastAPI app.


## Authors

- [@colddsam](https://www.github.com/colddsam)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at colddsam@gmail.com

