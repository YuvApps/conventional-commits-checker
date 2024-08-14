# Conventional Commits Checker

This package provides a tool for validating Conventional Commit messages according to the Conventional Commits specification.

## Installation

```bash
pip install conventional-commits-checker
```

## Conventional Commits Specification
Supported commit types and their importance levels:

- 'BREAKING CHANGE': 0 (highest importance) (Major version bump)
- 'feat': 1 (Minor version bump)
- 'fix': 2 (Patch version bump)
- 'perf': 3
- 'refactor': 4
- 'docs': 5
- 'style': 6
- 'test': 7
- 'build': 8
- 'ci': 9
- 'chore': 10
- 'revert': 11
- 'config': 12

## Usage

### Get the next version

```python
from conventional_commits_checker.conventional_commit import ConventionalCommit

previous_version = <previous_version as string> # e.g. "1.2.3"
commit_messages = <list of commit messages as strings> # e.g. ["feat(api): add user authentication endpoint", "fix(ui): correct button alignment"]

next_version = ConventionalCommit.get_next_version(previous_version, commit_messages)

print(next_version)
```

### Get the sorted commits

```python
from conventional_commits_checker.conventional_commit import ConventionalCommit

commit_messages = <list of commit messages as strings> # e.g. ["feat(api): add user authentication endpoint", "fix(ui): correct button alignment"]

sorted_commits = ConventionalCommit.get_commits_by_importance(commit_messages)

print(sorted_commits)
```

### Get the bump type

```python
from conventional_commits_checker.conventional_commit import ConventionalCommit

commit_messages = <list of commit messages as strings> # e.g. ["feat(api): add user authentication endpoint", "fix(ui): correct button alignment"]

bump_type = ConventionalCommit.get_version_type_by_commits(commit_messages)

print(bump_type)
```

## Example

```python
from conventional_commits_checker.conventional_commit import ConventionalCommit

previous_version = "1.2.3"
commit_messages = [
    "feat(api): add user authentication endpoint",
    "Not an important commit",
    "fix(ui): correct button alignment",
    "docs(readme): update installation guide",
    "style(core): format code according to PEP8",
    "refactor(api): optimize query performance",
    "BREAKING CHANGE: remove deprecated method",
    "WIP"
]

# Get the next version and sorted commits
next_version = ConventionalCommit.get_next_version(previous_version, commit_messages)
sorted_commits = ConventionalCommit.get_commits_by_importance(commit_messages)
bump_type = ConventionalCommit.get_version_type_by_commits(commit_messages)

# Output the results
print(f"Current version: {previous_version}")
print(f"Bump type: {bump_type}")
print(f"Next version: {next_version}")
print("Sorted valid commit messages:")
for sorted_commit in sorted_commits:
    print(f" - {sorted_commit}")
```


## Output
Current version: 1.2.3
Bump type: major
Next version: 2.0.0
Sorted valid commit messages:
 - ('BREAKING CHANGE', 'BREAKING CHANGE: remove deprecated method')
 - ('feat', 'feat(api): add user authentication endpoint')
 - ('fix', 'fix(ui): correct button alignment')
 - ('refactor', 'refactor(api): optimize query performance')
 - ('docs', 'docs(readme): update installation guide')
 - ('style', 'style(core): format code according to PEP8')
