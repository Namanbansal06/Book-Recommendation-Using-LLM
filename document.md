# Approach and Reasoning for Book Recommendation Service

### Why I Chose This Approach :
#### FastAPI: 
It is mordern and fast way to create api. It is also simple and user friendly interface which makes it suitable for web services quickly.

#### Hugging Face Transformers:
It provides a wide range of pre trained models. we can leverage advanced text generation capabilities without needing to train models from scratch. It is also very flexible to use.Integrating Hugging Face transformers with FastAPI is straightforward, allowing us to build sophisticated services quickly.

I used model = "distlgpt2" which is a good open ai with high performance and it is free to use. It is version of gpt-2.

#### get_top_100_books(genre):
This gives the dummy data of 100 books which is being used to create a Book recommendation model.

#### get_top_10_books(books): 
This returns the top 10 books from top 100 books based on their ratings.

#### get_one_book(books, preference_title):
Generate a recommendation based on user preference using a text generation model.

#### close-book:
This ends the search with a "Thanks Note"

### Text Generation Approach :

#### Prompt Construction: 
The prompt for the text generation model includes the list of books and asks the model to identify the one most similar to the user's preference. Constructing a clear and specific prompt helps the model generate accurate and relevant responses.

#### Post-Processing: 
After generating the text, the response is analyzed to extract the recommended book. Post-processing ensures that the final recommendation is correctly interpreted and matches the user's preference.

### Error Handling
#### Exception Handling: 
Each endpoint includes try-except blocks to handle potential errors gracefully.The error messages improves the user experience and helps in diagnosing issues during development and production.

### Streamlit App:
I created a web app to easily check the Book Recommendation System, It is a very user friendly app and can be understand by user. 
It is easy to build and enhances the code readiblity.

## Conclusion

The chosen approach combines the strengths of FastAPI and Hugging Face transformers to create a robust, efficient, and user-friendly book recommendation service. By leveraging state-of-the-art NLP models and a high-performance web framework, we can provide personalized and high-quality recommendations to users. This approach is scalable, flexible, and easy to maintain, making it an excellent choice for building modern web services.