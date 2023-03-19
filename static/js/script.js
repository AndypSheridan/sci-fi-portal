
// Shows profile form on button-click in profile.html
function changeStyle() {
    var element = document.getElementById("profile-form");
    element.style.display = "block";
}

// Automatically assigns user when adding a book review
let user = "{{ user.id }}";
document.getElementById("user").value = user;

// 
function addClass() {
    var elem = document.getElementByClassName("close");
    elem.classList.add("alert-button");
}