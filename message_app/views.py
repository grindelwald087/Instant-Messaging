import random
import string

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import users, message, conversation
from .forms import login_form, register_form, compose_msg_form

def userProfile(request):
    if 'username' in request.session:
        userName = request.session.get('username')
        userProfiles = users.objects.get(username = userName)
        messages = message.objects.filter(sender_id = userName)
        userName = request.session.get('username')
        convoId = message.objects.filter(sender_id = userName).values('convo_id')

        latestMsgs = []

        for id in convoId:
            latestMsg = conversation.objects.order_by('created_at').filter(convo_id = id['convo_id']).values_list(
                'convo_id',
                'message_content',
                'sender',
                'status'
                ).last()
            latestMsgs.append(latestMsg)
        
        return {
            'userProfiles': userProfiles,
            'messages': messages,
            'user': userName,
            'latestMsg': latestMsgs,
        }

# Send OTP ot Email
@staticmethod
def generate_otp(length = 8):
    characters = string.ascii_letters + string.digits
    
    random_id = ''.join(random.choices(characters, k=length))
    
    return random_id

# Redirect Page for unknown URL's
def redirect_page(request, ):
    return redirect('login')

# Login Page
def login_page(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pswrd = form.cleaned_data['password']

            user = users.objects.filter(username=uname).first()

            if user:
                if user and check_password(pswrd, user.password):
                    request.session['username'] = user.username

                    user.status = 'online'
                    user.save()
                        
                    return redirect('chats')
                else:
                    messages.error(request, "Incorrect password.")
            else:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "Invalid credentials")
    else:
        form = login_form()
        
    return render(request, 'login.html', {'login_form': form})

# Logout Page
def logout_page(request):
    uname = request.session['username']
    user = users.objects.get(username = uname)

    user.status = 'offline'
    user.save()

    request.session.flush()
    return redirect('login')

# Register Page
def register_page(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        
        if form.is_valid():
            otp = form.cleaned_data['otp']
            generated = request.session.get('generated_otp')

            if (generated == otp):
                users.objects.create (
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    gender = form.cleaned_data['gender'],
                    email = form.cleaned_data['email'],
                    username = form.cleaned_data['username'],
                    password = make_password(form.cleaned_data['password'])
                )
                del request.session['generated_otp']
                request.session['username'] = form.cleaned_data['username']
                return redirect('chats')
            else:
                messages.error(request, "Incorrect OTP.")
    elif 'generated_otp' in request.session:
        del request.session['generated_otp']
        form = register_form()
    else:
        form = register_form()

    return render(request, 'register.html', {
        'register_form': form,
        })

# Send OTP to Email
def send_otp(request, recipient):
    if request.method == 'GET':
        otp = generate_otp()
        request.session['generated_otp'] = otp

        sender = 'marichat.11.26.24@gmail.com'
        
        email = EmailMessage(
            subject = "MariChat",
            body = f'<b>{otp}</b> is your MariChat One Time Password (OTP). Don\'t share this to others.',
            from_email = sender,
            to = [recipient],
        )
        email.content_subtype = 'html'
        email.send()

        return JsonResponse({
            'success': True,
        })

# Chats Page
def chats_page(request):
    if 'username' in request.session:
        return render(request, 'content/chats.html', {
            'context': userProfile(request),
        })
    else:
        return redirect('login')

# Conversations
def chats_convo_page(request, id):
    form = compose_msg_form()

    if 'username' in request.session:
        user = request.session.get('username')
        receiver = message.objects.filter(convo_id = id, sender_id = user)
        messageContent = conversation.objects.filter(convo_id = id)

        return render(request, 'content/convo.html', {
            'receiver': receiver,
            'context': userProfile(request),
            'id': id,
            'messageContent': messageContent,
            'user': user,
            'form': form
        })

# Groups Page
def groups_page(request):
    if 'username' in request.session:    
        return render(request, 'content/groups.html', {
            'context': userProfile(request)
        })
    else:
        return redirect('login')

# Contacts Page
def contacts_page(request):
    if 'username' in request.session:
        return render(request, 'content/contacts.html', {
            'context': userProfile(request)
        })
    else:
        return redirect('login')

# Notifications Page
def notifications_page(request):
    if 'username' in request.session:
        return render(request, 'content/notifications.html', {
            'context': userProfile(request)
        })
    else:
        return redirect('login')
    

# Settings Page
def settings_page(request):
    if 'username' in request.session:
        return render(request, 'content/settings.html', {
            'context': userProfile(request)
        })
    else:
        return redirect('login')
    

# Profile Page
def profile_page(request):
    return render(request, 'content/profile.html', {
        'context': userProfile(request)
    })

def change_profile(request):
    return render(request, 'content/profile.html', {
        'context': userProfile(request)
    })