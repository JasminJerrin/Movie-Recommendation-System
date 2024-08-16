Recommendation systems are essential tools for digital platforms, helping users navigate vast amounts of content by offering personalized suggestions. 
By analyzing user behavior, these systems predict and display items tailored to individual preferences, enhancing user experience and driving engagement. 
They are crucial for companies like Netflix and Amazon, where dynamic, accurate recommendations significantly influence what users see and choose.
It is a simple movie recommendation system based on user preferences and provide recommendations via
a Flask API.This project leverages collaborative filtering, a popular recommendation technique, to provide personalized movie recommendations.
Dataset:The dataset is from the MovieLens dataset collected by the GroupLens Research Project at the University of Minnesota.
It has 3 dataset files, u.data, u.item, u.genre
Technologies Used:
• Python (NumPy, pandas)
• Flask (for API development)
• JSON (for data exchange)

Run command: python main.py
Postman API call 
Type : POST 
URL:http://localhost:5000/recommend
Body(RAW -Json format):
{
    "user_id": 100,
    "user_data": [
        {
            "movie_id": 1,
            "rating": 5
        },
        {
            "movie_id": 2,
            "rating": 4
        }
    ],
    "movies": [
        {
            "movie_id": 1,
            "title": "Movie A"
        },
        {
            "movie_id": 2,
            "title": "Movie B"
        },
        {
            "movie_id": 3,
            "title": "Movie C"
        }
    ],
    "num_recommendations": 5
}



