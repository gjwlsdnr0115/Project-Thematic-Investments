# Project-Thematic-Investments
Using Python and NLP, predicting stock themes with high potential based on news data

## Summary
* Used news data from 'Naver'
* Finialized 168 meaningful stock themes mentioned in everyday news over the last year
* Gathered 200 news data for each stock theme
* Train word2vec model
* Used cosine-similarity to predict theme

## 1. Background
### What is thematic investing?
* Thematic investing is a form of investment which aims to identify macro-level trends, and the underlying investments that stand to benefit from the materialisation of those trends
* A stock theme is a particular group of stocks that share a similar trend or trait

### Hypothesis
1. Individual investers are limited in obtaining information and therfore, rely on the news for such information. As a result, stock themes and the news have a strong correlation.
2. When an event occurs in the news about a particular stock theme, a certain amount of time must pass by for a noticable change to happen regarding the stock theme's price.
