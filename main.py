import praw
import webbrowser
import random
from nltk.tag import pos_tag

#nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

#returns every three words of string
word_interval = 3
def fragment(complete_text: str) -> str: 
    tagged_words = pos_tag(complete_text.split())
    nouns = [word for word,pos in tagged_words if pos == 'NNP' or pos == 'NN']

    return nouns
    # returned_words = []
    # for i in range(0, len(all_words) - len(all_words) % word_interval, word_interval):
    #     returned_words.append(all_words[i])
    # return returned_words




reddit = praw.Reddit('MyCredentials', user_agent="user_agent=Reddit Recall 1.0 by /u/Frolicks https://github.com/DrFrolicks/RedditRecall")

submissions = [] 

for submission in reddit.user.me().upvoted(limit=500): 
    if(not submission.over_18):
        submissions.append(submission)

random.shuffle(submissions)

for submission in submissions:
    print(fragment(submission.title))
    input()
    print(submission.title)
    if (input("Open post? (y/n)") == 'y'):
        webbrowser.open(submission.url)


        