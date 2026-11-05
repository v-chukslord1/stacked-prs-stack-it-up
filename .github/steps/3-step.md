## Step 3: Add the top layer and create the stack

Two layers are pushed. One more layer, then you'll turn the branches into linked pull requests.

### 📖 Theory: Creating and reading a stack

You create a stack on GitHub by opening a pull request for each branch, setting each base branch to the branch below it. When GitHub sees a chain like that, it shows a **Preview stack** banner. The preview has a **Create stack** button that links them. Your first branch targets `main`, and each later branch targets the one below it. Once linked, each pull request shows a stack icon, and the merge box shows a stack map of every layer. Branch protection rules and CI that apply to `main` run for every pull request in the stack.

#### References

- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)
- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)

### ⌨️ Activity: Add layer 3 and create the stack

1. Switch to the `feat/recipe-scaling` branch, then create a branch named `feat/recipe-cli` from it using the branch dropdown.

1. On `feat/recipe-cli`, create `cli.py` with a script that builds a sample recipe, scales it with `scale`, and prints the result. Commit it directly to `feat/recipe-cli`.

1. Open the **Pull requests** tab and select **New pull request**. Set the base to `main` and compare to `feat/recipe-model`, then select **Create pull request**.

1. Create the next pull request. Set the base to `feat/recipe-model` and compare to `feat/recipe-scaling`, then select **Create pull request**.

1. Create the last pull request. Set the base to `feat/recipe-scaling` and compare to `feat/recipe-cli`, then select **Create pull request**.

1. At the top of the pull request, GitHub shows a banner: **This pull request can be stacked with other pull requests.** Select **Preview stack**.

   ![The banner reading This pull request can be stacked with other pull requests, with a Preview stack button](https://github.com/{{ full_repo_name }}/blob/main/.github/images/3-preview-stack-banner.png?raw=true)

1. Check that the preview lists your three pull requests from top to bottom: `feat/recipe-cli`, `feat/recipe-scaling`, `feat/recipe-model`. Select **Create stack** to link them.

   ![The Preview stack dialog listing the three pull requests above main, with a Create stack button](https://github.com/{{ full_repo_name }}/blob/main/.github/images/3-preview-stack-dialog.png?raw=true)

1. Open the top pull request and find the stack icon and the stack map in the merge box.

   ![The stack map listing the three pull requests above main, each marked Ready](https://github.com/{{ full_repo_name }}/blob/main/.github/images/4-stack-map.png?raw=true)

1. Once the stack is linked, comment on this issue saying which branch each pull request targets. For example: `feat/recipe-model targets main`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Mona checks when you comment on this issue, so confirm the stack first. If the feedback says the pull requests aren't linked yet, select **Create stack** in the preview, then post another comment on this issue to run the check again.
- If a pull request has the wrong base, select **Edit** next to the title and change the base branch to the branch below it.
- If you don't see the **Preview stack** banner, check that each pull request's base is the branch below it. If you dismissed the banner, reload the page.
- If you don't see the stack map, create the stack from the preview. Check that all three pull requests are linked.
- Check that your branch names are exactly `feat/recipe-model`, `feat/recipe-scaling`, and `feat/recipe-cli`.

</details>

> [!TIP]
> **Extra: how to unstack.** Linked the wrong pull requests, or need to reorder or rename layers? Remove the stack link and rebuild it. With the [`gh stack` CLI](https://docs.github.com/en/pull-requests/reference/stacked-prs-cli-commands#gh-stack-unstack), run `gh stack unstack` (or `gh stack unstack STACK-NUMBER`, using the number shown in the stack map). Then fix the base branches and use **Preview stack** again. Don't do this before Mona checks your work.
