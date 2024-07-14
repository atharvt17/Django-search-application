# Django-search-application
Admin-template based Django search application that can search through the names of dishes and recommend the best match for the same.

## Description

The Dish Search Project is a Django-based web application designed to allow users to search for dishes offered by various restaurants. The project uses fuzzy string matching to handle potential spelling errors in search queries, ensuring accurate and relevant search results. Additionally, the project leverages caching mechanisms to enhance search performance.

![Image6](https://github.com/atharvt17/Django-search-application/blob/main/images/image6.png)

## Features

- **Search for Dishes:** Users can search for dishes using a search bar.
- **Fuzzy Matching:** The application uses fuzzy string matching to account for spelling errors and return the closest matching results.
- **Sort by Rating:** Search results are sorted based on the restaurant's aggregate rating, with higher-rated restaurants appearing first.
- **Caching:** The application employs caching to speed up repeated searches and reduce database load.

## How It Works

### Search Functionality

1. Users enter a query in the search bar and submit the form.
2. The query is processed using fuzzy string matching to find the closest matches to the dish names stored in the database.
3. The matched dish names are then used to query the database for the corresponding dishes.
4. The search results are sorted by the restaurant's aggregate rating and displayed to the user.

### Handling Spelling Errors

The project uses the `fuzzywuzzy` library to handle potential spelling errors in user queries. The fuzzy matching process works as follows:

1. Extract all dish names from the database.
2. Use `fuzzywuzzy.process.extract` to find the closest matches to the user's query.
3. Filter matches with a confidence score above a certain threshold (e.g., 50%).
4. Retrieve the dishes corresponding to the matched names from the database.

### Caching Mechanism

To improve search performance, the application employs a caching mechanism using Django's caching framework. Here's how caching is implemented:

1. When a user submits a search query, the application first checks if the results for that query are already cached.
2. If cached results are found, they are returned immediately, reducing the need for database queries and speeding up the response time.
3. If no cached results are found, the application performs the fuzzy matching and database query, then caches the results for future use.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/atharvt17/Django-search-application
   ```
2. **Navigate to the Directory**:
   ```bash
   cd dishsearch
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Load the initial data from the CSV file**:
   ```bash
   python manage.py load_dishes restaurants_small.csv
   ```
6. **Run the development server:**:
   ```bash
   python manage.py runserver
   ```
7. **Access the application in your web browser**:
   ```bash
   http://127.0.0.1:8000/search/
   ```
