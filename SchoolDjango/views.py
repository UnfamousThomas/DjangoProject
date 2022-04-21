from django.http import HttpResponseRedirect
from django.shortcuts import render
from discordwebhook import Discord


from .models import DiscordMessage

discord = Discord(url="https://discord.com/api/webhooks/966738095238176789/0_m-P7blnZ-nizkCTw-mQCnMo8SJLUok1TTVJjtuvhFMahvGh5rbiN0g9SREg887WqTk")

def get_name(request):

    if request.method == 'POST':

        form = DiscordMessage(request.POST)

        if form.is_valid():
            msg_value = form.cleaned_data["message"]

            discord.post(
                content=msg_value,
                username="DJango Veebileht",
                avatar_url="https://www.kindpng.com/picc/m/481-4819499_robot-icon-png-download-transparent-background-robot-icon.png"
            )
            return HttpResponseRedirect('/')

    else:
        form = DiscordMessage()

    return render(request, 'message.html', {'form': form})