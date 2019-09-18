def find_anagrams(word, candidates):
    results = []
    for i in range(len(candidates)):
        word_sorted = sorted(word)
        cand_sorted = sorted(candidates[i])
        if word_sorted == cand_sorted:
            results.append(candidates[i])
#            print(candidates[i])
#        else:
#            print("No matched word!")
    
    if len(results) == 0:
        print("There is no match")
    else:
        print("Matches word(s)...:")
        for i in range(len(results)):
            print(results[i])



find_anagrams("hello", ["lleho", "howdy", "pie", "lehol"])
find_anagrams("listen", ["enlists", "google", "inlets", "banana"])