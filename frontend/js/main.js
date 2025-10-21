document.addEventListener("DOMContentLoaded", () => {

  const loggedIn = localStorage.getItem("loggedIn");
  const currentPage = window.location.pathname.split("/").pop();

  if (loggedIn === "true" && currentPage === "login.html") {
    window.location.href = "dashboard.html";
    return;
  }

  if (currentPage === "dashboard.html") {

    if(!loggedIn) {
      window.location.href = "login.html";
      return;
    }

    const userData = JSON.parse(localStorage.getItem("user")) || { nombre: "Usuario", apellido: "", email: "usuario@mail.com" };

    document.getElementById("nombreUsuario").textContent = userData.nombre;
    document.getElementById("apellidoUsuario").textContent = userData.apellido;
    document.getElementById("emailUsuario").textContent = userData.email;

    document.getElementById("logoutBtn").addEventListener("click", () => {
      localStorage.removeItem("loggedIn");
      localStorage.removeItem("user");
      window.location.href = "login.html";
    });
 
  }

  const registerForm = document.getElementById("registerForm");
  if (registerForm) {
    registerForm.addEventListener("submit", event => {
      event.preventDefault();

      const form = registerForm;
      const password = document.getElementById('password')?.value || "";
      const passwordConfirm = document.getElementById('passwordConfirm')?.value || "";

      if (!form.checkValidity() || password !== passwordConfirm) {
        event.stopPropagation();
        if (password !== passwordConfirm) {
          document.getElementById('passwordConfirm').setCustomValidity("La contraseña no coincide");
        } else {
          document.getElementById('passwordConfirm').setCustomValidity("");
        }
        form.classList.add('was-validated');
        return;
      }

      const nombre = document.getElementById('nombre').value.trim();
      const apellido = document.getElementById('apellido').value.trim();
      const email = document.getElementById('email').value.trim();
      const userData = { nombre, apellido, email, password };
      localStorage.setItem('user', JSON.stringify(userData));

      const registroModalEl = document.getElementById('registroExitosoModal');
      const registroModal = new bootstrap.Modal(registroModalEl);
      registroModal.show();

      registroModalEl.addEventListener('hidden.bs.modal', () => {
        window.location.href = "login.html";
      });
    });
  }

  const DEFAULT_USER = { email: "usuario@mail.com", password: "123456", nombre: "Juan", apellido: "Pérez" };
  const loginForm = document.getElementById("loginForm");
  const loginError = document.getElementById("loginError");

  if (loginForm) {
    loginForm.addEventListener("submit", event => {
      event.preventDefault();

      const emailInput = document.getElementById("email");
      const passwordInput = document.getElementById("passwordInput");
      const email = emailInput.value.trim();
      const password = passwordInput.value;

      if (!loginForm.checkValidity()) {
        event.stopPropagation();
        loginForm.classList.add("was-validated");
        return;
      }

      if (email === DEFAULT_USER.email && password === DEFAULT_USER.password) {
        localStorage.setItem("loggedIn", "true");

        localStorage.setItem("user", JSON.stringify({
          nombre: DEFAULT_USER.nombre,
          apellido: DEFAULT_USER.apellido,
          email: DEFAULT_USER.email
        }));

        loginForm.classList.remove("was-validated");
        loginError.classList.add("d-none");
        window.location.href = "dashboard.html";
      } else {
        loginError.classList.remove("d-none");
        loginForm.classList.add("was-validated");
      }
    });

    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("passwordInput");

    emailInput.addEventListener("input", () => {
      loginError.classList.add("d-none");
    });

    passwordInput.addEventListener("input", () => {
      loginError.classList.add("d-none");
    });
  }

});