from textblob import TextBlob

def sent_analysis(text) -> dict:
    """
    Analyze the sentiment of the given text.

    :param text: The text to analyze.
    :return: A dictionary containing the polarity score and classification.
    """
    analysis = TextBlob(text)
    p_score = analysis.sentiment.polarity
    if p_score > 0:
        classification = 'positive'
    elif p_score == 0:
        classification= 'neutral'
    else:
        classification = 'negative'
    return {
        'polarity_score': p_score,
        'classification': classification
    }
