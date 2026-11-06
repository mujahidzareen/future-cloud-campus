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
  if (event.key === "Escape" && navigation.classList.contains("open")) {
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
const motionControl = document.querySelector("[data-motion]");
if (motionControl) {
  const hero = motionControl.closest("[data-hero]");
  motionControl.hidden = false;
  motionControl.addEventListener("click", () => {
    const paused = hero.classList.toggle("paused");
    motionControl.setAttribute("aria-pressed", String(paused));
  });
}
document.querySelectorAll(".tilt").forEach((card) => {
  let bounds;
  const reset = () => {
    card.style.removeProperty("--tilt-x");
    card.style.removeProperty("--tilt-y");
  };
  card.addEventListener("pointerenter", () => { bounds = card.getBoundingClientRect(); });
  card.addEventListener("pointermove", (event) => {
    if (reducedMotion.matches || !pointerCanTilt.matches || !bounds) return;
    const x = Math.max(-.5, Math.min(.5, (event.clientX - bounds.left) / bounds.width - .5));
    const y = Math.max(-.5, Math.min(.5, (event.clientY - bounds.top) / bounds.height - .5));
    const angle = card.hasAttribute("data-hero") ? 8 : 12;
    card.style.setProperty("--tilt-x", `${-y * angle}deg`);
    card.style.setProperty("--tilt-y", `${x * angle}deg`);
  }, { passive: true });
  card.addEventListener("pointerleave", reset);
  card.addEventListener("pointercancel", reset);
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
  if (reducedMotion.matches) return;
  const button = event.target.closest(".btn.primary");
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

const form = document.querySelector("#demo-form");
if (form) {
  const query = new URLSearchParams(location.search);
  const { country, timezone, code, course, phone } = form.elements;
  const defaultTimezones = {
    uk: "Europe/London", ireland: "Europe/Dublin", pakistan: "Asia/Karachi", "new-zealand": "Pacific/Auckland"
  };
  const syncCountry = () => {
    const selection = country.selectedOptions[0];
    code.value = selection?.dataset.code || (country.value === "other" ? "other" : "");
    timezone.value = defaultTimezones[country.value] || "";
  };
  for (const field of [course, country]) {
    const initial = query.get(field.name);
    if (initial && [...field.options].some((option) => option.value === initial)) field.value = initial;
  }
  syncCountry();
  country.addEventListener("change", syncCountry);
  phone.addEventListener("input", () => phone.setCustomValidity(""));
  const confirmation = document.querySelector("#confirmation");
  const summary = document.querySelector("#request-summary");
  const submit = form.querySelector('button[type="submit"]');
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const digits = phone.value.replace(/[^0-9]/g, "");
    if (digits.length < 7 || digits.length > 15) {
      phone.setCustomValidity("Enter a phone number with 7 to 15 digits.");
      phone.reportValidity();
      return;
    }
    const fields = [
      ["Country", country.selectedOptions[0].textContent],
      ["Time zone", timezone.selectedOptions[0].textContent],
      ["Subject", course.selectedOptions[0].textContent],
      ["Age, year or grade", form.elements.level.value.trim()],
      ["Preferred time", form.elements.time.value.trim() || "To discuss"],
      ["Learning goal", form.elements.goal.value.trim() || "To discuss"]
    ];
    summary.replaceChildren();
    for (const [label, value] of fields) {
      const term = document.createElement("dt");
      const description = document.createElement("dd");
      term.textContent = label;
      description.textContent = value;
      summary.append(term, description);
    }
    form.hidden = true;
    confirmation.hidden = false;
    confirmation.focus();
  });
  confirmation.querySelector("[data-edit]").addEventListener("click", () => {
    confirmation.hidden = true;
    summary.replaceChildren();
    form.hidden = false;
    submit.focus();
  });
  submit.disabled = false;
}
