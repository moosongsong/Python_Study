tweet_limit = 280
tweet_string = "Blah" * 90

#diff = tweet_limit - len(tweet_string)

if diff := tweet_limit - len(tweet_string) >= 0:
    print(diff)
    print("A fitting tweet")

# if diff := (tweet_limit - len(tweet_string)) >= 0:
#     print(diff)
#     print("A fitting tweet")

else:
    print(diff)
    print(f'Went over by, {abs(diff)}')