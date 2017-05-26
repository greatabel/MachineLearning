warned_of_error = False


# https://github.com/amueller/word_cloud

def create_cloud(text):
    '''Creates a word cloud (when pytagcloud is installed)

    Parameters
    ----------
    oname : output filename
    words : list of (value,str)
    maxsize : int, optional
        Size of maximum word. The best setting for this parameter will often
        require some manual tuning for each input.
    fontname : str, optional
        Font to use.
    '''
    # try:
    #     from pytagcloud import create_tag_image, make_tags
    # except ImportError:
    #     if not warned_of_error:
    #         print("Could not import pytagcloud. Skipping cloud generation")
    #     return
    from wordcloud import WordCloud
    from os import path
    # gensim returns a weight between 0 and 1 for each word, while pytagcloud
    # expects an integer word count. So, we multiply by a large number and
    # round. For a visualization this is an adequate approximation.
    # We also need to flip the order as gensim returns (value, word), whilst
    # pytagcloud expects (word, value):

    d = path.dirname(__file__)

    # Read the whole text.
    # text = open(path.join(d, 'constitution.txt')).read()
    # text = "test test test it again. I am free today. free\
    #         It's the first time for her to screen-test"
    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    create_cloud()