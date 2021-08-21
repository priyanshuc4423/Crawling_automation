from execute import InternetSpeedTwitterBot as t
PROMISEDSPEED  = 80.00
new_0bj = t()
new_0bj.get_internet_speed()
if PROMISEDSPEED > float(new_0bj.up):
    new_0bj.tweet_at_provider()
else:
    print('today GOD SPEED')












