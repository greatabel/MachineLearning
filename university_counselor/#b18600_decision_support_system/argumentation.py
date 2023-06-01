'''
amadeus.logic - A Simple Logic
@author: Sh'kyra Jordon
------------------------------

This system assumes the same (simple) base logic (Besnard & Hunter 2014) and
    consistency with prolog syntax as logic.py (see preamble of logic.py).

This system also uses a notion of cases and "support" built on this
(simple logic) base logic, and so, given a knowledge base:
    Support:
        A rule supports its consequent (head) literal with respects to its
            knowledge base KB, if every literal in its antecedent (body) is
            either contained by, or entailed by, KB. 
    Case:
        A case is in the form:
            (claim, asserting_clauses, supporting_rules)
        where:
            - claim is a literal.
            - asserting_clauses is a set of all clauses in the knowledge base
                that assert this case's claim.
            - supporting_rules is a set of all supported rules in the knowledge
                base that assert our claim as their consequent.
            
        Note: All arguments for a claim can be produced from a claim's case.
        
    (*) Given a knowledge base KB, a COMPLETE COLLECTION OF SUPPORTING EVIDENCE
        (CCoSE) is:
    
        For a LITERAL:
            A CCoSE FOR AN ENTAILED LITERAL L:
                Given a literal L entailed by KB, a CCoSE of L is:
                    - A set containing a rule R in KB that supports L, and a
                        CCoSE of R.
        For a RULE:
            A CCoSE FOR A RULE R THAT SUPPORTS ITS CONSEQUENT LITERAL L wrt KB:
                Given a rule R that supports its consequent literal L, a CCoSE
                    of R is:
                    - A set containing, for every antecedent literal L_i, a set
                        of supporting evidence for either the containment of,
                        or entailment of L_i by KB.

    (**) Note: Any union of supporting evidence sets for the containment or
        entailment of the antecedent literals L_i of a rule R, where each L_i
        contributes exactly one such set to this union, is a CCoSE of R.
'''

class Case():
    
    def __init__(self, literal, knowledgebase):
        self._claim = literal
        self._kb = knowledgebase
        self._asserting_clauses = frozenset(self.kb._asserting_clauses[str(self.claim)])
        self._asserting_rules = frozenset(self.kb._asserting_rules[str(self.claim)])
    
    @property  # no setter for claim
    def claim(self):
        return self._claim
    
    @property  # no setter for kb
    def kb(self):
        return self._kb
    
    @property  # no setter for asserting_clauses
    def asserting_clauses(self):  
        return self._asserting_clauses
    
    @property  # no setter for asserting_rules
    def asserting_rules(self):
        return self._asserting_rules
    
    # Initiates is_entailed for this case (which in turn value for self.supporting_rules)
    
    @property  # no setter for supporting_rules
    def supporting_rules(self):
        if not hasattr(self, "_supporting_rules"):
            self.is_entailed  # This function will calculate self._supporting_rules
        return self._supporting_rules
    
    @property
    def is_contained(self):
        if not hasattr(self, "_contained"):  # If we haven't done this check before, calculate its value     
            self._contained = False  # First assume self.claim is not contained in self.kb  
            self._asserting_clauses = frozenset(self.kb._asserting_clauses[str(self.claim)])  # Get all supporting clauses in the self.kb for self.claim
            if len(self._asserting_clauses) != 0:  # If there exists any clauses in self.kb that assert self.claim
                self._contained = True  # Then self.claim is contained in self.kb
        return self._contained
    
    # Generates self.supporting_rules
    @property
    def is_entailed(self):
        if not hasattr(self, "_entailed"):  # If we haven't done this check before, calculate its value     
            entailed = False  # Assume self.claim is not entailed by self.kb   
            # Check for supporting Rules in the KB (i.e supported Rules that assert self.claim)
            self._supporting_rules = set()
            for r in self.asserting_rules:
                if r.is_supported:
                    entailed = True  # If any such rules exist, self.claim is supported
                    self._supporting_rules.add(r)
                    # Keep checking through all asserting_rules so all _supporting_rules can be found
            self._supporting_rules = frozenset(self._supporting_rules)  # for hashability
            self._entailed = entailed
        return self._entailed
    
    def __str__(self): ###### TEMPORARY
        return "({" + " ".join([str(c) for c in self._asserting_clauses] + [str(r) for r in self._asserting_rules]) + "}, " + str(self.claim) + ")" 
    
    def __repl__(self):
        return str(self)
    
    def __hash__(self):
        return hash((self.claim, self.kb))
    
    def __eq__(self, other):
        if isinstance(other, Case):
            return (self.claim == other.claim) and (self.kb == other.kb)
        return False