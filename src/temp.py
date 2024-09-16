def apply_rule_a(expr):
    """
    for a given expression expr, this function applies rule a):
        a) if S evaluates to TRUE, then TS evaluates to S 
        
        else return 
        # note cannot assume:  TS --> FALSE iff N --> FALSE?
    therefore, TS -> S
    expr = 'NNNTNNTTS' 
        if S TRUE, apply rule a)
        expr = 'NNNTNNTTS' -> 
        

    expr = '************NS'
    expr = '************TS'
    """
    S = expr[-2] # S='NS'
    if S[0] == 'T':
        
    else:
        return 'NOT TRUE'

def apply_rule_b(expr):
    """
    applies rule b)
    b) if TS evaluates to FALSE, then NTS evaluates to TRUE # ?can we also assume: NTS --> FALSE iff S --> TRUE?
    - NTS -> NS
    """

def apply_rule_c(expr):
    """
    applies rule c)
    c) if  S evaluates to FALSE, then NTS --> TRUE  (N operator flips FALSE to TRUE,  )
    
    """

def apply_rule_d(expr):
    """
    applies rule a)
    d)if TS evaluates to TRUE,  then NTS --> FALSE (N operator flips TRUE  to FALSE, and FALSE to TRUE)
    """




def apply_rules(expr, rules=['a','b','c']):
    """
    applies the designated rules to reduce an expression.
    rules = a list of either 2 or 3 rules
    expr = 'NNNTNNTTS'
    rules = ['a,'b','c']

    step 1 S?
    step 2 T(S)?
    step 3 T(TS)?
    ...
    step N(NNTNNTTS)
    """
    
    if 'a' in rules:
        expr = apply_rule_a(expr)
    if 'b' in rules:
        return apply_rule_a(expr)
    if 'c' in rules:
        return apply_rule_a(expr)
        
    
    
    changed = True
    while changed:
        changed = False
        # rule c: FFS --> S (double-negation elimination)
        if 'FFS' in expr:
            expr = expr.replace('FFS', 'S')
            changed = True
        
        # Rule d: TTTS --> TS (triple-truth elimination)
        if 'TTTS' in expr:
            expr = expr.replace('TTTS', 'TS')
            changed = True
    
    return expr

def evaluate_expression(expr, s_value):
    expr = apply_rules(expr)
    
    if expr == 'S':
        return 'TS' if s_value else 'FS'
    elif expr == 'TS':
        return 'TS' if s_value else 'FS'
    elif expr == 'FS':
        return 'FS' if s_value else 'TS'
    elif expr.startswith('T'):
        return evaluate_expression(expr[1:], s_value)
    elif expr.startswith('F'):
        return evaluate_expression(expr[1:], not s_value)
    else:
        return expr  # If we can't evaluate further, return as is

def generate_expressions(max_length):
    expressions = ['S']
    for i in range(1, max_length):
        new_expressions = [op + expr for op in ['T', 'F'] for expr in expressions]
        expressions.extend(new_expressions)
    return expressions[:max_length]  # Limit to max_length expressions

def main():
    max_length = 20  # Adjust this to generate more or fewer expressions
    expressions = generate_expressions(max_length)
    
    results = []
    for expr in expressions:
        s_true_result = evaluate_expression(expr, True)
        s_false_result = evaluate_expression(expr, False)
        results.append({
            'Expression': expr,
            'S=True Result': s_true_result,
            'S=False Result': s_false_result
        })
    
    df = pd.DataFrame(results)
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()