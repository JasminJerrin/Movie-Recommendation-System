from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved model
with open('recommendation_model.pkl', 'rb') as f:
    model_components = pickle.load(f)

U = model_components['U']
sigma = model_components['sigma']
Vt = model_components['Vt']
ratings_mean = model_components['ratings_mean']
mtrx_df_columns = model_components['mtrx_df_columns']

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.json['user_id'])
    num_recommendations = int(request.json.get('num_recommendations', 5))

    # Reconstruct the predicted ratings
    all_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + ratings_mean.reshape(-1, 1)
    preds_df = pd.DataFrame(all_predicted_ratings, columns=mtrx_df_columns)

    # Get the user's predictions sorted
    user_row_number = user_id - 1
    sorted_user_predictions = preds_df.iloc[user_row_number].sort_values(ascending=False)

    # Assuming you pass the rated movies as part of the request
    user_data = request.json['user_data']  # Example: [{'movie_id': 1, 'rating': 5}, ...]
    user_rated_movies = [item['movie_id'] for item in user_data]

    # Example: this should come from your database or another source
    movies_df = pd.DataFrame(request.json['movies'])  # Example: [{'movie_id': 1, 'title': 'Movie A'}, ...]

    # Filter out already rated movies
    recommendations = (movies_df[~movies_df['movie_id'].isin(user_rated_movies)]
                       .merge(pd.DataFrame(sorted_user_predictions).reset_index(), how='left', left_on='movie_id', right_on='movie_id')
                       .rename(columns={user_row_number: 'Predictions'})
                       .sort_values('Predictions', ascending=False)
                       .iloc[:num_recommendations, :-1])

    # Convert the DataFrame to a list of dictionaries for JSON response
    recommendations_list = recommendations.to_dict('records')

    return jsonify(recommendations_list)

if __name__ == '__main__':
    app.run(debug=True)
