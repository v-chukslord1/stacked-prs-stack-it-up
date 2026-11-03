## Step 1: Install the tool and plan your stack

Your team lead dropped a feature request in your lap: a recipe scaler. Rather than one giant pull request, you'll ship it as a stack. First, let's get set up and plan.

### 📖 Theory: What is a stack?

A stack is a series of two or more pull requests in the same repository. The bottom pull request targets the trunk (usually `main`), and each later pull request targets the branch of the pull request below it. Put foundational code in lower layers and code that depends on it in higher layers. Each pull request then shows only its own small diff, so reviewers can approve layers independently.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Quickstart for stacked pull requests](https://docs.github.com/en/pull-requests/get-started/stacked-prs-quickstart)

### ⌨️ Activity: Install the extension and plan your layers

1. Check that your tools are new enough. You need GitHub CLI 2.90.0 or later and Git 2.36 or later.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh --version && git --version
   > ```

1. Clone your copy of the exercise.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh repo clone {{ full_repo_name }} && cd "$(basename {{ full_repo_name }})"
   > ```

1. Install the `gh stack` extension.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh extension install github/gh-stack
   > ```

1. Read `FEATURE_SPEC.md` in your clone.

1. Reply to this issue with a comment that lists your plan, one line per layer. Start each line with `-` or a number, and name the branch and what it contains.

   > [!TIP]
   > Lower layers hold code that higher layers depend on. For example: `1. feat/recipe-model: the Recipe dataclass`.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If `gh --version` is older than 2.90.0, upgrade GitHub CLI and run the check again.
- If the extension is already installed, run `gh extension upgrade stack`.
- If `gh` asks you to sign in, run `gh auth login`.
- Your comment needs at least three lines that start with `-`, `*`, or a number such as `1.`.

</details>
