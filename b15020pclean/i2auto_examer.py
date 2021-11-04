from libpgm.graphskeleton import GraphSkeleton
from libpgm.nodedata import NodeData
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.tablecpdfactorization import TableCPDFactorization

"""
The following discussion uses integers 0, 1, 2 for discrete outcomes of each random variable, where 0 is the worst outcome. For e.g, Interview=0 indicates the worst outcome of the interview and Interview=2 is the best outcome.

The first kind of reasoning we shall explore is called 'Causal Reasoning'. Initially we observe the prior probability of an event unconditioned by any evidence(for this example, we shall focus on the 'Offer' random variable). We then introduce observations of (one of) the parent variables. Consistent with our logical reasoning, we note that if one of the parents (equivalent to causes) of an event are observed, then we have stronger beliefs about the Offer random variable.

We start off by defining a function that reads the JSON data file and creating an object we can use to run probability queries on

"""

from spellchecker import SpellChecker
import re


def getTableCPD():
    nd = NodeData()
    skel = GraphSkeleton()
    jsonpath = "datasets/hospital_dirty.csv"
    nd.load(jsonpath)
    skel.load(jsonpath)
    bn = DiscreteBayesianNetwork(skel, nd)
    tablecpd = TableCPDFactorization(bn)
    return tablecpd


tcpd = getTableCPD()
tcpd.specificquery(dict(Offer="1"), {})

tcpd = getTableCPD()
tcpd.specificquery(dict(Experience="1"), {})

tcpd = getTableCPD()
tcpd.specificquery(dict(Experience="1"), dict(Interview="2"))


WORD = re.compile(r"\w+")
spell = SpellChecker()

print('--'*10, 'expeiment')
def reTokenize(doc):
    tokens = WORD.findall(doc)
    return tokens


text = [
    "Hi, welcmoe to speling.",
    "This is jsut an exapmle, but cosnider a veri big coprus.",
]


def spell_correct(text):
    sptext = [
        " ".join([spell.correction(w).lower() for w in reTokenize(doc)]) for doc in text
    ]
    return sptext


print(spell_correct(text))
