liar's paradox
===
# introduction
the liar's paradox can succinctly be described as a self-referencing and self-negating statement, e.g.: 'this statement is not true'. the paradox rises when we try to ascribe a truth value to the statement. if we believe it then it mustn't be true, and if we take it as true, it tells us it is not so. 

we are interested in establishing the truth value of statement under various assumptions. there are four possibilities. a statement may be deemed to be:

1. TRUE AND NOT FALSE
2. FALSE AND NOT TRUE
3. NOT TRUE AND NOT FALSE
4. TRUE AND FALSE

with the goal of exploring the liar's paradox, this software generates and parses logical expressions of a certain type. it applies a customizable set of logical rules to evaluate the truth value of the expressions.

for each statement S, we are interested in evaluating the outpcome of S when operated on by sequences of either of two operators: `{T,N}`, under certain *rules*.

# the components

- S is a **statement** from the set of statements that can only evaluate to either `TRUE` or `NOT TRUE`. note that `NOT TRUE` is **not** identical to FALSE (!). `NOT TRUE` merely negates that the statement is `TRUE`. the statement may still be FALSE, or it may be 'unknowable', NULL, 'undefined', etc.
    + the minimal statement, S, is merely something that evaluates to either `TRUE` or `NOT TRUE`.
    + let `S --> TRUE` denote the fact that the statement S evaluates to TRUE
    + let `S --> NOT TRUE` denote the fact that the statement S does not evaluate to `TRUE`, (i.e. S is `NOT TRUE`)
- {T,N} are **operators** acting on statements, yielding new statements (so they can be chained). it is best to not define the meaning of the operators except via the rules that describe their effect. still:
    - N resembles a **logical negation** operator
    - T resembles a **logical truth assertion** operator. 
- an expression, X, is a statement that results from S being operated on by a sequence of operators. we construct a number of example expressions: $X \in {S, NS, TS, NNS, NTS, TNS, TNS, TTS, NNNS, NNTS, NTNS, NTTS, TNNS, TNTS, TTNS, TTNS, TTTS, ..., TTTTTTS}
- the **rules** are as follows:
    + a) `iff  X --> TRUE     then  TX--> TRUE` 
    + b) `iff  X --> NOT TRUE then  TX--> NOT TRUE`
    + c) `iff TX - > NOT TRUE then NTX--> TRUE`
    + d) `iff TX --> TRUE     then NTX--> NOT TRUE`

## notes on the rules
- when applicable, rule c) overrides rule b)
- the rules say nothing about how to evaluate `NX` when `X --> TRUE`
- the rules say nothing about how to evaluate `NX` when `X --> NOT TRUE` and `X`'s latest previous operator isn't `T`
    + consider `S --> NOT TRUE`


# the task
the task is to note that given the above, even when an expression X evaluates to `NOT TRUE` in some cases, an operator operating on that expression yields an expression that is `TRUE`. the challenge here is to map out those cases. in short, the task is to consider a large sample of statements X, and find all those that evaluate to `TRUE` under the rules as stated. 
