# 🎬 Bollywood Movie Recommender System  

A simple **AI/ML project** that recommends Bollywood movies based on user choice.  
This project uses **Content-Based Filtering** with **NLP techniques** to find similar movies.  

---

## 🚀 Features
- Enter your favorite Bollywood movie and get **5 similar movie recommendations**.  
- Uses **CountVectorizer** + **Cosine Similarity** for recommendations.  
- Built with **Python, Scikit-learn, Pandas, and Streamlit**.  
- Beginner-friendly project (easy to understand & run).  

---

## 📂 Project Structure
Bolly-Movie-Recommender

│── app.py # Main Streamlit app

│── movies.csv # Dataset file

│── README.md # Project documentation

│── requirements.txt # Dependencies


---

## 📊 Dataset
The project uses a `movies.csv` file containing Bollywood movies.  
At minimum, the dataset should have these columns:  

- `title` → Movie name  
- `genre` → Genres of the movie  
- `actors` → Main actors  
- `director` → Movie director  
- `description` → Short storyline/overview  

Example row:  

| title        | genre    | actors                 | director     | description                          |
|--------------|---------|-------------------------|--------------|--------------------------------------|
| Kabir Singh  | Romance | Shahid Kapoor, Kiara A  | Sandeep Reddy | A surgeon goes into self-destruction |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
    git clone https://github.com/your-username/Bolly-Movie-Recommender.git
    cd Bolly-Movie-Recommender

### 2. Create virtual environment
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Run the app in folder's terminal
    streamlit run app.py

## 📦 requirements.txt

    Here’s a sample requirements.txt for this project:
    streamlit
    pandas
    scikit-learn

##🎯 How It Works

The dataset is loaded from movies.csv.

A tags column is created by combining genre + actors + director + description.

CountVectorizer converts tags into numerical vectors.

Cosine Similarity measures similarity between movies.

User selects a movie → top 5 similar movies are recommended.



## 🖥️ Demo Screenshot

<img width="1787" height="857" alt="Screenshot 2025-08-19 161044" src="https://github.com/user-attachments/assets/325f9442-5d96-4847-9b93-bc7078e9d246" />



## 👨‍💻 Author

Yatharth Joshi

GitHub: https://github.com/yatharth115

LinkedIn: https://www.linkedin.com/in/yatharth1704






