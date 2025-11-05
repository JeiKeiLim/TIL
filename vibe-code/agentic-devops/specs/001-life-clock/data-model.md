# Data Model: Life Clock App

**Date**: 2025-01-05  
**Feature**: Life Clock App ([spec.md](./spec.md))  
**Purpose**: Define data entities, relationships, and validation rules

## Entity Diagram

```
┌─────────────────────┐
│   UserProfile       │
├─────────────────────┤
│ birthDate: Date     │ 1
│ createdAt: DateTime │───┐
│ updatedAt: DateTime │   │
└─────────────────────┘   │
                          │ has many
                          │
                          │
                        * │
                  ┌───────▼─────────┐
                  │   LifeEvent     │
                  ├─────────────────┤
                  │ id: UUID        │
                  │ date: Date      │
                  │ description: str│
                  │ isFuture: bool  │
                  │ createdAt: ...  │
                  │ updatedAt: ...  │
                  └─────────────────┘
```

## Entities

### UserProfile

**Purpose**: Stores the user's birth date, which is the foundation for all season calculations.

**Attributes**:
- `birthDate` (Date, required): User's date of birth in YYYY-MM-DD format
  - **Validation**: Must be in the past (before today)
  - **Validation**: Must be a valid date (no Feb 30, etc.)
  - **Format**: ISO 8601 date string
- `createdAt` (DateTime, auto): Timestamp when profile was created
- `updatedAt` (DateTime, auto): Timestamp when profile was last modified

**Business Rules**:
- Only one profile per app instance (single-user constraint)
- Birth date cannot be changed to future date
- Birth date must result in valid age (0-150 years)

**Relationships**:
- One profile has many life events (1:N)

**Storage**:
- **Web**: localStorage key `lifeclock_profile`
- **Backend**: SQLite table `user_profile`

**Example**:
```json
{
  "birthDate": "1990-05-15",
  "createdAt": "2025-01-05T10:30:00Z",
  "updatedAt": "2025-01-05T10:30:00Z"
}
```

### LifeEvent

**Purpose**: Represents a significant moment in the user's life, past or future.

**Attributes**:
- `id` (UUID, required): Unique identifier for the event
  - **Generation**: Auto-generated on creation
  - **Format**: UUID v4 string
- `date` (Date, required): Date when the event occurred or will occur
  - **Validation**: Must be a valid date
  - **Format**: ISO 8601 date string
  - **Note**: Can be before birth date (family history) or in future (goals)
- `description` (String, required): Text description of the event
  - **Validation**: 1-500 characters
  - **Validation**: Not empty or whitespace only
- `isFuture` (Boolean, computed): Whether event is in the future
  - **Computation**: `date > today`
  - **Purpose**: Visual distinction on timeline (FR-017)
- `createdAt` (DateTime, auto): Timestamp when event was created
- `updatedAt` (DateTime, auto): Timestamp when event was last modified

**Business Rules**:
- Maximum 100 events per profile (soft limit for performance)
- Events must have unique IDs within the profile
- Description cannot be empty after trimming whitespace
- Events can overlap in time (multiple events on same date allowed)

**Relationships**:
- Many events belong to one profile (N:1)

**Storage**:
- **Web**: localStorage key `lifeclock_events` (array)
- **Backend**: SQLite table `life_events`

**Example**:
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "date": "2010-06-15",
  "description": "Graduated from university",
  "isFuture": false,
  "createdAt": "2025-01-05T10:35:00Z",
  "updatedAt": "2025-01-05T10:35:00Z"
}
```

### LifeSeason (Computed)

**Purpose**: Represents the user's current life stage based on age and life expectancy.

**Attributes** (all computed, not stored):
- `season` (Enum): One of ["Spring", "Summer", "Fall", "Winter"]
- `age` (Float): Current age in years (with decimal precision)
- `ageRange` (Object): Age boundaries for current season
  - `min` (Float): Minimum age for this season
  - `max` (Float): Maximum age for this season
- `progressPercent` (Float): Progress through current season (0-100)
- `lifeProgressPercent` (Float): Progress through entire life (0-100)

**Computation Logic**:
```
lifeExpectancy = 85 years
age = (today - birthDate) / 365.25 days

if age <= 21.25:
  season = "Spring"
  ageRange = [0, 21.25]
elif age <= 42.5:
  season = "Summer"
  ageRange = [21.25, 42.5]
elif age <= 63.75:
  season = "Fall"
  ageRange = [42.5, 63.75]
else:
  season = "Winter"
  ageRange = [63.75, 85]

progressPercent = ((age - ageRange.min) / (ageRange.max - ageRange.min)) * 100
lifeProgressPercent = (age / lifeExpectancy) * 100
```

**Business Rules**:
- Season is always one of the four defined values
- Users over 85 years remain in "Winter" season
- Progress percentages are capped at 100%

**Example**:
```json
{
  "season": "Summer",
  "age": 34.8,
  "ageRange": {
    "min": 21.25,
    "max": 42.5
  },
  "progressPercent": 63.8,
  "lifeProgressPercent": 40.9
}
```

## Database Schema (Backend - SQLite)

### Table: user_profile

```sql
CREATE TABLE user_profile (
  id INTEGER PRIMARY KEY CHECK (id = 1),  -- Only one row allowed
  birth_date DATE NOT NULL CHECK (birth_date < DATE('now')),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER update_profile_timestamp 
AFTER UPDATE ON user_profile
BEGIN
  UPDATE user_profile SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
```

### Table: life_events

```sql
CREATE TABLE life_events (
  id TEXT PRIMARY KEY,  -- UUID as text
  date DATE NOT NULL,
  description TEXT NOT NULL CHECK (LENGTH(TRIM(description)) > 0 AND LENGTH(description) <= 500),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_events_date ON life_events(date);

CREATE TRIGGER update_event_timestamp 
AFTER UPDATE ON life_events
BEGIN
  UPDATE life_events SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;
```

## Frontend Storage Schema (localStorage)

### Key: lifeclock_profile

```json
{
  "birthDate": "1990-05-15",
  "createdAt": "2025-01-05T10:30:00Z",
  "updatedAt": "2025-01-05T10:30:00Z"
}
```

### Key: lifeclock_events

```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "date": "2010-06-15",
    "description": "Graduated from university",
    "createdAt": "2025-01-05T10:35:00Z",
    "updatedAt": "2025-01-05T10:35:00Z"
  },
  {
    "id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
    "date": "2030-12-31",
    "description": "Retirement goal",
    "createdAt": "2025-01-05T10:40:00Z",
    "updatedAt": "2025-01-05T10:40:00Z"
  }
]
```

## Validation Rules Summary

### UserProfile Validation
- `birthDate`:
  - Required: Yes
  - Format: YYYY-MM-DD (ISO 8601)
  - Must be valid date
  - Must be before today
  - Must result in age 0-150 years

### LifeEvent Validation
- `id`:
  - Required: Yes (auto-generated)
  - Format: UUID v4
  - Must be unique
- `date`:
  - Required: Yes
  - Format: YYYY-MM-DD (ISO 8601)
  - Must be valid date
  - No restriction on past/future (allows family history and goals)
- `description`:
  - Required: Yes
  - Min length: 1 (after trim)
  - Max length: 500
  - Not empty or whitespace only

## State Transitions

### UserProfile States

```
[No Profile] 
    ↓ (user enters birth date)
[Profile Created] 
    ↓ (user updates birth date)
[Profile Updated]
```

### LifeEvent States

```
[No Event]
    ↓ (user adds event)
[Event Created]
    ↓ (user edits event)
[Event Updated]
    ↓ (user deletes event)
[Event Deleted]
```

### LifeSeason States (Automatic)

```
[Spring] (age 0-21.25)
    ↓ (time passes)
[Summer] (age 21.25-42.5)
    ↓ (time passes)
[Fall] (age 42.5-63.75)
    ↓ (time passes)
[Winter] (age 63.75+)
```

**Note**: Season transitions happen automatically based on current date and stored birth date. No user action triggers season change.

## Data Migration Strategy

### Version 1.0 (Initial)
- Single profile + array of events
- No migration needed

### Future Considerations
- If moving from localStorage to SQLite (desktop app):
  - Export localStorage data to JSON
  - Import JSON into SQLite tables
  - Validate all data during import
  - Keep localStorage as backup for one release cycle

## Performance Considerations

- **Event List**: For 100 events, array operations (filter, sort, map) perform adequately in JavaScript
- **Timeline Rendering**: Virtual scrolling if >50 events visible simultaneously
- **Season Calculation**: Pure function, no caching needed (compute on demand <1ms)
- **localStorage**: Total data size ~10-20KB for 100 events, well within 5MB browser limits

## Security & Privacy

- **No Authentication**: Single-user local app, no accounts
- **No Encryption**: Data stored in plain text locally (acceptable for personal use)
- **No Network**: All data stays on device, never transmitted
- **Data Export**: Consider adding export feature for user backup

## Testing Data Sets

### Test Profile
```json
{ "birthDate": "1990-01-01" }  // Age ~35, Summer season
```

### Test Events
```json
[
  { "date": "1989-01-01", "description": "Before birth (parents met)" },
  { "date": "2010-06-15", "description": "Past event (graduation)" },
  { "date": "2025-01-05", "description": "Today event" },
  { "date": "2030-12-31", "description": "Future event (goal)" }
]
```

### Edge Cases
- Birth date today (age 0, Spring)
- Birth date 100 years ago (age 100, Winter, exceeds expectancy)
- Event with maximum description length (500 chars)
- 100 events (performance test)
