import requests

def Start(_,a):
    from connect import network
    import random
    import os
    import time

    try:

        list1 = network(a, "Rishabh_0507", "Aowu282n@££@2927Ka")
        print(list1)

        name = f"Image{time.time()}.png"

        f = open(
            f"/home/rishabh/Documents/Python/Wallpaper/{name}", "wb")
        image = requests.get(random.choice(list1))
        f.write(image.content)
        f.close()
        # os.system("PID=$(pgrep gnome-session)")0
        # os.system("export $(grep -z DBUS_SESSIONS_BUS_ADDRESS /proc/$PID/environ)")
        os.system(f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/{name}")
        print("online")

    except Exception as error:

        print(E)

        list_a = [i for i in os.listdir(
            "/home/rishabh/Documents/Python/Wallpaper") if i[-3::1] == "png" or i[-3::1] == "jpg"]
        list_b = [i for i in os.listdir(
            "/home/rishabh/Documents/Python/Wallpaper/Wpaper/PICS") if i[-3::1] == "png" or i[-3::1] == "jpg"]
        list1 = list_a+list_b
        image = random.choice(list1)
        # os.system("PID=$(ps ax | grep 'Wallpaper.service')")
        # os.system("export $(grep -z DBUS_SESSIONS_BUS_ADDRESS /proc/$PID/environ)")
        # os.system("echo fj")
        if image in list_b:
            os.system(
                f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/Wpaper/PICS/{image}")
        else:
            os.system(
                f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/{image}")

if __name__ == "__main__":
    Start("_","wallpaper")
