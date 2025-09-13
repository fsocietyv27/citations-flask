async function fetchQuote() {
  const box = document.getElementById("quote-box");
  box.style.opacity = 0; // fade-out

  const res = await fetch("/quote");
  const data = await res.json();

  setTimeout(() => {
    document.getElementById("citation").textContent = data.citation;
    box.style.opacity = 1; // fade-in
  }, 400);
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("btn").addEventListener("click", fetchQuote);
});