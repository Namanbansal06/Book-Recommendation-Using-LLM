from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, set_seed
import os
import random

# Initialize FastAPI app
app = FastAPI()

# Set up Hugging Face transformers pipeline
model_name = "distilgpt2"
set_seed(42)
text_generator = pipeline('text-generation', model=model_name)

class BookRequest(BaseModel):
    genre: str
    preference: str = None

def generate_random_rating():
    return round(random.uniform(4.0, 5.0), 1)


# Dummy data function
def get_top_100_books(genre):
    books = [
        {"title": f"Book {i}", "genre": genre, "rating": 5 - (i % 5) * 0.1}
        for i in range(1, 101)
    ]
    return books

def get_top_10_books(books):
    sorted_books = sorted(books, key=lambda x: x["rating"], reverse=True)
    return sorted_books[:10]

def get_one_book(books, preference_title):
    # Construct the prompt
    prompt = f"From the following list of books, which one is most similar to '{preference_title}'?\n\n"
    for book in books:
        prompt += f"{book['title']}\n"
    prompt += "Answer:"


    print("Prompt: ", prompt)  # Debug: Print the prompt

    try:
        # Generate the response
        response = text_generator(prompt, max_new_tokens=50, num_return_sequences=1)
        generated_text = response[0]['generated_text']
        print("Generated Text: ", generated_text)

        if "Answer:" in generated_text:
            recommendation = generated_text.split("Answer:")[1].strip()
            ls = generated_text.split("\n")
            # print(type(ls))
            for i in ls:
                if preference_title == i:
                    recommendation= preference_title
                    print(i)
                    # return recommendation
        else:
            recommendation = ""

        print("Recommendation: ", recommendation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating book recommendation: {str(e)}")

    # Post-process the recommendation to find a matching book
    recommended_book = next((book for book in books if recommendation.lower() in book["title"].lower()), None)

    # If no match is found, default to the first book
    if not recommended_book:
        recommended_book = books[0]

    print("Selected Book: ", recommended_book["title"])
    return recommended_book


@app.post("/top-100-books/")
def top_100_books(request: BookRequest):
    try:
        books = get_top_100_books(request.genre)
        return {"books": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top 100 books: {str(e)}")

@app.post("/top-10-books/")
def top_10_books(request: BookRequest):
    try:
        books = get_top_100_books(request.genre)
        top_10 = get_top_10_books(books)
        return {"top_10_books": top_10}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching top 10 books: {str(e)}")

@app.post("/get-one-book/")
def one_book(request: BookRequest):
    try:
        books = get_top_100_books(request.genre)
        top_10 = get_top_10_books(books)
        book = get_one_book(top_10, request.preference)
        return {"book": book}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching one book: {str(e)}")

@app.get("/close-task/")
def close():
    return {"message": "Thank you for using the book recommendation service!"}

