# Final quiz for 46120

Repo URL: https://github.com/DTUWind-46120-2026/final-quiz.

### Problem

There is a bug in this repo.
The existing binary file `file.bin` has incorrect contents: it contains a string `"I am NOT done with 46120!"`.
But it SHOULD contain a string that says `"I AM done with 46120!"`

### Your task

Create a feature branch whose name is your student ID, e.g., a branch named `s123456`.

Modify `main.py` and generate a `file.bin` with the correct contents.
Optional: use `test_binary.py` to verify the contents of your `file.bin` are correct.
Open a PR on the final-quiz repo with the corrected `file.bin`.
I.e., in your PR, the content of `file.bin` is a string containing `"I AM done with 46120!"`.

Your PR should contain a short but accurate description of the motivation for/contents of your PR.
The target audience of your PR description is someone on the same dev team as you but who does not know about the bug.

It is not required to update/commit `main.py`, but you can do it if you want.
The `main.py` is not considered as part of the quiz; only the contents of `file.bin` and the PR itself matter.

### To pass the quiz

1. Open a PR from a feature branch on the final-quiz repo within the time limits set in class.
1. In your PR, the contents of `file.bin` must be the string `"I AM done with 46120!"`.
1. Your PR includes a brief but accurate description of the motivation behind/changes in the PR.
