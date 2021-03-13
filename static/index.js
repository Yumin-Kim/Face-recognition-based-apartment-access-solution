const xhr = new XMLHttpRequest();

xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("demo").innerHTML =
        this.responseText;
      }
  }

  xhr.open("GET", "/admin", true);
  xhr.send();

// var xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       document.getElementById("demo").innerHTML =
//       this.responseText;
//     }
//   };
//   xhttp.open("GET", "/admin", true);
//   xhttp.send();