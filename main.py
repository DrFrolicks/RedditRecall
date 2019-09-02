import praw
from nltk.corpus import wordnet as wn

nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

#returns every three words of string
word_interval = 3
def fragment(complete_text: str) -> str: 
    all_words = complete_text.split()

    return [word for word in all_words if word in nouns]
    # returned_words = []
    # for i in range(0, len(all_words) - len(all_words) % word_interval, word_interval):
    #     returned_words.append(all_words[i])
    # return returned_words



reddit = praw.Reddit('MyCredentials', user_agent="user_agent=Reddit Recall 1.0 by /u/Frolicks https://github.com/DrFrolicks/RedditRecall")

titles = []
for post in reddit.user.me().upvoted(limit=10): 
    if(post.over_18):
        print(fragment(post.title))