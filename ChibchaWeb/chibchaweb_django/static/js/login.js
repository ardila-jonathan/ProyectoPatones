const citiesByCountry = {
  USA: [
    "Nueva York",
    "Los Ángeles",
    "Chicago",
    "Miami",
    "San Francisco",
    "Las Vegas",
    "Houston",
  ],
  Canada: [
    "Toronto",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Ottawa",
    "Edmonton",
    "Winnipeg",
  ],
  Mexico: [
    "Ciudad de México",
    "Guadalajara",
    "Monterrey",
    "Cancún",
    "Tijuana",
    "Puebla",
    "Mérida",
  ],
  Argentina: [
    "Buenos Aires",
    "Córdoba",
    "Rosario",
    "Mendoza",
    "La Plata",
    "Mar del Plata",
    "Salta",
  ],
  Bolivia: [
    "La Paz",
    "Santa Cruz de la Sierra",
    "Cochabamba",
    "Sucre",
    "Tarija",
    "Potosí",
    "Oruro",
  ],
  Brasil: [
    "Sao Paulo",
    "Río de Janeiro",
    "Belo Horizonte",
    "Salvador",
    "Recife",
    "Brasilia",
    "Curitiba",
  ],
  Canada: [
    "Toronto",
    "Vancouver",
    "Montreal",
    "Calgary",
    "Ottawa",
    "Edmonton",
    "Winnipeg",
  ],
  Chile: [
    "Santiago",
    "Valparaíso",
    "Concepción",
    "Viña del Mar",
    "La Serena",
    "Antofagasta",
    "Temuco",
  ],
  Colombia: [
    "Bogotá",
    "Medellín",
    "Cali",
    "Barranquilla",
    "Cartagena",
    "Cúcuta",
    "Pereira",
  ],
  Costa_Rica: [
    "San José",
    "Limon",
    "Heredia",
    "Alajuela",
    "Cartago",
    "Puntarenas",
    "Guanacaste",
  ],
  Cuba: [
    "La Habana",
    "Santiago de Cuba",
    "Camagüey",
    "Holguín",
    "Santa Clara",
    "Guantánamo",
    "Cienfuegos",
  ],
  Ecuador: [
    "Quito",
    "Guayaquil",
    "Cuenca",
    "Santo Domingo",
    "Manta",
    "Loja",
    "Ambato",
  ],
  El_Salvador: [
    "San Salvador",
    "Santa Ana",
    "Soyapango",
    "San Miguel",
    "Mejicanos",
    "Santa Tecla",
    "Apopa",
  ],
  Estados_Unidos: [
    "Nueva York",
    "Los Ángeles",
    "Chicago",
    "Miami",
    "San Francisco",
    "Las Vegas",
    "Houston",
  ],
  Guatemala: [
    "Ciudad de Guatemala",
    "Quetzaltenango",
    "Escuintla",
    "San Juan Sacatepéquez",
    "Villa Nueva",
    "Mixco",
    "Petapa",
  ],
  Honduras: [
    "Tegucigalpa",
    "San Pedro Sula",
    "La Ceiba",
    "Choloma",
    "Villanueva",
    "La Lima",
    "El Progreso",
  ],
  México: [
    "Ciudad de México",
    "Guadalajara",
    "Monterrey",
    "Cancún",
    "Tijuana",
    "Puebla",
    "Mérida",
  ],
  Nicaragua: [
    "Managua",
    "León",
    "Granada",
    "Masaya",
    "Chinandega",
    "Juigalpa",
    "Estelí",
  ],
  Panamá: [
    "Ciudad de Panamá",
    "San Miguelito",
    "La Chorrera",
    "David",
    "Arraiján",
    "Colón",
    "Santiago",
  ],
  Paraguay: [
    "Asunción",
    "Ciudad del Este",
    "San Lorenzo",
    "Capiatá",
    "Lambaré",
    "Fernando de la Mora",
    "Luque",
  ],
  Perú: [
    "Lima",
    "Arequipa",
    "Trujillo",
    "Chiclayo",
    "Iquitos",
    "Huancayo",
    "Piura",
  ],
  Uruguay: [
    "Montevideo",
    "Salto",
    "Paysandú",
    "Las Piedras",
    "Rivera",
    "Maldonado",
    "Tacuarembó",
  ],
  Venezuela: [
    "Caracas",
    "Maracaibo",
    "Valencia",
    "Barquisimeto",
    "Maracay",
    "Ciudad Guayana",
    "Barcelona",
  ],
};

function checkPasswordsMatch() {
  let password = document.getElementById('password').value;
  let confirmPassword = document.getElementById('confirmPassword').value;
  let message = document.getElementById('message');

  if (password === confirmPassword && (password !== '' || confirmPassword !== '')) {
  message.innerHTML = 'Las contraseñas coinciden';
  message.style.color = 'green';
  } else if (password === '' && confirmPassword === '') {
  message.innerHTML = '';
  } else {
  message.innerHTML = 'Las contraseñas no coinciden';
  message.style.color = 'red';
  }
}

function updateCitySelect() {
  const countrySelect = document.getElementById("countrySelect");
  const citySelect = document.getElementById("citySelect");
  const selectedCountry = countrySelect.value;
  const cities = citiesByCountry[selectedCountry];

  // Limpiar el select de ciudades
  citySelect.innerHTML =
    "<option value='0'>Selecciona un país primero</option>";

  if (cities) {
    // Agregar las ciudades al select
    for (let i = 0; i < cities.length; i++) {
      const city = cities[i];
      const option = document.createElement("option");
      option.value = city;
      option.text = city;
      citySelect.appendChild(option);
    }
  }
}
