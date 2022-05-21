var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

let data = JSON.parse('bbc.json');
let div = document.createElement("div");
div.textContent = data[0]['link'];
// div.textContent = "Your favorite color is now " + data.color;
addonElement.appendChild(div);
