// JavaScript functionality can be added as needed.

// Example: Display search results when the "Buscar" button is clicked.
/*
document.querySelector(".search button").addEventListener("click", function () {
  const input = document.querySelector(".search input").value;
  // Perform a search and display results here.
  alert("Searching for: " + input);
});*/

document.addEventListener("DOMContentLoaded", function () {
  const cookieBanner = document.querySelector(".cookie-banner");
  const acceptButton = document.querySelector(".cookie-banner button");

  // Función para ocultar el banner de cookies
  function hideCookieBanner() {
    cookieBanner.style.display = "none";
  }

  // Agregar un controlador de eventos al botón "Aceptar"
  acceptButton.addEventListener("click", hideCookieBanner);
});
// You can add more JavaScript for interactive features.
