# Stack It Up: Ship a Big Feature as Small, Reviewable Pull Requests

## Summary

Learners split one feature into three stacked PRs with `gh stack`, then merge the stack from the bottom up.

## Exercise identity

- **Title**: Stack It Up: Ship a Big Feature as Small, Reviewable Pull Requests
- **Repository name**: `stacked-prs-stack-it-up` (approved)
- **Learner copy name**: `skills-stacked-prs-stack-it-up`
- **Target owner**: decide at publish
- **Copyright holder**: decide at publish

## Welcome block

- **Who is this for**: Developers comfortable with branches and pull requests.
- **What you'll learn**: What a stack is, `gh stack init/add/push/submit/view`, how base branches chain, and how bottom-up merging works.
- **What you'll build**: A 3-PR stack for a small Python "recipe scaler" app.
- **Prerequisites**: GitHub CLI 2.90.0 or later, Git 2.36 or later, `gh auth login` completed.
- **How long**: about 30 minutes.

## Learning objectives

- Explain how a stack is structured (trunk, base chaining, dependency direction).
- Create and submit a stack with `gh stack`.
- Read a stack's state with `gh stack view` and the stack map on GitHub.
- Merge part or all of a stack from the bottom up.

## Scenario

A team lead wants a "recipe scaler" feature. A single large PR would stall in review, so the learner ships three small layers: data model, scaling logic, and CLI output.

## Learner journey

### Step 1: Install the tool and plan your stack

- Theory: what a stack is (bottom PR targets trunk, each later PR targets the branch below, dependencies go in lower layers).
- Activity: clone the copy, install `gh extension install github/gh-stack`, comment a 3-layer plan on the Step 1 issue.
- Actions Trigger: `issue_comment`
- Grading-Check: graded; the comment lists at least 3 layers.
- Learner artifact: a comment with the layered plan.

### Step 2: Build the first two layers

- Theory: `gh stack init`, `gh stack add`, `gh stack add -Am`, dependency rule.
- Activity 1: layer 1 `feat/recipe-model` (`recipe.py`).
- Activity 2: layer 2 `feat/recipe-scaling` (`scale.py`), `gh stack view`, `gh stack push`.
- Actions Trigger: `push` to `feat/**` (decided in build round 1: replaces `workflow_dispatch`, because `gh stack push` already pushes the branches).
- Grading-Check: graded; both branches exist on the remote with their files, and the scaling branch is ahead of the model branch.
- Learner artifact: two pushed, ordered branches.

### Step 3: Add the top layer and submit the stack

- Theory: `gh stack submit`, the stack icon and stack map, rules and CI run for every layer.
- Activity: layer 3 `feat/recipe-cli` (`cli.py`), `gh stack submit`, comment on the Step 3 issue which branch each PR targets.
- Actions Trigger: `pull_request` (opened, only for head `feat/recipe-cli`), plus `issue_comment` on the Step 3 issue as a retry
- Grading-Check: graded; the stacks API returns one stack of three PRs with the expected branches on `main`.
- Learner artifact: a 3-PR linked stack.

### Step 4: Merge from the bottom up

- Theory: bottom-up merging, merging a mid-stack PR, automatic re-targeting.
- Activity: merge the middle PR, observe, merge the top PR.
- Actions Trigger: `pull_request` (closed, merged, only for head `feat/recipe-cli`)
- Grading-Check: graded; all three PRs are merged and `main` has `recipe.py`, `scale.py`, and `cli.py`.
- Learner artifact: all layers on `main`.

## Review recap

- Accomplishments: planned, built, submitted, and merged a 3-layer stack.
- What's next: managing stacks, the `gh-stack` skill for Copilot, rolling stacks out to an organization.

## File map

| File | Purpose |
| --- | --- |
| `.github/exercise-outline.md` | Approved outline |
| `README.md` | Welcome, badge, start |
| `.github/steps/{1,2,3,4}-step.md` | Step content |
| `.github/steps/x-review.md` | Review recap |
| `.github/workflows/0-start-exercise.yml` | Start workflow |
| `.github/workflows/{1,2,3}-step.yml` | Step workflows |
| `.github/workflows/4-step.yml` | `Step 4 # Last step of the exercise` |
| `FEATURE_SPEC.md` | Starter content: the recipe scaler spec |

## Risks and open questions

- Stacked PRs are new; the stacks REST API (`2026-03-10`) and `gh stack` behavior may change.
- `gh stack` runs locally, so the exercise cannot run entirely in the browser.
- Step 4 depends on the learner repository's merge settings.
