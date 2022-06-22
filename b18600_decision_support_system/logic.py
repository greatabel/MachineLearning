"""
amadeus.logic - A Simple Logic
@author: Sh'kyra Jordon
------------------------------

This system assumes the following (simple logic) base logic (Besnard & Hunter
2014) and is consistent with the prolog syntax:

    Atoms:
        An atom is an atomic formula (as in mathematical logic), aka an atomic
        logical assertion.
        
        - Atoms are denoted by some alpha-numerical string that accepts 
            underscores, and contains at least one non-numerical character).
        
        Example atoms include:
            - a
            - FranceIsCold
            - James_passed_module_CM1234
            
    Literals:
        Literals are positive or negative:
            - Positive literals assert some atom, denoted "a" for atom "a"
            - Negative literals assert the logical complement (as in
                mathematical logic) of some atom, denoted "~a" for atom "a"
        and thus literals are either atoms, or their logical complements.
        
        Example literals include:
            - a
            - ~a
            - FranceIsCold
            - ~FranceIsCold
            - James_passed_module_CM1234
            - ~James_passed_module_CM1234
    
    Negation:
        The negation of a literal with atom "a" is a literal that asserts the
        logical complement of "a" (as describe above), and is denoted "~a". 
        
        - Negation may only be performed on literals.
        
    Clauses:
        Clauses are in the form, where all a_i are literals the clause asserts
        in conjunction:
            a_1, a_2, ..., a_n.    (for positive integer n)
        
        - x, y denotes logical conjunction between literals x and y.
        - . denotes the end of a clause.
        - There is no logical disjunction in this definition of simple logic.
        - Thus, all clauses are in conjunctive negation normal form, with the
            absence of logical disjunction as a binary operator. 
        
        Note that conjunctions of clauses are equivalent to a single clause,
        and can be reduced as such.
        For example, since brackets are included in the syntax for simple
        logic:
            (a_1, a_2), (b_1, b_2).
        would be written as its equivalent
            a_1, a_2, b_1, b_2.
        Note also that a clause may consist of only a single literal.
    
    Rules:
        Rules are in the form:
            b :- a_1, a_2, ..., a_n.    (for positive integer n)
        where b is a (consequent) literal and a_i are a (antecedent) literals.
        
        - :- denotes modus ponens, the only proof rule in this definition of
            simple logic.
        - . denotes the end of a rule.
        
        Thus a rule asserts that its consequent logically follows (by the modus
        ponens rule of inference) from its antecedent.
    
    Statements:
        Clauses and rules are considered whole logical statements.
        
        - . denotes the end of a logical statement.
    
    Knowledge base (KB):
        A knowledge base is a collection of logical statements.
        
        Note: A KB's "content" refers to the clauses and rules it asserts.
        
    Containment:
        A literal is contained in its knowledge base if, within it, there exists
            a clause that asserts it.
            
        Any clause from the set of asserting clauses of a literal provides
            sufficient evidence of that literal's containment.
    
    Entailment:
        A literal is entailed by its knowledge base if, within it, there exists
            a rule that asserts this literal as its consequent, and all the
            antecedent literals of this rule are either contained, or entailed
            by the knowledge base.
        
        Any rule from the set of rules that assert a literal (as its consequent),
            and contain only contained or entailed antecedent literals, provides
            sufficient evidence of that literal's entailment.

This system also uses the notion of Cases and "support" used by
    argumentation.py (see preamble of argumentation.py).
"""
# TODO: Should CCoSE's be minimal sets?
from ast import literal_eval

class Literal():
    """
    An object representing a simple logic literal that asserts either an atom,
        or its logical complement.
    
    Properties:
        atom (str):
            The string representation of this Literal's atom. This is
            case-sensitive and should be non-empty, containing only chars
            "a-zA-Z0-9_", with at least 1 non-numerical char.
            This is read-only after initialisation.
        is_positive (bool):
            The sign of this Literal; True if positive, False if negative.
            This is read-only after initialisation.
        case (Case):
            The Case instance associated with this Literal. Needs to be set
            first time. Thereafter, it is read-only.
        is_supported (bool):
            True if this Literal/its case is supported by its KB, False if not.
    """
    
    def __init__(self, atom, is_positive=None):
        """
        Parameters:
            atom (str):
                The string representation of this Literal's atom. This is
                case-sensitive and should be non-empty, containing only chars
                "a-zA-Z0-9_", with at least 1 non-numerical char.
            is_positive (bool | None): 
                The sign of this Literal; True if positive, False if negative.
        Return type: None
        """
        # TODO: Implement checks to ensure atom is a nonempty str in the right format (a-zA-Z0-9_ with at least one non-numerical char).
        #     Currently this property is assumed.
        self._atom = atom
        if is_positive is None:  # If is_positive is not passed, assume is True
            is_positive = True
        # TODO: Implement check to ensure is_positive is bool, if not None.
        #     Currently this property is assumed.
        self._is_positive = is_positive
        
    @property  # no setter for atom; this value should not change.
    def atom(self):
        return self._atom
    
    @property  # no setter for is_positive; this value should not change.
    def is_positive(self):
        """Getter for this Literal's sign; True if positive, False if negative."""
        return self._is_positive

    @property  # Raises AttributeError if called before self.case has been set.
    def case(self):
        return self._case
    # TODOD: Where this function is called, deal with AttributeError if raised.
    
    @case.setter  # The value of case can only be set once.
    def case(self, case):
        """
        One-time setter for self.case (to a Case obj); its value does not
            change thereafter.
        """
        if hasattr(self, "_case"):  # If not first time setting self.case
            raise AttributeError("attribute value can only be set once, and already has value: {}".format(self.case))
        # TODO: Create check to ensure case is Case object.
        #     Currently this property is assumed
        self._case = case
    
    @property  # no setter for is_contained
    def is_contained(self):
        """
        True if this Literal is contained by the KB, and False if not.
        This value is calculated only once on the first call, and relies on the
            association of a Case object with self.case.
        """
        if not hasattr(self, "_contained"):
            self._contained = self.case.is_contained
        return self._contained
    
    @property  # no setter for is_entailed
    def is_entailed(self):
        """
        True if this Literal is entailed by the KB, and False if not.
        This value is calculated only once on the first call, and relies on the
            association of a Case object with self.case.
        """
        if not hasattr(self, "_entailed"):  # If first call to this method
            # This Literal is supported iff self.case is supported
            self._entailed = self.case.is_entailed  # May return AttributeError if self.case is not set.
        return self._entailed
    
    def is_negation_of(self, other):
        """
        Returns True if other is a Literal that asserts the logical complement
            of this Literal. Returns False otherwise.    
        """
        if isinstance(other, Literal):
            return (self.atom == other.atom) and (self.is_positive != other.is_positive())
        return False
        
    def negated(self):
        """
        Returns a literal instance with the same atom, but an opposite sign
        """
        return Literal(self.atom, not self.is_positive)

    def __str__(self):
        """
        Returns a string representation of this Literal in prolog syntax (w/o a 
            trailing fullstop)
        """
        if not self.is_positive:
            return "~" + self.atom
        return self.atom
    
    def __repr__(self):
        return str(self)
        
    def __eq__(self, other):  # Needed for hashability of Literals
        if isinstance(other, Literal):
            return (self.atom == other.atom) and (self.is_positive == other.is_positive)
        return False
    
    def __hash__(self):  # Needed for hashability of Literals
        return hash((self.atom, self.is_positive))
    
class Clause():
    """
    An object that represents a simple logic clause that asserts a set of
        literals in conjunction.
    
    Properties:
        literals (set):
            A set of the Literal instances this Clause asserts.   
    """
    #TODO Implement checks to ensure literals is a nonempty iterable of Literals       
    def __init__(self, *literals):
        """
        Parameters:
            literals (One or more Literals):
                The Literal instances this Clause asserts in conjunction.
        Return type: None
        """
        self._literals = frozenset(literals)
    
    @property  # no setter for literals
    def literals(self):
        return self._literals
    
    def __str__(self):
        """Returns a string of the Clause instance in prolog syntax"""
        return ", ".join([str(l) for l in sorted(list(self.literals), key=lambda x: str(x))]) + "."
         
    def __eq__(self, other):  # Needed for hashability
        if isinstance(other, Clause):
            return self.literals == other.literals  # these are frozensets
        return False
    
    def __hash__(self):  # Needed for hashability
        return hash(self.literals)

    def __repr__(self):
        return str(self)    

class Rule():
    """
    An object that represents a simple logic rule that, where it asserts that
        its head or "consequent" (Literal) logically follows (modus ponens)
        from the conjunction of the literals in its body or "antecedent" (set
        of Literals).
    
    Properties:
        head (Literal):
            The Literal that represents this Rule's consequent.
        body (set of Literals):
            The Literals which in conjunction represent this Rule's antecedent.
        is_supported (bool):
            True if all Literals in this Rule's body are supported by its KB,
            False if not.
    """
    
    def __init__(self, head, *body):
        """
        Parameters:
            head (Literal):
                The Literal that represents this simple logic Rule's consequent.
            body (set of Literals):
                The Literals which in conjunction represent this simple logic
                Rule's antecedent.
        Return type: None
        """
        # TODO: Implement check to ensure head is Literal.
        #     Currently this property is assumed.
        self._head = head
        # TODO: Implement check to body is a nonempty iterable of Literals.
        #     Currently this property is assumed.
        self._body = frozenset(body)
    
    @property  # no setter for head; this value should not change.
    def head(self):
        return self._head

    @property  # no setter for body; this value should not change.
    def body(self):
        return self._body
    
    @property  # no setter for is_supported
    def is_supported(self):
        """
        True if all Literals in this Rule's body are entailed or contained by
            the KB, and False if not.
        This value is calculated only once on the first call.
        """
        if not hasattr(self, "_supported"):  # If first call to this method
            supported = True  # Assume this Rule is supported
            for l in self.body:
                if not (l.is_entailed or l.is_contained):  # If a literal in self.body is neither entailed, nor contained by its knowledge base
                    supported = False  # If any l is unsupported, so is R.
                    # Keep running through this loop so all literals are asked the questions: "Are you entailed?" and "Are you contained?".
            self._supported = supported
        return self._supported
    
    def __str__(self):
        """Returns a strong of the Rule instance in prolog syntax"""
        return str(self.head) + ":- " + ", ".join([str(l) for l in self.body]) + "."
    
    def __eq__(self, other):  # Needed for hashability
        if isinstance(other, Rule):
            return (self.head == other.head) and (self.body == other.body)
        return False
       
    def __hash__(self):  # Needed for hashability
        return hash((self.head, self.body))
        
    def __repr__(self):
        return str(self)        
        
if __name__ == "__main__":
    
    """
    Let's directly create a few literals with the following meanings:
        happy := I am happy
        work_well := I work well
    """
    happy, work_well = Literal("happy"), Literal("work_well")
    print("Created literals:", happy, work_well, sep="\n\t")
    
    """
    Let's directly create a clause asserting the following literals, with the following meanings:
        sunny := It is sunny.
        stay_home := I stay home
    """
    sunny, stay_home = Literal("sunny"), Literal("stay_home")
    my_day = Clause(sunny, stay_home)
    print("Created clause:", my_day)

    """
    Let's create a few rules to explain some relationships between these literals.
        r1: ~happy :- sunny, stay_home := If it is sunny and I stay home, I am not happy
        r2: ~work_well :- stay_home := If I stay home, I do not work well
        r3: happy :- stay_home := If I stay home, I am happy
        r4: work_well :- happy := If I am happy, I work well
    """
    r1, r2, r3, r4 = Rule(happy.negated(), sunny, stay_home), Rule(work_well.negated(), stay_home), Rule(happy, stay_home), Rule(work_well, happy)
    print("Created rules:", r1, r2, r3, r4, sep="\n\t")