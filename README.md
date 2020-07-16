# Project-Thematic-Investments
Using Python and NLP, predicting stock themes with high potential based on news data

## Summary
* Used news data from 'Naver'
* Gathered meaningful stock themes mentioned in everyday news over the last year
* Gathered 200 news data for each stock theme
* Trained with word2vec model
* Used cosine-similarity to predict theme

## 1. Background
### What is thematic investing?
* Thematic investing is a form of investment which aims to identify macro-level trends, and the underlying investments that stand to benefit from the materialisation of those trends
* A stock theme is a particular group of stocks that share a similar trend or trait

### Hypothesis
1. Individual investers are limited in obtaining information and therfore, rely on the news for such information. As a result, stock themes and the news have a strong correlation.
2. When an event occurs in the news regarding a particular stock theme, some time must pass by for a noticable change to happen for that stock theme's price.
3. If a particular stock theme is mentioned too much in the news, its price will already be affected.

## 2. Data preprocessing
Crawling Naver news data using Beautifulsoup

1. **Stock themes:** Searched stock themes that were frequently mentioned in the news. Removed themes that were fewly referenced or were too specific in its meaning to be useful. A total of 168 themes were finalized. Each theme consists a list of corporations belonging to that theme.
2. **News data:** 200 news data were crawled for each of the 168 themes. Unusable data(photo news, video news) were manually removed from the dataset.

## 3. Model training

**KoBERT tokenizer + Word2Vec + cosine-similarity**

**KoBERT tokenizer:** Developed by SKTBrain\
**Word2Vec:** Represents words in vectors

**Model parameters:**\
vector dimension = 300, window = 8

**Model**
- Added all word vectors in a news data to make a news representation
- Generated each theme representations by adding all 200 news representations
- Normalization was not necessary since more information leads to accurate representations
- When a news data is given as input, the model will vectorize the data and use cosine-similarity to determine and return the most similar theme

## Testing
**Model**
- **Input:** Today news(approximately 2000 data each for IT, economy, society, lifestyle, international, politics)
- **Output:** A list of themes and its subordinate corporations that are considered to have high potential
- The model finds a similar theme for each news data and counts the number of its appearance. However, it only counts when the similarity is higher than 95%.
- When all of the input data is processed, the model generates a list of themes, whose count is less than 5(hypothesis 3).

