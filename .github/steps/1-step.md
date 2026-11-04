## Step 1: Understand stacks and plan your layers

Your team lead dropped a feature request in your lap: a recipe scaler. Rather than one giant pull request, you'll ship it as a stack, all from the GitHub website. First, let's learn what a stack is and plan the layers.

### 📖 Theory: What is a stack?

A stack is a series of two or more pull requests in the same repository. The bottom pull request targets the trunk (usually `main`), and each later pull request targets the branch of the pull request below it. Put foundational code in lower layers and code that depends on it in higher layers. Each pull request then shows only its own small diff, so reviewers can approve layers independently.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)

### ⌨️ Activity: Plan your pull request stack

Your team has divided the recipe scaler feature into three pieces of work. Before creating branches or pull requests, you need to determine the order in which they should be developed.

1. Open [`FEATURE_SPEC.md`](https://github.com/{{ full_repo_name }}/blob/main/FEATURE_SPEC.md) and read the descriptions of the three pieces of work.

1. Identify what each piece requires from the others. For example, the scaling functionality needs a recipe model to work with, while the command-line interface needs both the model and the scaling functionality.

1. Arrange the three pieces into a dependency order:

   - **Bottom layer:** the foundational piece that has no dependencies on the other pieces.
   - **Middle layer:** the piece that depends on the bottom layer.
   - **Top layer:** the piece that depends on the layers below it.

1. Find the corresponding branch name for each piece in `FEATURE_SPEC.md`.

1. Reply to this issue with your proposed stack, listing the layers from bottom to top, one line per layer, in this format:

   ```text
   1. `branch-name`: Briefly describe what this layer contains.
   2. `branch-name`: Briefly describe what this layer contains.
   3. `branch-name`: Briefly describe what this layer contains.
   ```

   > [!TIP]
   > Example of one line: `1. feat/example: Description of the foundational work.`

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

By completing this activity, you show that you can identify dependencies between pieces of work and organize them into a valid stacked pull request structure.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Ask yourself: which file would break if the others didn't exist? `scale.py` needs a `Recipe`, and `cli.py` needs `scale`. The thing nothing depends on goes on top.
- Your comment needs at least three lines that start with `-`, `*`, or a number such as `1.`.
- The first line of your list is the bottom layer, and it should be the one that defines the `Recipe` model.
- If the link doesn't open, go to the **Code** tab of your repository and select `FEATURE_SPEC.md`.

</details>
