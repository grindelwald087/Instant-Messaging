def sidebar(request):
    contents = [
        'chats',
        'groups',
        'contacts',
        'notifications',
        'settings',
    ]

    attrs = [
        'fa-solid fa-comment-dots',
        'fa-solid fa-user-group',
        'fa-solid fa-address-card',
        'fa-solid fa-bell',
        'fa-solid fa-gear',
    ]

    sidebars = zip(contents, attrs)

    return {'sidebars': sidebars,}

def profile(request):
    contents = [
        'change profile',
        'logout'
    ]

    attrs = [
        'fa-solid fa-user',
        'fa-solid fa-right-from-bracket'
    ]

    profiles = zip(contents, attrs)

    return {'profiles': profiles}