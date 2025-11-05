# Tasks: Life Clock App

**Input**: Design documents from `/specs/001-life-clock/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/api-spec.yaml ✓

**Tests**: Tests are included and follow TDD (Test-Driven Development) - write tests FIRST, ensure they FAIL, then implement.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

This is a web application with separate backend and frontend:
- Backend: `backend/src/`, `backend/tests/`
- Frontend: `frontend/src/`, `frontend/tests/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend/ directory structure (src/, tests/, requirements.txt, pyproject.toml)
- [X] T002 Create frontend/ directory structure (src/, tests/, package.json, vite.config.js, vitest.config.js)
- [ ] T003 [P] Initialize Python project with uv: create venv, install FastAPI, pytest, ruff, black
- [ ] T004 [P] Initialize Vue 3 project: install Vue 3, Pinia, Vite, Vitest, Playwright, prettier, eslint
- [X] T005 [P] Configure ruff and black for Python in backend/pyproject.toml
- [X] T006 [P] Configure prettier and eslint for Vue/JS in frontend/.prettierrc and frontend/.eslintrc.js
- [X] T007 [P] Create backend/README.md with setup and run instructions
- [X] T008 [P] Create frontend/README.md with setup and run instructions

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Backend Foundation

- [X] T009 Create SQLite database schema in backend/src/database.py (user_profile and life_events tables with triggers)
- [X] T010 [P] Create base FastAPI app in backend/src/api/main.py (CORS middleware, error handlers, health check)
- [X] T011 [P] Create backend/src/config.py (environment settings, database path, CORS origins)
- [X] T012 [P] Create backend/src/models/__init__.py (base model classes and common types)

### Frontend Foundation

- [X] T013 Create Vue Router in frontend/src/router.js (routes for Home, Setup, Events views)
- [X] T014 [P] Create Pinia store initialization in frontend/src/main.js
- [X] T015 [P] Create API client base in frontend/src/services/api.js (axios setup, error handling, base URL)
- [X] T016 [P] Create date utilities in frontend/src/services/dateUtils.js (age calculation, season mapping)
- [X] T017 [P] Create localStorage wrapper in frontend/src/services/storage.js (profile and events persistence)
- [X] T018 Create base App.vue with router-view and seasonal theme container
- [X] T019 [P] Create seasonal CSS themes in frontend/src/assets/styles/seasons.css (Spring, Summer, Fall, Winter)
- [X] T020 [P] Create main CSS in frontend/src/assets/styles/main.css (base layout, typography)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - View Life as Seasons (Priority: P1) 🎯 MVP

**Goal**: Users can enter their birth date and see their current life season with appropriate background

**Independent Test**: Enter birth date → Verify correct season displays → Verify seasonal background changes

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T021 [P] [US1] Unit test for season calculation in backend/tests/unit/test_season_calculator.py (test all 4 seasons, edge cases)
- [X] T022 [P] [US1] Unit test for UserProfile model in backend/tests/unit/test_models_profile.py (validation, past date check)
- [X] T023 [P] [US1] Integration test for GET/PUT /api/profile in backend/tests/integration/test_api_profile.py
- [X] T024 [P] [US1] Integration test for GET /api/season in backend/tests/integration/test_api_season.py
- [ ] T025 [P] [US1] Contract test for profile and season endpoints in backend/tests/contract/test_api_contract.py (OpenAPI spec validation)
- [X] T026 [P] [US1] Frontend unit test for dateUtils.js in frontend/tests/unit/services/test_dateUtils.spec.js
- [ ] T027 [P] [US1] Frontend component test for SeasonDisplay.vue in frontend/tests/unit/components/test_SeasonDisplay.spec.js
- [ ] T028 [P] [US1] Frontend component test for DateInput.vue in frontend/tests/unit/components/test_DateInput.spec.js
- [ ] T029 [US1] E2E test for birth date entry and season display in frontend/tests/e2e/lifecycle.spec.js

### Backend Implementation for User Story 1

- [X] T030 [P] [US1] Create UserProfile model in backend/src/models/user_profile.py (birthDate validation, timestamps)
- [X] T031 [P] [US1] Create LifeSeason model in backend/src/models/life_season.py (season enum, computed properties)
- [X] T032 [US1] Implement season calculator service in backend/src/services/season_calculator.py (age to season mapping, depends on T030, T031)
- [X] T033 [US1] Implement storage service in backend/src/services/storage_service.py (SQLite CRUD for profile, depends on T030)
- [X] T034 [US1] Implement GET /api/profile endpoint in backend/src/api/profile_routes.py (depends on T033)
- [X] T035 [US1] Implement PUT /api/profile endpoint in backend/src/api/profile_routes.py (validation, depends on T033)
- [X] T036 [US1] Implement GET /api/season endpoint in backend/src/api/season_routes.py (depends on T032, T033)
- [X] T037 [US1] Register profile and season routes in backend/src/api/main.py (depends on T034, T035, T036)
- [X] T038 [US1] Add error handling for profile not found (404) in backend/src/api/profile_routes.py
- [X] T039 [US1] Add validation for birth date in past in backend/src/api/profile_routes.py

### Frontend Implementation for User Story 1

- [X] T040 [P] [US1] Create profile store in frontend/src/stores/profile.js (birthDate state, fetchProfile, updateProfile actions)
- [X] T041 [P] [US1] Create season store in frontend/src/stores/season.js (season state, fetchSeason action, depends on profile store)
- [X] T042 [P] [US1] Create SeasonDisplay.vue component in frontend/src/components/SeasonDisplay.vue (season name, background, progress)
- [X] T043 [P] [US1] Create DateInput.vue component in frontend/src/components/DateInput.vue (date validation, past date check)
- [X] T044 [US1] Create SetupView.vue in frontend/src/views/SetupView.vue (initial birth date entry, depends on T040, T043)
- [X] T045 [US1] Create HomeView.vue in frontend/src/views/HomeView.vue (main season display, depends on T041, T042)
- [X] T046 [US1] Add seasonal background images in frontend/src/assets/images/ (spring-bg.jpg, summer-bg.jpg, fall-bg.jpg, winter-bg.jpg) - Using CSS gradients instead
- [X] T047 [US1] Implement seasonal theme switching logic in HomeView.vue (depends on T041, T046)
- [X] T048 [US1] Add navigation logic from SetupView to HomeView after profile creation (depends on T044, T045)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently
- Users can enter birth date
- System displays correct season
- Seasonal background changes appropriately
- All tests passing
- Run quality checks: `ruff format .`, `ruff check .`, `pytest` (backend), `npm run format`, `npm run lint`, `npm test` (frontend)

---

## Phase 4: User Story 2 - Add Life Events (Priority: P2)

**Goal**: Users can add life events with dates and descriptions to their timeline

**Independent Test**: Add event with date and description → Verify event appears on timeline → Verify event persists after refresh

### Tests for User Story 2 ⚠️

- [ ] T049 [P] [US2] Unit test for LifeEvent model in backend/tests/unit/test_models_event.py (validation, isFuture calculation)
- [ ] T050 [P] [US2] Unit test for event manager service in backend/tests/unit/test_event_manager.py (CRUD operations)
- [ ] T051 [P] [US2] Integration test for GET /api/events in backend/tests/integration/test_api_events.py (list, filter, sort)
- [ ] T052 [P] [US2] Integration test for POST /api/events in backend/tests/integration/test_api_events.py (create, validation)
- [ ] T053 [P] [US2] Contract test for events endpoints in backend/tests/contract/test_api_contract.py (OpenAPI spec validation)
- [ ] T054 [P] [US2] Frontend component test for EventForm.vue in frontend/tests/unit/components/test_EventForm.spec.js
- [ ] T055 [P] [US2] Frontend component test for EventCard.vue in frontend/tests/unit/components/test_EventCard.spec.js
- [ ] T056 [P] [US2] Frontend component test for TimelineView.vue in frontend/tests/unit/components/test_TimelineView.spec.js
- [ ] T057 [US2] E2E test for adding events in frontend/tests/e2e/lifecycle.spec.js (add event, verify display, verify persistence)

### Backend Implementation for User Story 2

- [ ] T058 [P] [US2] Create LifeEvent model in backend/src/models/life_event.py (UUID, date, description validation, isFuture property)
- [ ] T059 [US2] Implement event manager service in backend/src/services/event_manager.py (create, list, filter by past/future, sort, depends on T058)
- [ ] T060 [US2] Extend storage service in backend/src/services/storage_service.py (SQLite CRUD for events, depends on T058)
- [ ] T061 [US2] Implement GET /api/events endpoint in backend/src/api/event_routes.py (list, filter, sort parameters, depends on T059)
- [ ] T062 [US2] Implement POST /api/events endpoint in backend/src/api/event_routes.py (create with validation, depends on T059)
- [ ] T063 [US2] Register event routes in backend/src/api/main.py (depends on T061, T062)
- [ ] T064 [US2] Add validation for description length (1-500 chars) in backend/src/api/event_routes.py
- [ ] T065 [US2] Add validation for date format in backend/src/api/event_routes.py

### Frontend Implementation for User Story 2

- [ ] T066 [P] [US2] Create events store in frontend/src/stores/events.js (events array, fetchEvents, createEvent actions)
- [ ] T067 [P] [US2] Create EventForm.vue component in frontend/src/components/EventForm.vue (date input, description textarea, validation)
- [ ] T068 [P] [US2] Create EventCard.vue component in frontend/src/components/EventCard.vue (display date, description, past/future indicator)
- [ ] T069 [US2] Create TimelineView.vue component in frontend/src/components/TimelineView.vue (chronological event list, depends on T068)
- [ ] T070 [US2] Integrate TimelineView into HomeView.vue in frontend/src/views/HomeView.vue (depends on T069, T045)
- [ ] T071 [US2] Add event creation modal/form in HomeView.vue (depends on T067, T066)
- [ ] T072 [US2] Implement visual distinction for past vs future events in EventCard.vue (styling, icons, depends on T068)
- [ ] T073 [US2] Add error handling for event creation failures in EventForm.vue (display validation errors, depends on T067)
- [ ] T074 [US2] Add loading indicators for event operations in TimelineView.vue (depends on T069)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently
- Users can still view their season (US1)
- Users can now also add events (US2)
- Events display on timeline
- Past and future events visually distinguished
- All tests passing
- Run quality checks: `ruff format .`, `ruff check .`, `pytest` (backend), `npm run format`, `npm run lint`, `npm test` (frontend)

---

## Phase 5: User Story 3 - Manage Life Events (Priority: P3)

**Goal**: Users can edit or delete previously added events

**Independent Test**: Create event → Edit event → Verify changes persist → Delete event → Verify removal

### Tests for User Story 3 ⚠️

- [ ] T075 [P] [US3] Integration test for GET /api/events/{eventId} in backend/tests/integration/test_api_events.py
- [ ] T076 [P] [US3] Integration test for PUT /api/events/{eventId} in backend/tests/integration/test_api_events.py (update validation)
- [ ] T077 [P] [US3] Integration test for DELETE /api/events/{eventId} in backend/tests/integration/test_api_events.py
- [ ] T078 [P] [US3] Frontend integration test for event editing in frontend/tests/integration/views/test_EventsView.spec.js
- [ ] T079 [US3] E2E test for editing and deleting events in frontend/tests/e2e/lifecycle.spec.js (edit flow, delete with confirmation)

### Backend Implementation for User Story 3

- [ ] T080 [US3] Implement GET /api/events/{eventId} endpoint in backend/src/api/event_routes.py (depends on T059)
- [ ] T081 [US3] Implement PUT /api/events/{eventId} endpoint in backend/src/api/event_routes.py (update with validation, depends on T059)
- [ ] T082 [US3] Implement DELETE /api/events/{eventId} endpoint in backend/src/api/event_routes.py (depends on T059)
- [ ] T083 [US3] Add update method to event manager service in backend/src/services/event_manager.py (depends on T059)
- [ ] T084 [US3] Add delete method to event manager service in backend/src/services/event_manager.py (depends on T059)
- [ ] T085 [US3] Add error handling for event not found (404) in backend/src/api/event_routes.py
- [ ] T086 [US3] Add validation for partial updates in PUT /api/events/{eventId} (allow updating date or description separately)

### Frontend Implementation for User Story 3

- [ ] T087 [US3] Add updateEvent action to events store in frontend/src/stores/events.js (depends on T066)
- [ ] T088 [US3] Add deleteEvent action to events store in frontend/src/stores/events.js (depends on T066)
- [ ] T089 [US3] Create EventsView.vue in frontend/src/views/EventsView.vue (event management page with edit/delete actions)
- [ ] T090 [US3] Add edit mode to EventForm.vue in frontend/src/components/EventForm.vue (pre-populate form for editing, depends on T067)
- [ ] T091 [US3] Add edit button to EventCard.vue in frontend/src/components/EventCard.vue (opens EventForm in edit mode, depends on T068, T090)
- [ ] T092 [US3] Add delete button with confirmation to EventCard.vue (depends on T068, T088)
- [ ] T093 [US3] Implement delete confirmation modal in EventCard.vue (prevent accidental deletion, depends on T092)
- [ ] T094 [US3] Add navigation to EventsView from HomeView in frontend/src/views/HomeView.vue (depends on T089, T045)
- [ ] T095 [US3] Add error handling for update failures in EventForm.vue (display validation errors, depends on T090)
- [ ] T096 [US3] Add optimistic updates for edit/delete in events store (immediate UI feedback, rollback on error, depends on T087, T088)

**Checkpoint**: All user stories should now be independently functional
- Users can view their season (US1)
- Users can add events (US2)
- Users can now edit and delete events (US3)
- All CRUD operations working
- All tests passing
- Run quality checks: `ruff format .`, `ruff check .`, `pytest` (backend), `npm run format`, `npm run lint`, `npm test` (frontend)

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T097 [P] Add comprehensive error messages across all API endpoints in backend/src/api/
- [ ] T098 [P] Add loading states for all async operations in frontend/src/views/ and frontend/src/components/
- [ ] T099 [P] Implement accessibility improvements (ARIA labels, keyboard navigation) in frontend/src/components/
- [ ] T100 [P] Optimize seasonal background image loading (lazy load, WebP format) in frontend/src/assets/images/
- [ ] T101 [P] Add virtual scrolling for timeline if >50 events in frontend/src/components/TimelineView.vue
- [ ] T102 [P] Add unit tests for storage service in backend/tests/unit/test_storage_service.py
- [ ] T103 [P] Add unit tests for API client in frontend/tests/unit/services/test_api.spec.js
- [ ] T104 Add performance monitoring and logging in backend/src/api/main.py (request timing, error rates)
- [ ] T105 [P] Update backend/README.md with complete setup, testing, and deployment instructions
- [ ] T106 [P] Update frontend/README.md with complete setup, testing, and deployment instructions
- [ ] T107 Run full test suite: pytest (backend), npm test (frontend), npm run test:e2e (E2E)
- [ ] T108 Run full quality checks: ruff format/check (backend), npm run format/lint (frontend), npm run build (frontend)
- [ ] T109 Validate against specs/001-life-clock/quickstart.md (follow setup steps, verify all commands work)
- [ ] T110 Create deployment documentation in specs/001-life-clock/ (production build steps, environment setup)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3, 4, 5)**: All depend on Foundational phase completion
  - User Story 1 (P1 - Phase 3): Can start after Foundational - No dependencies on other stories
  - User Story 2 (P2 - Phase 4): Can start after Foundational - Independent from US1 (can run in parallel)
  - User Story 3 (P3 - Phase 5): Depends on User Story 2 completion (extends event CRUD with update/delete)
- **Polish (Phase 6)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1 - View Seasons)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2 - Add Events)**: Can start after Foundational (Phase 2) - Independent from US1 (can run in parallel)
- **User Story 3 (P3 - Manage Events)**: Requires User Story 2 (extends event functionality with edit/delete)

### Within Each User Story

- Tests MUST be written and FAIL before implementation (TDD)
- Backend models before services
- Backend services before endpoints
- Backend endpoints before frontend stores
- Frontend stores before components
- Frontend components before views
- Core implementation before error handling and polish
- Story complete and tested before moving to next priority

### Parallel Opportunities

**Phase 1 (Setup):**
- T003, T004 (backend and frontend initialization) can run in parallel
- T005, T006, T007, T008 (configuration and docs) can run in parallel after initialization

**Phase 2 (Foundational):**
- Backend tasks T010, T011, T012 can run in parallel after T009 (database schema)
- Frontend tasks T014, T015, T016, T017, T019, T020 can run in parallel after T013 (router)

**Phase 3 (User Story 1):**
- All test tasks T021-T028 can run in parallel (different test files)
- Backend models T030, T031 can run in parallel
- Frontend stores T040, T041 can run in parallel after backend endpoints
- Frontend components T042, T043 can run in parallel

**Phase 4 (User Story 2):**
- All test tasks T049-T056 can run in parallel
- Frontend components T067, T068 can run in parallel

**Phase 5 (User Story 3):**
- All test tasks T075-T078 can run in parallel
- Backend endpoints T080, T081, T082 can run in parallel after service methods

**Phase 6 (Polish):**
- Tasks T097-T103, T105, T106 can run in parallel (different areas)

---

## Parallel Example: User Story 1 Backend

```bash
# Launch all tests for User Story 1 Backend together:
Task T021: "Unit test for season calculation in backend/tests/unit/test_season_calculator.py"
Task T022: "Unit test for UserProfile model in backend/tests/unit/test_models_profile.py"
Task T023: "Integration test for GET/PUT /api/profile in backend/tests/integration/test_api_profile.py"
Task T024: "Integration test for GET /api/season in backend/tests/integration/test_api_season.py"
Task T025: "Contract test for profile and season endpoints in backend/tests/contract/test_api_contract.py"

# Then launch backend models together:
Task T030: "Create UserProfile model in backend/src/models/user_profile.py"
Task T031: "Create LifeSeason model in backend/src/models/life_season.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only) - Recommended ✅

1. Complete Phase 1: Setup → Project structure ready
2. Complete Phase 2: Foundational (CRITICAL) → Foundation ready
3. Complete Phase 3: User Story 1 → MVP ready!
4. **STOP and VALIDATE**: 
   - Test User Story 1 independently
   - Run all quality checks: `ruff format .`, `ruff check .`, `pytest`, `npm run format`, `npm run lint`, `npm test`
   - Follow quickstart.md to verify setup instructions
   - Demo to stakeholders
5. Decide: Ship MVP or continue to User Story 2

**MVP Deliverable**: Users can enter birth date, see their life season with seasonal background

### Incremental Delivery (All User Stories)

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Run quality checks → Deploy/Demo (MVP! ✅)
3. Add User Story 2 → Test independently → Run quality checks → Deploy/Demo (Enhanced timeline 📅)
4. Add User Story 3 → Test independently → Run quality checks → Deploy/Demo (Full CRUD ✏️)
5. Complete Polish → Test all stories together → Final quality checks → Production release 🚀

Each story adds value without breaking previous stories.

### Parallel Team Strategy (3+ Developers)

**Phase 1-2**: Team works together on Setup + Foundational

**After Foundational complete**:
- Developer A: User Story 1 (T021-T048) - Priority P1
- Developer B: User Story 2 (T049-T074) - Priority P2 (can start in parallel)
- Developer C: Sets up quality checks, CI/CD, documentation

**After User Story 2 complete**:
- Developer C: User Story 3 (T075-T096) - Priority P3 (depends on US2)

**Final Phase**: All developers collaborate on Polish (T097-T110)

Stories complete and integrate independently.

---

## Quality Gates (MANDATORY per Constitution)

### After EVERY code modification:

**Backend:**
```bash
ruff format .           # Auto-format code
ruff check .           # Lint code
pytest                 # Run all tests
```

**Frontend:**
```bash
npm run format         # Auto-format code
npm run lint          # Lint code
npm run test          # Run unit tests
npm run build         # Verify build succeeds
```

### Before marking User Story complete:

1. All tests for that story passing ✅
2. All code formatted and linted ✅
3. Build succeeds ✅
4. Story independently testable ✅
5. Documentation updated ✅
6. Constitution check passed ✅

### Before final release:

1. All user stories complete and tested
2. Full E2E test suite passing (`npm run test:e2e`)
3. Performance targets met (FCP <1.8s, API <100ms)
4. Accessibility validated (WCAG 2.1 AA)
5. quickstart.md verified (all commands work)
6. All quality checks passing

---

## Notes

- **[P] tasks**: Different files, no dependencies - can run in parallel
- **[Story] label**: Maps task to specific user story for traceability (US1, US2, US3)
- **TDD**: Write tests FIRST (T021-T029 before T030-T048 for US1)
- **Each user story**: Should be independently completable and testable
- **Verify tests fail**: Before implementing (Red-Green-Refactor)
- **Commit frequently**: After each task or logical group
- **Stop at checkpoints**: Validate story independently before continuing
- **Constitutional compliance**: Run quality checks after EVERY code modification (mandatory)
- **Performance**: Keep 50+ events support in mind (virtual scrolling if needed)
- **Accessibility**: WCAG 2.1 AA compliance throughout (ARIA labels, keyboard navigation)
- **Local-only**: No cloud services, no authentication (single-user app)

---

## Task Count Summary

- **Phase 1 (Setup)**: 8 tasks
- **Phase 2 (Foundational)**: 12 tasks (CRITICAL - blocks all stories)
- **Phase 3 (User Story 1 - P1)**: 28 tasks (9 tests + 19 implementation)
- **Phase 4 (User Story 2 - P2)**: 26 tasks (9 tests + 17 implementation)
- **Phase 5 (User Story 3 - P3)**: 22 tasks (5 tests + 17 implementation)
- **Phase 6 (Polish)**: 14 tasks

**Total**: 110 tasks

**MVP (User Story 1 only)**: 48 tasks (Phase 1 + Phase 2 + Phase 3)
**Enhanced (US1 + US2)**: 74 tasks (MVP + Phase 4)
**Full Feature (All stories)**: 96 tasks (Enhanced + Phase 5)
**Production Ready (All + Polish)**: 110 tasks (Full + Phase 6)
