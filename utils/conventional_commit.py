import re
from packaging.version import Version

# Regular expression to match conventional commit messages
CONVENTIONAL_COMMIT_PATTERN = re.compile(
    r'^(feat|fix|docs|style|refactor|perf|test|chore|build|ci|revert|config)(\(\w+\))?: (.+)$')

# Define the importance of each commit type, with BREAKING CHANGE being the highest
COMMIT_TYPE_IMPORTANCE = {
    'BREAKING CHANGE': 0,
    'feat': 1,
    'fix': 2,
    'perf': 3,
    'refactor': 4,
    'docs': 5,
    'style': 6,
    'test': 7,
    'build': 8,
    'ci': 9,
    'chore': 10,
    'revert': 11,
    'config': 12
}

class ConventionalCommit:
    @staticmethod
    def is_valid_conventional_commit(message):
        return CONVENTIONAL_COMMIT_PATTERN.match(message)

    @staticmethod
    def get_next_version(current_version, commit_messages):
        major_bump = False
        minor_bump = False
        patch_bump = False

        for message in commit_messages:
            if 'BREAKING CHANGE' in message:
                major_bump = True
            else:
                match = ConventionalCommit.is_valid_conventional_commit(message)
                if match:
                    commit_type = match.group(1)
                    if commit_type == 'feat':
                        minor_bump = True
                    elif commit_type == 'fix' or commit_type == 'perf':
                        patch_bump = True

        # Determine the next version
        version = Version(current_version)
        major, minor, patch = version.release

        if major_bump:
            next_version = f"{major + 1}.0.0"
        elif minor_bump:
            next_version = f"{major}.{minor + 1}.0"
        elif patch_bump:
            next_version = f"{major}.{minor}.{patch + 1}"
        else:
            next_version = current_version  # No relevant changes, keep the current version

        return next_version

    @staticmethod
    def get_commits_by_importance(commit_messages):
        valid_commits = []

        for message in commit_messages:
            if 'BREAKING CHANGE' in message:
                valid_commits.append(('BREAKING CHANGE', message))
            else:
                match = ConventionalCommit.is_valid_conventional_commit(message)
                if match:
                    commit_type = match.group(1)
                    valid_commits.append((commit_type, message))

        return sorted(valid_commits, key=lambda x: COMMIT_TYPE_IMPORTANCE[x[0]])


    @staticmethod
    def get_version_type_by_commits(commit_messages):
        bump_type = "patch"

        for message in commit_messages:
            if 'BREAKING CHANGE' in message:
                bump_type = "major"
            else:
                match = ConventionalCommit.is_valid_conventional_commit(message)
                if match:
                    commit_type = match.group(1)
                    if commit_type == 'feat':
                        bump_type = "minor"

        return bump_type


