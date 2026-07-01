# Log Terminal And Candidate Review Design

## Live log terminal

The terminal has a fixed grid width and height and can never contribute its content width to the page layout. Long lines remain intact and scroll horizontally inside the terminal; additional output scrolls vertically. The visible auto-follow button is removed. Tail following remains automatic only while the viewer is already at the bottom.

The terminal header contains three stage tabs: Qwen, InCoder, and difference detection. A tab is enabled once its log exists, remains available after the stage finishes, and displays the selected stage without changing the chart tab. A new job remounts the terminal and follows its current stage by default.

## Candidate review workbench

The three evidence-summary cards and three workbench columns share the same grid tracks so their edges align. The workbench keeps the existing candidate state and actions.

Representative source and repro draft use a file-workspace header with an icon, title, and wrapping metadata/path. Code remains read-only and scrolls inside a fixed-height editor surface. The review column is divided into header, scrollable evidence content, and a fixed action footer. Long paths and evidence text wrap without widening the page.

## Responsive behavior

Desktop uses three aligned columns. At the existing narrow breakpoint, evidence cards and workbench panels stack vertically. Neither terminal nor code content creates horizontal page overflow.

## Verification

Tests cover stage-log switching, disabled unavailable stages, log containment, candidate workbench structure, and preserved review actions. Full frontend tests, production build, and browser overflow checks are required.
