from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .models import users, message, conversation
from .forms import login_form, register_form, compose_msg_form

def userProfile(request):
    userName = request.session.get('username')
    userProfiles = users.objects.get(username = userName)
    messages = message.objects.filter(sender_id = userName)
    convoId = conversation.objects.filter(sender = userName).first()
    latestMsg = conversation.objects.filter(convo_id = 10).order_by('-created_at').first()

    return {
        'userProfiles': userProfiles,
        'messages': messages,
        'user': userName,
        'convoId': convoId,
        'latestMsg': latestMsg
    }

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
            users.objects.create (
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                password = make_password(form.cleaned_data['password'])
            )

            return redirect('chats')
    else:
        form = register_form()

    return render(request, 'register.html', {'register_form': form})

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
        userReceiver = conversation.objects.filter(sender = user).values('receiver').first()
        countMsg = conversation.objects.filter(receiver = userReceiver, status = 'sent').count()

        return render(request, 'content/convo.html', {
            'receiver': receiver,
            'context': userProfile(request),
            'id': id,
            'messageContent': messageContent,
            'countMsg': userReceiver,
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