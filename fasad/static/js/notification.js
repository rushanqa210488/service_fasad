
document.addEventListener('DOMContentLoaded', function () {
  setTimeout(function() {
    var element = document.getElementById("notification");
    if (element) {
      element.remove();
    }
  }, 5000);
});
