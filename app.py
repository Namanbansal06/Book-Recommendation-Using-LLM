import streamlit as st
import requests

# FastAPI service URL
BASE_URL = "http://localhost:8000"  # Adjust this if your FastAPI service is hosted elsewhere

# Streamlit app title
st.title("Book Recommendation Service")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")

# Function to get top 100 books
def get_top_100_books(genre):
    response = requests.post(f"{BASE_URL}/top-100-books/", json={"genre": genre})
    if response.status_code == 200:
        return response.json()["books"]
    else:
        st.error("Error fetching top 100 books")
        return []

# Function to get top 10 books
def get_top_10_books(genre):
    response = requests.post(f"{BASE_URL}/top-10-books/", json={"genre": genre})
    if response.status_code == 200:
        return response.json()["top_10_books"]
    else:
        st.error("Error fetching top 10 books")
        return []

# Function to get one book recommendation
def get_one_book(genre, preference):
    response = requests.post(f"{BASE_URL}/get-one-book/", json={"genre": genre, "preference": preference})
    if response.status_code == 200:
        return response.json()["book"]
    else:
        st.error("Error fetching book recommendation")
        return None

# User input for genre
genre = st.sidebar.text_input("Genre", "fiction")

# Fetch and display top 100 books
st.subheader("Top 100 Books")
if st.button("Get Top 100 Books"):
    books = get_top_100_books(genre)
    for book in books:
        st.write(f"{book['title']} (Rating: {book['rating']})")

# Fetch and display top 10 books
st.subheader("Top 10 Books")
if st.button("Get Top 10 Books"):
    top_10_books = get_top_10_books(genre)
    for book in top_10_books:
        st.write(f"{book['title']} (Rating: {book['rating']})")

# User input for book preference
st.subheader("Get Book Recommendation")
preference = st.text_input("Book Preference", "Book 1")

# Fetch and display one book recommendation
if st.button("Get Book Recommendation"):
    recommended_book = get_one_book(genre, preference)
    if recommended_book:
        st.write(f"Recommended Book: {recommended_book['title']} (Rating: {recommended_book['rating']})")

# Closing message
st.subheader("Close Task")
if st.button("Close Task"):
    response = requests.get(f"{BASE_URL}/close-task/")
    if response.status_code == 200:
        st.write(response.json()["message"])
    else:
        st.error("Error closing task")
