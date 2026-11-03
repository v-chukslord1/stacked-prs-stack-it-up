## Step 1: Understand stacks and plan your layers

Your team lead dropped a feature request in your lap: a recipe scaler. Rather than one giant pull request, you'll ship it as a stack, all from the GitHub website. First, let's learn what a stack is and plan the layers.

### 📖 Theory: What is a stack?

A stack is a series of two or more pull requests in the same repository. The bottom pull request targets the trunk (usually `main`), and each later pull request targets the branch of the pull request below it. Put foundational code in lower layers and code that depends on it in higher layers. Each pull request then shows only its own small diff, so reviewers can approve layers independently.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)

### ⌨️ Activity: Read the spec and plan your layers

1. Open [`FEATURE_SPEC.md`](https://github.com/{{ full_repo_name }}/blob/main/FEATURE_SPEC.md) in your copy of the repository and read the three layers it describes.

1. Reply to this issue with a comment that lists your plan, one line per layer. Start each line with `-` or a number, and name the branch and what it contains.

   > [!TIP]
   > Lower layers hold code that higher layers depend on. For example: `1. feat/recipe-model: the Recipe dataclass`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Your comment needs at least three lines that start with `-`, `*`, or a number such as `1.`.
- Mention what the first layer contains, such as the `Recipe` model or dataclass.
- If the link doesn't open, go to the **Code** tab of your repository and select `FEATURE_SPEC.md`.

</details>
