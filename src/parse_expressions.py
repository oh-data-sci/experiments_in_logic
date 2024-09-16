import pandas as pd

def apply_rules(expr):
    """
    applies the designated rules to reduce an expression.
    
    """
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