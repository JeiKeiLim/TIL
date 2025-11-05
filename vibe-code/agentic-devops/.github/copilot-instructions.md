# GitHub Copilot Instructions - Agentic DevOps

**Last updated**: 2025-01-05

## Project Overview

This is the Agentic DevOps project - a development operations system using speckit methodology for feature planning and implementation. The project follows strict constitutional principles for code quality, testing, user experience, performance, and build verification.

## Active Technologies

- Python 3.11 (backend) + FastAPI (001-life-clock)
- Vue 3 (frontend) + Vite (001-life-clock)
- SQLite (storage) (001-life-clock)

## Project Structure

```
backend/
├── src/
│   ├── api/           # FastAPI routes
│   ├── models/        # Data models
│   ├── services/      # Business logic
│   └── config.py
└── tests/
    ├── unit/
    ├── integration/
    └── contract/

frontend/
├── src/
│   ├── components/    # Vue components
│   ├── views/         # Page views
│   ├── stores/        # Pinia state management
│   ├── services/      # API client, utilities
│   └── assets/        # Images, styles
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/

specs/
└── [###-feature-name]/
    ├── spec.md
    ├── plan.md
    ├── research.md
    ├── data-model.md
    ├── quickstart.md
    └── contracts/
```

## Constitutional Principles (MANDATORY)

### I. Code Quality First (NON-NEGOTIABLE)

- **ALL code MUST pass formatting and linting before commit**
- Python: Use `ruff format` and `ruff check`
- JavaScript/Vue: Use `prettier` and `eslint`
- Zero warnings or errors allowed
- Run quality checks after EVERY code modification

### II. Test-Driven Development (NON-NEGOTIABLE)

- **Write tests BEFORE implementation**
- Red-Green-Refactor cycle: Tests fail → Implement → Tests pass
- Target >80% coverage on business logic
- Test types required:
  - Unit tests: isolated functions/classes/components
  - Integration tests: API endpoints, service interactions
  - Contract tests: API contracts
- Tests must be independent and runnable in any order

### III. User Experience Consistency

- Vue components follow design system
- UI interactions responsive (<100ms perceived latency)
- Error states handled gracefully with clear messages
- Loading indicators for operations >500ms
- WCAG 2.1 AA accessibility compliance
- API endpoints follow consistent naming and error formats

### IV. Performance Requirements

- API response times: p50 <100ms, p95 <500ms, p99 <2s
- Frontend: FCP <1.8s, TTI <3.9s, Lighthouse score >90
- Avoid N+1 queries, use eager loading
- Memory usage bounded and predictable

### V. Build and Test Verification (NON-NEGOTIABLE)

**After EVERY code modification, run and pass:**

Backend:
```bash
ruff format .           # Format code
ruff check .           # Lint code
pytest                 # Run tests
```

Frontend:
```bash
npm run format         # Format code
npm run lint          # Lint code
npm run test          # Run tests
npm run build         # Verify build
```

## Technology Stack Requirements (FIXED)

- **Python**: 3.11 (fixed version)
- **Frontend Framework**: Vue 3 (fixed version)
- **Backend Framework**: FastAPI (fixed version)
- **Package Management**: `uv` for Python packages
  ```bash
  uv venv                              # Create environment
  uv pip install -r requirements.txt   # Install deps
  uv pip install <package>             # Add package
  uv pip freeze > requirements.txt     # Update deps
  ```

## Build and Test Commands

### Backend (Python 3.11 + FastAPI)

```bash
cd backend

# Setup
uv venv
source .venv/bin/activate  # macOS/Linux
uv pip install -r requirements.txt

# Development
uvicorn src.api.main:app --reload --port 8000

# Testing
pytest                                    # Run all tests
pytest --cov=src --cov-report=html       # With coverage
pytest tests/unit/                       # Unit tests only
pytest tests/integration/                # Integration tests only

# Quality Checks (MANDATORY after every change)
ruff format .                            # Auto-format
ruff check .                            # Lint
mypy src/                               # Type check (if configured)
```

### Frontend (Vue 3 + Vite)

```bash
cd frontend

# Setup
npm install

# Development
npm run dev                              # Start dev server (port 5173)

# Testing
npm run test                             # Unit tests (Vitest)
npm run test:watch                       # Watch mode
npm run test:e2e                         # E2E tests (Playwright)

# Quality Checks (MANDATORY after every change)
npm run format                           # Auto-format (Prettier)
npm run lint                            # Lint (ESLint)
npm run lint:fix                        # Auto-fix linting issues
npm run build                           # Build for production
```

## Language-Specific Conventions

### Python 3.11
- Use type hints for all function parameters and returns
- Follow PEP 8 style guide (enforced by ruff)
- Use dataclasses or Pydantic models for data structures
- Async/await for I/O operations in FastAPI
- Exception handling: specific exceptions, not bare `except:`
- Docstrings: Google style for functions/classes

### Vue 3 (Composition API)
- Use `<script setup>` syntax
- Composition API over Options API
- TypeScript for type safety when practical
- Props validation with defineProps
- Emit events with defineEmits
- Reactive state with ref() and reactive()
- Component naming: PascalCase for files, kebab-case in templates

### FastAPI
- Use dependency injection for services
- Pydantic models for request/response validation
- Async route handlers for I/O operations
- OpenAPI documentation auto-generated
- Error handling with HTTPException
- CORS middleware configured for local development

## Code Review Checklist

Before submitting ANY code:

- [ ] Tests written FIRST (TDD)
- [ ] All tests passing
- [ ] Code formatted (ruff/prettier)
- [ ] Code linted (ruff/eslint)
- [ ] Type hints added (Python)
- [ ] Error handling implemented
- [ ] Edge cases covered
- [ ] Performance considerations addressed
- [ ] Accessibility requirements met (if UI)
- [ ] Documentation updated
- [ ] Build succeeds (npm run build for frontend)

## Current Feature: Life Clock App (001-life-clock)

**Purpose**: Personal life visualization tool mapping lifespan to seasons

**Key Requirements**:
- User enters birth date
- Calculate current life season based on 85-year life expectancy
  - Spring: 0-21.25 years
  - Summer: 21.25-42.5 years
  - Fall: 42.5-63.75 years
  - Winter: 63.75+ years
- Display seasonal background matching current season
- Add/edit/delete life events (past and future)
- Data stored locally (localStorage for web, SQLite for backend)
- Single-user app, no authentication required

**Data Entities**:
- UserProfile: birth date, timestamps
- LifeEvent: id (UUID), date, description (1-500 chars), timestamps
- LifeSeason: computed based on age (not stored)

**API Endpoints**:
- GET/PUT `/api/profile` - User profile (birth date)
- GET `/api/season` - Current life season calculation
- GET/POST `/api/events` - List/create events
- GET/PUT/DELETE `/api/events/{id}` - Event operations

**UI Components**:
- SeasonDisplay.vue - Main season visualization
- TimelineView.vue - Event timeline
- EventForm.vue - Add/edit event form
- EventCard.vue - Individual event display
- DateInput.vue - Birth date input

**State Management (Pinia)**:
- useProfileStore - birth date, current season, age
- useEventsStore - events array, CRUD operations

## Recent Changes

- 001-life-clock: Added Python 3.11 + FastAPI + Vue 3 + SQLite

## Testing Guidelines

### Backend Tests (pytest)

```python
# Unit test example
def test_calculate_life_season():
    """Test season calculation for different ages."""
    from services.season_calculator import calculate_life_season
    
    assert calculate_life_season(age=15) == "Spring"
    assert calculate_life_season(age=30) == "Summer"
    assert calculate_life_season(age=50) == "Fall"
    assert calculate_life_season(age=70) == "Winter"

# Integration test example
def test_create_event_api(client):
    """Test event creation via API."""
    response = client.post("/api/events", json={
        "date": "2010-06-15",
        "description": "Graduated from university"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["description"] == "Graduated from university"
```

### Frontend Tests (Vitest)

```javascript
// Component test example
import { mount } from '@vue/test-utils'
import { describe, it, expect } from 'vitest'
import SeasonDisplay from '@/components/SeasonDisplay.vue'

describe('SeasonDisplay', () => {
  it('displays correct season', () => {
    const wrapper = mount(SeasonDisplay, {
      props: { season: 'Spring' }
    })
    expect(wrapper.text()).toContain('Spring')
  })
})
```

## Common Patterns

### API Error Handling (FastAPI)

```python
from fastapi import HTTPException

def get_user_profile():
    profile = db.get_profile()
    if not profile:
        raise HTTPException(
            status_code=404,
            detail="Profile not found. Please set your birth date first."
        )
    return profile
```

### Vue Component Error Handling

```vue
<script setup>
import { ref } from 'vue'
import { useToast } from '@/composables/useToast'

const { showError } = useToast()
const loading = ref(false)

async function saveEvent() {
  loading.value = true
  try {
    await api.createEvent(eventData)
  } catch (error) {
    showError('Failed to save event. Please try again.')
  } finally {
    loading.value = false
  }
}
</script>
```

## Performance Best Practices

### Backend
- Use SQLite connection pooling
- Index frequently queried fields
- Avoid N+1 queries (eager load relationships)
- Use async/await for I/O operations
- Cache computed values (e.g., season calculation)

### Frontend
- Lazy load routes with Vue Router
- Virtual scrolling for long event lists (>50 items)
- Debounce user input
- Preload seasonal background images
- Use CSS containment for performance
- Optimize images (WebP format, responsive sizes)

## Commit Message Format

Follow conventional commits:

```
<type>(<scope>): <description>

[optional body]
```

**Types**: feat, fix, docs, style, refactor, test, chore, perf

**Examples**:
- `feat(api): add user profile endpoint`
- `fix(ui): resolve season background flicker`
- `test(services): add unit tests for season calculator`
- `chore(deps): update fastapi to 0.104.1`

## Documentation

- API docs auto-generated at http://localhost:8000/docs
- Component documentation in component files (JSDoc comments)
- Feature specs in `specs/[###-feature-name]/`
- Constitution reference: `.specify/memory/constitution.md`

## Resources

- **FastAPI**: https://fastapi.tiangolo.com/
- **Vue 3**: https://vuejs.org/
- **Pinia**: https://pinia.vuejs.org/
- **Vite**: https://vitejs.dev/
- **pytest**: https://docs.pytest.org/
- **Vitest**: https://vitest.dev/
- **uv**: https://github.com/astral-sh/uv

## Important Notes for Copilot

1. **ALWAYS follow TDD**: Write tests before implementation
2. **ALWAYS run quality checks**: Format, lint, test after every change
3. **NEVER skip constitutional principles**: All 5 principles are mandatory
4. **Use fixed versions**: Python 3.11, Vue 3, FastAPI (no version flexibility)
5. **Package management**: Use `uv` for Python, not pip directly
6. **Local-only**: No cloud services, no authentication, single-user
7. **Accessibility**: WCAG 2.1 AA compliance required for all UI
8. **Performance**: Meet the specified targets (FCP <1.8s, API <100ms)
9. **Error handling**: All error states must be handled gracefully
10. **Documentation**: Update relevant docs when changing code

## When Suggesting Code

- Suggest complete, working code (not pseudocode)
- Include necessary imports
- Add type hints (Python) or TypeScript types (Vue)
- Include error handling
- Add comments for complex logic
- Follow the language conventions above
- Ensure code passes linting/formatting rules
- Suggest corresponding tests (TDD approach)
