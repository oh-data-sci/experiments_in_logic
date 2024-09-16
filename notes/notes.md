ruminations on the liar's paradox
===

# introduction
gary wrote me to ask for assistance with python:

    Dear Oscar,
    I hope you are thriving.
    I wonder whether you could help me to fix a very short Python programme which I obtained from CHATGPT. It doesn't work, but it should be easy to fix, might take about an hour. I want to annex it to a paper I've written, which I shall send to a journal soon, as soon as I stop tinkering with it. It already has another even shorter Python programme which does work.
    Happy to come to Worthing any time.
    best regards, Gary

intrgued i offered to help and got more information about what was needed:

    The thing I tried to do is simple. It would be extremely useful to add a couple of complications.
    
    CAVEAT. Do not under any circumstances try to THINK about the problem except as a simple programming problem, otherwise you might go mad and you will not be the first victim. I am not being funny.
    The aim is to evaluate a solution (or, more complicated, five solutions) to the Liar Paradox. The paradox comes from Liar sentences together with four seemingly obvious rules/axioms. A Liar sentence is a sentence X which = 'X is not true'. For the simple solution, I have tried to do the work myself but it took four attempts, it's almost impossible not to make a mistake, and I would like to check that I got it right the fourth time. Saul Kripke's 1975 solution is slightly more complicated, and so are a couple of others.
    Simple programme

    1    Get Python to generate all the strings/sentences like this, where A is a constant. A, NA, TA; then NNA, NTA, TNA, TTA; then TNNA, TNTA, TTNA, TTTA, and NNNA, NNTA, NTNA, NTTA; then NNNNA etc. So it's like coin tossing, H, T, HH, HT, TT, TH etc. I think a maximum length of 6 or 7 is enough, and we don't want a printout with 2 to the power of n+1 results for n>6 or 7. The logicians are not satisfied unless they can prove that their theory works for sentences of infinite length (ie. omega if not omega to the omega or epsilon0 whatever that is), but I don't care. Let's start with 3 and then 4 because then I can check that the programme works.
    2    Get Python to evaluate each sequence according to the following definition and two rules, where S is a variable ranging over strings/sentences up to length n.
    DF)    if S is true then NS is false. (This just defines 'false' We don't need to operate on the false Ss.)
    a)    if S is true then TS is true
    b)    if TS is not true, then NTS is true.
    CHATGPT screwed up by generating some strings and then trying to evaluate each one individually using the rules. But the only way to do it is by first evaluating the two shortest strings NA and TA, and then the next four with three bits, and then the eight with four bits etc. until it gets to the length limit.
    3    Get Python to print the results: one set of true sentences and one set of false sentences, starting with the shortest. If there are any left over, which there should not be, that would be a third set.
    4    It would help to have a couple of sentence-shortening rules before printing them all.
    DNE)    NNS -> S (double-negation elimination)
    TTE)    TTTS -> TS (triple-truth elimination: a theorem of all the theories. TTS -> TS, and TS -> S are not always theorems). It's possible that I will need to rethink this rule.

    More complicated programme
    5.    Add two more evaluation rules and give users the opportunity to choose either two or three of the evaluation rules (a b c and d). The whole set of four rules is known to be inconsistent, and might cause the thing to crash.
    c)    if S is not true then TS is true
    d)    if TS is true, then NTS is not true
    6    Allow Liar sentences, i.e a sentence X plus the rule that NTX -> X. This should cause the whole set (a b c d) to crash but should not cause any subset to crash.
    If we can get the simple programme to work, it would reassure me. If we can get the complicated one to work, it would be interesting, it might be useful to others, and I will annex it to my paper with thanks to you.

    Let me know if this email doesn't make sense. If it does make sense, I can then send you the programme that I got from CHATGPT (or the whole chat before it cut me off) which does at least set up some useful-looking functions, and should be easy enough to modify.
    best wishes always,
    Gary


# first stab at the problem
i tried rephrasing the problem and feed back to gary to verify my understanding. 

### definitions
given
 - a statement S, from the set of statements that can only evaluate to either TRUE or FALSE, and
 - operators {T,F} that operate on the statements of this set, such that:
   - TS evaluates to TRUE  iff S evaluates to TRUE, and to FALSE iff S evaluates to FALSE
   - FS evaluates to FALSE iff S evaluates to TRUE, and to TRUE  iff S evaluates to FALSE
 - a set of rules to parse and compress repeated applications of the operators:
   a) if  S evaluates to TRUE,  then  TS evaluates to TRUE # can we also assume TS -- when S is FALSE?
   b) if TS evaluates to FALSE, then FTS evaluates to TRUE
 - and the following simplifying heuristic rules
   c)  FFS -->  S (double-negation elimination)
   d) TTTS --> TS (triple-truth elimination),

### tasks to be done

- first, construct a number of example expressions by applying a sequences of the operators {T,F} acting on S, e.g.:
    + {S, FS, TS, FFS, FTS, TFS, TFS, TTS, FFFS, FFTS, FTFS, FTTS, TFFS, TFTS, TTFS, TTFS, TTTS, ..., TTTTTTS}
- second, for each member of the sample expression set, apply rules a), b), c), d) iteratively until the truth value of the expression is determined. return, for each expression its resulting value (TS, or FS).
    + note, that the code cannot assume that
    +    TTS --> TS, and TS --> S,
    + and hence not that:
    +    T^nS --> S for any n in 0,1,2,3...
- third, add _optional_ rules for the evaluation of the expressions:
   + e) if S  evaluates to FALSE then  TS --> TRUE  (T operator flips FALSE to TRUE,  and TRUE  to TRUE )
   + f) if TS evaluates to TRUE  then FTS --> FALSE (F operator flips TRUE  to FALSE, and FALSE to TRUE)

now add flexibility to the expression parser such that the evaluation can be run with any two or any three of the rules in the set:
 { a), b), e), f) }
note that rules c) and d) are always applied.


# gary's clarification:
N is the the **logical negation** operator: given input S, when N operates on it *generates a new statement*. the output, NS, is the logical complement to S. since by definition we are only talking about statements that evaluate to TRUE or FALSE (S never evaluates to 'maybe', 'sometimes', nor 'unevaluatable'), this amounts to flipping S to its logical complement, NS = NOT S = !S.

conversely, F is a **logical test** operator which checks and evaluates its input statement and *outputs a boolean value*. the test for F is whether the statement is FALSE, so that when S=FALSE then FS --> TRUE and vice versa.

similarly, the T operator checks and evaluates the truth its input statement and *outputs a boolean value*. the test for T is whether the statement is TRUE, so TS --> FALSE when S=FALSE.

despite that conceptual difference, when each acts on a sentence S, or is implemented in a python program, there is no longer any difference between them, at least none that can appear in a truth table:

F operator truth table:

    |------------|---------|
    |    S       |   FS    |
    |------------|---------|
    | S is TRUE  |  FALSE  |
    | S is FALSE |  TRUE   |
    |------------|---------|

N operator truth table

    |------------|---------------|
    |    S       |  NS           |
    |------------|---------------|
    | S is TRUE  | X (--> FALSE) | * output is a new statement X which evaluates to FALSE 
    | S is FALSE | X (--> TRUE)  |
    |------------|---------------|

T, F operators operating on statement expressions S and NS:

    |------------|------------|------------|
    | expression | S is TRUE  | S is FALSE |
    |------------|------------|------------|
    | TS         | TRUE       | FALSE      |
    | FS         | FALSE      | TRUE       |
    | TNS        | FALSE      | TRUE       |
    | FNS        | TRUE       | FALSE      |
    |------------|------------|------------|


turns out, we don't need the F operator. we only require


# after the call.
gary and i had a call that clarified a lot of questions.

first of all F is not relevant to this




---



# sequence


what i am getting from you is that the N and the F operators have different meanings that i had not grasped.

N is the the **logical negation** operator: given input S, when N operates on it *generates a new statement*. the output, NS, is the logical complement to S. since by definition we are only talking about statements that evaluate to TRUE or FALSE (S never evaluates to 'maybe', 'sometimes', nor 'unevaluatable'), this amounts to flipping S to its logical complement, NS = NOT S = !S.

conversely, F is a logical test operator which checks and evaluates its input statement and *outputs a boolean value*. the test for F is whether the statement is FALSE, so that when S=FALSE then FS --> TRUE and vice versa.

similarly, the T operator checks and evaluates the truth its input statement and *outputs a boolean value*. the test for T is whether the statement is TRUE, so TS --> FALSE when S=FALSE.


despite that conceptual difference, when each acts on a sentence S, or is implemented in a python program, there is no longer any difference between them, at least none that can appear in a truth table:

F operator truth table:

   |------------|---------|
   |    S       |   FS    |
   |------------|---------|
   | S is TRUE  |  FALSE  |
   | S is FALSE |  TRUE   |
   |------------|---------|

N operator truth table

   |------------|---------------|
   |    S       |  NS           |
   |------------|---------------|
   | S is TRUE  | X (--> FALSE) | * output is a new statement X which evaluates to FALSE
   | S is FALSE | X (--> TRUE)  |
   |------------|---------------|

T, F operators operating on statement expressions S and NS:

   |------------|------------|------------|
   | expression | S is TRUE  | S is FALSE |
   |------------|------------|------------|
   | TS         | TRUE       | FALSE      |
   | FS         | FALSE      | TRUE       |
   | TNS        | FALSE      | TRUE       |
   | FNS        | TRUE       | FALSE      |
   |------------|------------|------------|

am i right that these are the ground rules?

--
Yup. N is logical negation. We don't need your F, but we do need the Boolean values true and (for completeness) false, in the evaluation rules.

The leading theories in this area nearly all say that Liar sentences are neither true nor false. A Liar sentence X is one which is the same as the sentence 'X is not true'. It is the negation of 'X is true'. So 'X is true' is false iff X is true, stupid as that may sound. (Contrast your FTX iff TX)

Looking forward to 4.30!

Gary

----

Oscar, I'm thinking through your important point that sometimes the chosen rules won't give a value to the strings "......S'. That's exactly right.

I think the answer is as follows. I'll try it with rules a) and b).

1    We have to say that S is true. (S can be anything you like, e.g. 'TTTTTA' or '(2+2=5) is true'. If the 'true' in S is in quotes it will not confuse Python.)

2    Then evaluate TS and NS as true or not true. If S is true and rule a) was chosen, then we get TS is true. We don't get NS is true (and we don't want that!) from any of the other rules.

We are only interested in the set of truths. We can also say that, if S is true (and TS is true), then NS is false, and NTS is false, but this doesn't add anything to the set of truths.

Obviously with rule a) we are going to get T^n(S) for n=1 to transfinite. This is Kripke's idea, and we are going to stop it with triple-T elimination.

3    Then do TTS, NTS, TNS and NNS. So rule a) again will give us TTS is true, and the other rules will do nothing (except to say that NTTS is false).

Incidentally, the rules I sent to you do not include the usual rules for negation: true(A) -> not true (not A), and not true(A) -> true(not A). Let's leave that for now. It only makes a small difference at the first one or two stages, where the strings might not have a T in them.

4    Next we do the length-4 strings.

    TTS: T(TTS) will be true, and N(TTS) will not be true (it's false already). We can get rid of TTTS or reduce it to TS.

    NTS: T(NTS) will not be true. N(NTS) will not be true in this system, without DN introduction, and anyway we get rid of it with NN-elimination.

    TNS: NT(NS) will be true according to rule b), because T(NS) is not true. And T(TNS) will not be true.

    NNS: NN-elimination got rid of it. So we don't bother with TNNS, or with NNNS which reduces to NS.

5. Five length strings.

    We got rid of TTTS, leaving NTTS. T(NTTS) is not true but it will feed into rule b) at the next stage, and we can get rid of N(NTTS).

    T(NTS) is not true, so rule b) says that NT(NTS) is true. TT(NTS) is not true.

   NTNS is true, so T(NTNS) is true by rule a), but N(NTNS) can be removed. T(TNS) is not true so NT(TNS) is true . TT(TNS) can be got rid of.

At this point, we have seven truths S, TS, TTS, NT(NS), NT(NTS), T(NTNS) and NT(TNS), and there will be more. Negating these truths gives us seven falsehoods, N(S), N(TS), N(TTS), N(NTNS),  N(NTNTS), N(TNTNS) and N(NTTNS). Total 14. Some other stuff was got rid of, to avoid clutter, total (31-14 = 17 junk); I should probably check them to make sure nothing useful has been lost, only TTTs and NNs.

The idea of the programme is to automate all this stuff to save our brains.

I can't remember if I said we will also need a simplification rule for Liar sentences: NTX -> X.

Bedtime for me,

Gary



   

   









I'm afraid the answer is that there are six pairs of rules. Four of them determine whether S is true or not, or they determine whether TS is true or not. The two exceptions are a)+c) and b)+d). Choosing three rules always determines S and TS.

This means the choice of rules is restricted. Must have either a) or c) AND either b) or d). Then it's a option to choose one more rule to make a total of three. Three rules means two pairs obviously. Can't have all four because they are inconsistent.

I think this means that the choose-rules routine must (for the time being) be controlled to avoid one rule, four rules, and a) + c) and b) +d). We can try to relax the controls later and watch it prove your point.

It also means the choose-rules routine will have to give the following initial assignments to S and TS, before they go off to help with NS, TS, NTS, TNS etc etc

a) + b) -> TS is true

a) + d) -> S is not true

c) + b) -> S is true

c) + d) -> TS is not true



Therefore three rules a) + b) +c) -> TS is true and S is true.


--
this should go better now that i finally understand what you meant by don't think about it. using boolean variables and thinking in terms of logic gates and truth values is the wrong approach because we do not want to utilise their expressive efficiency and live with all the assumptions that they entail. instead, we want to discover the behaviours of an abstract model/system.

so, if i were to describe what we are doing now, i'd attempt to avoid value-laden terminology and use as abstract a language as i can:

"""
there are:
- some objects (i.e. statements, e.g. S and other expressions),
- a set of operators {N,T} that can act on the objects (multiple operators can be applied sequentially)
- a set of output values {'t', 'f', 'u'}, where the latter is a null value. each statement or statement expression must evaluate to one of those (i will try as hard as i can not to read too much into the "truth" values of 't', 'f', and 'u', these are just individual possible outcomes).
- let S --> 't' denote the fact that the statement or expression S evaluates to output value 't'
- rules that describe the effects of operators on statements, e.g. rule a) := "iff S --> 't' :-> TS --> 't'"
- assume we have a complete set of rules { a), b), c), d) } that can each individually be applied to determine the output value when any operator acts on an object.
"""

the minimal statement S is just "something_that_evaluates_to one of the three output values". all other statements of interest are expressions formed by the application of one or more operators on the minimal statement. for instance, the expression TS denotes the minimal statement S operated on by operator T. applying the operator twice yields the expression TTS.

the task at hand is to discover and describe what happens to the output value of any particular statement expression when any particular subset of the rules, e.g. { a), b), d) }, is chosen to apply.

given a value of S, and a rule subset, what does each statement in the set of possible expressions that result from any arbitrary combination of operators acting on S, e.g. {S, TS, NS, TTS, TNS, NTS, NNS, ..., TNNTNTNTS, ..., TTTTTTTS, ..., NNNNNNNS}. for practical reasons we shall stop at some operator-depth of n symbols, though the point of the program is to be able to compute much the results at a further depth than can be achieved manually.

does this formulation match your expectations?

---

for example, let's say the choice set contains rules  { a), b), d) }.
now the task is to all the resulting output values (the question marks in the below):

iff S-->'t', then
 -  TS --> ?
 - TTS --> ?
 -  NS --> ?
 - ...
 - NNNNNS --> ?

iff S-->'f', then
 -  TS --> ?
 - TTS --> ?
 -  NS --> ?
 - ...
 - NNNNNS --> ?

based on the fact that none of the rules address statement expressions that evaluate to 'u', there is one shortcut we can take that reduces the workload:
iff S-->'u', then
 -  TS --> 'u'
 - TTS --> 'u'
 -  NS --> 'u'
 - ... --> 'u'

----

now. as far as expressing all this in a python program, here are the steps i see:

1. refine and express each rule in terms of what they do to the input.
the rules are:
 - a) iff S-->'t' then TS-->'t', else leave expression un-evaluated.
   - note that this rule says _nothing_ about how to evaluate NS, even when S-->'t'
   - note that this rule says _nothing_ about how to evaluate TS when S-->'f' or S-->'u'
 - b) iff S-->'f' then NS-->'t', else leave expression un-evaluated.
   - note that this rule says nothing about how to evaluate TS, even when S-->'f'
   - note that this rule says nothing about how to evaluate NS when S-->'t' or S-->'u'
   - note that i have interpreted what you wrote:
     - ("if TS is not true, then NTS is true.") to apply to an arbitrary S, instead of TS explicitly.
 - c) iff S-->'f', then TS-->'t', else leave expression un-evaluated.
 - d) iff S-->'t', then NS-->'f', else leave expression un-evaluated.
2. given a set of rules determine the order of application of the rules.
3. for each expression seq(N,T)S, step through it in reverse order. starting with S.
 - first assume S-->'t' and continue through all the expressions
 - then assume S-->'f' and continue through all the expressions
4. then consider one operator acting on S, starting with TS,
 - go through all the rules and check whether any rule determines the output value of TS given value of S.
 - if so, set the value of TS to the determined output, save the (expression, value) pair
 - if not, set the value of TS to 'u', the null output, save the pair.
5. check NS
 - step through the chosen rules, in order to determine whether any of them determines the output value of NS given the value of S.
 - if so set the value of NS to the determined output, save the (expression, value) pair.
 - if not, set the value of NS to 'u' and save the pair
6. trim the tree of any sub-branches from one that outputs 'u', as the only conclusion hence forth for any subsequent operators will end in 'u' as well.
7. for the remaining branches, add one more operator to get either TTS, TNS, NTS, NNS and repeat the process of checking against the rules, replacing TS/NS with the outcome from the previous step (guaranteed due to trimming to be either 't' or 'f'.)
8. repeat procees till:
- either all branches conclude in 'u'
- or an expression of length 8 has been evaluated.

---

Condolences, and thanks for your email below. Please come to Brighton I will collect you from the station, the pickup taxi zone. You can see the wine collection and use my laptop if desired.
Immediate thoughts on your email. The output value ARE true, false and neither, the T and N operators can be uninterpreted. Your steps 1 to 8 look  more complex than I expected but let's discuss them first, ie get the program spec right first.
Are you also an expert on the Gentzen sequent calculus?
Yours ever, Gary

---

