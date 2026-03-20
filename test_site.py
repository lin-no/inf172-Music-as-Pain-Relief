"""
Playwright tests for INF172 Music as Pain Relief website.
Run with: python test_site.py
"""
import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

# Build file:// URL for the HTML file
HTML_PATH = Path(__file__).parent / "index.html"
BASE_URL = HTML_PATH.as_uri()

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

results: list[tuple[str, bool, str | None]] = []

def check(name, fn):
    try:
        fn()
        print(f"  {PASS} {name}")
        results.append((name, True, None))
    except Exception as e:
        print(f"  {FAIL} {name}: {e}")
        results.append((name, False, str(e)))


def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")

        print("\n=== Page Basics ===")
        check("Title contains 'Music as Pain Relief'",
              lambda: assert_contains(page.title(), "Music as Pain Relief"))

        check("Meta description present",
              lambda: assert_truthy(
                  page.locator('meta[name="description"]').count() > 0))

        check("Hero headline visible",
              lambda: page.locator("h1.hero-headline").wait_for(state="visible"))

        check("'Pain Relief' accent text present",
              lambda: assert_contains(
                  page.locator(".hero-headline-accent").text_content(), "Pain Relief"))

        check("Hero subtitle text present",
              lambda: assert_contains(
                  page.locator(".hero-subtitle").text_content(),
                  "Can listening to music"))

        print("\n=== Navigation ===")
        check("Nav logo 'Team 2' visible",
              lambda: assert_contains(
                  page.locator(".nav-logo").text_content(), "Team 2"))

        expected_links = ["Background", "Question", "Procedure",
                          "Results", "Implications", "Limitations", "Team"]
        for link_text in expected_links:
            check(f"Nav link '{link_text}' exists",
                  lambda t=link_text: assert_truthy(
                      page.locator(f".nav-links a:text('{t}')").count() > 0))

        check("Nav CTA 'GitHub' link present",
              lambda: assert_truthy(
                  page.locator(".nav-links .nav-cta").count() > 0))

        print("\n=== Hero Stats ===")
        check("Stat '73.3%' displayed",
              lambda: assert_contains(
                  page.locator(".hero-stat-strip").text_content(), "73.3"))

        check("Stat '60%' displayed",
              lambda: assert_contains(
                  page.locator(".hero-stat-strip").text_content(), "60"))

        check("Stat '15 participants' described",
              lambda: assert_contains(
                  page.locator(".hero-stat-strip").text_content(), "15"))

        print("\n=== CTA Buttons ===")
        check("'See Results' button present and links to #results",
              lambda: assert_attr(
                  page.locator("a.hero-btn-primary"), "href", "#results"))

        check("'View Study Design' button present and links to #procedure",
              lambda: assert_attr(
                  page.locator("a.hero-btn-ghost").first, "href", "#procedure"))

        print("\n=== Sections Present ===")
        section_ids = ["background", "question", "procedure",
                       "results", "implications", "limitations", "team"]
        for sid in section_ids:
            check(f"Section #{sid} exists",
                  lambda s=sid: assert_truthy(
                      page.locator(f"#{s}").count() > 0))

        print("\n=== Content Accuracy ===")
        check("Background section has 4 cards",
              lambda: assert_eq(
                  page.locator("#background .card").count(), 4))

        check("Research question Q1 text present",
              lambda: assert_contains(
                  page.locator(".question-cards").text_content(),
                  "self-reported pain intensity"))

        check("Research question Q2 text present",
              lambda: assert_contains(
                  page.locator(".question-cards").text_content(),
                  "pain tolerance time"))

        check("Procedure has 4 timeline steps",
              lambda: assert_eq(
                  page.locator(".timeline-item").count(), 4))

        check("Procedure overview shows 15 participants",
              lambda: assert_contains(
                  page.locator(".procedure-overview").text_content(), "15"))

        check("Results: 73.3% stat card present",
              lambda: assert_contains(
                  page.locator(".stat-cards").text_content(), "73.3"))

        check("Results: 60% stat card present",
              lambda: assert_contains(
                  page.locator(".stat-cards").text_content(), "60"))

        check("Bar chart: 'Tolerability Comparison' chart present",
              lambda: assert_contains(
                  page.locator(".chart-section").text_content(),
                  "Tolerability Comparison"))

        check("Bar chart: 'Effectiveness Ratings' chart present",
              lambda: assert_contains(
                  page.locator(".chart-section").text_content(),
                  "Effectiveness Ratings"))

        check("Bar fills have correct data-value attributes",
              lambda: assert_truthy(
                  page.locator('.bar-fill[data-value="73.3%"]').count() > 0))

        check("Implications section has 4 cards",
              lambda: assert_eq(
                  page.locator("#implications .card").count(), 4))

        check("Limitations list has 4 items",
              lambda: assert_truthy(
                  page.locator("#limitations .col-card").first
                  .locator("li").count() >= 4))

        check("Future Directions list has 4 items",
              lambda: assert_truthy(
                  page.locator("#limitations .col-card").last
                  .locator("li").count() >= 4))

        print("\n=== Team Section ===")
        team_members = ["Linn Oo", "Samara Jimmy", "Elias Barakzoy", "Lynh Mai"]
        for member in team_members:
            check(f"Team member '{member}' displayed",
                  lambda m=member: assert_contains(
                      page.locator("#team").text_content(), m))

        check("Team roles visible (CTO, Research Lead, etc.)",
              lambda: assert_contains(
                  page.locator("#team").text_content(), "CTO"))

        print("\n=== Footer ===")
        check("Footer copyright text present",
              lambda: assert_contains(
                  page.locator("footer").text_content(), "2026"))

        check("Footer GitHub link present",
              lambda: assert_truthy(
                  page.locator("footer a[href='https://github.com']").count() > 0))

        check("Footer quick links present",
              lambda: assert_contains(
                  page.locator("footer").text_content(), "Quick Links"))

        print("\n=== Mobile Nav Toggle ===")
        mobile_page = browser.new_page(viewport={"width": 390, "height": 844})
        mobile_page.goto(BASE_URL)
        mobile_page.wait_for_load_state("networkidle")

        check("Mobile toggle button present",
              lambda: assert_truthy(
                  mobile_page.locator("#navToggle").count() > 0))

        check("Toggle aria-expanded starts as 'false'",
              lambda: assert_attr(
                  mobile_page.locator("#navToggle"),
                  "aria-expanded", "false"))

        check("Toggle click opens nav (aria-expanded becomes 'true')",
              lambda: test_mobile_toggle(mobile_page))

        mobile_page.close()

        print("\n=== Accessibility ===")
        check("Nav has aria-label",
              lambda: assert_truthy(
                  page.locator("nav[aria-label]").count() > 0))

        check("Hero image has alt text",
              lambda: assert_truthy(
                  len(page.locator(".hero-image").get_attribute("alt") or "") > 0))

        check("Bar charts have role='img' and aria-label",
              lambda: assert_truthy(
                  page.locator(".bar-chart[role='img'][aria-label]").count() >= 2))

        check("Page lang attribute is 'en'",
              lambda: assert_eq(
                  page.locator("html").get_attribute("lang"), "en"))

        print("\n=== Scroll & Interaction ===")
        check("'See Results' CTA scrolls to results section",
              lambda: test_cta_scroll(browser, BASE_URL))

        browser.close()

    # Summary
    passed = sum(1 for _, ok, _ in results if ok)
    failed = sum(1 for _, ok, _ in results if not ok)
    total = len(results)
    print(f"\n{'='*45}")
    print(f"Results: {passed}/{total} passed", end="")
    if failed:
        print(f"  ({failed} failed)")
        print("\nFailed tests:")
        for name, ok, err in results:
            if not ok:
                print(f"  {FAIL} {name}")
                print(f"       {err}")
    else:
        print()
    print('='*45)
    return failed == 0


# ── Helpers ────────────────────────────────────────────────

def assert_contains(text, substr):
    assert substr in (text or ""), f"Expected to find {substr!r} in {text!r}"

def assert_truthy(val):
    assert val, f"Expected truthy, got {val!r}"

def assert_eq(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"

def assert_attr(locator, attr, expected):
    actual = locator.get_attribute(attr)
    assert actual == expected, f"Expected attr {attr}={expected!r}, got {actual!r}"

def test_mobile_toggle(page):
    toggle = page.locator("#navToggle")
    toggle.click()
    page.wait_for_timeout(300)
    val = toggle.get_attribute("aria-expanded")
    assert val == "true", f"Expected aria-expanded='true' after click, got {val!r}"

def test_cta_scroll(browser, url):
    p = browser.new_page(viewport={"width": 1280, "height": 800})
    p.goto(url)
    p.wait_for_load_state("networkidle")
    p.locator("a.hero-btn-primary").click()
    p.wait_for_timeout(800)
    results_section = p.locator("#results")
    box = results_section.bounding_box()
    scroll_y = p.evaluate("window.scrollY")
    p.close()
    assert scroll_y > 100, f"Page didn't scroll — scrollY={scroll_y}"


if __name__ == "__main__":
    ok = run_tests()
    sys.exit(0 if ok else 1)
