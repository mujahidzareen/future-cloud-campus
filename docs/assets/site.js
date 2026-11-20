"use strict";

document.documentElement.classList.add("js");

const menu = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#nav-links");
const setMenu = (open) => {
  navigation.classList.toggle("open", open);
  menu.setAttribute("aria-expanded", String(open));
  menu.setAttribute("aria-label", open ? "Close menu" : "Open menu");
};
menu.addEventListener("click", () => setMenu(menu.getAttribute("aria-expanded") !== "true"));
document.addEventListener("keydown", (event) => {
  if (event.key !== "Escape") return;
  const openMenu = navigation.querySelector(".nav-dropdown[open]");
  if (openMenu) {
    openMenu.open = false;
    openMenu.querySelector("summary").focus();
    return;
  }
  if (navigation.classList.contains("open")) {
    setMenu(false);
    menu.focus();
  }
});
document.addEventListener("pointerdown", (event) => {
  if (!navigation.contains(event.target) && !menu.contains(event.target)) setMenu(false);
});
navigation.addEventListener("focusout", (event) => {
  if (!navigation.contains(event.relatedTarget) && event.relatedTarget !== menu) setMenu(false);
});

const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
const pointerCanTilt = matchMedia("(hover: hover) and (pointer: fine)");
const motionControl = document.querySelector("[data-motion-global]");
if (motionControl) {
  motionControl.hidden = false;
  motionControl.addEventListener("click", () => {
    const paused = document.documentElement.classList.toggle("motion-paused");
    motionControl.setAttribute("aria-pressed", String(paused));
  });
}
document.querySelectorAll(".tilt, .btn, .country-btn, .region-pill, .site-motion, .menu-toggle").forEach((card) => {
  let bounds;
  const reset = () => {
    card.style.removeProperty("--tilt-x");
    card.style.removeProperty("--tilt-y");
    card.style.removeProperty("--glow-x");
    card.style.removeProperty("--glow-y");
  };
  card.addEventListener("pointerenter", () => { bounds = card.getBoundingClientRect(); });
  card.addEventListener("pointermove", (event) => {
    if (reducedMotion.matches || !pointerCanTilt.matches || !bounds || document.documentElement.classList.contains("motion-paused")) return;
    const x = Math.max(-.5, Math.min(.5, (event.clientX - bounds.left) / bounds.width - .5));
    const y = Math.max(-.5, Math.min(.5, (event.clientY - bounds.top) / bounds.height - .5));
    const angle = card.hasAttribute("data-hero") ? 12 : card.classList.contains("tilt") ? 16 : 8;
    card.style.setProperty("--tilt-x", `${-y * angle}deg`);
    card.style.setProperty("--tilt-y", `${x * angle}deg`);
    card.style.setProperty("--glow-x", `${(x + .5) * 100}%`);
    card.style.setProperty("--glow-y", `${(y + .5) * 100}%`);
  }, { passive: true });
  card.addEventListener("pointerleave", reset);
  card.addEventListener("pointercancel", reset);
  reducedMotion.addEventListener("change", reset);
  pointerCanTilt.addEventListener("change", reset);
  motionControl?.addEventListener("click", reset);
});

if ("IntersectionObserver" in window && !reducedMotion.matches) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  }, { threshold: .14 });
  document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
}

document.addEventListener("pointerdown", (event) => {
  if (reducedMotion.matches || document.documentElement.classList.contains("motion-paused")) return;
  const button = event.target.closest(".btn, .subject-card, .feature-link, .story-card, .resource-card, .country-btn, .region-pill, .site-motion, .menu-toggle");
  if (!button || button.disabled || button.querySelector(".pulse")) return;
  const pulse = document.createElement("span");
  pulse.className = "pulse";
  pulse.addEventListener("animationend", () => pulse.remove(), { once: true });
  button.append(pulse);
  window.setTimeout(() => pulse.remove(), 550);
});

document.querySelectorAll(".country-picker").forEach((picker) => {
  const buttons = picker.querySelectorAll("[data-country]");
  const panels = picker.querySelectorAll("[data-panel]");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
      panels.forEach((panel) => { panel.hidden = panel.dataset.panel !== button.dataset.country; });
    });
  });
});

// Native disclosure menus also support touch and keyboard input.
const dropdowns = document.querySelectorAll(".nav-dropdown");
dropdowns.forEach((dropdown) => {
  dropdown.addEventListener("toggle", () => {
    if (!dropdown.open) return;
    dropdowns.forEach((other) => { if (other !== dropdown) other.open = false; });
  });
});
document.addEventListener("pointerdown", (event) => {
  dropdowns.forEach((dropdown) => {
    if (!dropdown.contains(event.target)) dropdown.open = false;
  });
});

const market = document.querySelector("[data-pricing-country]");
if (market) {
  market.addEventListener("change", () => {
    document.querySelectorAll("[data-plan-link]").forEach((link) => {
      const destination = new URL(link.href);
      if (market.value) destination.searchParams.set("country", market.value);
      else destination.searchParams.delete("country");
      link.href = destination.href;
    });
  });
}

const planner = document.querySelector("#package-planner");
if (planner) {
  const summary = document.querySelector("#package-summary");
  const link = document.querySelector("#package-link");
  const feedback = document.querySelector("#package-feedback");
  const updatePackage = () => {
    const selected = [...planner.querySelectorAll('input[name="subjects"]:checked')];
    const goal = planner.elements.goal.value.trim();
    const timetable = planner.elements.schedule.value.trim();
    const stage = planner.elements.stage.value;
    const frequency = planner.elements.frequency.value;
    summary.replaceChildren();
    const values = [
      ["Subjects", selected.map((input) => input.value).join(", ") || "To discuss"],
      ["School stage", stage || "To discuss"],
      ["Lesson rhythm", frequency],
      ["Main goal", goal || "To discuss"],
      ["Availability", timetable || "To discuss"]
    ];
    values.forEach(([label, value]) => {
      const term = document.createElement("dt");
      const description = document.createElement("dd");
      term.textContent = label;
      description.textContent = value;
      summary.append(term, description);
    });
    const destination = new URL(link.href);
    destination.search = "";
    destination.searchParams.set("plan", "Custom package");
    const incomingCountry = new URLSearchParams(location.search).get("country");
    if (["uk","usa","canada","uae","saudi-arabia","qatar","oman","other-countries"].includes(incomingCountry)) destination.searchParams.set("country", incomingCountry);
    destination.searchParams.set("goal", [
      selected.length ? "Subjects: " + selected.map((input) => input.value).join(", ") : "",
      goal,
      "Lesson rhythm: " + frequency
    ].filter(Boolean).join(". ").slice(0, 400));
    if (selected.length === 1) destination.searchParams.set("course", selected[0].dataset.course);
    if (stage) destination.searchParams.set("level", stage);
    if (timetable) destination.searchParams.set("time", timetable);
    link.href = destination.href;
  };
  planner.addEventListener("change", updatePackage);
  planner.addEventListener("input", updatePackage);
  planner.addEventListener("submit", (event) => {
    event.preventDefault();
    updatePackage();
    feedback.textContent = "Your selections are ready to review in the demo enquiry.";
    link.focus();
  });
  updatePackage();
}
