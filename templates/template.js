function shuffleImages() {
    var container = document.getElementById('masonry-container');
    var items = container.getElementsByClassName('masonry-item');
    for (var i = items.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        container.insertBefore(items[j], items[i]);
    }
}

function copyToClipboard(text) {
    navigator.clipboard.writeText(text)
        // .then(() => alert("Copied to clipboard:\\n" + text))
        // .catch(err => console.error("Failed to copy:", err));
}

document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("columnCountInput");
    var container = document.querySelector(".masonry-container");

    if (input && container) {
        input.addEventListener("input", function () {
            const count = parseInt(input.value, 10);
            if (count >= 1) {
                container.style.columnCount = count;
            }
        });
    }
});
