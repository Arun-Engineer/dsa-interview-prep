# GitHub Actions CI (W1D4)

## 1. What is CI?

CI is continous integrations used for testing the code before it is merged in to the main code.

**Example:** lets say already there is a feature checkout now new features requirement is released and the code is prepared for the same and pushed to github now the code may have passed in the local or dev might have forgot to test the code, so via ci before merging the test is run by github actions based on yaml file, if passed successull the code is without error and we can merge if there is an error we have to correct and then push it once again back.

## 2. What triggers my workflow?

`on` is the part makes when should it run like during push and pull request in the main branch alone.

## 3. What does the runner do, in order?

1. Get the code `actions/checkou@v5`
2. Setup the python `actions/setup python@v6` with version `"3.14"`
3. Show python version via `run`
4. Install dependencies `run python -m pip install -r requirements.txt`
5. Run tests via `python -m pytest -v`

## 4. Red: what does it mean and whats the first thing i do?

It means there is a failure, it may be due to:

- .env usage failure
- install dependencies
- code failure itself
- leftout file when add
- different python version

## 5. Install requirements/ .env file or leftout file when add . etc

## 5. One trap:

---

# Two Pointers Pattern

## 1. Pattern - What the two fingers do

Two fingers points to index 0 first start and last as `index(len(word) -1 )` by this way we are able to compare the values with our targets very easily and effectively until the before finger overlap `while left < right:`

## 2. Tiny example

```python
def pair_with_sum(prices: list, target: int) -> dict:

    left = 0
    right = len(prices) - 1

    while left < right:
        sum = prices[left] + prices[right]

        if sum == target:
            return [left, right]

        elif sum > target:
            right = right - 1

        else:
            left = left + 1

    return []


print(pair_with_sum([100, 150, 200, 350, 450], 500))
```

## 3. why

this is useful only when the sorted list is available and moreover its easy to identify the pairs in limited steps

## 4. Trap

we must use `<` not `<=` since it overlaps the value for example if target is 300 and low is pointing at 150 if less or eqaul and no pair matching earlier when the right reaches to 150 on using `<=` so 150+150 = 300 target acheived this is not pair this the same value added twice.

## 5. we must use `.sort()` but original positions get replaced?

---

## Cosine similarity (W2D1)

### 1. Pattern

first we have to calcualte the dot product , its nothing but list a x list b -> the sum up together and find the vector lengths square of individual list items  then mulitply the square values and then take the square root of final value and final thing of cosine similarity is dotproduct/ (length of A x length of B)

### 2. Tiny example

```python
from app.embeddings import get_embedding, cosine_similarity

a = get_embedding("My order hasn't arrived yet")
b = get_embedding("Delivery is late")
c = get_embedding("How do i change my password")

print("Length of one embedding:", len(a))
print("A vs B:", round (cosine_similarity(a,b), 3))
print("A vs C:", round(cosine_similarity(b, c), 3))
```

### 3. Why

for example if you walk 3km east and 4 km north and whats the length from the start to endpoint is  5 for that we have square 3x3 = 9 , 4 x4 = 16 = 25 sqrt = 5 this is done to identify the straight line distance

### 4. Trap

if its a zero vector , anything divided by zero is not possible so it throws zero division error to avoid this if we find length of any vector is 0 then return 0.0 to avoid crash

### 5.
