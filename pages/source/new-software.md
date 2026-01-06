# Making New Software

## Python Repository Template

### Purpose of This Template

The purpose of this template is to act as a **baseline for new pure Python software projects** within the CCPBioSim ecosystem.

It provides a standardised project structure, development tooling, and automation to help developers:

- Start new projects quickly with minimal setup
- Follow best practices for scientific Python software
- Ensure reproducibility and maintainability
- Integrate easily with CCPBioSim infrastructure (CI, documentation, citation)

This template is intended to be **customised**, not used unchanged.

---

### When to Use This Template

Use this template when creating:

- A new pure Python library or application
- Research software intended for publication or reuse
- Tools that will be maintained within the CCPBioSim organisation
- Projects requiring testing, documentation, and automated releases

This template may **not** be appropriate for:

- Single-use scripts or notebooks
- Projects dominated by non-Python code (e.g., C/C++, Fortran)
- Experimental prototypes with no intention of long-term maintenance

---

### Creating a New Repository

New projects should be created using GitHub’s template mechanism to ensure the full project structure and configuration are copied correctly.

---

#### Using GitHub “Use this template”

1. Navigate to the CCPBioSim Python repository template on GitHub.
2. Click **“Use this template”**.
3. Select **“Create a new repository”**.
4. Choose:
   - A repository name (lowercase, hyphen-separated)
   - The CCPBioSim organisation
   - Repository visibility (public or private)

GitHub will create a new repository containing an independent copy of the template.

---

#### Initial Repository Setup

Once the repository has been created from the template, a small amount of initial configuration is required before development can begin.

1. **Clone the repository locally**

    ```bash
    git clone https://github.com/CCPBioSim/<your-project-name>.git
    cd <your-project-name>
    ```

2. **Rename the Python package**

    The directory under `src/` defines the import name of your Python package. This name will be used when importing the package in code and when the project is installed.

    - Locate the package directory under `src/`
    - Rename it to match your chosen package name
    - Ensure the name is a valid Python identifier (lowercase, underscores allowed)

    Example:

        src/
        your_package_name/

3. **Update project metadata**

    Update the following files to reflect your project:

    - `pyproject.toml`
        - `project.name`
        - `project.description`
        - `project.authors`
        - `project.license`
    - `README.md`
        - Project name and description
        - Badges and links
    - `CITATION.cff`
        - Title
        - Authors
        - Version (if applicable)

4. **Set up a Python environment**

    Create and activate a virtual environment using your preferred tool (e.g., `venv`, `conda`):

        python -m venv .venv
        source .venv/bin/activate

5. **Install the project in editable mode**

    Install the package along with development dependencies:

        pip install -e .[pre-commit,docs,testing]

6. **Run the test suite**

    Verify that the template is functioning correctly:

        pytest

7. **Run linters and formatters**

    This repository uses **pre-commit hooks** to automatically run linters, formatters, and other quality checks before each commit. This ensures consistent code style and reduces errors.

    #### Install the hooks in the repository

    Run the following command in the root of your repository:

        pre-commit install

    This configures Git to run the pre-commit checks automatically before each commit.

    #### Verify hooks and run manually (optional)

    To check that everything is working correctly, or to run the hooks on all files immediately:

        pre-commit run --all-files

    This will run all configured hooks (linters, formatters, etc.) on every file in the repository.

    #### Notes

    - After installing, the hooks will run **automatically on every commit**.
    - If a hook fails, the commit will be blocked until the issues are fixed.
    - You can still run hooks manually as shown above to check the entire codebase.

    If all checks pass, the repository is ready for development. At this stage it is encouraged to make an initial commit after completing these steps.

---

### Repository Structure

This template follows a standard Python project layout designed to support development, testing, documentation, and packaging. Below is an overview of the key directories and files.

---

#### Standard Directory Layout

The repository is organized as follows:

    docs/
    src/example_package_YOUR_USERNAME_HERE/
    tests/
    pyproject.toml
    README.md
    LICENSE
    CITATION.cff
    .pre-commit-config.yaml
    .readthedocs.yaml
    .gitignore

- `docs/` - Sphinx documentation source
- `src/` - Python source code
- `tests/` - Unit and integration tests
- `pyproject.toml` - Project metadata and dependencies
- `README.md` / `LICENSE` - Standard project documentation
- `CITATION.cff` - Citation metadata for the package
- `.pre-commit-config.yaml` - Pre-commit hooks configuration
- `.readthedocs.yaml` - Read the Docs configuration
- `.gitignore` - Git ignore rules for temporary and generated files

> **Note:** Generated folders like `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, and `docs/build/` exist but are not relevant for day-to-day development.

---

##### Source Code (`src/`)

All Python code lives under `src/`, using the **package name** you specify:

    src/example_package_YOUR_USERNAME_HERE/
        __init__.py
        example.py

- `__init__.py` - Makes the directory a Python package
- `example.py` - Minimal placeholder function included for coverage and testing

> **Tip:** Rename the `example_package_YOUR_USERNAME_HERE` folder to match your project’s package name. Make sure it’s a valid Python identifier (lowercase letters, underscores allowed).

Example placeholder function:

    # src/example_package_YOUR_USERNAME_HERE/example.py

    def placeholder():
        """Minimal function to allow coverage and serve as a template."""
        return True

This structure ensures that the package is **importable** and ready for expansion.

---

##### Tests (`tests/`)

Unit tests live under the `tests/` directory, mirroring the package structure:

    tests/test_example_package_YOUR_USERNAME_HERE/
        __init__.py
        conftest.py
        test_example.py
    tests/data/  # Optional folder for test data

- `__init__.py` - Allows the test folder to be treated as a package
- `conftest.py` - For pytest fixtures
- `test_example.py` - Placeholder test module demonstrating usage

Example test:

    # tests/test_example_package_YOUR_USERNAME_HERE/test_example.py

    from example_package_YOUR_USERNAME_HERE.example import placeholder

    class TestExamplePackage:
        """
        Class-based placeholder tests for example_package_YOUR_USERNAME_HERE.

        - Demonstrates using a test class with pytest.
        - Can easily be extended with more methods for real tests.
        """

        def test_placeholder(self):
            """
            Minimal placeholder test.

            - Verifies that the placeholder function runs.
            - Serves as a template for adding future tests.
            """
            assert placeholder() is True

> **Tip:** Run all tests with:

    pytest

This layout makes it easy to **add new modules and tests** while keeping the code organized and compatible with pytest.

---

##### Documentation (`docs/`)

The documentation source uses **Sphinx**:

    docs/
        conf.py
        index.rst
        _static/
        _templates/

- `conf.py` - Sphinx configuration file
- `index.rst` - Root of the documentation tree
- `_static/` - Static assets for the documentation (CSS, JS, images)
- `_templates/` - Optional Sphinx templates for customizing layout

> **Tip:** Build the documentation locally with:

    sphinx-build -b html docs/source docs/build/html

The generated HTML will appear in `docs/build/html`.  

This setup allows for **automatic API documentation generation** with `sphinx-autodoc` and seamless integration with Read the Docs.

---

### Customising the Template

#### Project Name and Package Name

- Rename the folder under `src/` to match your package name.
- Must be a valid Python identifier: lowercase letters and underscores.
- This determines the import name of your package.

#### Author and Organisation Information

- Update `pyproject.toml` with author and organisation information.
- Update `CITATION.cff` authors section for proper credit.

#### Licensing

- Update `LICENSE` file if needed.
- Update `pyproject.toml` `project.license` to match.

#### Metadata (`pyproject.toml`)

- Update project name, description, authors, license, and version.
- Ensure dependencies are listed under `[project.dependencies]`.
- Add development dependencies under `[project.optional-dependencies.testing]`
  or `[project.optional-dependencies.pre-commit]` or `[project.optional-dependencies.docs]`.

#### README Customisation

- Update README title, badges, and project description.
- Add links to documentation, issues, and citation information.
- Include installation instructions and a quick-start example.

---

### Development Workflow

#### Setting Up a Local Development Environment

1. Create and activate a virtual environment:

        python -m venv .venv
        source .venv/bin/activate  # Unix/macOS
        .venv\Scripts\activate     # Windows

2. Install the package with development dependencies:

       pip install -e .[pre-commit,docs,testing]

---

#### Running Tests

- Run the full test suite with:

        pytest

- Coverage is measured automatically in CI.
- Tests live under the `tests/` directory.

---

#### Linting and Formatting

- Code style and quality checks are enforced via **pre-commit hooks**.
- Run all checks locally with:

        pre-commit run --all-files

- Hooks run automatically before every commit once installed.

---

#### Pre-commit Hooks

1. Install hooks:

        pre-commit install

2. (Optional) Run hooks manually on all files:

        pre-commit run --all-files

> Pre-commit ensures consistent formatting and prevents common errors
> from entering the codebase.

---

### Continuous Integration, Automation, and Repository Requirements

This section describes how continuous integration (CI), automation services,
documentation, releases, and external tooling are configured and managed for
repositories under the CCPBioSim organisation.

The provided Python template includes preconfigured workflows and configuration
files, but several services require one-time external enablement at the
organisation or repository level.

---

#### Continuous Integration (CI)

##### GitHub Actions

All repositories use GitHub Actions for continuous integration.

###### Key characteristics

- CI is enabled by default
- Workflows live in `.github/workflows/`
- CI runs automatically on pushes and pull requests

###### Standard CI checks

- Unit tests across supported Python versions and platforms
- Pre-commit linting and formatting
- Documentation builds
- Test coverage reporting

CI workflows assume the project can be installed using:

    pip install -e .[pre-commit,docs,testing]

No manual setup is required to enable GitHub Actions.

---

#### Automation and External Services

The template supports several automation services that integrate with CI.
Most configuration already exists in the repository; however, some services
require one-time external activation.

You do not need to enable every service, but any enabled service must be
configured correctly to avoid CI failures.

---

##### Documentation Hosting - Read the Docs

Read the Docs builds and hosts project documentation.

###### Repository configuration

- `.readthedocs.yaml` is provided at the repository root
- Documentation source lives in `docs/`
- Documentation dependencies are installed via the `docs` optional dependency group

###### External setup (one-time)

1. Log in to [Read the Docs](https://readthedocs.org/)
2. Import the GitHub repository
3. Select the default branch (usually `main`)
4. Enable automatic builds

**Authentication**

- Public repositories require no secrets
- Private repositories may require an `RTD_API_KEY` GitHub secret

---

##### Test Coverage - Coveralls

Coveralls collects and displays test coverage results from CI.

###### Repository configuration

- Coverage is generated using `pytest --cov`
- Coverage is uploaded automatically during CI runs

###### External setup (one-time)

1. Log in to [coveralls](https://coveralls.io/)
2. Enable the repository
3. Select GitHub as the provider

**Authentication**

- Public repositories use the default `GITHUB_TOKEN`
- No repository-level secrets are required

Once enabled, add a coverage badge to the README.

---

##### Dependency Management - Renovate (via [mend.io](https://www.mend.io/))

Dependency updates are managed automatically using Renovate, administered
through [mend.io](https://www.mend.io/) at the CCPBioSim organisation level.

###### Repository requirements

- A `.github/renovate.json` configuration file
- All dependencies declared in `pyproject.toml`

###### Enabling Renovate for a repository (one-time)

1. Go to the CCPBioSim GitHub organisation
2. Open **Settings → Installed GitHub Apps**
3. Select **Mend / Renovate**
4. Authenticate if prompted
5. Under **Repository access**, enable the repository

Authentication is handled at the organisation level.
No repository secrets are required.

---

##### Releases and Publishing

###### Automated Releases

Releases are handled via GitHub Actions (for example, `release.yaml`).

The release workflow:

- Creates a version bump pull request
- Tags the release
- Publishes the package to PyPI
- Creates a GitHub release

Repositories must follow semantic versioning:

    MAJOR.MINOR.PATCH

---

###### Publishing to PyPI

Publishing requires a PyPI API token.

###### Required GitHub secret

| Name             | Purpose                     |
|------------------|-----------------------------|
| PYPI_API_TOKEN   | Publishing releases to PyPI |

Secrets are configured via:

    GitHub → Repository → Settings → Secrets and variables → Actions

PyPI credentials must never be committed to the repository.

---

#### Documentation Infrastructure

##### Sphinx Configuration

- Documentation is built using Sphinx
- Configuration lives in `docs/conf.py`
- API documentation is generated using `sphinx-autodoc`

Build documentation locally with:

    sphinx-build -b html docs/source docs/build/html

---

##### Citation and Research Credit

##### CITATION.cff

Each repository must include a `CITATION.cff` file containing:

- Project title
- Authors
- Version
- Release date

This enables citation support on GitHub and DOI generation via Zenodo.

---

##### Archival and DOI Generation - Zenodo

Zenodo archives releases and mints DOIs.

##### External setup (one-time)

1. Log in to [zenodo](https://zenodo.org/)
2. Sign in using GitHub
3. Navigate to **Account → GitHub**
4. Locate the CCPBioSim organisation
5. Enable the repository

Once enabled:

- Each GitHub release is archived automatically
- A DOI is minted per release
- No secrets or tokens are required

---

#### Repository Requirements

Repositories under the CCPBioSim organisation must meet the following
requirements.

---

##### Required Repository Structure

    src/<package_name>/
    tests/
    docs/
    .github/

- The folder under `src/` defines the import path
- It must be a valid Python identifier
- It must match the package name used throughout the project

---

##### Required Files

The following files must exist at the repository root:

- `pyproject.toml`
- `README.md`
- `LICENSE`
- `CITATION.cff`

---

##### pyproject.toml

Defines metadata, dependencies, and build configuration.

Must include:

- Project name, version, description, authors, and license
- Runtime dependencies under `[project.dependencies]`
- Development and documentation dependencies under
  `[project.optional-dependencies]`
- A supported build backend (for example, flit or setuptools)

All CI, documentation, release, and automation tooling depends on this file.

---

##### README.md

Must include:

- Project title and short description
- Installation instructions
- Basic usage or quick-start example
- Links to documentation and issue tracker
- Badges for CI, coverage, documentation, and DOI (where applicable)

---

##### LICENSE

- Must be OSI-approved
- Must match the licence declared in `pyproject.toml`
- Must comply with CCPBioSim licensing policy

---

#### Security and Secrets Policy

- Secrets must never be committed to the repository
- All credentials must be stored as GitHub Actions secrets

##### Allowed secrets

| Secret Name      | Required | Purpose                              |
|------------------|----------|--------------------------------------|
| PYPI_API_TOKEN   | Optional | Publishing to PyPI                   |
| AUTO_PR_MERGE    | Optional | Automated release PR merging         |
| RTD_API_KEY      | Optional | Private Read the Docs builds         |

##### Services requiring no repository secrets

- Read the Docs (public repositories)
- Coveralls
- Renovate (Mend.io)
- Zenodo

Authentication for these services is handled at the CCPBioSim organisation level.

---

### Long-Term Maintenance

- Maintain stable and development branches
- Deprecate features gradually
- Keep documentation, releases, and citation metadata in sync

---

### Common Pitfalls

- Forgetting to rename the `src/` package directory
- Working outside an active virtual environment
- Committing secrets or generated files
- Ignoring CI or pre-commit failures
- Not running tests before pushing changes

---

### Further Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [Read the Docs](https://readthedocs.org/)
- [Pre-commit Hooks](https://pre-commit.com/)
- [Semantic Versioning](https://semver.org/)
- [Zenodo Guide for GitHub Repos](https://guides.github.com/activities/citable-code/)