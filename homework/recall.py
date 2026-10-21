
def relevant_doc(retrieved: list, relevant: list) :
    top_k = retrieved[:5]
    return set(relevant) & set(top_k)

def recall_k(retrieved: list, relevant: list):
    retrieved_set = set(retrieved)
    relevant_set = set(relevant)

    found = retrieved_set & relevant_set

    return len(found)/len(relevant_set)

retrieved = ["docA", "docB", "docY", "docZ", "docE", "docH"]
relevant = ["docA", "docX", "docH"]
print(relevant_doc(retrieved, relevant))
print(recall_k(retrieved, relevant))