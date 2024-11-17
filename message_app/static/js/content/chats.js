window.onload = function () {
    const container = document.getElementById('custom_convo')
    container.scrollTop = container.scrollHeight
}


function convo(id) {
    location.href = id // To Conversation
}

const messageInput = document.getElementById('custom_message')
const maxHeight = 100 // Set maximum height in pixels

messageInput.addEventListener('input', function () {
    this.style.height = '0px' // Reset height to recalculate
    if (this.scrollHeight > maxHeight) {
        this.style.height = maxHeight + 'px' // Set to max height if exceeded
        this.style.overflowY = 'auto' // Show scrollbar when max height is reached
    } else {
        this.style.height = this.scrollHeight + 'px' // Expand to fit content
        this.style.overflowY = 'hidden' // Hide scrollbar until max height is reached
    }
})

const url = `ws://${window.location.host}/ws/socket-server/`
const chatSocket = new WebSocket(url)

let form = document.getElementById('form')
form.addEventListener('submit', (e) => {
    e.preventDefault()

    let msg = e.target.compose_msg.value
    let user = e.target.user.value
    let receiver = e.target.receiver.value
    let convo_id = e.target.convo_id.value

    chatSocket.send(JSON.stringify({
        'message': msg,
        'user': user,
        'receiver': receiver,
        'convo_id': convo_id
    }))

    form.reset()
    messageInput.style.height = '0'
    messageInput.style.overflowY = 'hidden'
})

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    let display = document.getElementById('custom_convo')
    let convo_id = document.getElementById('convo_id').value
    let user = document.getElementById('user').value

    let latest_msg = document.getElementById('latest_msg')
    
    if (data.convo_id == convo_id) {
        if (data.type === 'new_chat') {
            let appendNewMessage = ``
    
            if (data.sender == user) {
                appendNewMessage += `
                    <div class="align-self-end d-flex gap-2 align-items-end">
                        <pre class="px-3 py-2 m-0 custom_single_msg">${data.message_content}</pre>
                        <img src="${data.profile_url.toLowerCase()}" alt="${data.sender}">
                    </div>`
                
                latest_msg.innerText = `You: ${data.message_content}`
            } else {
                appendNewMessage += `
                    <div class="d-flex gap-2 align-items-end">
                        <img src="${data.profile_url.toLowerCase()}" alt="${data.receiver}">
                        <pre class="px-3 py-2 m-0 custom_single_msg">${data.message_content}</pre>
                    </div>`

                latest_msg.innerText = `${data.message_content}`
            }
    
            display.insertAdjacentHTML('beforeend', appendNewMessage)
            display.scrollTop = display.scrollHeight
        }
    }
}