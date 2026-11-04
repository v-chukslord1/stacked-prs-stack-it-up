# Recipe scaler: feature spec

The team wants a small tool that scales a recipe up or down. The work breaks into three pieces, listed here in no particular order:

- **Print the result.** `cli.py` builds a sample recipe, scales it with `scale`, and prints it.
- **Scale a recipe.** `scale.py` has `scale(recipe, factor)`, which returns a new `Recipe` with every quantity multiplied by `factor`.
- **Define a recipe.** `recipe.py` has a `Recipe` dataclass with `name`, `servings`, and `ingredients` (a dict of ingredient name to quantity).

Ship it as **three stacked layers**, one branch and one pull request per piece. Each layer may only depend on itself or the layers below it, so the order matters.

Use these branch names (also not in order) once you have worked out the layering:

- `feat/recipe-cli`
- `feat/recipe-scaling`
- `feat/recipe-model`
