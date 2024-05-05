form = document.getElementsByClassName("form")[0];
textInput = document.getElementById("name");
searchButton = document.getElementById("search");

    searchButton.addEventListener("click", () => {
    var name = textInput.value;
    form.action = "/plan/workout/search/" + name;
});