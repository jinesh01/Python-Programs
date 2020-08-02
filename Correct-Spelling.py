from textblob import TextBlob
a = "cmputr"
print("Original text :"+str(a))
b = TextBlob(a)
print("Correct text :"+str(b.correct()))
