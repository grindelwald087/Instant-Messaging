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

chatSocket.onmessage = (e) => {
    let data = JSON.parse(e.data)
    console.log(data)
}

// chatSocket.onmessage = (e) => {
//     let data = JSON.parse(e.data)
//     let display = document.getElementById('custom_convo')
//     let user = document.getElementById('user').value
//     let receiver = document.getElementById('receiver').value
//     let convo_id = document.getElementById('convo_id').value
//     let custom_new_msg = document.getElementById('custom_new_msg')

//     if (data.convoId == convo_id) {
//         if (data.type === 'chats') {
//             let messageHtml = ``
    
//             if (data.sender == user) {
//                 messageHtml += `
//                     <div class="align-self-end d-flex gap-2 align-items-end">
//                         <pre class="px-3 py-2 m-0 custom_single_msg">${data.message}</pre>
//                         <img src="${data.profile_url.toLowerCase()} " alt="${data.sender}">
//                     </div>`
//             } else {
//                 messageHtml += `
//                     <div class="d-flex gap-2 align-items-end">
//                         <img src="${data.profile_url.toLowerCase()}" alt="${data.receiver}">
//                         <pre class="px-3 py-2 m-0 custom_single_msg">${data.message}</pre>
//                     </div>`
//             }

//             // if (data.receiver == receiver) {
//             //     custom_new_msg.innerHTML += 1
//             // }
    
//             display.insertAdjacentHTML('beforeend', messageHtml)
    
//             display.scrollTop = display.scrollHeight
//         }
//     }
// }

// let form = document.getElementById('form')
// form.addEventListener('submit', (e) => {
//     e.preventDefault()
//     let message = e.target.compose_msg.value
//     let user = e.target.user.value
//     let receiver = e.target.receiver.value
//     let url = e.target.profile_url.value
//     let convoId = e.target.convo_id.value

//     chatSocket.send(JSON.stringify({
//         'message': message,
//         'user': user,
//         'receiver': receiver,
//         'profileUrl': url,
//         'convoId': convoId,
//     }))

//     form.reset()

//     messageInput.style.height = '0'
//     messageInput.style.overflowY = 'hidden'
// })