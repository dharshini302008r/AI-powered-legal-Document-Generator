async function generateDocument() {

    let type = document.getElementById("documentType").value;
    let details = document.getElementById("details").value;

    let response = await fetch("http://127.0.0.1:8001/generate", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            document_type: type,
            details: details
        })
    });

    let data = await response.json();

    document.getElementById("result").innerHTML =
        "<h3>Generated Document</h3>" +
        "<pre>" + data.document + "</pre>";
}