function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  respond(message);
  input.value = '';
}

function appendMessage(sender, message) {
  const chatBox = document.getElementById("chat-box");
  const msgDiv = document.createElement("div");
  msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function respond(message) {
  let reply = "Sorry, I don't understand.";

  const lower = message.toLowerCase();

  if (lower.includes("hello") || lower.includes("hi")) {
    reply = "Hello! How can I help you?";
  } else if (lower.includes("your name")) {
    reply = "I am your friendly chatbot!";
  } else if (lower.includes("bye")) {
    reply = "Goodbye! Have a nice day!";
  } else if (lower.includes("how are you")) {
    reply = "I'm just a bot, but I'm doing great!";
  } else if (lower.includes("help")) {
	reply = "What type of help do you need?";
  }

  setTimeout(() => appendMessage("Bot", reply), 500);
}
