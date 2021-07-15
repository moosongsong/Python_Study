tweet_limit = 280
tweet_string = "Blah" * 80

diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")

else:
    print(f'Went over by, {abs(diff)}')