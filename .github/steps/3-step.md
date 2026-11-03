## Step 3: Add the top layer and submit the stack

Two layers are pushed. One more layer, then you'll turn the branches into linked pull requests.

### 📖 Theory: Submitting and reading a stack

`gh stack submit` pushes your branches and opens a pull request for each one with the correct base branch. Your first branch targets `main`, and each later branch targets the one below it. On GitHub, each pull request shows a stack icon, and the merge box shows a stack map of every layer. Branch protection rules and CI that apply to `main` run for every pull request in the stack.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Managing stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/managing-stacked-pull-requests)

### ⌨️ Activity: Add layer 3 and submit

1. Create `cli.py` with a script that builds a sample recipe, scales it with `scale`, and prints the result.

1. Add the third branch on top of the stack and commit your work.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack add feat/recipe-cli && git add cli.py && git commit -m "Add CLI output"
   > ```

1. Check that all three branches are in order.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack view
   > ```

1. Create the pull requests and link them as a stack.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack submit
   > ```

1. Open the top pull request on GitHub and find the stack map in the merge box.

1. Comment on this issue saying which branch each pull request targets. For example: `feat/recipe-model targets main`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If the feedback says the pull requests aren't linked as a stack yet, wait a few seconds, then post another comment on this issue to run the check again.
- If the branch name wasn't accepted, check that it is exactly `feat/recipe-cli`.
- If `gh stack submit` can't push, confirm you have push access to your copy of the repository.
- If a pull request has the wrong base, run `gh stack view` to compare it with the order of your branches.

</details>
