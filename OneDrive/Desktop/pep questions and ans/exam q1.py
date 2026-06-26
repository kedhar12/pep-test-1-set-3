from collections import Counter

def frequent_words(text, k):
   
    words = text.split()

  
    freq = Counter(words)

    
    result = []
    seen = set()

    for word in words:
        if word not in seen:
            seen.add(word)
            if freq[word] >= k:
                result.append(word)

    return result


# Example
text = "a mouse is smaller than a dog but a dog is stronger"
k = 2

print(frequent_words(text, k))