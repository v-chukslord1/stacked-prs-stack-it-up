## Step 1: Understand stacks and plan your layers

Your team lead dropped a feature request in your lap: a recipe scaler. Rather than one giant pull request, you'll ship it as a stack, all from the GitHub website. First, let's learn what a stack is and plan the layers.

### 📖 Theory: What is a stack?

A stack is a series of two or more pull requests in the same repository. The bottom pull request targets the trunk (usually `main`), and each later pull request targets the branch of the pull request below it. Put foundational code in lower layers and code that depends on it in higher layers. Each pull request then shows only its own small diff, so reviewers can approve layers independently.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)

### ⌨️ Activity: Order the work into layers

1. Open [`FEATURE_SPEC.md`](https://github.com/{{ full_repo_name }}/blob/main/FEATURE_SPEC.md) and read the three pieces of work. They are listed in no particular order.

1. Decide which piece everything else depends on, then which depends on that, and so on. The piece with no dependencies is the bottom layer.

1. Reply to this issue with a comment that lists your plan from the bottom layer to the top, one line per layer. Start each line with a number, then the branch name and what it contains.

   > [!TIP]
   > For example: `1. feat/your-branch: what this layer holds`. Use the branch names from the spec.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Ask yourself: which file would break if the others didn't exist? `scale.py` needs a `Recipe`, and `cli.py` needs `scale`. The thing nothing depends on goes on top.
- Your comment needs at least three lines that start with `-`, `*`, or a number such as `1.`.
- The first line of your list is the bottom layer, and it should be the one that defines the `Recipe` model.
- If the link doesn't open, go to the **Code** tab of your repository and select `FEATURE_SPEC.md`.

</details>
