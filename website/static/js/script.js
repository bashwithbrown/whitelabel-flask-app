function togglePassword(fieldId) {
  var field = document.getElementById(fieldId);
  var button = field.nextElementSibling;
  if (field.type === "password") {
    field.type = "text";
    button.innerText = "Hide";
  } else {
    field.type = "password";
    button.innerText = "Show";
  }
}
