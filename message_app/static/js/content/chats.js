window.onload = function () {
    const container = document.getElementById('custom_convo')
    const msg = document.getElementById('custom_message')

    container.scrollTop = container.scrollHeight
    msg.focus()
}

function convo(id) {
    location.href = id

}

const display = document.getElementById('custom_convo')
const messageInput = document.getElementById('custom_message')
const maxHeight = 100

messageInput.addEventListener('input', function () {
    this.style.height = '0px'
    if (this.scrollHeight > maxHeight) {
        this.style.height = maxHeight + 'px'
        this.style.overflowY = 'auto'
    } else {
        this.style.height = this.scrollHeight + 'px'
        this.style.overflowY = 'hidden'
        display.scrollTop = display.scrollHeight
    }
})

// const convo_id = document.getElementById('convo_id').value

// const url = `ws://${window.location.host}/ws/socket-server/`
// const chatSocket = new WebSocket(url)

// if (chatSocket) {
//     console.log('connected')
// }

const formToSubmit = document.getElementById('form')

formToSubmit.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        if (!e.shiftKey) {
            e.preventDefault()
            const msg = document.getElementById('custom_message').value.trim()
            const user = document.getElementById('user').value
            const receiver = document.getElementById('receiver').value
            const convo_id = document.getElementById('convo_id').value

            if (msg == '') {
                return
            }

            chatSocket.send(JSON.stringify({
                'message': msg,
                'user': user,
                'receiver': receiver,
                'convo_id': convo_id
            }))

            formToSubmit.reset()
            messageInput.style.height = '0'
            messageInput.style.overflowY = 'hidden'
        }
    }
})

chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data)
    const display = document.getElementById('custom_convo')
    const convo_id = document.getElementById('convo_id').value
    const user = document.getElementById('user').value
    const latest_msg = document.querySelector(`[data-convo-id="${data.convo_id}"]`)

    function truncateText(text, maxLength) {
        if (text.length > maxLength) {
          return text.substring(0, maxLength) + '...'
        }
        return text
    }
    
    if (data.convo_id == convo_id) {
        if (data.type === 'new_chat') {
            let appendNewMessage = ``
    
            if (data.sender == user) {
                appendNewMessage += `
                    <div class="align-self-end d-flex gap-2 align-items-end">
                        <pre class="px-3 py-2 m-0 custom_single_msg">${data.message_content}</pre>
                        <img src="${data.profile_url.toLowerCase()}" alt="${data.sender}">
                    </div>`
            } else {
                appendNewMessage += `
                    <div class="d-flex gap-2 align-items-end">
                        <img src="${data.profile_url.toLowerCase()}" alt="${data.receiver}">
                        <pre class="px-3 py-2 m-0 custom_single_msg">${data.message_content}</pre>
                    </div>`
            }
    
            display.insertAdjacentHTML('beforeend', appendNewMessage)
            display.scrollTop = display.scrollHeight
        }
    }   

    if (latest_msg) {
        if (data.sender == user) {
            latest_msg.innerHTML = `You: ${truncateText(data.message_content, 30)}`
        } else {
            latest_msg.innerHTML = truncateText(data.message_content, 35)
        }
    }
}

chatSocket.onclose = function(e) {
    console.error('Websocket closed unexpectedly')
}