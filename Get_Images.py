def Start(a, username, password):
    from connect import network
    import random
    import os

    try:
        list1 = network(a,username, password)
        print("\n\n\nnetworking done")
        status= "online"
        #os.system(
        #    f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/{name}")
        #print("online")

    except Exception as E:

        list_a = [i for i in os.listdir(
            "/home/rishabh/Documents/Python/Wallpaper") if i[-3::1] == "png" or i[-3::1] == "jpg"]
        list_b = [i for i in os.listdir(
            "/home/rishabh/Documents/Python/Wallpaper/Wpaper/PICS") if i[-3::1] == "png" or i[-3::1] == "jpg"]
        list1 = list_a+list_b
        status= "offline"
        '''if image in list_b:
            os.system(
                f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/Wpaper/PICS/{image}")
        else:
            os.system(
                f"/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/rishabh/Documents/Python/Wallpaper/{image}")
        '''
    print("\n\n\n\n\n\n",status)
    return list1, status

if __name__ == "__main__":
    print(Start("wallpaper", "Rishabh_0507", "Aowu282n@££@2927Ka"))
