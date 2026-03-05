document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('llm-form');
  const preguntaEl = document.getElementById('pregunta');
  const resultado = document.getElementById('resultado');

  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    const pregunta = preguntaEl.value.trim();
    if (!pregunta) return;
    resultado.textContent = 'Cargando...';

    try {
      const q = encodeURIComponent(pregunta);
      // Intentar con query param primero (backend actualizado)
      let res = await fetch(`/llm?pregunta=${q}`);

      // Si no funciona, intentar enviar como parte del path (por compatibilidad)
      if (res.status === 404) {
        res = await fetch(`/llm${q}`);
      }

      if (!res.ok) {
        const text = await res.text();
        throw new Error(`${res.status} ${res.statusText}: ${text}`);
      }

      const data = await res.json();
      resultado.textContent = data.respuesta || JSON.stringify(data, null, 2);
    } catch (err) {
      resultado.textContent = 'Error: ' + (err.message || err);
    }
  });
});
