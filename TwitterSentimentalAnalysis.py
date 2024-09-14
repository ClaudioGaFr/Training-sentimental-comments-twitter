import pandas as pd
#DATA COLLECTION AND PREPARATION
# loading data set
train_data = pd.read_csv('/Users/claudiogf/Desktop/archive/twitter_training.csv')
validation_data = pd.read_csv('/Users/claudiogf/Desktop/archive/twitter_validation.csv')
#Rename columns for clarity
train_data.columns = ['ID', 'Platform', 'Sentiment', 'Text']
validation_data.columns = ['ID', 'Platform', 'Sentiment', 'Text']
#Check for missing values and remove rows with missing 'text'
train_data_clean = train_data.dropna(subset=['Text'])
# Preview the first few rows
print("First few rows of the training data:")
print(train_data_clean.head())
# Check for missing values
print("\nMissing values in the dataset:")
print(train_data_clean.isnull().sum())

#DESCRIPTIVE STATISTIC
# Create a new column for tweet length
train_data_clean['Tweet_Length'] = train_data_clean['Text'].apply(len)
# Descriptive statistics for numerical features 
print("\nDescriptive statistics for tweet length:")
print(train_data_clean['Tweet_Length'].describe())
# Frequency distribution of sentiment labels
print("\nSentiment label distribution:")
print(train_data_clean['Sentiment'].value_counts())

#DATA VISUALIZATION
import seaborn as sns
import matplotlib.pyplot as plt

# Distribution of Sentiment (Bar Chart)
plt.figure(figsize=(8, 6))
sns.countplot(x='Sentiment', data=train_data_clean, palette='viridis')
plt.title('Distribution of Sentiments')
plt.show()

# Histogram of Tweet Length
plt.figure(figsize=(10, 6))
sns.histplot(train_data_clean['Tweet_Length'], bins=30, kde=True, color='blue')
plt.title('Distribution of Tweet Length')
plt.show()

# Boxplot of Tweet Length by Sentiment
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sentiment', y='Tweet_Length', data=train_data_clean, palette='coolwarm')
plt.title('Boxplot of Tweet Length by Sentiment')
plt.show()

#Sentiment analysis 
# Sentiment distribution by Platform (Bar Chart)
plt.figure(figsize=(10, 6))
sns.countplot(x='Platform', hue='Sentiment', data=train_data_clean, palette='Set2')
plt.title('Sentiment Distribution by Platform')
plt.xticks(rotation=45)
plt.show()

# Relationship between Tweet Length and Sentiment (Histogram)
plt.figure(figsize=(10, 6))
sns.histplot(data=train_data_clean, x='Tweet_Length', hue='Sentiment', multiple='stack', palette='Set1', bins=30)
plt.title('Relationship between Tweet Length and Sentiment')
plt.show()

# Create new numeric features based on tweet content
# 1. Word count in the tweet
train_data_clean['Word_Count'] = train_data_clean['Text'].apply(lambda x: len(x.split()))

# 2. Count of exclamation marks in the tweet
train_data_clean['Exclamation_Count'] = train_data_clean['Text'].apply(lambda x: x.count('!'))

# 3. Count of question marks in the tweet
train_data_clean['Question_Count'] = train_data_clean['Text'].apply(lambda x: x.count('?'))

# 4. Count of hashtags in the tweet
train_data_clean['Hashtag_Count'] = train_data_clean['Text'].apply(lambda x: x.count('#'))

# 5. Count of mentions in the tweet (@)
train_data_clean['Mention_Count'] = train_data_clean['Text'].apply(lambda x: x.count('@'))

# Create a correlation matrix with the numeric features
correlation_matrix = train_data_clean[['Tweet_Length', 'Word_Count', 'Exclamation_Count', 'Question_Count', 'Hashtag_Count', 'Mention_Count']].corr()

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap for Tweet Features')
plt.show()