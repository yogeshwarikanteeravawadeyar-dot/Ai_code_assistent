async function sendMessage() {
    const input = document.getElementById("input");
    const message = input.value;

    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();
        addMessage(data.response, "ai");

    } catch (error) {
        addMessage("Error connecting to server", "ai");
    }
}

function addMessage(text, sender) {
    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = sender;
    div.innerText = text;

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}
