function login() {
    var username = document.getElementById("inputUsername").value;
    var password = document.getElementById("inputPassword").value;

    var url = "http://localhost:5000/login?username=" + username + "&password=" + password;

    window.location.replace(url);
}