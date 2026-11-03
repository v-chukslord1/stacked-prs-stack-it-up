## Step 2: Build the first two layers

Plan approved. Now you'll build the bottom two layers of the stack, each on its own branch.

### 📖 Theory: Branches as layers

`gh stack init` starts tracking a stack and creates the first branch. `gh stack add <name>` adds the next branch on top of the current one. The key rule: code may only depend on the same branch or a lower one. `gh stack add -Am "message"` stages everything, commits, and creates the next branch in one step.

#### References

- [Stacked pull requests CLI commands](https://docs.github.com/en/pull-requests/reference/stacked-prs-cli-commands)

### ⌨️ Activity 1: Layer 1, the data model

1. Start the stack and name the first branch `feat/recipe-model`.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack init
   > ```

1. Create `recipe.py` with a `Recipe` dataclass that has `name`, `servings`, and `ingredients` fields, as described in `FEATURE_SPEC.md`.

1. Commit your work.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > git add recipe.py && git commit -m "Add Recipe model"
   > ```

<details>
<summary>Having trouble? 🤷</summary><br/>

- Run `gh stack init` from inside your clone of the repository.
- If the commit reports nothing to commit, make sure `recipe.py` is saved in the repository root.
- If you named the branch differently, create it again with the exact name `feat/recipe-model`.

</details>

### ⌨️ Activity 2: Layer 2, the scaling logic

1. Add the next branch on top of the stack.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack add feat/recipe-scaling
   > ```

1. Create `scale.py` with a `scale(recipe, factor)` function that imports `Recipe` from `recipe.py` and returns a new `Recipe` with every quantity multiplied by `factor`.

1. Commit your work.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > git add scale.py && git commit -m "Add recipe scaling"
   > ```

1. Check the shape of your stack. Both branches should appear in order.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack view
   > ```

1. Push every branch in the stack.

   > ![Static Badge](https://img.shields.io/badge/Terminal-text?logo=gnometerminal&labelColor=0969da&color=ddf4ff)
   >
   > ```bash
   > gh stack push
   > ```

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If `scale.py` can't import `recipe`, check that you ran `gh stack add` first, so `recipe.py` from layer 1 is part of this branch.
- If `gh stack view` shows the branches in the wrong order, rerun it and check that you added the second branch while on the first.
- If the push fails, confirm you have push access to your copy of the repository.

</details>
