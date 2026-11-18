## Step 4: Merge from the bottom up and see your site

Your stack is up. Time to land it and see the recipe scaler live.

### 📖 Theory: Merging a stack

Pull requests in a stack merge from the bottom up. You can merge the whole stack at once by merging the top pull request, which brings every pull request below it along. If you merge a pull request in the middle, the ones below it merge too, and the ones above stay open and are automatically re-targeted to the stack's base branch. GitHub rebases the remaining branches for you.

#### References

- [Merging stacked pull requests](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-stacked-pull-requests)
- [Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

### ⌨️ Activity: Merge part of the stack, then the rest

1. First, get a place ready for your site. In your repository, go to **Settings** > **Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose the `main` branch and the `/ (root)` folder, then select **Save**. Your site will appear once your code reaches `main`.

1. Open the pull request for `feat/recipe-scaling`, the middle layer.

1. In the merge box, find the stack map, then select **Merge stack**.

   ![The stack map in the merge box listing the three pull requests above main](https://github.com/{{ full_repo_name }}/blob/main/.github/images/4-stack-map.png?raw=true)

1. Look at the other two pull requests. The pull request for `feat/recipe-model` is merged along with it, and the pull request for `feat/recipe-page` is still open and now targets `main`.

1. Merge the pull request for `feat/recipe-page`.

1. Wait a minute for your site to publish. Go back to **Settings** > **Pages** and select **Visit site**. Select the **1x**, **2x**, **3x**, and **4x** buttons and watch more pancakes appear.

   ![A recording of the recipe scaler: selecting 1x, 2x, 3x, and 4x adds more plates of pancakes and increases the ingredient amounts](https://github.com/{{ full_repo_name }}/blob/main/.github/images/4-recipe-scaler-site.gif?raw=true)

   Use the buttons at the top of the page to scale the recipe. Each button is a multiplier, and the page redraws straight away when you select one:

   | Button | Servings | Plates of pancakes | Flour | Milk | Eggs |
   | --- | --- | --- | --- | --- | --- |
   | **1x** | 2 | 2 | 1 | 1 | 1 |
   | **2x** | 4 | 4 | 2 | 2 | 2 |
   | **3x** | 6 | 6 | 3 | 3 | 3 |
   | **4x** | 8 | 8 | 4 | 4 | 4 |

   The heading changes to match, such as **Pancakes for 4**. This works because `index.html` (layer 3) asks `scale.js` (layer 2) to multiply the recipe from `recipe.js` (layer 1). All three layers of your stack are working together.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

<details>
<summary>Having trouble? 🤷</summary><br/>

- If you don't see feedback after merging the middle pull request, that's expected. Mona checks your work once the `feat/recipe-page` pull request is merged.
- If **Merge stack** is disabled, check that required checks pass. Every layer must meet the same rules as `main`.
- If the top pull request still shows the old base branch, refresh the page. The automatic rebase can take a few seconds.
- If a pull request shows merge conflicts, make sure you merged from the bottom up.
- If your site shows a 404 page, wait a minute and reload. Publishing can take a short while after the final merge. Check **Settings** > **Pages** to confirm the source is `main` and `/ (root)`.

</details>
