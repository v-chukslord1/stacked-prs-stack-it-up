## Step 2: Build the first two layers

Plan approved. Now you'll build the bottom two layers of the stack on GitHub, each on its own branch. You don't need to know JavaScript: the code is provided, so you can focus on branches and commits. Mona only checks your work after you commit `scale.js` to the second branch, so take your time with both layers.

### 📖 Theory: Branches as layers

Each layer of a stack lives on its own branch, and each new branch is created from the branch below it. The key rule: code may only depend on the same branch or a lower one. That's why you create `feat/recipe-scaling` from `feat/recipe-model`, not from `main`: `scale.js` needs `recipe.js`, which only exists on the lower branch.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)
- [Creating new files](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files)

### ⌨️ Activity 1: Layer 1, the recipe

1. Open the [**Code** tab](https://github.com/{{ full_repo_name }}) of your repository, select the branch dropdown, type `feat/recipe-model`, and select **Create branch feat/recipe-model from main**.

   ![The branch dropdown with feat/recipe-model typed in and the Create branch feat/recipe-model from main option shown](https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-branch-dropdown-create.png?raw=true)

1. On the new branch, select **Add file** > **Create new file**.

   ![The Add file menu open, showing Create new file and Upload files](https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-add-file-menu.png?raw=true)

1. Name the file `recipe.js`. This file defines the recipe: its name, how many servings it makes, and its ingredients. Copy this into the file:

   ```js
   export const recipe = {
     name: "Pancakes",
     servings: 2,
     ingredients: {
       "Flour (cups)": 1,
       "Milk (cups)": 1,
       "Eggs": 1,
     },
   };
   ```

1. Select **Commit changes...**, choose **Commit directly to the `feat/recipe-model` branch**, and commit.

   <img src="https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-commit-dialog.png?raw=true" alt="The Commit changes dialog with Commit directly to the branch selected" width="400">

<details>
<summary>Having trouble? 🤷</summary><br/>

- Check that the branch name is exactly `feat/recipe-model`, and that the branch dropdown shows it before you add the file.
- If the commit dialog offers a new branch instead, choose to commit directly to `feat/recipe-model`.
- Put `recipe.js` in the repository root, not in a folder.

</details>

### ⌨️ Activity 2: Layer 2, the scaling logic

1. Make sure you're on the `feat/recipe-model` branch. Use the branch dropdown to switch if needed.

1. Open the branch dropdown again, type `feat/recipe-scaling`, and select **Create branch feat/recipe-scaling from feat/recipe-model**. The new branch must start from `feat/recipe-model`, not `main`. That is what makes it the next layer of the stack.

1. On the `feat/recipe-scaling` branch, select **Add file** > **Create new file**. Name it `scale.js`. This file holds the instructions for making the recipe bigger or smaller. Notice that its first line imports the recipe from `recipe.js`, which only exists on the branch below. That import is the dependency that makes this a stack. Copy this into the file:

   ```js
   import { recipe } from "./recipe.js";

   export function scale(factor) {
     return {
       name: recipe.name,
       servings: recipe.servings * factor,
       ingredients: Object.fromEntries(
         Object.entries(recipe.ingredients).map(([item, quantity]) => [item, quantity * factor])
       ),
     };
   }
   ```

1. Commit directly to the `feat/recipe-scaling` branch. This commit is what tells Mona you're ready, so make sure both layers are finished first.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you can't see `recipe.js` on `feat/recipe-scaling`, the branch was created from `main`. Delete it from the branch list and create it again from `feat/recipe-model`.
- Make sure the first line of `scale.js` is `import { recipe } from "./recipe.js";`.
- Confirm your last commit went to `feat/recipe-scaling`, not `main`.

</details>
