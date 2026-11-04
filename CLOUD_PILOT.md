# Cloud Pilot Notes

This file was added during a cloud development connectivity test. It
describes the repository's layout and how to validate it.

## Repository structure

```
github-demo/
├── README.md       # Project description: a simple demo of the basic Git workflow
├── start.txt       # Plain-text sample file ("Test Git Quick Start demo")
└── CLOUD_PILOT.md  # This file
```

- Default branch: `master`
- There is no application code, build system, package manifest, or CI
  configuration (no `.github/workflows/`) in the repository.

## Running tests

The repository has no test suite and no test runner, so there are no
tests to run.

Lightweight checks you can run locally:

```bash
git status
```

```bash
git diff --check master...HEAD
```

The second command flags whitespace errors (such as trailing whitespace
or conflict markers) introduced on the current branch.
