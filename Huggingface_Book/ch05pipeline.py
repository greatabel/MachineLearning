#第5章/文本分类
from transformers import pipeline

print('-----------1-----------')
classifier = pipeline("sentiment-analysis")

result = classifier("I hate you")[0]
print(result)

result = classifier("I love you")[0]
print(result)


print('-----------2-----------')
#第5章/阅读理解
question_answerer = pipeline("question-answering")

context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a 
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune 
a model on a SQuAD task, you may leverage the examples/pytorch/question-answering/run_squad.py script.
"""

result = question_answerer(
    question="What is extractive question answering?",
    context=context,
)
print(result)

print('##########')

result = question_answerer(
    question="What is a good example of a question answering dataset?",
    context=context,
)

print(result)


print('-----------3-----------')
#第5章/完形填空
from transformers import pipeline

unmasker = pipeline("fill-mask")

from pprint import pprint

sentence = 'HuggingFace is creating a <mask> that the community uses to solve NLP tasks.'

t = unmasker(sentence)
print(t)

print('-----------4-----------')
from transformers import pipeline

text_generator = pipeline("text-generation")

t = text_generator("As far as I am concerned, I will",
               max_length=50,
               do_sample=False)

print(t)

'''

print('-----------5-----------')
#第5章/命名实体识别
from transformers import pipeline

ner_pipe = pipeline("ner")

sequence = """Hugging Face Inc. is a company based in New York City. Its headquarters are in DUMBO,
therefore very close to the Manhattan Bridge which is visible from the window."""

for entity in ner_pipe(sequence):
    print(entity)


print('-----------6-----------')



#第5章/文本摘要
from transformers import pipeline

summarizer = pipeline("summarization")

ARTICLE = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, 
sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, 
she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree,"
 referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, 
who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly
 sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 
1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, 
and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""

summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)

print('-----------7-----------')
#第5章/翻译
from transformers import pipeline

translator = pipeline("translation_en_to_de")

sentence = "Hugging Face is a technology company based in New York and Paris"

translator(sentence, max_length=40)


'''

print('-----------8-----------')
#第5章/替换模型执行中译英任务
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

#要使用该模型，需要安装sentencepiece
# !pip install sentencepiece
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

translator = pipeline(task="translation_zh_to_en",
                      model=model,
                      tokenizer=tokenizer)

sentence = "我叫萨拉，我住在伦敦。"

t = translator(sentence, max_length=20)
print(t)


print('-----------9-----------')
#第5章/替换模型执行英译中任务
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

#要使用该模型，需要安装sentencepiece
# !pip install sentencepiece
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")

translator = pipeline(task="translation_en_to_zh",
                      model=model,
                      tokenizer=tokenizer)

sentence = "My name is Sarah and I live in London"

t = translator(sentence, max_length=20)
print(t)
