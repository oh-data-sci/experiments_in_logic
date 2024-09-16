liar's paradox
===
# introduction
the liar's paradox can succinctly be described as a self-referencing and self-negating statement, e.g.: 'this statement is FALSE'. the paradox rises when we try to ascribe a truth value to the statement. if it is TRUE, we should believe when it tells us it is FALSE. 

we are interested in establishing the truth value of that statement under various cases of assumptions. there are four possibilities. a statement may be deemed to be:

1. TRUE & NOT FALSE
2. FALSE & NOT TRUE
3. NOT TRUE & NOT FALSE
4. TRUE & FALSE

with the goal of exploring the liar's paradox, this software generates and parses logical expressions of a certain type. it applies a customizable set of logical rules to evaluate the truth value of the expressions.



# logical sequences
the first piece of code generates a sequence of expressions as strings like 'NNNTTNTTNTTTNS'. where

- S is a **statement** from the set of statements that can only evaluate to either TRUE or FALSE (S never evaluates to 'maybe', 'sometimes', nor 'unevaluatable', 'NA', 'NULL' or such),
- N is the the **logical negation** operator: given input statement S, N operating on it *generates a new statement*. the output, NS, is the logical complement to S. this amounts to flipping S , NS = NOT S = !S.
- T is another operator that can be applied to statements. it closely resembles the **logical test operator** that checks the truth value of its input. however, it is not identically the same, and we have to be careful not to assume its behaviour matches it.

we construct a number of example expressions by applying a sequences of the operators {T,N} acting on S, e.g.:
{S, NS, TS, NNS, NTS, TNS, TNS, TTS, NNNS, NNTS, NTNS, NTTS, TNNS, TNTS, TTNS, TTNS, TTTS, ..., TTTTTTS}


first, it may be useful to weed out the difference between boolean logical value and the truth value that we are after here. this is perhaps more clear to do via some example statements:

    |---------------------------------------------------------|
    | statement              | booelan | truth value          |
    |------------------------|-------- |----------------------|
    | S1:  2+2=5             | FALSE   |  NOT TRUE            |
    | NS1: (2+2!=5)          | TRUE    |  TRUE                |
    | S2: 2+2=4              | TRUE    |  TRUE                |
    | NS2: (2+2!=4)          | FALSE   |  NOT TRUE            |
    | S:  my_house           | NA      |  NOT TRUE/NOT FALSE  |
    | NSl: -(my_house)       | NA      |  NOT TRUE/NOT FALSE  |
    | Sl: 'Sl is not true'   | NA      |  TRUE/NOT TRUE       | *) depending on evaluation rules
    | Sm:  ?????             | ~FALSE  |  NOT TRUE            | 
    |                        |         |                      |



# expression parsing rules
rather than rely on intuition or the definition of the operators {N, T} and assume their properties we should only think of them as placeholders that the rules (see below) are

we also have a set of rules to parse and compress repeated applications of the operators:
- **a)** if  S evaluates to TRUE,  then  TS evaluates to TRUE
- **b)** if TS evaluates to FALSE, then NTS evaluates to TRUE
- **c)** if  S evaluates to FALSE, then  TS --> FALSE (T operator flips FALSE to TRUE,  and TRUE  to TRUE )
- **d)** if TS evaluates to TRUE,  then NTS --> FALSE (N operator flips TRUE  to FALSE)

as well as the following simplifying heuristics:
- **h1)**  NNS -->  S (double-negation elimination)
- **h2)** TTTS --> TS (triple-truth elimination)

by repeated use of the simplifying heuristics we should be able to compress an arbitrarily long expression into a sequence of powers of the operators applied to the input statement S, e.g.:

    TTTTT FF TT FFFFF T S --> T^5 F^2 T^2 F^5 T^1 S

now, we can compress each segment of repeated operators into a single operator using the heuristics.

- T^n --> T for all n (n in {0,1,2,3,...}) (follows from TS->S, TTS->TS, TTTS->TS)
- N^m --> N iff m is odd (m in {1,3,5,7,...})
- N^l --> T iff l is even (l in {0,2,4,6,8,...})


# the task to be done
first, construct a number of example expressions by applying a sequences of the operators {T,N} acting on S, e.g.:
{S, NS, TS, NNS, NTS, TNS, TNS, TTS, NNNS, NNTS, NTNS, NTTS, TNNS, TNTS, TTNS, TTNS, TTTS, ..., TTTTTTS}

second, select any 2 or 3 of the rules above { a), b), c), d) }

third, for each member of the sample expression set, apply the selected rules iteratively until the truth value of the expression is determined. return, for each expression its resulting value (TS, or NS).

---

### second, some clarifications are needed.

my understanding has a gap somewhere because:

1. i cannot marry my interpretation of the T operator:
   TS evaluates to TRUE  iff S evaluates to TRUE, and to FALSE iff S evaluates to FALSE
 and the statement that "TTS -> TS, and TS -> S are not always theorems" meaning that it is not necessarily true that:
   TTS --> TS, and TS --> S.
 but that means that the expressions FTTS, FTS, and TS cannot be further simplified even when S-->FALSE? i feel like i must be missing something.

2. what does the resolution of the above issue mean for the interpretation of the F operator? i.e.
   "FS evaluates to FALSE iff S evaluates to TRUE, and to TRUE  iff S evaluates to FALSE"

3. i am not sure, for a given set of rules to apply, what effect the order of precedence of the rules has, and which order to apply them in?


### third, a possibly irrelevant suggestion:
depending on your answer to the required clarification above (again there is a gap in my understanding), what i would have thought we could do is to compress each repeated subsections of any expression sequence, e.g.:
   TTTTT FF TT FFFFF T S --> T^5 F^2 T^2 F^5 T^1 S
and then process, in turn, each compressed subsection with the heuristic:
 g) T^n --> T, for all n in {0,1,2,3,...}
 h) F^m --> F, for all odd  m (m in {1,3,5,7,...}), contradicts rule f)
 i) F^l --> T, for all even l (l in {2,4,6,8,...}), contradicts rule f)
in the case where rule f) is applied, the F operator heuristic changes to:
 h*) F^m --> F, for all odd  m (m in {1,3,5,7,...}),
 i*) F^l --> T, for all even l (l in {2,4,6,8,...}), contradicts rule f)

you may want to not assume the above heuristic but i honestly cannot see a way to interpret the repeated application of an operator in a way that does not obey the above compression?

----

finally, i did play a little bit with a python code for this challenge (as per my understanding above).

i generated a data frame with all possible sequences with up to 10 operators acting on S, and put these 1025 expressions, and their length in a data frame ordered by expression length. that means you can easily view the shorter sequences at the top of the frame or selectively filter out the expressions of any given length.

the evaluation of the rules is trickier and i need more time to finish that up.

my number is 07923901469 if you want to connect over the phone, and we could also set up a time for a zoom call.

all the best.

--
oskar

An introduction to Apache Spark