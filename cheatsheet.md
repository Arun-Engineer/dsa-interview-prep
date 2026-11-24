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
