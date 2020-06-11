
lst = [x for x in range(1, 100)]
print(lst)

wrd = [w for w in 'string']
print(wrd)

##even numbers
even = [x for x in range(100) if x%2==0]
print(even)

st = 'Print only the words that start with s in this sentence'
print(st.split())
swords =[word for word in st.split() if word.startswith('s')]
print(swords)

st = 'Print every word in this sentence that has an even number of letters'
elword = [word for word in st.split() if(len(word)%2 == 0)]
print(elword)

st = 'Create a list of the first letters of every word in this string'
fletter = [word[0] for word in st.split()]
print(fletter)

num = [i for i in range(1, 100) if(i%3==0)]