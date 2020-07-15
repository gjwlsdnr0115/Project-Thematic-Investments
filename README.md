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

## 2. Data crawling
Crawling Naver news data using Beautifulsoup

1. **Stock themes:** Searched stock themes that were frequently mentioned in the news. Removed themes that were fewly referenced or were too specific in its meaning to be useful
