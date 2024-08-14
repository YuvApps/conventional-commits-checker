from conventional_commits_checker.utils.conventional_commit import ConventionalCommit

def test_conventional_commit_simple():
    # Example input
    previous_version = "1.2.3"
    commit_messages = [
        "feat(api): add user authentication endpoint",
        "fix(ui): correct button alignment",
        "docs(readme): update installation guide",
        "style(core): format code according to PEP8",
        "refactor(api): optimize query performance",
        "BREAKING CHANGE: remove deprecated method"
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

if __name__ == "__main__":
    test_conventional_commit_simple()