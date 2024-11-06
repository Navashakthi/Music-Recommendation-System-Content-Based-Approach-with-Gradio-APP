# Music Recommendation System using Content Based Features 🎶

This project builds a music recommendation system that can suggest similar music of users choice of track implemented with Content-Based-Features and Gradio App using machine learning techniques on a dataset containing various audio features for songs. It provides song recommendations based on input song names, using Gradio to create an interactive app.

## Project Overview

- **Data Source**: Audio feature dataset containing information such as `valence`, `acousticness`, `danceability`, `duration_ms`, `energy`, and more.
- **Recommendation Approach**: Content-based recommendations using FAISS for efficient similarity search.
- **Deployment**: The Gradio app allows users to input a song and get recommendations based on similar songs.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
[git clone https://github.com/Navashakthi/music-recommendation-system.git
cd music-recommendation-system](https://github.com/Navashakthi/Music-Recommendation-System-Content-Based-Approach-with-Gradio-APP.git)
```

### 2. Execute music_recommendation.ipynb

Place your dataset link in the placeholder of downloading it as zip file. Ensure it includes the following fields:

- **Audio Features**: `valence`, `acousticness`, `danceability`, `duration_ms`, `energy`, `instrumentalness`, `liveness`, `loudness`, `speechiness`, `tempo`, etc.
- **Identifiers**: `name`, `artists`, `id`, `release_date`, etc.

### 3. Install Requirements

This project requires Python 3.7+ and the dependencies listed in `requirements.txt`. To install them:

```bash
pip install -r requirements.txt
```

**Note**: FAISS is not available on PyPI, so if you encounter issues installing it, install the appropriate version directly:

- For **CPU-only** environment:
  ```bash
  pip install faiss-cpu
  ```
- For **GPU environment** (if using Google Colab with GPU):
  ```bash
  pip install faiss-gpu
  ```

### 4. Preprocessing and EDA

Use the `music_recommendation.ipynb` notebook for data preprocessing and exploratory data analysis (EDA).

- **Preprocessing**: Prepare the dataset by normalizing or standardizing audio features and handling missing values.
- **EDA**: Explore data distributions, relationships between features, and other insights.

### 5. Running the Gradio App

The Gradio app (`app.py`) lets users input a song name and receive song recommendations.

#### To run the app:

1. From your terminal, navigate to the project directory:

    ```bash
    cd music-recommendation-system
    ```

2. Run the Gradio app:

    ```bash
    python app.py
    ```

3. The terminal will output a local URL. Open this URL in your browser to access the app.

#### Example Usage:

```bash
python app.py
```

Example Gradio output:

```plaintext
Running on local URL: http://localhost:7860
Running on public URL: https://xxxxx.gradio.app
```

Visit the link to access the app similar to the below output.

![Screenshot 2024-11-06 at 12 38 12 PM](https://github.com/user-attachments/assets/60dc80f9-9295-406d-9364-754f5cf80ac8)

##### Sample input songs for testing:
    -Danny Boy
    -Up And Down
    -Not Alone
    *Note: The inputs are case-sensitive


## Repository Contents

- **app.py**: Code for running the Gradio app.
- **music_recommendation.ipynb**: Jupyter notebook for preprocessing, EDA, and implementing the recommendation function.
- **requirements.txt**: Required Python packages.

## Troubleshooting

- **FAISS Installation Issues**: Follow the instructions above to install either `faiss-cpu` or `faiss-gpu` depending on your environment.
- **Gradio Public Link Not Working**: Ensure you’re setting `share=True` in `launch()` to get a public link.

## License

This project is open-source and available under the MIT License.

---

This README provides a full guide for setting up, running, and using your music recommendation system. Let me know if there are additional details you would like included!

### Sample Output

