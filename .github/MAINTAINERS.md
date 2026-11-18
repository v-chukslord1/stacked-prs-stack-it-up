# Maintainer notes

## Before publishing

- Mark the repository as a **template** in Settings. The start workflow is guarded by `!github.event.repository.is_template`, so it only starts an exercise in a learner's copy.
- Confirm the Copy Exercise badge in `README.md` names the publishing owner and the repository name.

## Validate end to end

1. Copy the exercise into a scratch account or organization and wait for the Step 1 issue.
1. Follow the steps in the GitHub web UI (no CLI needed), using branches `feat/recipe-model`, `feat/recipe-scaling`, and `feat/recipe-page`.
1. Confirm each step's feedback fails with useful hints before it passes, and that the next step is posted.
1. Confirm in step 3 that the `stacks` API (`X-GitHub-Api-Version: 2026-03-10`) returns the stack, and that closing and reopening the top pull request re-runs the check. Also confirm Step 0 created the "Plan your recipe scaler stack" issue, and that editing its body triggers Step 1.

## Reset a learner copy

Delete the copy and create a new one from the template. Step workflows are enabled one at a time by the previous step, so re-enabling them by hand will not restore the exercise state.

## Toolkit version

Every workflow pins `skills/exercise-toolkit@v0.9.3`. When upgrading, change every reference together and confirm the tag exists with `gh api repos/skills/exercise-toolkit/git/ref/tags/TAG`.
