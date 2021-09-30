import i1forked_altered_lib as mytwint
import schedule
import time


# you can change the name of each "job" after "def" if you'd like.
def jobone():
    print("Fetching Tweets")
    c = mytwint.Config()
    # choose username (optional)
    # c.Username = ""
    # choose search term (optional)
    c.Search = "eth"
    # c.Search = "#eth"
    # choose beginning time (narrow results)
    c.Since = "2021-01-01"
    # set limit on total tweets
    c.Limit = 1000
    # no idea, but makes the csv format properly
    c.Store_csv = True

    # change the name of the csv file
    c.Output = "../downloads/#eth.csv"
    mytwint.run.Search(c)



# run once when you start the program

jobone()


# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

# schedule.every(1).minutes.do(jobone)
schedule.every().hour.do(jobone)



while True:
    schedule.run_pending()
    time.sleep(1)
