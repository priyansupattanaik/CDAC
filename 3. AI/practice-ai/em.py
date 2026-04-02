import math

# some sample data
docs = [
    "AI is powerful",
    "Machine learning is useful",
    "Cricket is a sport",
    "Deep learning is part of AI"
]

# convert text to words
def tokenize(text):
    return text.lower().split()

# create vocabulary
vocab = []
for d in docs:
    for w in tokenize(d):
        if w not in vocab:
            vocab.append(w)

# convert sentence to vector (bag of words)
def make_vector(text):
    vec = [0] * len(vocab)
    words = tokenize(text)
    
    for w in words:
        if w in vocab:
            index = vocab.index(w)
            vec[index] += 1
            
    return vec

# cosine similarity
def cosine(v1, v2):
    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    
    mag1 = math.sqrt(sum([x*x for x in v1]))
    mag2 = math.sqrt(sum([x*x for x in v2]))
    
    if mag1 == 0 or mag2 == 0:
        return 0
    
    return dot / (mag1 * mag2)

# store vectors (like vector db)
db = []
for d in docs:
    v = make_vector(d)
    db.append((d, v))

# search function
def search(query):
    q_vec = make_vector(query)
    
    best_text = ""
    best_score = -1
    
    for text, vec in db:
        score = cosine(q_vec, vec)
        
        if score > best_score:
            best_score = score
            best_text = text
    
    return best_text, best_score

# test
query = "AI and machine learning"
ans, score = search(query)

print("Query:", query)
print("Result:", ans)
print("Score:", score)