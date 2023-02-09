# CLProject_A-distant-reading-analysis-of-American-Literature - 2. text extration [ii. local storing]

# [A] code to local storing the extracted text
# [B] input corpus to local storing

----------------------------------
# [A] code to local storing the extracted text

import os
import requests
import re
from urllib import request
import nltk
import string
from nltk.stem import WordNetLemmatizer

title = 'Ulysses'
author = 'James Joyce'
url = 'https://www.gutenberg.org/files/4300/4300-0.txt'
path = ''

def find_text(raw):
    pass

def text_from_gutenberg(title, author, url, path='', return_raw=False,
                        return_tokens=False):
    title = title.lower()
    author = title.lower()
    
    filename = path + title #path to insert
    if os.path.isfile(filename) and os.stat(filename).st_size != 0:
        print("{title} file already exists".format(title=title))
        print(filename)
        with open(filename, 'r') as f:
            raw = f.read()
    else:
        print("{title} file does not already exist. Grabbing from Project Gutenberg".format(title=title))
        response = request.urlopen(url)
        raw = response.read().decode('utf-8-sig')
        print("Saving {title} file".format(title=title))
        with open(filename, 'w') as outfile:
            outfile.write(raw)
    if return_raw:
        return raw
        
    if return_tokens:
        return nltk.word_tokenize(find_text(raw))
    else:
        return raw

def preprocessing(text):
    lower_text = text.lower()
    no_punct_corpus = lower_text.translate(str.maketrans("", "", string.punctuation))
    no_number_corpus = re.sub(r'\d+', '', no_punct_corpus)
    tokenized_corpus = nltk.word_tokenize(no_number_corpus)
    lemmatizer = WordNetLemmatizer()
    lemmatized_corpus = " ".join([lemmatizer.lemmatize(word) for word in tokenized_corpus])

    return lemmatized_corpus
    
book_info = [ ] #book info to insert

path = '' #path to insert

for title, author, url in book_info:
    processed_text = preprocessing(text_from_gutenberg(title, author, url))
    filename = f"{path}lemmatized_{title.lower().replace('-', '')}.txt"
    with open(filename, "w") as f:
        f.write(processed_text)

    lemmatized_cs = preprocessing(processed_text)
    with open("lemmatized_corpus.txt", "w") as f:
        f.write(str(lemmatized_cs))
    print(lemmatized_cs)
    
book_info = [ ]

path = ''

for title, author, url in book_info:
    processed_text = preprocessing(text_from_gutenberg(title, author, url))
    filename = f"{path}lemmatized_{title.lower().replace('-', '')}.txt"
    with open(filename, "w") as f:
        f.write(processed_text)

    lemmatized_cs = preprocessing(processed_text)
    with open("lemmatized_corpus.txt", "w") as f:
        f.write(str(lemmatized_cs))
    print(lemmatized_cs)
    
----------------------------------

# [B] input corpus to local storing

book_info = [
	('hawthorne1', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/976/pg976.txt'),
	('hawthorne2', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/1916/1916-0.txt'
),
	('hawthorne3', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/2081/pg2081.txt'),
    ('hawthorne4', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/files/2181/2181-0.txt'),
    ('hawthorne5', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/2182/2182-0.txt'),
    ('hawthorne6', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/7119/pg7119.txt'),
    ('hawthorne7', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/7183/7183-0.txt'),
    ('hawthorne8', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/7372/pg7372.txt'),
    ('hawthorne9', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/7878/pg7878.txt'),
	('hawthorne10', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/7881/pg7881.txt'
),
	('hawthorne11', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/8088/pg8088.txt'),
    ('hawthorne12', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/8090/pg8090.txt'),
    ('hawthorne13', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/8091/8091-0.txt'),
    ('hawthorne14', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/8429/pg8429.txt'),
    ('hawthorne15', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9201/pg9201.txt'),
    ('hawthorne16', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9202/pg9202.txt'),
    ('hawthorne17', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9203/pg9203.txt'),
	('hawthorne18', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9204/9204-0.txt'
),
	('hawthorne19', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9206/pg9206.txt'),
    ('hawthorne20', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/9207/pg9207.txt'),
    ('hawthorne21', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9208/pg9208.txt'),
    ('hawthorne22', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9213/9213-0.txt'),
    ('hawthorne23', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9214/9214-0.txt'),
    ('hawthorne24', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9216/pg9216.txt'),
    ('hawthorne25', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9216/pg9216.txt'),
	('hawthorne26', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9217/9217-0.txt'
),
	('hawthorne27', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9218/pg9218.txt'),
    ('hawthorne28', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/files/9220/9220-0.txt'),
    ('hawthorne29', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/512/pg512.txt'),
    ('hawthorne30', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9222/pg9222.txt'),
    ('hawthorne31', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9236/pg9236.txt'),
    ('hawthorne32', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9237/pg9237.txt')
    ('hawthorne19', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9206/pg9206.txt'),
    ('hawthorne20', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/9207/pg9207.txt'),
    ('hawthorne21', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9208/pg9208.txt'),
    ('hawthorne22', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9213/9213-0.txt'),
    ('hawthorne23', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9214/9214-0.txt'),
    ('hawthorne24', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9216/pg9216.txt'),
    ('hawthorne25', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9216/pg9216.txt'),
	('hawthorne26', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9217/9217-0.txt'
),
	('hawthorne27', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9218/pg9218.txt'),
    ('hawthorne28', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/files/9220/9220-0.txt'),
    ('hawthorne29', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/512/pg512.txt'),
    ('hawthorne30', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9222/pg9222.txt'),
    ('hawthorne31', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9236/pg9236.txt'),
    ('hawthorne32', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9237/pg9237.txt'),
    ('hawthorne33', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9238/pg9238.txt'),
	('hawthorne34', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9239/pg9239.txt'
),
	('hawthorne35', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9240/pg9240.txt'),
    ('hawthorne36', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/9241/pg9241.txt'),
    ('hawthorne37', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9242/pg9242.txt'),
    ('hawthorne38', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9243/pg9243.txt'),
    ('hawthorne39', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9244/pg9244.txt'),
    ('hawthorne40', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9246/pg9246.txt'),
    ('hawthorne41', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9247/9247-0.txt'),
	('hawthorne42', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9248/9248-0.txt'
),
	('hawthorne43', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9249/pg9249.txt'),
    ('hawthorne44', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/9250/pg9250.txt'),
    ('hawthorne45', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9255/9255-0.txt'),
    ('hawthorne46', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9256/9256-0.txt'),
    ('hawthorne47', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9258/9258-0.txt'),
    ('hawthorne48', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/15697/15697-0.txt'),
    ('hawthorne49', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/77/77-0.txt',),
	('hawthorne50', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/41368/pg41368.txt'
),
	('hawthorne51', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/33/pg33.txt'),
    ('hawthorne52', 'Nathaniel Hawthorne',  'https://www.gutenberg.org/cache/epub/30376/pg30376.txt'),
    ('hawthorne53', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/9208/pg9208.txt'),
    ('hawthorne54', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/cache/epub/41309/pg41309.txt'),
    ('hawthorne55', 'Nathaniel Hawthorne', 'https://www.gutenberg.org/files/9214/9214-0.txt')
]

book_info = [
	('melville1', 'Herman Melville', "https://www.gutenberg.org/cache/epub/2489/pg2489.txt"),
	('melville2', 'Herman Melville', "https://www.gutenberg.org/cache/epub/2694/pg2694.txt"),
	('melville3', 'Herman Melville', "https://www.gutenberg.org/cache/epub/4045/pg4045.txt"),
    ('melville4', 'Herman Melville',     "https://www.gutenberg.org/cache/epub/10712/pg10712.txt",),
    ('melville5', 'Herman Melville', "https://www.gutenberg.org/cache/epub/11231/pg11231.txt"),
    ('melville6', 'Herman Melville', "https://www.gutenberg.org/cache/epub/34970/pg34970.txt"),
    ('melville7', 'Herman Melville', "https://www.gutenberg.org/cache/epub/21816/pg21816.txt"),
    ('melville8', 'Herman Melville', "https://www.gutenberg.org/cache/epub/15859/pg15859.txt"),
    ('melville9', 'Herman Melville', "https://www.gutenberg.org/cache/epub/15422/pg15422.txt"),
    ('melville10', 'Herman Melville', "https://www.gutenberg.org/cache/epub/13721/pg13721.txt"),
    ('melville11', 'Herman Melville', "https://www.gutenberg.org/cache/epub/13720/pg13720.txt")
]

book_info = [
	('thoreau1', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/4066/pg4066.txt"),
	('thoreau2', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/4232/pg4232.txt"),
	('thoreau3', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/9846/pg9846.txt"),
    ('thoreau4', 'Henry David Thoreau',     "https://www.gutenberg.org/cache/epub/34990/pg34990.txt"),
    ('thoreau5', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/42500/pg42500.txt"),
    ('thoreau6', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/60951/pg60951.txt"),
    ('thoreau7', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/2567/pg2567.txt"),
    ('thoreau8', 'Henry David Thoreau', "https://www.gutenberg.org/cache/epub/15859/pg15859.txt")
]

book_info = [
	('poe1', 'Edgar Allan Poe', 'https://www.gutenberg.org/cache/epub/2148/pg2148.txt'),
	('poe2', 'Edgar Allan Poe', 'https://www.gutenberg.org/cache/epub/2147/pg2147.txt'),
	('poe3', 'Edgar Allan Poe', 'https://www.gutenberg.org/cache/epub/17192/pg17192.txt'),
    ('poe4', 'Edgar Allan Poe',  'https://www.gutenberg.org/cache/epub/2151/pg2151.txt'),
    ('poe5', 'Edgar Allan Poe', 'https://www.gutenberg.org/files/2149/2149-0.txt'),
    ('poe6', 'Edgar Allan Poe', 'https://www.gutenberg.org/files/2150/2150-0.txt'),
    ('poe7', 'Edgar Allan Poe', 'https://www.gutenberg.org/files/32037/32037-0.txt'),
    ('poe8', 'Edgar Allan Poe', 'https://www.gutenberg.org/cache/epub/2151/pg2151.txt')
]

book_info = [('dickinson1', 'Emily Dickinson', 'https://www.gutenberg.org/cache/epub/12242/pg12242.txt'),]

book_info = [
	  ('emerson1', 'Ralph Waldo Emerson', 'https://www.gutenberg.org/cache/epub/12843/pg12843.txt'),
	  ('emerson2', 'Ralph Waldo Emerson', 'https://www.gutenberg.org/cache/epub/16643/pg16643.txt'),
	  ('emerson3', 'Ralph Waldo Emerson', 'https://www.gutenberg.org/cache/epub/69258/pg69258.txt'),
    ('emerson4', 'Ralph Waldo Emerson',  'https://www.gutenberg.org/cache/epub/6312/pg6312.txt',),
    ('emerson5', 'Ralph Waldo Emerson', 'https://www.gutenberg.org/cache/epub/2945/pg2945.txt'),
]

book_info = [('james01', 'Henry James', 'https://www.gutenberg.org/cache/epub/69629/pg69629.txt'), ('james02', 'Henry James', 'https://www.gutenberg.org/cache/epub/209/pg209.txt'), ('james03', 'Henry James', 'https://www.gutenberg.org/cache/epub/432/pg432.txt'), ('james04', 'Henry James', 'https://www.gutenberg.org/cache/epub/1093/pg1093.txt'), ('james05', 'Henry James', 'https://www.gutenberg.org/cache/epub/1190/pg1190.txt'), ('james06', 'Henry James', 'https://www.gutenberg.org/cache/epub/1195/pg1195.txt'), ('james07', 'Henry James', 'https://www.gutenberg.org/cache/epub/2366/pg2366.txt'), ('james08', 'Henry James', 'https://www.gutenberg.org/cache/epub/2425/pg2425.txt'), ('james09', 'Henry James', 'https://www.gutenberg.org/cache/epub/2426/pg2426.txt'), ('james10', 'Henry James', 'https://www.gutenberg.org/cache/epub/2460/pg2460.txt'), ('james11', 'Henry James', 'https://www.gutenberg.org/cache/epub/2534/pg2534.txt'), ('james12', 'Henry James', 'https://www.gutenberg.org/cache/epub/4264/pg4264.txt'), ('james13', 'Henry James', 'https://www.gutenberg.org/cache/epub/7118/pg7118.txt'), ('james14', 'Henry James', 'https://www.gutenberg.org/cache/epub/8080/pg8080.txt'), ('james15', 'Henry James', 'https://www.gutenberg.org/cache/epub/8081/pg8081.txt'), ('james16', 'Henry James', 'https://www.gutenberg.org/cache/epub/19718/pg19718.txt'), ('james17', 'Henry James', 'https://www.gutenberg.org/cache/epub/19717/pg19717.txt'), ('james18', 'Henry James', 'https://www.gutenberg.org/cache/epub/20085/pg20085.txt'), ('james19', 'Henry James', 'https://www.gutenberg.org/cache/epub/25500/pg25500.txt'), ('james20', 'Henry James', 'https://www.gutenberg.org/cache/epub/26115/pg26115.txt'), ('james21', 'Henry James', 'https://www.gutenberg.org/cache/epub/28004/pg28004.txt'), ('james22', 'Henry James', 'https://www.gutenberg.org/cache/epub/29452/pg29452.txt'), ('james23', 'Henry James', 'https://www.gutenberg.org/cache/epub/30059/pg30059.txt'), ('james24', 'Henry James', 'https://www.gutenberg.org/cache/epub/32649/pg32649.txt'), ('james25', 'Henry James', 'https://www.gutenberg.org/cache/epub/32939/pg32939.txt'), ('james26', 'Henry James', 'https://www.gutenberg.org/cache/epub/33325/pg33325.txt'), ('james27', 'Henry James', 'https://www.gutenberg.org/cache/epub/37424/pg37424.txt'), ('james28', 'Henry James', 'https://www.gutenberg.org/cache/epub/37425/pg37425.txt'), ('james29', 'Henry James', 'https://www.gutenberg.org/cache/epub/38424/pg38424.txt'), ('james30', 'Henry James', 'https://www.gutenberg.org/cache/epub/55078/pg55078.txt'), ('james31', 'Henry James', 'https://www.gutenberg.org/cache/epub/68340/pg68340.txt'), ('james32', 'Henry James', 'https://www.gutenberg.org/cache/epub/68717/pg68717.txt'), ('james33', 'Henry James', 'https://www.gutenberg.org/cache/epub/68961/pg68961.txt'), ('james34', 'Henry James', 'https://www.gutenberg.org/cache/epub/69628/pg69628.txt'), ('james35', 'Henry James', 'https://www.gutenberg.org/cache/epub/179/pg179.txt')]

book_info = [('howell 1', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/7359/pg7359.txt'), ('howell 2', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/4646/pg4646.txt'), ('howell 3', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/4600/pg4600.txt'), ('howell 4', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3406/pg3406.txt'), ('howell 5', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3405/pg3405.txt'), ('howell 6', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3388/pg3388.txt'), ('howell 7', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3376/pg3376.txt'), ('howell 8', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3375/pg3375.txt'), ('howell 9', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/3365/pg3365.txt'), ('howell 10', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/2506/pg2506.txt'), ('howell 11', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/728/pg728.txt'), ('howell 12', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/66257/pg66257.txt'), ('howell 13', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/47060/pg47060.txt'), ('howell 14', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/43469/pg43469.txt'), ('howell 15', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/33608/pg33608.txt'), ('howell 16', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/30108/pg30108.txt'), ('howell 17', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/29993/pg29993.txt'), ('howell 18', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/28763/pg28763.txt'), ('howell 19', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/28305/pg28305.txt'), ('howell 20', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/27880/pg27880.txt'), ('howell 21', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/23030/pg23030.txt'), ('howell 22', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/22519/pg22519.txt'), ('howell 23', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/22297/pg22297.txt'), ('howell 24', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/22219/pg22219.txt'), ('howell 25', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/20403/pg20403.txt'), ('howell 26', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/20225/pg20225.txt'), ('howell 27', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/18605/pg18605.txt'), ('howell 28', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/18565/pg18565.txt'), ('howell 29', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/18555/pg18555.txt'), ('howell 30', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/154/pg154.txt'), ('howell 31', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/723/pg723.txt'), ('howell 32', 'William Dean Howell ', 'https://www.gutenberg.org/cache/epub/66584/pg66584.txt')]

book_info = [('crane1', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/43706/pg43706.txt'), ('crane2', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/39644/pg39644.txt'), ('crane3', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/33579/pg33579.txt'), ('crane4', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/31488/pg31488.txt'), ('crane5', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/31189/pg31189.txt'), ('crane6', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/19593/pg19593.txt'), ('crane7', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/9870/pg9870.txt'), ('crane8', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/7239/pg7239.txt'), ('crane9', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/2364/pg2364.txt'), ('crane10', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/463/pg463.txt'), ('crane11', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/447/pg447.txt'), ('crane12', 'Stephen Crane', 'https://www.gutenberg.org/cache/epub/45524/pg45524.txt')]

book_info = [('twain01', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/1086/pg1086.txt'), ('twain02', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/1213/pg1213.txt'), ('twain03', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/3176/pg3176.txt'), ('twain04', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/3177/pg3177.txt'), ('twain05', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/2572/pg2572.txt'), ('twain06', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/3179/pg3179.txt'), ('twain07', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5782/pg5782.txt'), ('twain08', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5783/pg5783.txt'), ('twain09', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5784/pg5784.txt'), ('twain10', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5786/pg5786.txt'), ('twain11', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5787/pg5787.txt'), ('twain12', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5788/pg5788.txt'), ('twain13', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5808/pg5808.txt'), ('twain14', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5809/pg5809.txt'), ('twain15', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5810/pg5810.txt'), ('twain16', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5811/pg5811.txt'), ('twain17', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5812/pg5812.txt'), ('twain18', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5813/pg5813.txt'), ('twain19', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5814/pg5814.txt'), ('twain20', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5818/pg5818.txt'), ('twain21', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5819/pg5819.txt'), ('twain22', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5820/pg5820.txt'), ('twain23', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5821/pg5821.txt'), ('twain24', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5822/pg5822.txt'), ('twain25', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5823/pg5823.txt'), ('twain26', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5824/pg5824.txt'), ('twain27', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5836/pg5836.txt'), ('twain28', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5837/pg5837.txt'), ('twain29', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5838/pg5838.txt'), ('twain30', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5839/pg5839.txt'), ('twain31', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5840/pg5840.txt'), ('twain32', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5841/pg5841.txt'), ('twain33', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/5842/pg5842.txt'), ('twain34', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7100/pg7100.txt'), ('twain35', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7101/pg7101.txt'), ('twain36', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7102/pg7102.txt'), ('twain37', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7103/pg7103.txt'), ('twain38', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7104/pg7104.txt'), ('twain39', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7105/pg7105.txt'), ('twain40', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7106/pg7106.txt'), ('twain41', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7107/pg7107.txt'), ('twain42', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7154/pg7154.txt'), ('twain43', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7155/pg7155.txt'), ('twain44', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7156/pg7156.txt'), ('twain45', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7157/pg7157.txt'), ('twain46', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7158/pg7158.txt'), ('twain47', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7159/pg7159.txt'), ('twain48', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7160/pg7160.txt'), ('twain49', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7161/pg7161.txt'), ('twain50', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7162/pg7162.txt'), ('twain51', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7193/pg7193.txt'), ('twain52', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7194/pg7194.txt'), ('twain53', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7195/pg7195.txt'), ('twain54', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7196/pg7196.txt'), ('twain55', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7197/pg7197.txt'), ('twain56', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7198/pg7198.txt'), ('twain57', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7199/pg7199.txt'), ('twain58', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7200/pg7200.txt'), ('twain59', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7242/pg7242.txt'), ('twain60', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7243/pg7243.txt'), ('twain61', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7244/pg7244.txt'), ('twain62', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7245/pg7245.txt'), ('twain63', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7246/pg7246.txt'), ('twain64', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7247/pg7247.txt'), ('twain65', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7248/pg7248.txt'), ('twain66', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7249/pg7249.txt'), ('twain67', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/7250/pg7250.txt'), ('twain68', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8471/pg8471.txt'), ('twain69', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8472/pg8472.txt'), ('twain70', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8473/pg8473.txt'), ('twain71', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8474/pg8474.txt'), ('twain72', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8475/pg8475.txt'), ('twain73', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8476/pg8476.txt'), ('twain74', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8477/pg8477.txt'), ('twain75', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8478/pg8478.txt'), ('twain76', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8479/pg8479.txt'), ('twain77', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8480/pg8480.txt'), ('twain78', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8481/pg8481.txt'), ('twain79', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8482/pg8482.txt'), ('twain80', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8526/pg8526.txt'), ('twain81', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8527/pg8527.txt'), ('twain82', 'Mark Twain', 'https://www.gutenberg.org/cache/epub/8528/pg8528.txt')]

book_info = [('jacobs01', 'Harriet Jacobs', 'https://www.gutenberg.org/cache/epub/11030/pg11030.txt')]

book_info = [('whitman01', 'Walt Whitman', 'https://www.gutenberg.org/cache/epub/8388/pg8388.txt'), ('whitman02', 'Walt Whitman', 'https://www.gutenberg.org/cache/epub/8813/pg8813.txt')]

book_info = [('irving01', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/8571/pg8571.txt'), ('irving02', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/7948/pg7948.txt'), ('irving03', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/1850/pg1850.txt'), ('irving04', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/14228/pg14228.txt'), ('irving05', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/13042/pg13042.txt'), ('irving06', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/41/pg41.txt'), ('irving07', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/7994/pg7994.txt'), ('irving08', 'Washington Irving', 'https://www.gutenberg.org/cache/epub/7993/pg7993.txt')]

[('bryant01', 'William Cullen Bryant', 'https://www.gutenberg.org/cache/epub/16341/pg16341.txt')]

book_info = [('longfellow01', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/cache/epub/976/pg976.txt'), ('longfellow02', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/files/1916/1916-0.txt'), ('longfellow03', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/cache/epub/2081/pg2081.txt'), ('longfellow04', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/files/2181/2181-0.txt'), ('longfellow05', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/files/2182/2182-0.txt'), ('longfellow06', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/cache/epub/7119/pg7119.txt'), ('longfellow07', 'Henry Wadsworth Longfellow', 'https://www.gutenberg.org/files/7183/7183-0.txt')]

book_info = [('london01', 'Jack London', 'https://www.gutenberg.org/cache/epub/12336/pg12336.txt'), ('london02', 'Jack London', 'https://www.gutenberg.org/cache/epub/11051/pg11051.txt'), ('london03', 'Jack London', 'https://www.gutenberg.org/cache/epub/14449/pg14449.txt'), ('london04', 'Jack London', 'https://www.gutenberg.org/cache/epub/14654/pg14654.txt'), ('london05', 'Jack London', 'https://www.gutenberg.org/cache/epub/14658/pg14658.txt'), ('london06', 'Jack London', 'https://www.gutenberg.org/cache/epub/215/pg215.txt'), ('london07', 'Jack London', 'https://www.gutenberg.org/cache/epub/18062/pg18062.txt'), ('london08', 'Jack London', 'https://www.gutenberg.org/cache/epub/21936/pg21936.txt'), ('london09', 'Jack London', 'https://www.gutenberg.org/files/21970/21970-0.txt'), ('london10', 'Jack London', 'https://www.gutenberg.org/files/21971/21971-0.txt'), ('london11', 'Jack London', 'https://www.gutenberg.org/cache/epub/22104/pg22104.txt'), ('london12', 'Jack London', 'https://www.gutenberg.org/cache/epub/28693/pg28693.txt'), ('london13', 'Jack London', 'https://www.gutenberg.org/cache/epub/48474/pg48474.txt'), ('london14', 'Jack London', 'https://www.gutenberg.org/files/54068/54068-0.txt'), ('london15', 'Jack London', 'https://www.gutenberg.org/cache/epub/55948/pg55948.txt'), ('london16', 'Jack London', 'https://www.gutenberg.org/cache/epub/16257/pg16257.txt'), ('london17', 'Jack London', 'https://www.gutenberg.org/cache/epub/318/pg318.txt'), ('london18', 'Jack London', 'https://www.gutenberg.org/cache/epub/710/pg710.txt'), ('london19', 'Jack London', 'https://www.gutenberg.org/cache/epub/746/pg746.txt'), ('london20', 'Jack London', 'https://www.gutenberg.org/cache/epub/910/pg910.txt'), ('london21', 'Jack London', 'https://www.gutenberg.org/cache/epub/1074/pg1074.txt'), ('london22', 'Jack London', 'https://www.gutenberg.org/cache/epub/1089/pg1089.txt'), ('london23', 'Jack London', 'https://www.gutenberg.org/cache/epub/1096/pg1096.txt'), ('london24', 'Jack London', 'https://www.gutenberg.org/cache/epub/1160/pg1160.txt'), ('london25', 'Jack London', 'https://www.gutenberg.org/cache/epub/1161/pg1161.txt'), ('london26', 'Jack London', 'https://www.gutenberg.org/cache/epub/1163/pg1163.txt'), ('london27', 'Jack London', 'https://www.gutenberg.org/cache/epub/1187/pg1187.txt'), ('london28', 'Jack London', 'https://www.gutenberg.org/cache/epub/1596/pg1596.txt'), ('london29', 'Jack London', 'https://www.gutenberg.org/cache/epub/1655/pg1655.txt'), ('london30', 'Jack London', 'https://www.gutenberg.org/cache/epub/1669/pg1669.txt'), ('london31', 'Jack London', 'https://www.gutenberg.org/cache/epub/1730/pg1730.txt'), ('london32', 'Jack London', 'https://www.gutenberg.org/cache/epub/2152/pg2152.txt'), ('london33', 'Jack London', 'https://www.gutenberg.org/cache/epub/2377/pg2377.txt'), ('london34', 'Jack London', 'https://www.gutenberg.org/cache/epub/2416/pg2416.txt'), ('london35', 'Jack London', 'https://www.gutenberg.org/cache/epub/4953/pg4953.txt'), ('london36', 'Jack London', 'https://www.gutenberg.org/cache/epub/6455/pg6455.txt'), ('london37', 'Jack London', 'https://www.gutenberg.org/cache/epub/10736/pg10736.txt')]

book_info = [('norris01', 'Frank Norris', 'https://www.gutenberg.org/files/48620/48620-0.txt'), ('norris02', 'Frank Norris', 'https://www.gutenberg.org/files/165/165-0.txt'), ('norris03', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/26026/pg26026.txt'), ('norris04', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/16096/pg16096.txt'), ('norris05', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/14712/pg14712.txt'), ('norris06', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/9905/pg9905.txt'), ('norris07', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/4382/pg4382.txt'), ('norris08', 'Frank Norris', 'https://www.gutenberg.org/cache/epub/401/pg401.txt'), ('norris09', 'Frank Norris', 'https://www.gutenberg.org/files/321/321-0.txt'), ('norris10', 'Frank Norris', 'https://www.gutenberg.org/files/268/268-0.txt')]

book_info = [('douglass01', 'Frederick Douglass', 'https://www.gutenberg.org/cache/epub/202/pg202.txt'), ('douglass02', 'Frederick Douglass', 'https://www.gutenberg.org/cache/epub/34915/pg34915.txt'), ('douglass03', 'Frederick Douglass', 'https://www.gutenberg.org/files/59116/59116-0.txt'), ('douglass04', 'Frederick Douglass', 'https://www.gutenberg.org/cache/epub/67919/pg67919.txt'), ('douglass05', 'Frederick Douglass', 'https://www.gutenberg.org/files/23/23-0.txt')]

book_info = [('hemingway01', 'Ernest Hemingway', 'https://www.gutenberg.org/cache/epub/69683/pg69683.txt'), ('hemingway02', 'Ernest Hemingway', 'https://www.gutenberg.org/cache/epub/67138/pg67138.txt'), ('hemingway03', 'Ernest Hemingway', 'https://www.gutenberg.org/files/61085/61085-0.txt'), ('hemingway04', 'Ernest Hemingway', 'https://www.gutenberg.org/files/59603/59603-0.txt')]

book_info = [('hurston01', 'Zora Neale Hurston', 'https://www.gutenberg.org/files/19435/19435-0.txt'), ('hurston02', 'Zora Neale Hurston', 'https://www.gutenberg.org/cache/epub/22146/pg22146.txt'), ('hurston03', 'Zora Neale Hurston', 'https://www.gutenberg.org/cache/epub/17187/pg17187.txt'), ('hurston04', 'Zora Neale Hurston', 'https://www.gutenberg.org/cache/epub/15902/pg15902.txt')]

book_info = [('fitzgerald01', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/cache/epub/68229/pg68229.txt'), ('fitzgerald02', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/files/805/805-0.txt'), ('fitzgerald03', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/cache/epub/4368/pg4368.txt'), ('fitzgerald04', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/files/6695/6695-0.txt'), ('fitzgerald05', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/files/9830/9830-0.txt'), ('fitzgerald06', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/files/60962/60962-0.txt'), ('fitzgerald07', 'F. Scott Fitzgerald', 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt')]

book_info = [('vonnegut01', 'Kurt Vonnegut', 'https://www.gutenberg.org/cache/epub/68229/pg68229.txt'), ('vonnegut02', 'Kurt Vonnegut', 'https://www.gutenberg.org/files/805/805-0.txt')]

book_info = [('dick01', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/28554/pg28554.txt'), ('dick02', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/28644/pg28644.txt'), ('dick03', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/28698/pg28698.txt'), ('dick04', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/28767/pg28767.txt'), ('dick05', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/29132/pg29132.txt'), ('dick06', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/30255/pg30255.txt'), ('dick07', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/31516/pg31516.txt'), ('dick08', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/32032/pg32032.txt'), ('dick09', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/32154/pg32154.txt'), ('dick10', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/32522/pg32522.txt'), ('dick11', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/32832/pg32832.txt'), ('dick12', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/40964/pg40964.txt'), ('dick13', 'Philip K Dick', 'https://www.gutenberg.org/cache/epub/41562/pg41562.txt')]
