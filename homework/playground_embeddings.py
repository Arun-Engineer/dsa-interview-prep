from app.embeddings import get_embedding, cosine_similarity

a = get_embedding("My order hasn't arrived yet")
b = get_embedding("Delivery is late")
c = get_embedding("How do i change my password")

print("Length of one embedding:", len(a))
print("A vs B:", round (cosine_similarity(a,b), 3))
print("A vs C:", round(cosine_similarity(b, c), 3))