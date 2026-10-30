---
name: auto-commit-task
description: Safely create a meaningful Git commit after completing any task that changes files in a Git repository. Use automatically at the end of implementation, refactoring, configuration, documentation, test, or asset-editing work when the requested work is complete and verified.
---

# Auto Commit Task

Create one focused commit for the completed request without capturing unrelated user work.

## Workflow

1. Confirm the requested work is complete and run proportionate verification.
2. Confirm the current directory belongs to a Git repository with `git rev-parse --show-toplevel`.
3. Inspect `git status --short` and the relevant diffs before staging anything.
4. Identify only the paths and changes produced for the current request.
5. Check those changes for secrets, credentials, generated junk, and unintended files.
6. Stage only the identified task changes using explicit paths.
7. Review `git diff --cached --stat` and `git diff --cached`.
8. Create a focused commit using the PDF-derived message rules below. Split independent completed changes into separate commits when useful.
9. Report the commit hash and message in the final response.

## Safety Rules

- Preserve all pre-existing, unrelated, and user-authored changes.
- Never use `git add .`, `git add -A`, broad globs, or destructive Git commands.
- Never amend, squash, rebase, reset, force-push, or push unless the user explicitly requests it.
- Never bypass hooks with `--no-verify` unless the user explicitly requests it.
- Do not commit secrets, credentials, environment files, or suspicious generated artifacts.
- If a touched file also contains unrelated pre-existing edits that cannot be isolated safely, do not commit that file automatically. Explain the conflict.
- If hooks modify files, inspect the new diff, re-run relevant checks, and commit only when the result remains in scope.
- If verification fails, do not create a commit unless the user explicitly accepts the failure.
- If the directory is not a Git repository or the task creates no changes, skip the commit and state why.

## Commit Message

Follow the supplied `How to Write a Git Commit Message.pdf` (H4mit, Bamdad Group). Use English Conventional Commit messages with this shape:

```text
[ISSUE_KEY] [#COMMANDS] type[(scope)]: subject [#meta]
```

Brackets denote optional parts; never include literal placeholders. The PDF's complete template is `<ISSUE_KEY> #<COMMANDS> <type>(scope): <subject> #<meta>`. Omit Jira fields when no real issue or command authorization is available.

- Choose the type from `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, or `ci`.
- `style` means formatting without behavior changes; `refactor` means restructuring without a feature or fix; `build` covers compilation, packaging, and auxiliary tooling; `ci` covers delivery automation.
- Add a scope only when it identifies the affected subsystem clearly, such as `auth`, `wallet`, or `pwa`.
- Describe the actual outcome in imperative present tense, start the subject text with lowercase, and omit its final period.
- Keep the subject concise, normally within 72 characters. Add a body separated by a blank line when motivation, behavior, tradeoffs, or breaking changes need explanation.
- Copy an issue key exactly from the user's task or an authoritative project reference. Never invent an issue key or infer one from an unrelated ticket.
- Jira Smart Commit commands can mutate external issue state. Include `#in-progress`, `#close`, or `#time` only when explicitly authorized for the identified issue. Use supplied or verified work duration; never fabricate logged time or equate unattended elapsed time with work.
- Do not interpret automatic local commit authorization as permission to update Jira or push a commit.
- The PDF defines optional `#wip` for unfinished work, `#irrelevant` for changes excluded from changelogs such as typos, and `#nocomp` for incomplete commits. Use these only when applicable and requested or established by the repository. The ordinary automatic workflow commits completed work, so it does not add incomplete-work tags.

Examples without Jira automation:

```text
feat(auth): add passwordless login
fix(cart): preserve quantities after refresh
docs: clarify local setup
refactor(api): centralize error mapping
test(search): cover empty query behavior
```

Example only when the real issue and Smart Commit actions are explicitly authorized:

```text
BAMD-23649 #close #time 1h 15m feat(auth): introduce BMI oauth sign-in
```
