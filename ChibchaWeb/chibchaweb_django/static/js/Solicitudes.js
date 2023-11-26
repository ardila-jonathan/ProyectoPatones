
function copyXml() {
  const xmlContent = document.getElementById('xmlContent');
  xmlContent.select();
  document.execCommand('copy');
  alert('XML copiado al portapapeles');
}

function downloadXml() {
  const xmlContent = document.getElementById('xmlContent').value.trim(); // Obtener el contenido del textarea
  const element = document.createElement('a');
  const file = new Blob([xmlContent], { type: 'text/xml' }); // Crear un Blob con el contenido XML
  element.href = URL.createObjectURL(file);
  element.setAttribute('download', 'solicitud.xml');
  element.style.display = 'none';
  document.body.appendChild(element);
  element.click();
  document.body.removeChild(element);
}
