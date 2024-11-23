import uuid
from django.db import models

# Users Login Table
class users(models.Model):
    class Meta:
        db_table = 'users'

    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=100, null=False, default='')
    profile = models.ImageField(upload_to='images/', null=False, default='images/default-profile.jpg')
    first_name = models.CharField(max_length=50, null=False, default='')
    last_name = models.CharField(max_length=50, null=False, default='')
    status = models.CharField(max_length=10, null=False, default='online')
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.username

# Conversation Table
class conversation(models.Model):
    class Meta:
        db_table = 'conversation'

    message_content_id = models.BigAutoField(primary_key=True)
    convo_id = models.CharField(max_length=20, null=True)
    message_content = models.CharField(max_length=1000)
    sender = models.CharField(max_length=255, null=True)
    receiver = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.message_content
    
# Messages Table
class message(models.Model):
    class Meta:
        db_table = 'message'

    messages_id = models.BigAutoField(primary_key=True)
    convo_fk = models.ForeignKey(conversation, on_delete=models.CASCADE, null=True, related_name='convo_id_fk')
    convo_id = models.IntegerField(null=True)
    sender = models.ForeignKey(users, on_delete=models.CASCADE, null=True, related_name='sender_username', to_field='username')
    receiver = models.ForeignKey(users, on_delete=models.CASCADE, null=True, related_name='receiver_username', to_field='username')

    def __str__(self):
        return str(self.sender)