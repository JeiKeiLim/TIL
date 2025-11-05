# Research: Life Clock App

**Date**: 2025-01-05  
**Feature**: Life Clock App ([spec.md](./spec.md))  
**Purpose**: Resolve technical unknowns and establish best practices for implementation

## Research Areas

### 1. Local Data Storage Strategy

**Decision**: Use browser localStorage for web version, SQLite for potential Electron desktop version

**Rationale**:
- localStorage is built into all modern browsers, requires no additional dependencies
- Maximum 5-10MB storage is sufficient for user profile + 100 events (~1-2KB per event max)
- Synchronous API makes it simple to use with Vue 3 Composition API
- For desktop app variant, SQLite provides more robust storage with better performance
- Both options keep data entirely local as required by spec

**Alternatives Considered**:
- **IndexedDB**: More powerful but overkill for simple key-value storage of profile + events; adds complexity
- **File system API**: Not universally supported across browsers; requires permissions
- **In-memory only**: Would lose data on refresh, violating FR-008 persistence requirement

**Implementation Notes**:
- Use JSON serialization for storing user profile and events array
- Structure: `{ profile: { birthDate: "ISO-8601" }, events: [ { id, date, description, isFuture } ] }`
- Validate data on read to handle corruption gracefully
- Consider migration strategy if switching to SQLite for desktop

### 2. Date Calculation and Season Mapping

**Decision**: Use native JavaScript Date for calculations, implement pure function for season mapping

**Rationale**:
- Native Date handles timezone, leap years, and edge cases automatically
- Season calculation is simple math: `(age / 85) * 4` mapped to [Spring, Summer, Fall, Winter]
- Pure functions are easily testable and have no side effects
- date-fns library for formatting and manipulation if needed, but native Date sufficient

**Alternatives Considered**:
- **Moment.js**: Deprecated and large bundle size (problematic for <50MB constraint)
- **Day.js**: Lighter alternative but still adds dependency for basic operations we can do natively
- **Luxon**: Excellent but overkill for our simple use case

**Implementation Notes**:
```javascript
// Season calculation logic
function calculateLifeSeason(birthDate, lifeExpectancy = 85) {
  const now = new Date();
  const birth = new Date(birthDate);
  const ageInYears = (now - birth) / (365.25 * 24 * 60 * 60 * 1000);
  const seasonIndex = Math.floor((ageInYears / lifeExpectancy) * 4);
  const seasons = ['Spring', 'Summer', 'Fall', 'Winter'];
  return seasons[Math.min(seasonIndex, 3)]; // Cap at Winter
}
```

### 3. Vue 3 State Management

**Decision**: Use Pinia for global state management of profile and events

**Rationale**:
- Pinia is the official state management solution for Vue 3 (Vuex replacement)
- Provides reactive state with TypeScript support
- Lightweight (~1KB gzipped)
- Better DevTools integration than plain reactive objects
- Composition API friendly

**Alternatives Considered**:
- **Vuex**: Older, more verbose, being phased out in favor of Pinia
- **Plain reactive()**: Works for simple cases but harder to organize and debug at scale
- **Provide/Inject**: Good for component trees but lacks time-travel debugging and DevTools support

**Implementation Notes**:
- Create two stores: `useProfileStore` and `useEventsStore`
- Profile store: manages birthDate, currentSeason, age
- Events store: manages event array, CRUD operations, filtering (past/future)
- Both stores sync to localStorage on mutations

### 4. Seasonal Theme Implementation

**Decision**: CSS custom properties (variables) + Vue reactive classes + background images

**Rationale**:
- CSS variables allow dynamic theme switching without JavaScript overhead
- Vue's `:class` binding makes reactive theme application trivial
- Background images preloaded for smooth transitions
- Supports user preferences (reduced motion, high contrast)

**Alternatives Considered**:
- **CSS-in-JS libraries**: Adds bundle size and complexity
- **Separate CSS files per season**: Harder to maintain, no smooth transitions
- **Inline styles**: Works but harder to maintain and override

**Implementation Notes**:
```css
/* Season themes via CSS variables */
:root.spring {
  --bg-primary: #E8F5E9;
  --accent: #4CAF50;
  --text: #1B5E20;
}
:root.summer {
  --bg-primary: #FFF9C4;
  --accent: #FFD54F;
  --text: #F57F17;
}
/* etc for fall, winter */
```

### 5. Timeline Visualization

**Decision**: Custom SVG-based timeline with Vue component

**Rationale**:
- SVG provides crisp rendering at any zoom level
- Can handle 50+ events efficiently
- Fully styleable with CSS
- Accessible (screen reader compatible with proper ARIA)
- No external charting library needed

**Alternatives Considered**:
- **Canvas**: Better for >1000 elements, but overkill and less accessible
- **Chart.js / D3**: Heavy dependencies, designed for data visualization not timeline
- **HTML/CSS only**: Difficult to position events precisely on timeline scale

**Implementation Notes**:
- Timeline renders as horizontal SVG with year markers
- Events positioned by date relative to birth and life expectancy
- Past events render below line, future events above line (visual distinction per FR-017)
- Click event for editing, hover shows full description

### 6. Backend API Design

**Decision**: REST API with FastAPI, minimal endpoints

**Rationale**:
- RESTful design is simple and well-understood
- FastAPI provides automatic OpenAPI docs, request validation, async support
- For local-only app, API overhead is minimal but provides clean separation
- Enables future multi-device sync if requirements change

**Alternatives Considered**:
- **No backend**: Could work with localStorage only, but limits testing and future extensibility
- **GraphQL**: Overkill for simple CRUD operations
- **gRPC**: Too complex for local-only app

**API Endpoints**:
```
GET    /api/profile          # Get user profile (birth date)
PUT    /api/profile          # Set/update birth date
GET    /api/season           # Get current season calculation
GET    /api/events           # List all events
POST   /api/events           # Create event
PUT    /api/events/{id}      # Update event
DELETE /api/events/{id}      # Delete event
```

### 7. Testing Strategy

**Decision**: 
- Backend: pytest with >80% coverage target
- Frontend: Vitest for unit/integration, Playwright for E2E
- TDD approach: write tests before implementation

**Rationale**:
- pytest is Python standard with excellent fixture support
- Vitest is Vite-native, faster than Jest for Vue 3 projects
- Playwright provides cross-browser E2E testing
- Aligns with Constitution Principle II (TDD mandatory)

**Test Coverage Plan**:
- **Unit tests**: All calculation functions (season, age, date validation)
- **Component tests**: Each Vue component in isolation
- **Integration tests**: API endpoints, store mutations, localStorage sync
- **E2E tests**: Complete user journeys (setup → add events → edit → delete)

**Implementation Notes**:
- Use test fixtures for date mocking (avoid flaky tests from "now" changes)
- Mock localStorage in frontend tests
- Use FastAPI TestClient for backend integration tests

### 8. Accessibility (WCAG 2.1 AA Compliance)

**Decision**: Follow Vue A11y best practices, use semantic HTML, ARIA labels

**Rationale**:
- Constitution Principle III mandates WCAG 2.1 AA compliance
- Semantic HTML provides free accessibility
- Vue has excellent a11y ecosystem (vue-a11y plugins)

**Implementation Checklist**:
- [ ] Keyboard navigation for all interactive elements
- [ ] Focus indicators visible and clear
- [ ] Color contrast ratios meet AA standards (4.5:1 for text)
- [ ] Screen reader labels for timeline events
- [ ] Form inputs have associated labels
- [ ] Error messages announced to screen readers
- [ ] Skip links for navigation
- [ ] No motion for users with `prefers-reduced-motion`

**Tools**:
- axe DevTools for automated testing
- NVDA/VoiceOver for manual screen reader testing
- Lighthouse accessibility audits

### 9. Performance Optimization

**Decision**: Lazy load seasonal background images, virtualize timeline if >50 events

**Rationale**:
- Constitution Principle IV sets performance budgets
- Background images (4 x ~500KB each) are largest assets
- Timeline with 100 events needs virtualization to maintain 60fps scroll

**Optimization Techniques**:
- Image preloading with `<link rel="preload">`
- Responsive images (different sizes for mobile/desktop)
- Virtual scrolling for timeline (only render visible events)
- Code splitting by route (Vue Router async components)
- Tree shaking unused dependencies

**Performance Targets** (from Constitution):
- First Contentful Paint < 1.8s ✓
- Time to Interactive < 3.9s ✓
- Lighthouse Performance score > 90 ✓

### 10. Development Tools Setup

**Decision**: 
- Python: uv for package management, ruff for linting/formatting, mypy for type checking
- Frontend: Vite for build, Prettier for formatting, ESLint for linting

**Rationale**:
- Constitution mandates uv for Python package management
- ruff is faster than black+flake8 combined
- Vite provides fastest HMR for Vue 3
- Prettier/ESLint are industry standard

**Configuration Files Needed**:
- `pyproject.toml` (Python tools config)
- `requirements.txt` (Python dependencies)
- `package.json` (Node dependencies)
- `.prettierrc` (Prettier config)
- `.eslintrc.cjs` (ESLint config)
- `vite.config.js` (Vite config)
- `vitest.config.js` (Vitest config)

## Technology Stack Summary

### Backend
- **Language**: Python 3.11
- **Framework**: FastAPI 0.104+
- **Package Manager**: uv
- **Validation**: Pydantic v2
- **Testing**: pytest, pytest-asyncio
- **Linting**: ruff
- **Type Checking**: mypy
- **Storage**: SQLite (via sqlite3 module)

### Frontend
- **Framework**: Vue 3.3+ (Composition API)
- **State**: Pinia 2.1+
- **Routing**: Vue Router 4
- **Build**: Vite 5
- **Testing**: Vitest, Playwright
- **Linting**: ESLint 8
- **Formatting**: Prettier 3
- **Utilities**: date-fns 3 (if needed)

### Development
- **Version Control**: Git
- **Package Manager**: uv (Python), npm (Node)
- **Environment**: Python 3.11, Node 18+

## Next Steps

1. ✅ Research complete
2. → Proceed to Phase 1: Design (data-model.md, contracts/)
3. → Proceed to Phase 1: Quickstart guide
4. → Update agent context with technology decisions
5. → Proceed to Phase 2: Task breakdown (tasks.md via /speckit.tasks)
