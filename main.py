import praw

reddit = praw.Reddit(client_id='OuaP4CeKSjP0xbUmUmK67g',
                     client_secret='nEAexElCPM1-ZOPXdwNuefXx4f87hA', 
                    user_agent='reddit.com:caw-caaw:v1 (by u/cultist48)', 
                     password='kap252-STSbot',
                     username='cultist48')


subreddit = reddit.subreddit('slaythespire')

def get_all_comments(): #gets all comments
    print('getting all comments')
    all_comments = []
    for submission in subreddit.new(limit = 500):
        for comment in submission.comments:
            all_comments.append(comment)
    return all_comments
        
def check_for_caw(all_comments): #filters to comments with caw not by the bot
    caw_comments = []
    for comment in all_comments:
        if "caw" in comment.body.lower() and comment.author.name != 'cultist48': 
            print(f"The post is: {comment.submission.title} \n")
            print(f"The comment is: {comment.body}") 
            caw_comments.append(comment)
    
    return caw_comments

def check_for_bot(caw_comments): #checks if bot already replied
    eligblie_comments = caw_comments
    for comment in caw_comments:
        print('replies:')
        print(comment.replies.list())
        for reply in comment.replies.list():
            print(f"The reply to the comment was {reply.body}")
            
            if (reply.author.name == 'cultist48'):
                print(f"This reply is from the bot and is not eligible: {reply.body}")

                eligblie_comments.remove(comment)
    
    return eligblie_comments


def reply_to_comment(eligible_comments):
    print('replying to comments')
    print(eligible_comments)
    for comment in eligible_comments:
        print(f'commenting on {comment.body}')
        comment.reply('CAW CAAW!')


def main():
    all_comments = get_all_comments()
    caw_comments = check_for_caw(all_comments)
    eligible_comments = check_for_bot(caw_comments)
    reply_to_comment(eligible_comments)


main()