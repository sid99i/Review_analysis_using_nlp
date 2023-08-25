# Restaurant Review Sentiment Analysis

Welcome to the repository containing Python code for sentiment analysis on restaurant reviews. This project analyzes restaurant reviews using natural language processing (NLP) techniques to determine the sentiment expressed in each review.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Example](#example)
- [Contributing](#contributing)

## Introduction
This repository demonstrates sentiment analysis on restaurant reviews using the Natural Language Toolkit (NLTK) library. It preprocesses and cleans the data, then trains a Naive Bayes classifier on a labeled dataset of restaurant reviews to predict the sentiment of new reviews.

## Features
- **Sentiment Analysis:** The code employs a Naive Bayes classifier to predict the sentiment (positive/negative) of restaurant reviews based on their text content.
- **Data Preprocessing:** The script uses NLTK for text preprocessing, including lowercasing, stemming, and removing stopwords.
- **Model Saving:** After training, the Naive Bayes model is saved to a file using the `pickle` library.
- **Interactive Testing:** The code provides an example of testing the trained model with new reviews.

## Usage
1. Clone or download the repository.
2. Run the Python script in your preferred environment.
3. View the sentiment predictions for the new reviews provided in the script.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/restaurant-review-sentiment-analysis.git
   ```
2. Navigate to the project directory:
   ```sh
   cd restaurant-review-sentiment-analysis
   ```
3. Run the Python script:
   ```sh
   python sentiment_analysis.py
   ```

## Example
1. Run the `sentiment_analysis.py` script.
2. Observe the sentiment predictions for the new restaurant reviews provided in the script.

## Contributing
Contributions are welcome! Feel free to enhance the features or fix any issues by creating a pull request.

---

*Note: This README provides an overview of the code's functionality and usage. For detailed implementation, please refer to the source code in `review_analysis_using_nlp1.py`.*
