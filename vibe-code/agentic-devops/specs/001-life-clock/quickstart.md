# Quickstart Guide: Life Clock App

**Date**: 2025-01-05  
**Feature**: Life Clock App  
**Purpose**: Get the Life Clock app running locally for development

## Prerequisites

### Required Software

- **Python 3.11**: [Download](https://www.python.org/downloads/)
- **Node.js 18+**: [Download](https://nodejs.org/)
- **uv**: Python package manager
  ```bash
  pip install uv
  ```
- **Git**: Version control

### Verify Installation

```bash
python --version  # Should show 3.11.x
node --version    # Should show 18.x or higher
npm --version     # Should show 9.x or higher
uv --version      # Should show uv version
```

## Initial Setup

### 1. Clone Repository (if not already done)

```bash
git clone <repository-url>
cd agentic-devops
git checkout 001-life-clock
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create Python virtual environment with uv
uv venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Verify installation
python -c "import fastapi; print('FastAPI installed successfully')"
```

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install Node dependencies
npm install

# Verify installation
npm list vue  # Should show Vue 3.x
```

## Running the Application

### Terminal 1: Start Backend Server

```bash
cd backend
source .venv/bin/activate  # If not already activated

# Run FastAPI development server
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output**:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Verify**: Open http://localhost:8000/docs to see auto-generated API documentation

### Terminal 2: Start Frontend Dev Server

```bash
cd frontend

# Run Vite development server
npm run dev
```

**Expected output**:
```
VITE v5.x.x  ready in xxx ms

➜  Local:   http://localhost:5173/
➜  Network: use --host to expose
➜  press h + enter to show help
```

**Verify**: Open http://localhost:5173/ to see the app

## Quick Test

### 1. Set Birth Date

1. Open http://localhost:5173/
2. You should see a setup screen
3. Enter your birth date (e.g., January 1, 1990)
4. Click "Continue" or "Save"

### 2. View Life Season

- You should see your current life season (Spring/Summer/Fall/Winter)
- Background should change to match the season
- Season name should be displayed prominently

### 3. Add a Life Event

1. Click "Add Event" or similar button
2. Enter event date (e.g., June 15, 2010)
3. Enter description (e.g., "Graduated from university")
4. Save the event
5. Event should appear on the timeline

### 4. Edit an Event

1. Click on the event you just created
2. Modify the description
3. Save changes
4. Verify the change appears immediately

### 5. Delete an Event

1. Click delete button on the event
2. Confirm deletion
3. Verify event is removed from timeline

## Development Commands

### Backend

```bash
cd backend

# Run tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Run linting
ruff check .

# Run formatting check
ruff format --check .

# Auto-format code
ruff format .

# Type checking (if mypy configured)
mypy src/
```

### Frontend

```bash
cd frontend

# Run unit tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run E2E tests
npm run test:e2e

# Run linting
npm run lint

# Auto-fix linting issues
npm run lint:fix

# Format code
npm run format

# Check formatting
npm run format:check

# Build for production
npm run build

# Preview production build
npm run preview
```

## API Endpoints

### Profile
- `GET /api/profile` - Get user profile
- `PUT /api/profile` - Set/update birth date

### Season
- `GET /api/season` - Get current life season

### Events
- `GET /api/events` - List all events
- `POST /api/events` - Create new event
- `GET /api/events/{id}` - Get specific event
- `PUT /api/events/{id}` - Update event
- `DELETE /api/events/{id}` - Delete event

**Full API Documentation**: http://localhost:8000/docs (when backend is running)

## Project Structure

```
backend/
├── src/
│   ├── api/           # FastAPI routes
│   ├── models/        # Data models
│   ├── services/      # Business logic
│   └── config.py      # Configuration
├── tests/             # Backend tests
└── requirements.txt   # Python dependencies

frontend/
├── src/
│   ├── components/    # Vue components
│   ├── views/         # Page views
│   ├── stores/        # Pinia stores
│   ├── services/      # API client, utilities
│   └── assets/        # Images, styles
├── tests/             # Frontend tests
└── package.json       # Node dependencies
```

## Troubleshooting

### Backend won't start

**Error**: `ModuleNotFoundError: No module named 'fastapi'`
**Solution**: Make sure virtual environment is activated and dependencies are installed
```bash
source backend/.venv/bin/activate
cd backend && uv pip install -r requirements.txt
```

**Error**: `Address already in use`
**Solution**: Port 8000 is occupied. Kill the process or use different port
```bash
# Find process using port 8000
lsof -ti:8000 | xargs kill -9
# Or run on different port
uvicorn src.api.main:app --reload --port 8001
```

### Frontend won't start

**Error**: `Cannot find module 'vue'`
**Solution**: Install dependencies
```bash
cd frontend && npm install
```

**Error**: `Port 5173 already in use`
**Solution**: Vite will automatically try the next available port, or specify manually
```bash
npm run dev -- --port 5174
```

### API requests failing

**Error**: CORS errors in browser console
**Solution**: Make sure backend CORS is configured to allow frontend origin (localhost:5173)

**Error**: `fetch failed` or network errors
**Solution**: 
1. Verify backend is running (http://localhost:8000/docs should load)
2. Check API base URL in frontend config
3. Verify network requests in browser DevTools

### Data not persisting

**Problem**: Events disappear after refresh
**Solution**:
- Check browser console for localStorage errors
- Verify localStorage is not disabled in browser settings
- Check that storage service is correctly saving data

### Tests failing

**Backend**:
```bash
# Clear pytest cache
rm -rf .pytest_cache
rm -rf backend/.pytest_cache

# Run tests with verbose output
pytest -v
```

**Frontend**:
```bash
# Clear node modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Run tests with verbose output
npm run test -- --reporter=verbose
```

## Next Steps

After getting the app running:

1. **Read the spec**: Review `specs/001-life-clock/spec.md` for requirements
2. **Review data model**: Check `specs/001-life-clock/data-model.md` for schema
3. **Check API contract**: See `specs/001-life-clock/contracts/api-spec.yaml`
4. **Follow TDD**: Write tests before implementing features
5. **Run quality checks**: Use linting and formatting tools after every change
6. **Commit frequently**: Make small, atomic commits with clear messages

## Quality Checklist (Run Before Every Commit)

```bash
# Backend
cd backend
ruff format .           # Format code
ruff check .           # Lint code
pytest                 # Run tests

# Frontend
cd frontend
npm run format         # Format code
npm run lint          # Lint code
npm run test          # Run tests
npm run build         # Verify build works
```

**All checks must pass before pushing code!**

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Vue 3 Documentation](https://vuejs.org/)
- [Pinia Documentation](https://pinia.vuejs.org/)
- [Vite Documentation](https://vitejs.dev/)
- [pytest Documentation](https://docs.pytest.org/)
- [Vitest Documentation](https://vitest.dev/)

## Getting Help

If you encounter issues not covered here:

1. Check the API docs: http://localhost:8000/docs
2. Review browser console for errors
3. Check backend logs in terminal
4. Verify all prerequisites are installed correctly
5. Review the constitution: `.specify/memory/constitution.md`
