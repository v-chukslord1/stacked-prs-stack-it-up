## Step 2: Build the first two layers

Plan approved. Now you'll build the bottom two layers of the stack on GitHub, each on its own branch. Mona only checks your work after you commit `scale.py` to the second branch, so take your time with both layers.

### 📖 Theory: Branches as layers

Each layer of a stack lives on its own branch, and each new branch is created from the branch below it. The key rule: code may only depend on the same branch or a lower one. That's why you create `feat/recipe-scaling` from `feat/recipe-model`, not from `main`: `scale.py` needs `recipe.py`, which only exists on the lower branch.

#### References

- [About stacked pull requests](https://docs.github.com/en/pull-requests/get-started/about-stacked-prs)
- [Creating stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-stacked-pull-requests)

### ⌨️ Activity 1: Layer 1, the data model

1. Open the [**Code** tab](https://github.com/{{ full_repo_name }}) of your repository, select the branch dropdown, type `feat/recipe-model`, and select **Create branch feat/recipe-model from main**.

   ![The branch dropdown with feat/recipe-model typed in and the Create branch feat/recipe-model from main option shown](https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-branch-dropdown-create.png?raw=true)

1. On the new branch, select **Add file** > **Create new file**.

   ![The Add file menu open, showing Create new file and Upload files](https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-add-file-menu.png?raw=true)

   Name the file `recipe.py`. This file defines what information a recipe contains: a name, how many servings it makes, and its ingredients with quantities. You don't need to know Python. Copy this into the file:

   ```python
   from dataclasses import dataclass


   @dataclass
   class Recipe:
       name: str
       servings: int
       ingredients: dict  # ingredient name -> quantity
   ```

1. Select **Commit changes...**, choose **Commit directly to the `feat/recipe-model` branch**, and commit.

   ![The Commit changes dialog with Commit directly to the branch selected](https://github.com/{{ full_repo_name }}/blob/main/.github/images/2-commit-dialog.png?raw=true)

<details>
<summary>Having trouble? 🤷</summary><br/>

- Check that the branch name is exactly `feat/recipe-model`, and that the branch dropdown shows it before you add the file.
- If the commit dialog offers a new branch instead, choose to commit directly to `feat/recipe-model`.
- Put `recipe.py` in the repository root, not in a folder.

</details>

### ⌨️ Activity 2: Layer 2, the scaling logic

1. Switch to the `feat/recipe-model` branch using the branch dropdown.

1. Open the branch dropdown again, type `feat/recipe-scaling`, and select **Create branch feat/recipe-scaling from feat/recipe-model**.

   > [!IMPORTANT]
   > The new branch must start from `feat/recipe-model`, not `main`. That is what makes it the next layer of the stack.

1. On the `feat/recipe-scaling` branch, select **Add file** > **Create new file**. Name it `scale.py`. This file holds the instructions for making a recipe bigger or smaller by multiplying every ingredient quantity. Notice that it imports `Recipe` from `recipe.py`, which only exists on the branch below. That import is the dependency that makes this a stack. Copy this into the file:

   ```python
   from recipe import Recipe


   def scale(recipe, factor):
       return Recipe(
           name=recipe.name,
           servings=recipe.servings * factor,
           ingredients={name: qty * factor for name, qty in recipe.ingredients.items()},
       )
   ```

1. Commit directly to the `feat/recipe-scaling` branch. This commit is what tells Mona you're ready, so make sure both layers are finished first.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you can't see `recipe.py` on `feat/recipe-scaling`, the branch was created from `main`. Delete it from the branch list and create it again from `feat/recipe-model`.
- Make sure `scale.py` contains `from recipe import Recipe`.
- Confirm your last commit went to `feat/recipe-scaling`, not `main`.

</details>
