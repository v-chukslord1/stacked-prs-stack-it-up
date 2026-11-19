## Feature request: recipe scaler

Your team lead has a feature request for you:

> **Recipe scaler:** "We want a small web page that shows a recipe, such as pancakes for 2 people, and lets visitors scale it up or down. Pick 4 servings and the page should show twice the ingredients and twice the pancakes."

Your team split the work into three files, listed here in no particular order.

| File | What it does |
| --- | --- |
| `index.html` | The web page. It shows the recipe and some buttons, and draws plates of pancakes for the chosen number of servings. |
| `scale.js` | The instructions for making a recipe bigger or smaller by multiplying every ingredient quantity. |
| `recipe.js` | The recipe itself: its name, how many servings it makes, and its ingredients with quantities. |

## Your plan

Decide which file must be built first and which files depend on others. The bottom layer needs nothing from the other files, and each layer above it can use the layers below.

For each layer, tick the box next to the file that belongs there. Tick one file per layer, and use each file once. Ticking a box saves it automatically. Mona checks your plan once every layer has a file, then replies on the exercise issue.

### Layer 1 (bottom)

- [ ] `recipe.js`
- [ ] `scale.js`
- [ ] `index.html`

### Layer 2 (middle)

- [ ] `recipe.js`
- [ ] `scale.js`
- [ ] `index.html`

### Layer 3 (top)

- [ ] `recipe.js`
- [ ] `scale.js`
- [ ] `index.html`
