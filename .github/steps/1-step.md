## Step 1: Understand stacks and plan your layers

Your team lead has a feature request for you:

> **Recipe scaler:** "We want a small web page that shows a recipe, such as pancakes for 2 people, and lets visitors scale it up or down. Pick 4 servings and the page should show twice the ingredients and twice the pancakes."

Rather than one giant pull request, you'll ship it as a **stack** of small pull requests, all from the GitHub website. First, let's learn what a stack is and plan the layers.

### 📖 Theory: What is a stack?

A stack is a series of two or more pull requests in the same repository. The bottom pull request targets the trunk (usually `main`), and each later pull request targets the branch of the pull request below it. Put foundational code in lower layers and code that depends on it in higher layers. Each pull request then shows only its own small diff, so reviewers can approve layers independently.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)

### ⌨️ Activity: Plan your pull request stack

I opened a separate issue for your team's feature request: [Plan your recipe scaler stack]({{ plan_issue_url }}). It lists the three pieces of work, in no particular order, and has checkboxes for your plan.

1. Open [Plan your recipe scaler stack]({{ plan_issue_url }}) and read the three pieces of work.

1. Decide what each piece needs from the others. Ask yourself: which file would stop working if the others didn't exist?

1. In the issue, tick one file under each layer heading, from the bottom layer to the top layer. Use each file exactly once. Ticking a box saves it.

1. Once every layer has a file, Mona checks your plan and replies on this issue.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Tick the boxes in the issue description itself, not in a comment. Mona checks when you change the description.
- Tick exactly one box under each of the three layer headings. If you tick the wrong one, untick it and tick another.
- Mona waits until every layer has a file ticked, then checks.
- The bottom layer needs nothing from the other files, and the top layer is the one nothing else depends on.
- If you got feedback, change your ticks. Each change is checked once every layer has a file.
- Only the file name matters at this stage. You'll choose branch names in the next step.

</details>
