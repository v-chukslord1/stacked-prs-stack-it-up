# Recipe scaler: feature spec

The team wants a small command-line tool that scales a recipe up or down.

Ship it as **three stacked layers**. Each layer depends only on itself or the layers below it.

| Layer | Branch | File | What it contains |
| --- | --- | --- | --- |
| 1 | `feat/recipe-model` | `recipe.py` | A `Recipe` dataclass with `name`, `servings`, and `ingredients` (a dict of ingredient name to quantity) |
| 2 | `feat/recipe-scaling` | `scale.py` | `scale(recipe, factor)` that returns a new `Recipe` with every quantity multiplied by `factor` |
| 3 | `feat/recipe-cli` | `cli.py` | A script that builds a sample recipe, scales it with `scale`, and prints the result |
