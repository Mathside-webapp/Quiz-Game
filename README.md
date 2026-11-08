# Quiz Game Library

An illustrated, responsive classroom website preview built with native HTML, CSS and modular JavaScript. No runtime dependencies, CDN scripts, credentials, or build step.

## Run

From `/workspace/Quiz-Game`:

```sh
python3 -m http.server 5173 --bind 0.0.0.0
```

Open the served site in a browser. ES modules require HTTP; do not open index.html using file://. All navigation uses hashes, so the files work on a GitHub Pages project subpath.

## Included

- Landing page, dashboard, game library with detail dialogs, quiz library, editor, sessions, results and settings.
- Search and subject filters; grade/topic metadata; preview, edit, duplicate and confirmed deletion.
- Multiple-choice editor with correct-answer selection and local draft autosave.
- Browser-local quiz storage, preferences and JSON export.
- Teacher quiz rehearsal with answer feedback and local rehearsal history.
- Five original PNG assets, separately generated, in `assets/`. See `assets/index.html` for the inspection gallery.

## Important scope

This is an interactive preview, not a production account system. Sample quizzes are illustrative. Local storage is device/origin-specific and can be lost when browser data is cleared. Use Export in Settings to keep a copy; import is not yet implemented. Do not use the preview for private student records. The Login action explains account availability; no passwords are collected.

Comic Race, Castle Siege and Tug of War are artwork previews marked Coming soon. Their rules and engines are intentionally not invented. The rehearsal is a content presentation tool only. There is no remote joining or student scoring.

Supabase auth, database schema/RLS deployment, realtime joining, cloud storage, rich media, diagrams, mathematics rendering and additional question types remain for the production phase after preview approval and backend configuration. No production data or services were connected.

## Architecture / future games

`js/registry.js` separates game metadata and compatibility from quizzes. `canLaunch` rejects missing engines and unsupported question formats. Register only reviewed developer-built modules; never load executable public uploads. A future engine must provide start, stop and results lifecycle methods; the eventual adapter should receive only authorized session content and return a validated result. The current preview does not execute engines.

`js/store.js` owns local sample data and persistence. `js/app.js` contains routes, views and interaction handling. Replace local persistence with an authenticated owner-scoped repository in the production phase; do not place privileged Supabase keys in browser code.

## Publish later

The repository root is static-host compatible. For GitHub Pages, select the intended branch and root folder in repository Settings → Pages after reviewing and committing the files. No deployment was performed in this task.

## Verification

Browser smoke test: `python3 tests/browser_smoke.py` with the server running and Playwright plus `/usr/bin/chromium` available. It uses a fresh browser profile and synthetic data. See TESTING.md for actual results.
