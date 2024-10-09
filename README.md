# Exploratory Data Analysis (EDA) for Twitter Sentimental Analysis Dataset


Project title: Exploratory Data Analysis of Twitter Sentiment: Understanding Public Opinion through Text Mining

Objective: The primary goal of this project is to perform an exploratory data analysis (EDA) on the Twitter Sentiment Analysis dataset to uncover patterns, trends, and insights related to public opinion. By analyzing various features such as tweet length, sentiment distribution, and word frequency, we aim to understand the factors that influence sentiment in tweets and identify key terms and trends that reflect public emotions and opinions on specific topics

Dataset: Training Dataset, Validation Dataset

Training Dataset:
It contains information related to tweets and their respective sentiment tag. The columns identified are:

ID (2401): This appears to be a unique identifier for each tweet.
Platform (Borderlands): Platform or topic related to the tweet.
Sentiment (Positive): Tweet sentiment rating (e.g. "Positive").
Text: The content or text of the tweet.

Validation Dataset:
It is similar to the training dataset, with the following columns:

ID (3364): A unique identifier for each tweet.
Platform (Facebook): Platform or topic related to the tweet.
Sentiment (Irrelevant): Sentiment classification of the tweet (e.g. "Irrelevant").
Text: The content or text of the tweet.
Example of Dataset Description:
Dataset: The Twitter Sentiment Analysis Dataset contains information related to sentiment analysis in tweets, organized in the following columns:

ID: Unique identifier for each tweet.
Platform: Platform or topic the tweet is about (e.g., Borderlands, Facebook, Microsoft).
Sentiment: Sentiment label associated with the tweet, which can be:
Positive
Negative
Neutral
Irrelevant
Text: Content of the tweet, where the user's opinion or comment is expressed

Methodology 

1.- Data Collection and Preparation 
Loading dataset from Twitter Training and and Validation data, using Python Library Pandas as pd: 

<img width="657" alt="Screenshot 2024-09-13 at 22 51 45" src="https://github.com/user-attachments/assets/05baae39-d017-4351-8aa9-f2e0979c7cac">

Primary cleaning renaming columns for clarity, checking missing values and removing rows with missing text, then preview the first few rows and checking.

<img width="660" alt="Screenshot 2024-09-13 at 22 53 43" src="https://github.com/user-attachments/assets/21109b47-e14a-407c-a86f-6ceeea52e91d">

<img width="613" alt="Screenshot 2024-09-13 at 22 54 10" src="https://github.com/user-attachments/assets/6201568c-28c9-4e76-8e1d-9abca4dba696">

2.- Descriptive Analysis
This code performs descriptive statistics analysis on the tweets dataset. Specifically, it performs three main tasks: Tweet length calculation: Create a new column containing the number of characters in each tweet. Descriptive statistics: Generates a statistical summary of the length of the tweets (including the total number, mean, median, and minimum and maximum values). Sentiment Tag Distribution: Shows the frequency of each sentiment category (how many tweets are positive, negative, neutral, etc.).
This analysis provides an overview on the length of tweets and the distribution of sentiments in the data set.

<img width="546" alt="Screenshot 2024-09-13 at 23 00 14" src="https://github.com/user-attachments/assets/cdf68be1-aae3-4317-92de-89be601a2630">

<img width="556" alt="Screenshot 2024-09-13 at 23 00 37" src="https://github.com/user-attachments/assets/d70237d3-5c2b-424c-ac01-2504cf260dda">

3.- Data visualization 
Using python library seaborn, matplotlib for chart, bloxplot and historigram, this visualization approach allows you to identify patterns and differences between platforms and the way users interact with them. Improvements could be suggested on platforms that display a large number of negative or neutral tweets, and explore how to encourage more positive interactions between users.

Bar Charts: Show the distribution of sentiment across different platforms.

First Bar Chart which is realted to the distribution of sentiments only on tweet, which prioritizes the number of negative comments according to the dataset sample.

<img width="557" alt="Screenshot 2024-09-13 at 23 17 31" src="https://github.com/user-attachments/assets/b6315918-c73f-4ba6-ac9a-bf9871daf818">


The bar chart reveals significant differences in how sentiments are distributed across various platforms:
Facebook: This platform has a higher proportion of Neutral tweets compared to others. This could indicate that users on Facebook tend to share more informational or balanced content.
Twitter: There is a noticeable balance between Positive and Negative tweets, suggesting that this platform fosters more polarized opinions.
Microsoft and CS: These platforms see a predominance of Negative tweets, which may reflect user dissatisfaction or frustration with specific products or services related to those platforms.
Google: Similar to CS and Microsoft, Google also shows a relatively high proportion of Negative sentiment, which might indicate challenges or criticisms faced by users.

<img width="542" alt="Screenshot 2024-09-13 at 23 13 21" src="https://github.com/user-attachments/assets/a5f3d4b4-0372-4423-96d2-e1455d7a2419">

Histograms and Boxplots: Analyze the distribution of continuous variables (tweet length).

Histogram of Tweet Length: The histogram of tweet lengths shows that most tweets are between 50 and 150 characters long. This is consistent with Twitter's typical usage patterns, where tweets are often concise.

<img width="551" alt="Screenshot 2024-09-13 at 23 19 00" src="https://github.com/user-attachments/assets/68ebad39-e648-49c4-a63f-10c218a04d67">

Boxplot of Tweet Length by Sentiment: The boxplot reveals that:

Neutral and Irrelevant tweets tend to be longer on average.
Positive and Negative tweets are generally shorter. This suggests that users tend to use shorter, more concise messages when expressing strong opinions or emotions, while more neutral or less emotional content tends to be longer.

<img width="546" alt="Screenshot 2024-09-13 at 23 19 29" src="https://github.com/user-attachments/assets/48f2b875-30d8-4d6a-8b8b-2bf0664f5365">

Heatmaps: Visualize the correlation between numerical variables.

Correlation between Tweet Length and Sentiment: While we don't have other numerical variables in this dataset, the heatmap shows minimal correlation between the length of tweets and the sentiment. This indicates that the length of a tweet alone is not a strong predictor of its sentiment, although shorter tweets do tend to be more emotional (Positive or Negative).

<img width="553" alt="Screenshot 2024-09-13 at 23 20 42" src="https://github.com/user-attachments/assets/84e9a46a-a303-4041-8746-e0b0028f56b0">

Correlation matrix: by numerics feactures, related to tweet content counting exclamation marks, question marks, hashtags, and word counting, we can create an correlation matrix by this, Tweet Length and Word Count to be positively correlated (longer tweets generally contain more words).
Exclamation Count or Question Count might correlate with tweet sentiment (e.g., more exclamation marks could correlate with positive or negative emotions).

<img width="624" alt="Screenshot 2024-09-13 at 23 30 52" src="https://github.com/user-attachments/assets/8f9c1414-5376-41bf-bf2b-aefcf357c926">

4 Analysis based on results:

Based on the correlation matrices, visualizations, and exploratory analysis performed on the Twitter Sentiment Analysis Dataset, we can draw several conclusions regarding the relationships between tweet characteristics and sentiment distribution. Here are the key insights:

4.1. Tweet Length Distribution:
   
Tweet length: A histogram of tweet length that reveals the number of tweets in the range [50–150] are by far more common than other ranges, matching what one would expect regarding social media use case prioritizing small and to-the-point messages (as opposed to long-form content).

Sentiment and Tweet Length: As seen from the boxplot Neutral and Irrelevant tweets have longer lengths. Tweets that are labeled Positive and Negative tend to be short. This possibly relates to the inclination of brevity in shorter tweets for emotional and subjective assertions and specifically wordier ones for description or neutral facts.

4.2. Sentiment Distribution Across Platforms:
   
More of the Neutral tweets end up on Facebook though. Perhaps this means that Facebook users post more nuanced or less emotionally charged content. For example, Twitter is a bit more well balanced with both Positive and Negative tweets, this means people feel able to express their emotions comfortably with twitter. A larger percentage of Negative tweets are observed with Microsoft, CS, and Google which may imply the reason why customers post negative feedbacks using these platforms.

4.3. Correlation Analysis (Heatmap):

Length (Characters) and Word Count: Of course, there is also a very strong positive correlation between the length of tweats in characters and word counts. In order to hit the post length restriction, longer tweets just have more words.

Counts of Exclamations and Questions: Although these counts do not appear to be particularly predictive of other variables, they may provide an indirect clue as to the emotional tone of a tweet; For instance, tweets with additional exclamation points may be more sentimental (either positive or negative emotion).

Hashtag counts and Mention Counts: While hashtag and mention counts do not show a high correlation with other variables, they might have a bearing on the rating of some types of tweets(i.e., promotional tweets or highly engaging tweets).

Emotional Content (.!): Using more exclamation points in tweets can be a sign of emotion; either highly positive or negative but is most frequent in short tweets. I suspect that while the these question marks do not have a 1:1 correlation with Neutral sentiment frequency, they have some relationship as question marks are often an indication of curiosity, uncertainty or engagement.

Hashtags & Mentions: The application of hashtags and mentions is consistent across all types of tweets, and no particularly strong correlation emerges with tweet length or sentiment. Even so, these can be signals of activity in terms of engaging with hot topics or certain discourses.

Twitter, Facebook offer slightly neutral sentiment based on languageiOS is more comparatively neutral than Android for communication. Microsoft, CS, and Google all rate under 50%, which suggests there are areas in the user-experience that require attention to reduce the complaints and negative sentiment.

Conclusion

The Twitter Sentiment Analysis Dataset shows us how the sentiment of a user differs in various platforms and gives us an insight, too, as to how the length of a tweet and their choice of words affect this sentiment. Short and brief tweets may have an emotional load (either positive or negative) associated with them whereas longer tweets tend to be neutral or irrelevant.

First are clearly platform effects: some platforms (like Facebook) have more neutral content and others (including Microsoft and CS) are losing us more customers sentiment-wise. This content-reaction categorisation can inform platforms where people are coming to say what, and thus how they might tweak their working practices to cultivate more joyful stimulus/response loops.

Lastly, although specific features in tweets such as hashtags and mentions do not correlate very well with sentiment or length, they are great indicators of user interaction with a tweet and participation in trends. This feedback can help companies and platforms refine user experience and identify key areas in which users are unhappy.

Tools and Technologies:

Python: Pandas, Matplotlib, Seaborn for data manipulation and visualization. Visual Studio Code (VSC) for interactive data exploration and documentation of steps, and terminal interactive integrate.
