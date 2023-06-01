'''
amadeus.logic - A Simple Logic
@author: Sh'kyra Jordon
------------------------------
'''
from logic import Clause, Literal, Rule
from argumentation import Case
from itertools import product, chain
from functools import reduce
from operator import concat

class KnowledgeBase():
    """
    A knowledge base (KB) which is capable of:
        - Creating a simple logic* KB by either:
            - Taking a collection of Clauses and Rules and recreating a set of
                Literals, Clauses and Rules from them
            - Reading in simple logic KB contents from a text-file in prolog
                syntax, and creating sets of corresponding Literals, Clauses
                and Rules.
            - Taking a string representation of a simple logic KB from a string
                in prolog syntax and creating sets of corresponding Literals, Clauses
                and Rules.
        - Generating a Case** instance for every Literal instance in the KB
            (with which it mutually references), and prompting these Cases to
            populate their supports (their "support" attributes).
            
    (*) This system assumes the same (simple) base logic (Besnard & Hunter
        2014) and consistency with prolog syntax as logic.py (see preamble of
        logic.py).
    (**)This system also uses the notion of Cases, Arguments and "support"
        used by argumentation.py (see preamble of argumentation.py).
        
    Note that this knowledge base forbids the inclusion of cycles.
    
    Properties:
        clauses (set of Clauses):
             A set of all Clauses in the KB
        rules (set of Rules):
            A set of all Rules in the KB
    """
  
    def __init__(self, *contents):
        """
        Parameters:
            contents (iterable of Clauses and Rules | str):
                The contents intended for this KB.
                This may be:
                    - One or more Clause or Rule objects
                    - a str representing either a simple logic prolog-syntax KB,
                        or the filename of text-file containing the same. 
        Return type: None
        
        Note that if a KB is created from Clauses and Rules, any references to
            these Clauses or Rules, or the Literals they were built with, will
            not point to any members within the new KB. These are recreated for
            use in the new KB.
        """
        # GETTING KB CLAUSES, RULES AND LITERALS:
        
        # If contents has only one element, if it is of type str, assume it is
        #     a simple logic prolog-syntax string, or the filename to a
        #     text-file containing the same.
        if len(contents) == 1 and isinstance(contents[0], str):
            # Use PrologString to convert contents[0] into a set of Clauses and
            #     a set of Rules, where contents[0] can be either a simple
            #     logic prolog-syntax string, or a filename to a text-file
            #     containing the same.
            ps = PrologString(contents[0]) 
            
            # Get the dict mapping the str reprsentation of Literal instances to
            #     their unique instances. Note that these are the exact Literal 
            #     instances ps's Clauses and Rules reference. 
            self._literals_dict = ps.literals 
            self._clauses = ps.clauses  # Set of all Clauses
            self._rules = ps.rules      # Set of all Rules
        
        # Otherwise, assume contents are all Clause and Rule instances, and
        #     create a KB from them. Note that this method recreates all
        #     Literals, Clauses and Rules to ensure:
        #      - All Clauses and Rules point to the same set of Literal 
        #         instances
        #      - No Cases associated with foreign KBs accidentally make their
        #         their way into this KB through association with a reused
        #         Literal
        # Note that this means references to the old Literal, Rule and Clause
        #     instances that this KB is made from will not point to those in the
        #     new KB
        else:      
            # The dict mapping the str reprsentation of Literal instances to
            #     their unique instances. Note that these will be the exact
            #     Literal instances our Clauses and Rules will reference.
            self._literals_dict = dict()   
            self._clauses = set()  # to store Clause instances
            self._rules = set()    # to store Rule instances

            for content in contents:
                if isinstance(content, Clause):
                    # Consolidation of the Literals in content.literals
                    literals = self._consolidate_literals(content.literals)
                    # Creating a new Clause from these literals and storing.
                    self._clauses.add(Clause(*literals))
                elif isinstance(content, Rule):
                    # Consolidation of the Literal in content.head
                    head = self._consolidate_literal(content.head)
                    # Consolidation of the Literals in content.body
                    body = self._consolidate_literals(content.body)
       
                    # Creating a new Rule from this head and body, then storing.
                    self._rules.add(Rule(head, *body))
                else:
                    raise TypeError("Cannot add content of type {} to a KnowledgeBase".format(type(content).__name__))
        
        self._clauses, self._rules = frozenset(self._clauses), frozenset(self._rules)  # helps with hashability of KB
        # TODO: Add cycle checking and forbid KB contents (abort) if cyclic.
        
        
        # GETTING MAPPINGS FROM STR REPRESENTATIONS OF LITERALS TO:
        #     - THE CLAUSES THAT ASSERT THEM
        #     - THE RULES THAT ASSERT THEM
        
        # For each Literal L in self._literals_dict.values(), get the set of
        #     Clauses that assert it in a dict, indexed by str(L).
        self._asserting_clauses = self._get_asserting_clauses()

        # And do the same for Rules;
        # For each Literal L in self._literals_dict.values(), get the set of
        #     Rules that assert it (as its head) in a dict, indexed by str(L).
        self._asserting_rules = self._get_asserting_rules()
        
        # For each Literal L in self._literals_dict.values(), create a Case instance
        # C such that L.case = C and C.claim = L.
        self._cases = self._generate_cases()
        
        # ASSOCIATING ALL CASES WITH THEIR SUPPORTING CLAUSES AND RULES:
        #     - This process is prompted when is_entailed() called on a Case
        self._supported_literals = {k : v for k,v in self._literals_dict.items() if v.is_entailed}
    
    @property  # no setter for clauses
    def clauses(self):
        return self._clauses
    
    @property  # no setter for rules
    def rules(self):
        return self._rules
    
    @property  # mo setter fpr cases
    def cases(self):
        return self._cases
    
    def _consolidate_literal(self, l):
        """
        Function that returns the original version of Literal l in self._literals_dict, or adds it if there is no original, and returns l.
        """
        if not str(l) in self._literals_dict:  # If l is a new Literal
            self._literals_dict[str(l)] = Literal(l.atom, l.is_positive)  # Recreate and add to self._literals_dict
        return self._literals_dict[str(l)]  # And return our unique instance
    
    def _consolidate_literals(self, literals):
        """
        Function that runs self._consolidate_literal on an iterable of Literals,
            and returns as a set
        """
        return set([self._consolidate_literal(l) for l in literals])
        
    def _get_asserting_clauses(self):
        """
        # For each Literal in literals, get the set of Clauses that assert it
        # Then put these sets in a dictionary, indexed by the str representation of the Literal they assert.
        """
        literals = self._literals_dict.values()  # Set of all Literal instances
        return {str(l) : set([clause for clause in self.clauses if l in clause.literals]) for l in literals}
    
    def _get_asserting_rules(self):
        """
        For each Literal in literals, get the set of Rules that assert it as its head
        # Then put these sets in a dictionary, indexed by the str representation of the Literal they assert.
        """
        literals = self._literals_dict.values()  # Set of all Literal instances
        return {str(l) : set([rule for rule in self.rules if l == rule.head]) for l in literals}
    
    def _generate_cases(self):
        """
         This function generates the Cases for each unique Literal instance in
             this KB. Each Case mutually references its corresponding Literal
             instance, also referencing the KB it belongs to.
         """
        literals = self._literals_dict.values()  # Set of all Literal instances
        cases = set()
        for l in literals:
            # Assign a Case instance to each literal  (calling l's one-time
            #     setter for l.case)
            l.case = Case(l, self)
            cases.add(l.case)  # Then add this Case instance to cases.
        return cases
    
    def __str__(self):
        """Returns a string representation of the KnowledgeBase contents in prolog syntax"""
        return "".join(["{}\n".format(str(s)) for s in self.clauses.union(self.rules)])
         
class PrologString():
    """
    A string representation of (simple logic) prolog-syntax Clauses and Rules
        that can be converted to a set of corresponding Clause and Rule objects.
    
    Properties:
    
        
    
    @param s: A (simple logic) prolog-syntax string of Clauses and Rules, or the
        filename of a text-file containing the same.
    @type s: str
    """
    
    def __init__(self, s):
        if isinstance(s, str):
            try:
                with open(s) as infile:
                    s = infile.read()
            except (FileNotFoundError, OSError) as err:
                pass  # If not a file, assume s is intended to be a prolog-syntax string.
                # TODO: A check to see if s is in prolog syntax can be implemented; If it is not in prolog syntax, raise. Otherwise, pass.
            
            self._literals_dict = dict()  # to hold the Literal instances shared between Clauses and Rules
            self._clauses, self._rules = self._parse(s)
        else:
            raise TypeError("PrologString takes a str input of a (simple logic) prolog-syntax knowledge base, or the filemame of a textfile containing the same. Invalid input: {}".format(repr(s)))
  
    @property  # no setter for clauses
    def clauses(self):
        return self._clauses

    @property  # no setter for rules
    def rules(self):
        return self._rules
    
    @property  # no setter for literals
    def literals(self):
        return self._literals_dict

    def _parse(self, s):
        """Turns a string s in Prolog syntax into a set of Clauses and a set of Rules."""
        
        clauses = set()
        rules = set()
        # TODO: Add syntax checks to ensure Clauses and Rules are in correct prolog-syntax before passing to the parsers.
        for p in s.split("."):  # Splitting s into statements
            p = p.strip()
            if p == "":  # Ignore empty strings (e.g trailing whitespace after last '.').
                continue
            elif ":-" in p:  # If ":-" in p, assume p is a Rule
                rules.add(self._parse_rule(p))
            else:  # Otherwise assume p is a Clause
                clauses.add(self._parse_clause(p))
        return clauses, rules
                
    def _parse_rule(self, s):
        """Takes a string s, splits it around ':-', and assumes only 2 substrings will result from this, s1 and s2.
            Strips whitespace from s1 and assumes it is a (simple logic) prolog-syntax Literal.
            Converts s1 to its corresponding Literal with _parse_literal(s), and sets head equal to this Literal.
            Strips whitespace from s2 and assumes it is a string of comma separated (simple logic) prolog-syntax Literals.
            Converts s2 to a set of the corresponding Literals with _parse_literals(s), and sets body equal to this set.
        """
        head, body = s.split(":-")    
        head = self._parse_literal(head.strip())
        body = self._parse_literals(body.strip())
        return Rule(head, *body)
        
    def _parse_literal(self, s):
        """
        s is assumed to be a string of a (simple logic) prolog-syntax Literal.
        Takes a string s, strips whitespace from s, and checks for '~' in s[0]:
            If s[0] != '~', s is taken as a positive literal, and Literal(s) is returned.
            Otherwise, s is taken as a negative literal, and Literal(s, False) is returned.
        """
        s = s.strip()  # shouldn't need this since all functions that call this method strip s before call, but redundancy just in case.
        if not s in self._literals_dict:  # If we have not encountered this literal before
            if s[0] == "~":  # If this is a negative Literal
                literal = Literal(s[1:], False)
            else:  # Otherwise this is a positive Literal
                literal = Literal(s)
            self._literals_dict[s] = literal  # Add this Literal to all the set of all Literals
        return self._literals_dict[s]  # And return it
    
    def _parse_literals(self, s):
        """
        s is assumed to be a string of comma separated (simple logic) prolog-syntax Literals.
        This function:
            Takes s, splits it around ','s, and strips the whitespace from these substrings.
            The substrings are assumed to be literals and are converted as such with _parse_literal(s).
            The resulting Literals are returned in a set.
        """
        literals = set()
        for l in s.split(","):  # Split s into literals
            l = l.strip()
            if l != "":  # Ignore e.g the railing whitespace after the last ','
                literals.add(self._parse_literal(l))
        return literals
    
    def _parse_clause(self, s):
        """
        s is assumed to be a (simple logic) prolog-syntax Clause.
        This function:
            Takes s, obtains a set of its Literals with with _parse_literals(s).
            These Literals are used to instantiate a Clause, which is then returned.
        """
        literals = self._parse_literals(s)
        return Clause(*literals)
    
    def __str__(self):
        return super().__str__()    

        
if __name__ == "__main__":
    """ FOR TESTINNG THAT KnowledgeBase INPUT METHODS ALL FUNCTION THE SAME """
#     kb = """
# beta. alpha, beta.
# beta:- alpha. ~gamma:- beta."""
#     KB1 = KnowledgeBase(kb)
#     KB2 = KnowledgeBase("test file input to KB.txt")
#     KB3 = KnowledgeBase(Clause( Literal("beta") ),
#                         Clause( Literal("alpha"), Literal("beta") ),
#                         Rule( Literal("beta"), Literal("alpha") ),
#                         Rule( Literal("gamma", False), Literal("beta") ))
#     
#     print("KB1:", str(KB1).replace("\n", " "))
#     print("KB2:", str(KB2).replace("\n", " "))
#     print("KB3:", str(KB3).replace("\n", " "))
#     
#     print("KB1's Literals:", *KB1._literals_dict.values())
#     print("KB2's Literals:", *KB2._literals_dict.values())
#     print("KB3's Literals:", *KB3._literals_dict.values())
# 
#     print("KB1's dict of asserting clauses:", KB1._asserting_clauses)
#     print("KB2's dict of asserting clauses:", KB2._asserting_clauses)
#     print("KB3's dict of asserting clauses:", KB3._asserting_clauses)
# 
#     print("KB1's dict of asserting rules:", KB1._asserting_rules)
#     print("KB2's dict of asserting rules:", KB2._asserting_rules)
#     print("KB3's dict of asserting rules:", KB3._asserting_rules)

    """ FOR GETTING ALL ARGUMENTS IN A KNOWLEDGE BASE """
    """
    Let's create the following knowledge base with prolog syntax:
        MEANINGS OF LITERALS:
            happy                          := I am happy
            work_well                      := I work well
            sunny                          := It is sunny
            stay_home                      := I stay home
        MEANING OF CLAUSES:
            sunny, stay_home.               := It was sunny and I stayed home
        MEANING OF RULES:
            ~happy :- sunny, stay_home.     := If it is sunny and I stay home, I am not happy
            ~work_well :- stay_home.        := If I stay home, I do not work well
            happy :- stay_home.             := If I stay home, I am happy
            work_well :- happy.             := If I am happy, I work well
    """
    prolog_kb = """
        sunny, stay_home.
        ~happy :- sunny, stay_home.
        ~work_well :- stay_home.
        happy :- stay_home.
        work_well :- happy.
    """
   
#     prolog_kb = "a:- b. b:-c. a:-c. a. b, c."

    kb = KnowledgeBase(prolog_kb)
    
    print("KB:", kb, sep="\n")
    for case in kb.cases:
        print("claim:", case.claim, "\n\tclauses:", *case.asserting_clauses, "\n\trules:", *case.supporting_rules)
    
    def rule_supporting_evidence(r):
        """
        Returns a collection (generator) of sets of supporting evidence for Rule r.
        """
        yield from (reduce(set().union, ccose).union({r})  for ccose in product(*(literal_supporting_evidence(l) for l in r.body)))
        """
        Equivalent to:
        antecedent_evidence_items = [literal_supporting_evidence(l.case) for l in r.body]
        for antecedent_evidence_item in product(*antecedent_evidence_items):
            yield reduce(set().union, antecedent_evidence_item).union({r})
        """ 
    
    def literal_supporting_evidence(l):
        """
        Returns a collection (generator) of sets of supporting evidence for the Literal l.
        """
        c = l.case
        yield from ({clause} for clause in c.asserting_clauses)  # base step: yield each asserting clause of l as a set
        yield from chain.from_iterable((rule_supporting_evidence(r) for r in c.supporting_rules))  # recursive step: yield each collection of supporting evidence for (supported) asserted rules of l (as a set)

    for l in kb._supported_literals.values():
        print("\nArguments for {}:".format(l))
        supporting_evidence = chain.from_iterable((rule_supporting_evidence(r) for r in l.case.supporting_rules))
        print(*supporting_evidence, sep=" ")
    