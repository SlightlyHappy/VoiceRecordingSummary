import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

def merge_paragraphs(paragraphs):
    # Join the paragraphs together
    text = "Client requires aid with medication management, attending appointments, managing activities of daily independent living and come up with effective coping strategies for symptoms of diagnosis - mainly anxiety. Staff intervention aims to ensure medication compliance, ensure client attends appointments, and help client manage symptoms of anxiety. Client requires aid in medication management, understanding what the purpose of the medication is. Client also requires aid in managing activities of daily independent living, client requires help advocating for self in some situations. Staff intervention aims to ensure medication compliance with client, staff also aids client in advocating for themselves. Client requires regular check ins to ensure client is well and is able to handle independent daily living tasks. Client also needs check ins to ensure compliance to treatment. Staff intervention aids by coming up with coping mechanisms to handle symptoms of diagnosis - anxiety - and by helping client manage tasks of daily independent living. Client benefits from regular check ins to ensure wellbeing and that necessities are being met. Client also requires aid in managing activities of daily independent living. Client benefits from regular check ins and needs aid in managing finances. Staff intervention aims to provide finances (trilogy is payee) and check in about clients needs and progress. (Ron W). Client benefits from regular check ins to ensure wellbeing and that necessities are being met, client also requires staff to pack clients medications to ensure medication compliance. Without staff intervention, client will be overburdened in inaction with their symptoms of anxiety. Client requires aid with medication management, attending appointments, managing activities of daily independent living and come up with effective coping strategies for symptoms of diagnosis - anxiety, psychosis, and additional medical/administrative issues. Without staff intervention client would not be able to cope with symptoms and fail to comply with treatment plans.".join(paragraphs)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize each sentence into words and tag them
    tagged_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        tagged_sentences.append(tagged_words)

    # Identify the narrative of the text by finding the most common part-of-speech tags
    narrative_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    narrative_words = []
    for tagged_sentence in tagged_sentences:
        for tagged_word in tagged_sentence:
            if tagged_word[1] in narrative_tags:
                narrative_words.append(tagged_word[0])

    # Merge the narrative words into a single paragraph
    narrative_paragraph = " ".join(narrative_words)

    return narrative_paragraph
