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

Your team split the recipe scaler into three pieces of work, listed here in no particular order. Before creating any branches, work out which piece must be built first, and which must wait for another.

| File | What it does |
| --- | --- |
| `index.html` | The web page. It shows the recipe and some buttons, and draws plates of pancakes for the chosen number of servings. |
| `scale.js` | The instructions for making a recipe bigger or smaller by multiplying every ingredient quantity. |
| `recipe.js` | The recipe itself: its name, how many servings it makes, and its ingredients with quantities. |

1. Decide what each piece needs from the others. Ask yourself: which file would stop working if the others didn't exist?

1. Arrange the three files from the bottom layer to the top layer. The bottom layer needs nothing from the others, and each layer above it can use the layers below it.

1. Reply to this issue with your plan, one line per layer, starting each line with a number and the file name. The first line is the bottom layer. For example:

   ```text
   1. file-name: what this layer contains
   2. file-name: what this layer contains
   3. file-name: what this layer contains
   ```

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- Your comment needs three lines that each start with a number such as `1.`, a dash, or a star, followed by the file name.
- The first line is the bottom layer, and it should be `recipe.js`. The top layer is the one nothing else depends on.
- Only the file name matters at this stage. You'll choose branch names in the next step.

</details>
