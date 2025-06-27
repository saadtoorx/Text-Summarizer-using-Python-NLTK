# ✂️ Text Summarizer using Python & NLTK

A simple frequency-based text summarizer built using the Natural Language Toolkit (NLTK). This project takes user input, analyzes sentence importance, and returns a concise summary.

---

## 🧠 About the Project

This beginner-friendly NLP project demonstrates how to extract key information from a block of text by identifying and ranking the most important sentences. It uses classic **word frequency scoring**, filters out stopwords, and generates a meaningful summary using Python’s `nltk` library.

---

## 🚀 Features

* 🔤 Accepts user input directly from the terminal
* 📑 Tokenizes text into words and sentences
* 🚫 Removes English stopwords and non-alphabetic tokens
* 📈 Ranks sentences based on word frequency
* 🧠 Outputs a summary of top `n` sentences (default: 2)
* 📓 Includes a Jupyter notebook for better understanding

---

## 🛠️ Tech Stack

* Python 3.x  
* NLTK  

---

## 📁 Project Structure

```
Text-Summarizer/
├── summarizer.py               # Main Python script
├── summarizer.ipynb            # Jupyter notebook walkthrough
├── README.md                   # Project documentation
├── requirements.txt            # Required Python libraries
```

---

## 💻 How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/saadtoorx/Text-Summarizer.git
cd Text-Summarizer
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Summarizer**

```bash
python summarizer.py
```

4. **Enter your text when prompted**, and get a summary of the top 2 sentences (or change the number manually in code).

---

## 📌 Sample Use

```bash
Enter the text you want to summarize:
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris...

✅ Summary:
The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris. It is named after the engineer Gustave Eiffel.
```

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Made with ✍️ by [@saadtoorx](https://github.com/saadtoorx)  
Feel free to explore, use, and ⭐ the repo if you found it helpful!

