# Changes and releases

Open or reuse an issue before implementing a change. State the problem, scope, and acceptance criteria. Each pull request must link its corresponding issue.

For changes targeting the default branch, use `Closes #123` in the PR body so GitHub closes the issue when the PR merges. For an intermediate branch, link the issue with `Refs #123`; the final release PR must carry the closing reference.

Each release has a release issue and a release PR. The release issue lists the scope and outstanding checks. The release PR targets `main`, records validation and limitations, and includes `Closes #<release-issue>`. Leave the release issue open until its release PR merges. Do not close unfinished work merely because a release ships.

Review public biographical claims and links before merging. Record completed work accurately; distinguish plans, ongoing work, and published results. Do not publish confidential correspondence, commercial terms, or personal contact details from supporting records.
