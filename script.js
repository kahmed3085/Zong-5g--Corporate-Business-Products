/* ============================================
   Zong Business — shared site behaviour
   - mobile nav toggle
   - "interest list" persisted in localStorage,
     followed across category pages via a
     floating bar, and submitted on contact.html
   ============================================ */

(function () {
  var STORAGE_KEY = "zongInterestProducts";

  /* ---------- storage helpers ---------- */
  function getSelected() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function setSelected(list) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
    } catch (e) {
      /* localStorage unavailable — degrade silently, form still works manually */
    }
  }

  function addProduct(name) {
    var list = getSelected();
    if (list.indexOf(name) === -1) list.push(name);
    setSelected(list);
    refreshAll();
  }

  function removeProduct(name) {
    var list = getSelected().filter(function (p) { return p !== name; });
    setSelected(list);
    refreshAll();
  }

  function clearAll() {
    setSelected([]);
    refreshAll();
  }

  /* ---------- mobile nav ---------- */
  function initNavToggle() {
    var toggle = document.getElementById("navToggle");
    var links = document.querySelector(".nav-links");
    if (!toggle || !links) return;
    toggle.addEventListener("click", function () {
      var isOpen = links.style.display === "flex";
      links.style.display = isOpen ? "none" : "flex";
      links.style.flexDirection = "column";
      links.style.position = "absolute";
      links.style.top = "72px";
      links.style.left = "0";
      links.style.right = "0";
      links.style.background = "#fff";
      links.style.padding = "18px 24px";
      links.style.borderBottom = "1px solid #E7E7EA";
      links.style.gap = "16px";
    });
  }

  /* ---------- add-toggle checkboxes on product cards ---------- */
  function initAddToggles() {
    var toggles = document.querySelectorAll(".add-toggle");
    var selected = getSelected();

    toggles.forEach(function (label) {
      var input = label.querySelector("input[type=checkbox]");
      if (!input) return;
      var name = input.value;

      if (selected.indexOf(name) !== -1) {
        input.checked = true;
        label.classList.add("is-added");
      }

      input.addEventListener("change", function () {
        if (input.checked) {
          label.classList.add("is-added");
          addProduct(name);
        } else {
          label.classList.remove("is-added");
          removeProduct(name);
        }
      });
    });
  }

  /* ---------- floating bar (shown on category pages) ---------- */
  function initFloatingBar() {
    var bar = document.getElementById("floatingBar");
    if (!bar) return;
    updateFloatingBar();

    var clearBtn = bar.querySelector(".fb-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", function () {
        clearAll();
      });
    }
  }

  function updateFloatingBar() {
    var bar = document.getElementById("floatingBar");
    if (!bar) return;
    var count = getSelected().length;
    var textEl = bar.querySelector(".fb-count");
    if (textEl) textEl.textContent = count;

    if (count > 0) {
      bar.classList.add("visible");
    } else {
      bar.classList.remove("visible");
    }
  }

  /* ---------- header interest pill (shown on every page) ---------- */
  function updateInterestPill() {
    var pill = document.getElementById("interestPill");
    if (!pill) return;
    var count = getSelected().length;
    var countEl = pill.querySelector(".count");
    if (countEl) countEl.textContent = count;
    pill.style.display = count > 0 ? "inline-flex" : "none";
  }

  /* ---------- contact page: render chips + inject hidden inputs ---------- */
  function initContactPage() {
    var chipList = document.getElementById("chipList");
    var emptyMsg = document.getElementById("selectedEmpty");
    var hiddenWrap = document.getElementById("hiddenProductInputs");
    var form = document.getElementById("interestForm");
    if (!chipList || !form) return;

    function render() {
      var selected = getSelected();
      chipList.innerHTML = "";
      if (hiddenWrap) hiddenWrap.innerHTML = "";

      if (selected.length === 0) {
        if (emptyMsg) emptyMsg.style.display = "block";
      } else {
        if (emptyMsg) emptyMsg.style.display = "none";
        selected.forEach(function (name) {
          var chip = document.createElement("span");
          chip.className = "chip";
          chip.innerHTML = '<span></span><button type="button" aria-label="Remove">×</button>';
          chip.querySelector("span").textContent = name;
          chip.querySelector("button").addEventListener("click", function () {
            removeProduct(name);
            render();
          });
          chipList.appendChild(chip);

          if (hiddenWrap) {
            var hidden = document.createElement("input");
            hidden.type = "hidden";
            hidden.name = "Products Interested In";
            hidden.value = name;
            hiddenWrap.appendChild(hidden);
          }
        });
      }
    }

    render();
  }

  /* ---------- refresh everything after a change ---------- */
  function refreshAll() {
    updateFloatingBar();
    updateInterestPill();
    var chipList = document.getElementById("chipList");
    if (chipList) initContactPage();
  }

  /* ---------- footer year ---------- */
  function setYear() {
    var el = document.getElementById("year");
    if (el) el.textContent = new Date().getFullYear();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNavToggle();
    initAddToggles();
    initFloatingBar();
    updateInterestPill();
    initContactPage();
    setYear();
  });
})();
