# Easy Habits

Easy Habits is a deliberately constrained habit-tracking system designed to emphasize focus, accountability, and clean system design.

This project was built as a backend-focused demonstration of authenticated users, time-scoped state, and read-only data sharing, rather than as a feature-heavy product.

---

## Core Concept

Many habit trackers encourage users to track dozens of behaviors at once.  Easy Habits intentionally limits scope to encourage focus. Users create a small number of habits, complete them within clearly defined time periods, and optionally share read-only progress with trusted users for accountability without the infinite scrolling, likes, or gamification.

Easy Habits tracks simply with one-click checkbox completion. The more you practice a habit the merrier, but the goal of Easy Habits is to get over that entry point every day or week. Consistency beats impulse. The same applies to streaks other habit tracking apps might promote. Consistency should be celebrated, but missing one day or one week should not mean you've failed your habit.

---

## Features

### Authentication
- Email + password login
- Secure password hashing
- JWT-based authentication
- Protected API routes

### Habit Tracking
- Daily or weekly habits
- Checkbox-based completion
- Time-scoped completion tracking
- Persistent history

### Read-Only Sharing
- Invite-code-based connections
- Users can share specific habits
- Shared users can view but cannot modify
- All authorization enforced server-side

---

## Design Constraints

This project intentionally avoids:

- OAuth providers
- Public profiles
- Social feeds
- Likes or comments
- Streak gamification
- Complex analytics
- Multiple completion counters per period

The goal is to demonstrate clean modeling, authorization boundaries, and time-based state management without unnecessary product complexity.

---

## Technical Stack

Backend:
- Python
- PostgreSQL
- JWT authentication

Deployment:
- Deployed on [VPS / Cloud platform]
- Environment-based configuration
- Persistent database

---

## Architecture Overview

The system is structured around three core models:

### User
Represents an authenticated account.

### Habit
Represents a user-owned habit with:
- Name
- Cadence (daily or weekly)
- Owner reference

### Completion
Represents a habit’s completion within a specific time period:
- Habit reference
- User reference
- Period start timestamp

Completion records are uniquely constrained per habit per period to enforce single completion.

Sharing is modeled via an explicit relationship table that grants read-only access to selected users.

---

## Authorization Model

- Users may only modify habits they own.
- Shared users may view but never mutate shared habits.
- All access checks are enforced in backend middleware and route handlers.

---

## Period Handling

- Daily habits reset at midnight (UTC or configured timezone).
- Weekly habits reset at the start of the week (Monday).
- Completion is computed based on the period start timestamp.
- The system ensures idempotent completion per period.

---

## Running Locally

1. Clone repository
2. Create `.env` file with required variables
3. Install dependencies
4. Run database migrations
5. Start development server

---

## Deployment

The `main` branch represents the stable, deployed version.

Deployment is performed from `main` to ensure production stability.

---

## Project Goals

This project was built to demonstrate:

- Authenticated multi-user systems
- Relational data modeling
- Time-scoped state management
- Server-side authorization enforcement
- Structured Git workflow
- Production deployment

It is intentionally constrained to emphasize clarity and correctness over feature volume.
