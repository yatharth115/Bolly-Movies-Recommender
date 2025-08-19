import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load dataset
@st.cache_data
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "movies.csv")
    df = pd.read_csv(file_path)

    # Make sure all required columns exist
    for col in ["title", "genre", "actors", "director", "description"]:
        if col not in df.columns:
            df[col] = ""   # create empty column if missing

    # Create 'tags' column by combining text info
    df["tags"] = (
        df["genre"].astype(str) + " " +
        df["actors"].astype(str) + " " +
        df["director"].astype(str) + " " +
        df["description"].astype(str)
    )

    return df

# Recommendation function
def recommend(movie, df, similarity):
    if movie not in df['title'].values:
        return ["Movie not found in database."]
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [df.iloc[i[0]].title for i in movie_list]

# Streamlit app
def main():
    st.title("🎬 Bollywood Movie Recommender System")
    st.write("Get personalized Bollywood movie recommendations based on your favorite movie!")

    df = load_data()

    # Feature extraction
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(df['tags']).toarray()
    similarity = cosine_similarity(vectors)

    # Movie selection
    movie_list = df['title'].values
    selected_movie = st.selectbox("Choose a movie you like:", movie_list)

    if st.button("Recommend"):
        recommendations = recommend(selected_movie, df, similarity)
        st.write("### Recommended Movies:")
        for rec in recommendations:
            st.write(f"- {rec}")

if __name__ == '__main__':
    main()
