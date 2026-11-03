## Step 4: Merge from the bottom up

Your stack is up. Time to land it.

### 📖 Theory: Merging a stack

Pull requests in a stack merge from the bottom up. You can merge the whole stack at once by merging the top pull request, which brings every pull request below it along. If you merge a pull request in the middle, the ones below it merge too, and the ones above stay open and are automatically re-targeted to the stack's base branch. GitHub rebases the remaining branches for you.

#### References

- [Merging stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests)

### ⌨️ Activity: Merge part of the stack, then the rest

1. Open the pull request for `feat/recipe-scaling`, the middle layer.

1. Merge it using the merge button.

1. Look at the other two pull requests. The pull request for `feat/recipe-model` is merged along with it, and the pull request for `feat/recipe-cli` is still open and now targets `main`.

1. Merge the pull request for `feat/recipe-cli`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you don't see feedback after merging the middle pull request, that's expected. Mona checks your work once the `feat/recipe-cli` pull request is merged.
- If the merge button is disabled, check that required checks pass. Every layer must meet the same rules as `main`.
- If the top pull request still shows the old base branch, refresh the page. The automatic rebase can take a few seconds.
- If a pull request shows merge conflicts, make sure you merged from the bottom up.

</details>
