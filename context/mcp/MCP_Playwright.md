### Playwright

**Purpose**: Browser automation and E2E testing with real browser interaction

#### Triggers

- Browser testing and E2E test scenarios
- Visual testing, screenshot, or UI validation requests
- Form submission and user interaction testing
- Cross-browser compatibility validation
- Performance testing requiring real browser rendering
- Accessibility testing with automated WCAG compliance

#### Choose When

- **For real browser interaction**: When you need actual rendering, not just code
- **Over unit tests**: For integration testing, user journeys, visual validation
- **For E2E scenarios**: Login flows, form submissions, multi-page workflows
- **For visual testing**: Screenshot comparisons, responsive design validation
- **Not for code analysis**: Static code review, syntax checking, logic validation

#### Works Best With

- **Sequential**: Sequential plans test strategy → Playwright executes browser automation
- **Magic**: Magic creates UI components → Playwright validates accessibility and behavior

#### How to Use

You may encounter a situation where the development port (e.g. 3000) is already in use because the user has manually
started the development server.

##### ❌ DO NOT:

- Attempt to kill the existing process
- Try to start a new server on a different port
- Stop or restart the development server

##### ✅ DO:

- Proceed directly with Playwright testing
- Navigate to `http://localhost:3000` (or whatever port the development server is running on) without starting any
  server

##### Rationale

The user may have intentionally started the development server themselves for debugging or monitoring purposes.
Attempting to manage the server lifecycle can interfere with their workflow.

#### Examples

```
"test the login flow" → Playwright (browser automation)
"check if form validation works" → Playwright (real user interaction)
"take screenshots of responsive design" → Playwright (visual testing)
"validate accessibility compliance" → Playwright (automated WCAG testing)
"review this function's logic" → Native Claude (static analysis)
"explain the authentication code" → Native Claude (code review)
```
