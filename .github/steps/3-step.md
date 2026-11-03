## Step 3: Add the top layer and create the stack

Two layers are pushed. One more layer, then you'll turn the branches into linked pull requests.

### 📖 Theory: Creating and reading a stack

You create a stack on GitHub by opening a pull request for each branch, setting each base branch to the branch below it, and selecting the **Create stack** option to link them. Your first branch targets `main`, and each later branch targets the one below it. Once linked, each pull request shows a stack icon, and the merge box shows a stack map of every layer. Branch protection rules and CI that apply to `main` run for every pull request in the stack.

#### References

- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)
- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)

### ⌨️ Activity: Add layer 3 and create the stack

1. Switch to the `feat/recipe-scaling` branch, then create a branch named `feat/recipe-cli` from it using the branch dropdown.

1. On `feat/recipe-cli`, create `cli.py` with a script that builds a sample recipe, scales it with `scale`, and prints the result. Commit it directly to `feat/recipe-cli`.

1. Open the **Pull requests** tab and select **New pull request**. Set the base to `main` and compare to `feat/recipe-model`, then select **Create pull request**.

1. Create the next pull request. Set the base to `feat/recipe-model` and compare to `feat/recipe-scaling`. Select the **Create stack** option, then create the pull request.

1. Create the last pull request. Set the base to `feat/recipe-scaling` and compare to `feat/recipe-cli`. Add it to the stack, then create the pull request.

   > [!TIP]
   > If you opened pull requests without selecting the stack option, GitHub shows a banner on them that suggests turning the chain into a stack. Select it, review the preview, and confirm.

1. Open the top pull request and find the stack icon and the stack map in the merge box.

1. Comment on this issue saying which branch each pull request targets. For example: `feat/recipe-model targets main`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If the feedback says the pull requests aren't linked as a stack yet, wait a few seconds, then post another comment on this issue to run the check again.
- If a pull request has the wrong base, select **Edit** next to the title and change the base branch to the branch below it.
- If you don't see the stack map, make sure all three pull requests have the stack option applied. Use the banner or **Add to stack** from the stack menu in the pull request header.
- Check that your branch names are exactly `feat/recipe-model`, `feat/recipe-scaling`, and `feat/recipe-cli`.

</details>
