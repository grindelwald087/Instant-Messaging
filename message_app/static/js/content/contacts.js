// const group_name = document.getElementById('current_user').value
// const contact_url = `ws://${window.location.host}/ws/socket-server/${group_name}`

// const contactSocket = new WebSocket(contact_url)

const notif_url = `ws://${window.location.host}/ws/socket-server/notification`
const notifSocket = new WebSocket(notif_url)


// if (contactSocket) {
//     console.log('connected')
// }

if (notifSocket) {
    console.log('connected')
}

// const search_contact = document.getElementById('search_form')
// const display_search = document.getElementById('display_search')

// search_contact.addEventListener('submit', (e) => {
//     e.preventDefault()
//     search = e.target.search_contact.value

//     contactSocket.send(JSON.stringify({
//         'search': search,
//     }))
// })

const req_from = document.getElementById('req_from').value
const req_to = document.getElementById('req_to').value

function send_req() {
    const send_reqs = document.getElementById('send_req')

    notifSocket.send(JSON.stringify({
        'type': 'send',
        'req_from': req_from,
        'req_to': req_to,
    }))

    send_reqs.outerHTML = `
    <div class="d-flex flex-column gap-3 justify-content-center">
        <span class="fw-bold border text-success fs-3">Request sent</span>
        <button type="button" class="btn btn-danger" id="cancel_req" onclick="cancel_req()">Cancel request</button>
    </div>
    `
}

function cancel_req() {
    const cancel_reqs = document.getElementById('cancel_req')
    
    notifSocket.send(JSON.stringify({
        'type': 'cancel',
        'req_to': req_to,
    }))

    cancel_reqs.outerHTML = `<button type="button" class="btn btn-success" id="send_req" onclick="send_req()">Send request</button>`
}

// contactSocket.onmessage = (e) => {
//     const data = JSON.parse(e.data)

//     if (data.type == 'search_contacts') {
//         display_search.style.display = 'block'
//         display_search.innerHTML = `
        
//         `
        
//         const search_display = document.getElementById('search_display')
        

//         const profile = document.getElementById('profile')
//         const fullname = document.getElementById('fullname')
//         const gender = document.getElementById('gender')
//         const status = document.getElementById('status')
//         const joined = document.getElementById('joined')

//         const timestamp = data.joined
//         const date = new Date(timestamp)
//         const options = { year: 'numeric', month: 'long', day: 'numeric' }
//         const formattedDate = date.toLocaleDateString('en-US', options) 


//         search_display.addEventListener('click', () => {
//             display.style.display = 'none'
//             display_profile.style.display = 'block'
//             profile.src = `${data.profile_url.toLowerCase()}`
//             profile.alt = `${data.username}`
//             fullname.innerHTML = `${data.first_name} ${data.last_name}`
//             gender.innerHTML = `${data.gender}`
//             status.innerHTML = `${data.status}`
//             joined.innerHTML = `${formattedDate}`
//         })

//     } else if (data.type == 'no_records') {
//         display_search.style.display = 'block'
//         display_search.innerHTML = `
//         <h5 class="fw-bold text-center mt-3">Username does not exist.</h5>
//         `
//     }
// }

// contactSocket.onclose = function(e) {
//     console.error('Websocket closed unexpectedly')
// }

notifSocket.onclose = function(e) {
    console.error('Websocket closed unexpectedly')
}


const contacts = document.getElementById('contacts')
const display = document.getElementById('display')
const display_profile = document.getElementById('display_profile')

contacts.addEventListener('click', () => {
    display.style.display = 'none'
    display_profile.style.display = 'block'
})