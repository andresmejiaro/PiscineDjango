#%%
def my_var():
    x=(42, "42", "quarante-deux", 42.0, True, [42], {42:42}, (42,), set())
    for j in x:
        print(f'{j} has a type {type(j)}\n')


#%%

if __name__=='_main__':
    my_var()


