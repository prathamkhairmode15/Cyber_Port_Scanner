function toggleTheme(){
    document.body.classList.toggle("dark")
    document.body.classList.toggle("light")
}

function setProgress(v){
    document.getElementById("progress").style.width = v + "%"
}

function value(id){
    return document.getElementById(id).value.trim()
}

async function startScan(){

    setProgress(10)

    let res = await fetch("/scan",{
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body:JSON.stringify({
            target:value("target"),
            start:value("start"),
            end:value("end")
        })
    })

    setProgress(60)

    let data = await res.json()

    renderResults(data)

    setProgress(100)
}

function renderResults(data){

    let html = `
        <div class="mb-2">
            <span class="result-title">Target:</span> ${data.target}
        </div>

        <div class="mb-2">
            <span class="result-title">Detected OS:</span> ${data.os}
        </div>

        <div class="mb-2">
            <span class="result-title">Scan Time:</span> ${data.time}
        </div>

        <div class="mt-3">
            <span class="result-title">Open Ports</span><br>
            ${data.open_ports.length > 0 
                ? data.open_ports.map(p => `<span class="port-badge">${p}</span>`).join("")
                : "<i>No open ports found</i>"}
        </div>

        <div class="mt-3">
            <span class="result-title">Vulnerability Notes</span><br>
            ${data.tags.length > 0
                ? data.tags.map(t => `<span class="vuln">Port ${t.port}: ${t.note}</span>`).join("")
                : "<i>No risk indicators detected</i>"}
        </div>
    `

    document.getElementById("results").innerHTML = html
}

function downloadPDF(){
    window.location = "/export"
}
