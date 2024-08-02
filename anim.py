def my_generator():
    yield [3, 1, 0.002731724032298605]

# Creating the generator object
generator = my_generator()

# Iterating over the generator to access the list
for item in generator:
    print(item)
