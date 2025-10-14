// login

const USER = "usuario@mail.com";
const PASSWORD = "123456";

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("passwordInput").value;

  if (email === USER && password === PASSWORD) {
    alert("Login exitoso");
    window.location.href = "index.html";
  } else {
    alert("Usuario o contraseña incorrectos");
  }
});

// registro

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("registerForm");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const apellido = document.getElementById("apellido").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const passwordConfirm = document.getElementById("passwordConfirm").value;

    if (password !== passwordConfirm) {
      alert("Las contraseñas no coinciden. Por favor, verifica.");
      return;
    }

    if (!nombre || !apellido || !email || !password) {
      alert("Por favor, completa todos los campos obligatorios.");
      return;
    }

    alert("Registro exitoso. Ahora puedes iniciar sesión.");

    setTimeout(() => {
      window.location.href = "login.html";
    }, 500);
  });
});
