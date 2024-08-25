document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const urlInput = document.querySelector("#id_url");

    form.addEventListener("submit", function(event) {
        const urlValue = urlInput.value;
        if (!isValidUrl(urlValue)) {
            event.preventDefault();
            alert("Iltimos, to'g'ri URL ni kiriting.");
        }
    });

    function isValidUrl(url) {
        const pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
            '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.?)+[a-z]{2,}|'+ // domain name
            '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
            '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
            '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
            '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
        return !!pattern.test(url);
    }
});
