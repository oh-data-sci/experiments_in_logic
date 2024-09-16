import pandas as pd


MAXIT = 10
statements = set('S')
operators = ['T','N']


for iteration in range(MAXIT):
    new_expressions = []
    for statement in statements:
        new_expressions.append(operators[0]+statement)
        new_expressions.append(operators[1]+statement)
    for expression in new_expressions:
        statements.add(expression)

df = (
    pd.DataFrame({'expression':sorted(list(statements))})
    .assign(expression_length=lambda df: df['expression'].str.len())
    .sort_values(['expression_length', 'expression'])
    .reset_index()
    .drop(columns=['index'])
)

display(df.head(4))
display(df[df['expression_length']==8])
display(df.tail(5))