str_to_split = input("Please provide a sentence with 2 or more words in it: \n")
result = str_to_split.split(' ')


if len(result) < 2:
    print("Sentence is too short")
else:
    print(f"Number of words in the provided sentence: {len(result)}")