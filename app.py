import pandas as pd
import numpy as np
import faiss
import gradio as gr

# Loading dataset
data = pd.read_csv("/content/musicRec/data/data.csv")  # Replace with your actual file path

# Specify the numerical columns used for recommendations
num_cols = ['valence', 'acousticness', 'danceability', 'duration_ms',
            'energy', 'instrumentalness', 'liveness',
            'loudness', 'speechiness', 'tempo']  # Adjust as needed

# Preprocessing the data
data_processed = data[num_cols]

# Converting data to numpy array
data_array = data_processed.values.astype('float32')  # FAISS requires float32

# Creating the FAISS index
index = faiss.IndexFlatL2(data_array.shape[1])  # L2 distance
index.add(data_array)  # Add data to the index

# Defining the recommendation function
def recommend_songs_faiss(song_name, top_n=5):
    # Check if the song exists in the dataset
    if song_name not in data['name'].values:
        return f"Song '{song_name}' not found in the dataset."

    # Getting the index of the song in the dataset
    song_idx = data[data['name'] == song_name].index[0]
    song_vector = data_array[song_idx].reshape(1, -1)

    # Searching for nearest neighbors
    _, indices = index.search(song_vector, top_n + 1)  # Get top_n + 1 because the first is the song itself
    song_indices = indices[0][1:]  # Exclude the input song

    # Getting recommended song names and artists
    recommended_songs = [(data.iloc[i]['name'], data.iloc[i]['artists']) for i in song_indices]
    return recommended_songs

# Gradio interface function
def gradio_interface(song_name):
    recommendations = recommend_songs_faiss(song_name)

    if isinstance(recommendations, str):  # Check if the recommendation is an error message
        return recommendations

    # Creating a new DataFrame from the recommendations
    recommendations_df = pd.DataFrame(recommendations, columns=["Song Name", "Artists"])
    return recommendations_df  # Return the DataFrame

# Creating the Gradio interface
iface = gr.Interface(
    fn=gradio_interface,
    inputs=gr.Textbox(label="Enter a Song Name"),
    outputs=gr.Dataframe(label="Recommended Songs",  headers=["Song Name", "Artists"]),
    title="Music Recommendation System",
    description="Enter the name of a song to get similar song recommendations based on audio features."
)

# Launching the Gradio app
if __name__ == "__main__":
    iface.launch(share=True)
