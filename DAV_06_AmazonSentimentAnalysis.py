import pandas as pd
import re

data = pd.read_csv("20191226-reviews.csv")
reviews = data["body"]

pos = [
    "good","great","excellent","amazing","love","best","nice","happy",
    "awesome","fantastic","perfect","reliable","wonderful","satisfied","cool"
]

neg = [
    "bad","worst","poor","terrible","hate","problem","slow","broken",
    "awful","issue","disappointed","lag","bug","useless","worst"
]

for i in range(10):
    text = str(reviews[i])

    # Clean text
    clean = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    words = clean.split()

    # Count positive & negative words
    p = sum(w in pos for w in words)
    n = sum(w in neg for w in words)
    total = len(words)

    # METHOD 1: Normalization
    method1 = (p - n) / total if total != 0 else 0

    # METHOD 2: Semi Normalization
    if (p + n) == 0:
        method2 = 0
    else:
        method2 = (p - n) / (p + n)

    print("Review:", text.split(".")[0])
    print("Positive:", p, "Negative:", n)
    print("Method 1 Normalization Sentiment Score :", round(method1, 3))
    print("Method 2 Semi Normalization Sentiment Score :", round(method2, 3))
    print()
    print()

# pip install pandas numpy