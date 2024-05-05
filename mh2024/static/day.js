var modal = document.getElementById("myModal");

var btn = document.getElementsByClassName("add-workout")[0];

var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  console.log("test");
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}