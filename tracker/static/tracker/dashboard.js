document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.querySelector("[data-js='search-input']");
  const statusSelect = document.querySelector("[data-js='status-filter']");
  const rows = Array.from(document.querySelectorAll("[data-js='applications-table'] tbody tr"));

  if (!searchInput || !statusSelect || !rows.length) {
    return;
  }

  function normalise(text) {
    return text.toLowerCase().trim();
  }

  function applyFilters() {
    const query = normalise(searchInput.value || "");
    const status = statusSelect.value;

    rows.forEach((row) => {
      const company = normalise(row.getAttribute("data-company") || "");
      const position = normalise(row.getAttribute("data-position") || "");
      const rowStatus = row.getAttribute("data-status") || "";

      const matchesQuery =
        !query ||
        company.includes(query) ||
        position.includes(query);

      const matchesStatus = !status || rowStatus === status;

      row.style.display = matchesQuery && matchesStatus ? "" : "none";
    });
  }

  searchInput.addEventListener("input", applyFilters);
  statusSelect.addEventListener("change", applyFilters);
});