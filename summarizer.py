#Importing necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

#Downloading Stopwords. (Only needed once, if code need to be run agin comment it)
nltk.download("stopwords") 
nltk.download("punkt")

#Function generating frequency based summary
def summerize_text(text, num_sentences = 2): #The default value of num_Sentences is set to 2

    #Tokenize text into sentences and words
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    #Filter out stopwords and non-alphabetic words
    stop_words = set(stopwords.words("english"))
    word_frequencies = {}

    for word in words:
        if word.isalpha() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0 ) + 1
    
    #Score each sentence based on word frequency
    sentence_score = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_score[sentence] = sentence_score.get(sentence, 0) + word_frequencies[word]
 
    #Sort sentences by score and select the top 'num_sentences'
    summary_sentences = sorted(sentence_score, key=sentence_score.get, reverse=True)[:num_sentences]
    summary = " ".join(summary_sentences)
    return summary

# Get user input
user_text = input("Enter the text you want to summarize:\n")

# Generate and print summary
summary = summerize_text(user_text, num_sentences=2)

print("\n✅ Summary:\n", summary)