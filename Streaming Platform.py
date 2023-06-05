@app.route('/movies/<movie_id>/play', methods=['GET'])
def play_movie(movie_id):
    # Retrieve movie file path or URL from the database
    # Implement logic to stream the movie to the user
    return jsonify({'message': 'Streaming movie...'})
