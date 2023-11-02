#%%
def dictionarize():
    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]

    d1= list(map(lambda x: x[0], d))
    d2= list(map(lambda x: x[1], d))
    hey_dict= dict(zip(d2,d1))
    for key, value in hey_dict.items():
        print(f'{key}: {value}')


#%%
if __name__ == "__main__":
    dictionarize()

#%%
dictionarize()

# %%
