const sendOTP = () => {
    const recipient = document.getElementById('email').value
    let emptyEmail = document.getElementById('emptyEmail')

    const allowedDomains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
    const domain = recipient.split('@').pop()

    if (recipient == '') {
        emptyEmail.style.display = 'block'
    }
    else if (!allowedDomains.includes(domain)) {
        emptyEmail.innerHTML = 'Invalid email address.'
        emptyEmail.style.display = 'block'
    } else {
        let btn = document.getElementById('send')
        let seconds = 60

        btn.disabled = true

        const interval = setInterval(() => {
            seconds -= 1
            btn.textContent = `${seconds}'s`

            if (seconds <= 0) {
                clearInterval(interval)
                btn.textContent = "Send OTP"
                btn.disabled = false
            }
        }, 1000)

        

        fetch(`${recipient}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('success')
            } else {
                console.log('error')
            }
        })
    }
}

const fields = [
    { field: 'fname', error: 'fnameError' },
    { field: 'lname', error: 'lnameError' },
    { field: 'uname', error: 'unameError' },
    { field: 'password', error: 'passError' },
    { field: 'confirm_password', error: 'confError' },
    { field: 'email', error: 'emailError' },
    { field: 'email', error: 'emptyEmail' },
    { field: 'otp', error: 'otpError' },
]

fields.forEach(({ field, error }) => {
    document.getElementById(field).addEventListener('focus', () => {
        document.getElementById(error).style.display = 'none'
    })
})