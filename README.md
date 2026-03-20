# Music as Pain Relief — INF172 Research Project

A public-facing research website for the IN4MTX 172 (Track 3: Music & Health) student project. The site presents a controlled experimental study investigating whether listening to music during a cold pressor discomfort task reduces perceived pain intensity and increases pain tolerance compared to a silent control condition.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Research Background](#research-background)
- [Study Design](#study-design)
- [Key Findings](#key-findings)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Team](#team)
- [References](#references)

---

## Project Overview

This website is the primary deliverable for the IN4MTX 172 group project. It communicates the study's motivation, methodology, quantitative results, and conclusions to a general audience. The site is a fully static build — no server, no build step, no framework — consisting of a single HTML file, one CSS stylesheet, and one JavaScript file.

The study examined two research questions:

1. Does music reduce self-reported pain intensity during a cold pressor discomfort task?
2. Does music increase pain tolerance time during a cold pressor discomfort task?

---

## Research Background

Pain is one of the most common reasons people seek medical care. Traditional pharmacological treatments such as analgesics and opioids carry risks including dependency, tolerance, and financial barriers. Non-pharmacological alternatives are therefore a clinical priority.

Music is inexpensive, widely accessible, and non-invasive. Prior research suggests it can influence emotional regulation, reduce anxiety, and redirect attention away from painful stimuli — all mechanisms relevant to pain perception. This project adds a small, controlled data point to that literature using a standardized cold pressor method that could be replicated by other student research teams.

The project began as a study of music's effects on emotional states (stress and mood) but evolved, following a literature review on music-induced analgesia, into a focus on physical discomfort and pain tolerance.

---

## Study Design

**Method:** Cold pressor test — non-dominant hand submerged in ice water for up to 60 seconds

**Design:** Within-subjects — each participant completed the task under both conditions

**Conditions:**
- Music condition: participant listened to music during the task
- Control condition: participant completed the task in silence or with neutral audio

**Participants:** 15, recruited from the team's personal networks

**Data collected:**
- Self-reported pain intensity at 30 seconds and 60 seconds (scale of 1 to 10)
- Total time hand remained submerged (pain tolerance)

**Implementation stages:**
1. Pre-experiment survey collecting demographics, music preferences, stress levels, and expectations about music as a pain management tool
2. Cold pressor experiment run under both conditions for each participant
3. Post-collection analysis comparing pain perception and tolerance between conditions

---

## Key Findings

| Metric | Result |
|---|---|
| Participants who found music more tolerable | 73.3% |
| Participants who rated effectiveness at 4 or 5 out of 5 | 60% |
| Participants who rated audio distraction level at 4 out of 5 | 53.3% (8 of 15) |

Participants frequently reported that music helped distract them from the sensation of cold and discomfort. The results suggest that music may function as an effective cognitive distraction during painful experiences, though the sample size limits generalizability.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Markup | HTML5 |
| Styling | CSS3 (custom properties, Grid, Flexbox) |
| Scripting | Vanilla JavaScript (ES6+) |
| Fonts | Google Fonts — Inter, Playfair Display |

No build tools, bundlers, or frameworks are used.

---

## Project Structure

```
inf172 website/
├── index.html          # Single-page markup — all sections in one document
├── style.css           # Full stylesheet with CSS custom properties
├── script.js           # Navigation, scroll reveal, bar chart animations
├── inf172.ico          # Site favicon
├── test_site.py        # Playwright end-to-end test suite
└── images/
    ├── hero-fusion.png     # Hero section image
    └── team/
        ├── Linn.jpg
        ├── Samara.jpg
        ├── Lynh.jpg
        └── Elias.jpg
```

### index.html

Contains all page sections as a single scrolling document:

| Section ID | Content |
|---|---|
| `#hero` | Headline, stat strip, CTA buttons, hero image card |
| `#background` | Four-card grid covering research context and motivation |
| `#question` | Two research questions and project vision statement |
| `#procedure` | Four-step timeline of the experiment |
| `#results` | Stat cards, animated bar charts, takeaway summary |
| `#implications` | Four-card grid interpreting the findings |
| `#limitations` | Two-column grid of limitations and future directions |
| `#team` | Team member cards with photos and roles |
| `#references` | APA-formatted reference list in the footer |

### script.js

Provides the following runtime behaviors:

1. **Mobile nav toggle** — opens and closes the hamburger menu, manages `aria-expanded`, and focuses the first nav link on open (WCAG 2.4.3)
2. **Navbar auto-hide** — hides the fixed navbar when scrolling down past 150px, reveals it when scrolling up
3. **Active nav highlighting** — applies an `.active` class to the nav anchor matching the current scroll position
4. **Scroll reveal** — `IntersectionObserver` fades in `.reveal` elements as they enter the viewport
5. **Bar chart animation** — triggers CSS width transitions on `.bar-fill` elements when they scroll into view
6. **Smooth scroll fallback** — handles `href="#anchor"` clicks with `scrollIntoView` for broader browser support

---

## Limitations

1. **Small sample size** — 15 participants limits statistical power and the generalizability of results to broader populations.
2. **Music selection not evidence-based** — the track used was not chosen from a validated stimulus database, which may affect the consistency and reliability of results across participants.
3. **Non-standardized pain scale** — the 1–10 self-report scale was not derived from a clinically validated instrument such as the Visual Analogue Scale or the McGill Pain Questionnaire.
4. **Simulated discomfort** — cold pressor results may not translate directly to real clinical or chronic pain contexts.
5. **Environmental confounds** — individual differences in prior cold exposure history, baseline stress levels, and pain tolerance threshold were not controlled or accounted for.
6. **No music preference control** — participants did not self-select music, which may have reduced or amplified the analgesic effect depending on personal preference and genre familiarity.

---

## Future Work

1. **Standardized stimulus selection** — use a validated music database to isolate tempo and rhythmic structure as independent variables across conditions
2. **Larger and more diverse sample** — expand beyond 15 participants with particular attention to demographics including those with chronic pain conditions
3. **Validated measurement tools** — adopt the Visual Analogue Scale, Numeric Rating Scale, or McGill Pain Questionnaire to improve data accuracy and comparability with published literature
4. **Genre and preference comparison** — test whether specific genres, tempo ranges, or listener-selected music produce meaningfully different outcomes
5. **Physiological measures** — add heart rate, skin conductance, or cortisol data to complement self-reported pain ratings
6. **Clinical settings** — replicate the study in post-operative or emergency care environments to assess real-world applicability

---

## Team

| Name | Role | Contribution |
|---|---|---|
| Samara Jimmy | Research Lead | Study design, participant recruitment, data collection, and analysis |
| Lynh Mai | UI/UX Lead | Visual design, layout decisions, and presentation |
| Linn Oo | Technology Lead | Website development and technical implementation |
| Elias Barakzoy | Business Lead | Project coordination, deliverables management, and documentation |

---

## References

Garza-Villarreal, E. A., Pando, V., Vuust, P., & Parsons, C. (2017). Music-induced analgesia in chronic pain conditions: A systematic review and meta-analysis. *Pain Physician, 20*(7), 597–610.

Getie, A., Bimerew, M., & Kitaw, T. A. (2026). The effect of music therapy on pain management: A systematic review and meta-analysis of randomized controlled trials. *Discover Psychology*. https://doi.org/10.1007/s44202-026-00600-2

Goldfine, C. E., Wilson, J. M., Kaithamattam, J., Hasdianda, M. A., Mancey, K., Rehding, A., Schreiber, K. L., Chai, P. R., & Weiner, S. G. (2025). Randomized trial of self-selected music intervention on pain and anxiety in emergency department patients with musculoskeletal back pain. *Western Journal of Emergency Medicine, 26*(4), 1112–1119. https://doi.org/10.5811/westjem.34871

Hunter, A. R., Heiderscheit, A., Galbally, M., Gravina, D., Mutwalli, H., & Himmerich, H. (2023). The effects of music-based interventions for pain and anxiety management during vaginal labour and caesarean delivery: A systematic review and narrative synthesis of randomized controlled trials. *International Journal of Environmental Research and Public Health, 20*(23), 7120. https://doi.org/10.3390/ijerph20237120
