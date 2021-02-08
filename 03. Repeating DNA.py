def get_repeating_DNA(test):
    i=0
    subsequences = set()
    while i <= len(test)-10:
        current_sequences = test[i:i+10]
        if test.count(current_sequences)>1:
            subsequences.add(current_sequences)
        elif current_sequences.count(current_sequences[0])==10:
            subsequences.add(current_sequences)
        i+=1
    return sorted(subsequences)


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
