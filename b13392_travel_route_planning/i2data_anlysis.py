from csv_operation import csv_reader
from sentiment import anlaysis

# twint -s "senkaku islands" --since 2021-08-01  -o senkaku.csv --csv
# twint -s "south China sea" --since 2021-08-01  -o southchinasea.csv --csv
tweets_list = ["%.2d" % i for i in range(5)]
print(tweets_list)

for target in tweets_list:
    data2020 = csv_reader(str(target) + ".csv", "i1SGScrapy/downloads")
    print(data2020[0], "#" * 10, data2020[1], "#" * 10, " \n", data2020[2])

    print("-" * 10, "tweets:")
    print(data2020[1][10], "\n", "#" * 10, "\n")

    js_txt = """

    var DATA = {
    """

    print("\n1. Heat comparison")
    print(len(data2020), " VS ", 0)

    compare_txt = "'data2021':" + str(len(data2020)) + ", 'data2020': 0"
    js_txt += compare_txt

    # data2020full = csv_reader("2021-06senkaku.csv", "data")
    data2020full = data2020

    print("\n2. sentiment anlaysis")
    total_sentiment = 0

    num_positive = 0
    num_neural = 0
    num_nagtive = 0

    unwanted_chars = ".,-_ ()’'"
    black_list = [
        "//t.co/daqs0qh2wb #",
        "# #",
        "[ auto ]",
        "//t.co/tgzew5at0r https",
        "s territory",
    ]
    wordfreq = {}

    usernamefreq = {}

    split = 101
    # pick_twlist = data2020full[0::split]
    pick_twlist = data2020full[0::split]
    for tw in pick_twlist:
        text = tw[10]
        username = tw[8]
        print("text=", text, "\n@@@username=", username, "\n")
        words, sentiment_tw = anlaysis(text)
        print(sentiment_tw)
        total_sentiment += sentiment_tw
        if sentiment_tw < 0:
            num_nagtive += 1
        if sentiment_tw == 0:
            num_neural += 1
        if sentiment_tw > 0:
            num_positive += 1
        # print('words=', words)
        for raw_word in words:
            word = raw_word.strip(unwanted_chars)
            if word not in wordfreq:
                if word not in black_list:
                    wordfreq[word] = 0
            if word not in black_list:
                wordfreq[word] += 1

        username = username.replace("'", "")
        if username not in usernamefreq:
            usernamefreq[username] = 0
        usernamefreq[username] += 1

    print("@" * 30, usernamefreq)

    print("tatal sentiment polarity:", total_sentiment)
    print("average sentiment polarity:", total_sentiment / len(pick_twlist))
    print(
        "number of (positive VS neural VS nagtive):",
        num_positive * split,
        num_neural * split,
        num_nagtive * split,
    )
    sentiment_txt = (
        ",'total_sentiment_polarity':"
        + str(round(total_sentiment, 2))
        + ", 'average_sentiment_polarity':"
        + str(round(total_sentiment / len(pick_twlist), 2))
        + ",'num_positive':"
        + str(num_positive * split)
        + ", 'num_neural':"
        + str(num_neural * split)
        + ",'num_nagtive':"
        + str(num_nagtive * split)
        + ", 'data2021':"
        + str(len(data2020))
    )
    js_txt += sentiment_txt

    js_txt += " };\n"

    print("\n 3. related words related to this topic")

    js_txt += "var RELATED_WORDS = {"
    # print(wordfreq)
    index = 0
    a1_sorted_keys = sorted(wordfreq, key=wordfreq.get, reverse=True)
    for r in a1_sorted_keys:
        if wordfreq[r] > 1:
            print(r, wordfreq[r])
            if index < 10:
                js_txt += "'" + r + "':" + str(wordfreq[r]) + ","
                index += 1

    js_txt += " };\n"

    index = 0
    print("\n 4. username often posts related topics")
    js_txt += "var WHO_TWEETS = {"
    a2_sorted_keys = sorted(usernamefreq, key=usernamefreq.get, reverse=True)
    # print('#'*20, usernamefreq)

    for r in a2_sorted_keys:
        if usernamefreq[r] >= 1 and r not in ("name"):
            print(r, usernamefreq[r])
            if index < 10:
                js_txt += "'" + r + "':" + str(usernamefreq[r]) + ","
                index += 1

    js_txt += " };"

    # write to a local js file , let d3 do data-visual
    with open("i3data_visualization/" + target + ".js", "w") as file:
        file.write(js_txt.strip())
