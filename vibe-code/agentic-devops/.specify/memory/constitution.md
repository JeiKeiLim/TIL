# Agentic DevOps Constitution

<!--
========================================
SYNC IMPACT REPORT
========================================
Version Change: [NEW] → 1.0.0
Change Type: Initial creation of project constitution

Modified Principles:
  - N/A (initial version)

Added Sections:
  - Core Principles (5 principles covering code quality, testing, UX, performance, build verification)
  - Technology Stack Requirements
  - Development Workflow Standards
  - Governance

Removed Sections:
  - N/A (initial version)

Templates Requiring Updates:
  ✅ plan-template.md - Constitution Check section aligns with new principles
  ✅ spec-template.md - Already reviewed, compatible with constitution requirements
  ✅ tasks-template.md - Testing and build verification gates align with principles

Follow-up TODOs:
  - None - all placeholders filled

Rationale for Version 1.0.0:
  Initial constitution establishing foundational governance for code quality, testing,
  user experience, performance, and build verification standards for Python 3.11/Vue 3/FastAPI
  stack using uv package management.
========================================
-->

## Core Principles

### I. Code Quality First (NON-NEGOTIABLE)

**All code MUST meet quality standards before merge:**

- **Formatting & Linting**: All code MUST pass formatting and linting checks configured for the project
  - Python code formatted with `black` and `ruff` (or configured formatters)
  - Vue/JavaScript code formatted with `prettier` and linted with `eslint`
  - Zero warnings or errors in linting output before commit
- **Automatic Verification**: Quality checks MUST be run after every code modification
- **Pre-commit Gates**: Code quality tools MUST be configured in development environment
- **Type Safety**: Python code SHOULD use type hints; Vue components SHOULD use TypeScript when practical

**Rationale**: Consistent code quality prevents technical debt, improves maintainability, enables confident refactoring, and ensures all team members work with the same standards. Automated enforcement removes subjective judgment and reduces review friction.

### II. Test-Driven Development (NON-NEGOTIABLE)

**TDD workflow MUST be followed for all features:**

- **Red-Green-Refactor Cycle**: Tests written → User approval → Tests fail → Implementation → Tests pass → Refactor
- **Test First**: No production code written without a failing test demonstrating the need
- **Test Coverage**: All critical paths MUST have test coverage; aim for >80% coverage on business logic
- **Test Types Required**:
  - **Unit Tests**: For isolated functions, classes, and components
  - **Integration Tests**: For API endpoints, service interactions, and data flow
  - **Contract Tests**: For API contracts and external interfaces
- **Test Independence**: Tests MUST be runnable independently and in any order
- **Fast Feedback**: Unit test suite MUST run in <10 seconds; integration tests <2 minutes

**Rationale**: TDD ensures requirements are understood before implementation, creates living documentation, enables safe refactoring, catches regressions immediately, and produces inherently testable designs. Mandatory TDD prevents untested code from entering the codebase.

### III. User Experience Consistency

**User-facing interfaces MUST provide consistent, predictable experiences:**

- **Design System**: Vue components MUST follow established design system and component library
- **Response Time**: UI interactions MUST feel responsive (<100ms perceived latency)
- **Error Handling**: All error states MUST be handled gracefully with clear, actionable user messages
- **Loading States**: Long operations (>500ms) MUST show loading indicators
- **Accessibility**: UI MUST meet WCAG 2.1 AA standards (keyboard navigation, screen reader support, color contrast)
- **Mobile Responsive**: Interfaces SHOULD be usable on mobile devices unless desktop-only is explicitly specified
- **API Consistency**: REST API endpoints MUST follow consistent naming, error format, and response structure conventions

**Rationale**: Consistent UX reduces cognitive load, builds user trust, decreases support burden, and enables users to transfer knowledge across features. Accessibility compliance ensures product usability for all users and may be legally required.

### IV. Performance Requirements

**All implementations MUST meet performance standards:**

- **API Response Time**: 
  - p50 < 100ms for simple queries
  - p95 < 500ms for complex operations
  - p99 < 2s maximum acceptable latency
- **Frontend Performance**:
  - First Contentful Paint (FCP) < 1.8s
  - Time to Interactive (TTI) < 3.9s
  - Lighthouse Performance score > 90
- **Database Queries**: N+1 queries MUST be avoided; eager loading MUST be used where appropriate
- **Resource Limits**:
  - API endpoints MUST handle rate limiting gracefully
  - Memory usage SHOULD be bounded and predictable
  - File uploads MUST have size limits enforced
- **Performance Testing**: Performance-critical features MUST include load testing as part of acceptance

**Rationale**: Performance directly impacts user satisfaction, retention, and operational costs. Defining clear performance budgets prevents performance degradation over time and ensures consistent user experience across load conditions.

### V. Build and Test Verification (NON-NEGOTIABLE)

**After EVERY code modification, the following MUST be executed and pass:**

- **Formatting Check**: Run formatters in check mode to verify code formatting
  - Python: `ruff format --check .` and/or `black --check .`
  - Vue/JS: `npm run format:check` or `prettier --check .`
- **Linting Check**: Run linters to verify code quality standards
  - Python: `ruff check .` and/or `pylint src/`
  - Vue/JS: `npm run lint` or `eslint .`
- **Type Checking**: Run type checkers if project uses typing
  - Python: `mypy src/` (if configured)
  - TypeScript: `tsc --noEmit` (if configured)
- **Test Suite**: Run all applicable test suites
  - Backend: `pytest` (unit, integration, contract tests)
  - Frontend: `npm test` or `vitest`
- **Build Verification**: Verify the application builds successfully
  - Backend: Ensure FastAPI server starts without errors
  - Frontend: `npm run build` must succeed

**Enforcement**: Developers MUST run these checks locally before pushing. CI/CD pipeline MUST enforce all checks and block merge on failure.

**Rationale**: Immediate verification catches issues at the earliest, cheapest point in the development cycle. Mandatory post-modification testing prevents broken code from propagating, reduces debugging time, and maintains codebase health. This principle ensures the project is always in a shippable state.

## Technology Stack Requirements

**The following technology versions are FIXED for this project:**

- **Python**: 3.11 (fixed version)
- **Frontend Framework**: Vue 3 (fixed version)
- **Backend Framework**: FastAPI (fixed version)
- **Package Management**: `uv` MUST be used for all Python package management
  - Installation: `pip install uv`
  - Create environment: `uv venv`
  - Install dependencies: `uv pip install -r requirements.txt`
  - Add package: `uv pip install <package>`
  - Freeze: `uv pip freeze > requirements.txt`

**Dependency Management**:

- All Python dependencies MUST be tracked in `requirements.txt` with pinned versions
- Frontend dependencies MUST be tracked in `package.json` with semantic versioning ranges
- Dependency updates MUST be reviewed for breaking changes before upgrading
- Security vulnerabilities in dependencies MUST be addressed within 2 weeks of disclosure

**Rationale**: Fixed technology versions ensure consistency across development environments, reduce compatibility issues, and simplify onboarding. Using `uv` provides faster, more reliable Python package management. Version pinning prevents unexpected breakage from dependency updates.

## Development Workflow Standards

**All development work MUST follow these workflow standards:**

### Code Modification Workflow

1. **Before Starting**: 
   - Pull latest changes from main branch
   - Create feature branch from up-to-date main
   - Review relevant specifications and design documents

2. **During Development**:
   - Write tests first (TDD principle)
   - Implement feature incrementally
   - Commit frequently with clear, descriptive messages
   - **After each modification**: Run formatting, linting, type checking, tests, and build verification
   - Fix any failures immediately before continuing

3. **Before Push**:
   - Rebase on latest main if needed
   - Ensure all quality checks pass locally
   - Review your own changes (self-review)
   - Write/update documentation as needed

4. **Pull Request Requirements**:
   - Title follows convention: `type(scope): description`
   - Description includes: problem, solution, testing performed, breaking changes
   - All CI checks MUST pass (green build)
   - Code coverage MUST not decrease
   - At least one approval from code owner required

### Code Review Standards

**Reviewers MUST verify**:

- [ ] Principle I: Code quality checks pass (formatting, linting)
- [ ] Principle II: Tests exist and follow TDD (tests written first, adequate coverage)
- [ ] Principle III: User experience is consistent (if user-facing changes)
- [ ] Principle IV: Performance requirements met (if performance-sensitive)
- [ ] Principle V: All build and test verification steps documented and passing
- [ ] Code is understandable and maintainable
- [ ] Edge cases are handled
- [ ] Security implications are considered
- [ ] Documentation is updated

**Reviewers SHOULD**:

- Provide constructive, actionable feedback
- Ask questions rather than making demands
- Acknowledge good practices and improvements
- Approve promptly when standards are met

### Commit Standards

- **Format**: `type(scope): description`
- **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`
- **Examples**:
  - `feat(api): add user authentication endpoint`
  - `fix(ui): resolve button alignment issue on mobile`
  - `test(services): add integration tests for payment flow`
  - `chore(deps): update fastapi to 0.104.1`

### Branch Strategy

- **Main Branch**: Always deployable, protected, requires PR for changes
- **Feature Branches**: `feature/<issue>-<description>` or `###-<feature-name>`
- **Fix Branches**: `fix/<issue>-<description>`
- **Release Branches**: `release/<version>` (if applicable)
- **Hotfix Branches**: `hotfix/<issue>-<description>`

## Governance

**Constitution Authority**: This constitution supersedes all other development practices and guidelines. When conflicts arise between this document and other documentation, the constitution takes precedence.

**Amendment Process**:

1. **Proposal**: Any team member may propose an amendment via documented RFC
2. **Discussion**: Team reviews amendment, discusses implications and alternatives
3. **Approval**: Amendments require consensus or majority vote (as defined by team)
4. **Documentation**: Approved amendments MUST be documented with:
   - Version bump (using semantic versioning: MAJOR.MINOR.PATCH)
   - Rationale for change
   - Impact analysis on existing principles and practices
   - Migration plan if existing code is affected
5. **Communication**: All team members MUST be notified of constitutional changes
6. **Synchronization**: Related templates and documentation MUST be updated to reflect amendments

**Version Control**:

- **Version Format**: MAJOR.MINOR.PATCH semantic versioning
- **MAJOR**: Backward-incompatible governance changes, principle removals, or redefinitions
- **MINOR**: New principles added, material expansion of existing principles
- **PATCH**: Clarifications, wording improvements, typo fixes, non-semantic refinements

**Compliance Verification**:

- All PRs and code reviews MUST verify compliance with constitutional principles
- Constitution violations MUST be documented with justification in Complexity Tracking section of plan.md
- Unjustified complexity or principle violations MUST be rejected
- Regular compliance audits SHOULD be performed quarterly

**Continuous Improvement**:

- Constitution SHOULD be reviewed quarterly for relevance and effectiveness
- Retrospectives SHOULD identify process improvements and potential amendments
- Metrics SHOULD be tracked to measure adherence and outcomes:
  - Test coverage percentage
  - Code quality check pass rate
  - PR review cycle time
  - Build success rate
  - Performance metrics

**Enforcement**:

- Automated tooling MUST enforce principles where possible (CI/CD gates)
- Code review process MUST verify manual compliance
- Constitution violations in production MUST be addressed with corrective action plan
- Repeated non-compliance MUST be escalated and addressed

**Runtime Guidance**:

For day-to-day development guidance and agent-specific instructions, refer to:
- Template files in `.specify/templates/`
- Command documentation in `.github/prompts/speckit.*.prompt.md`
- Feature specifications in `specs/[###-feature-name]/`

**Version**: 1.0.0 | **Ratified**: 2025-01-05 | **Last Amended**: 2025-01-05
