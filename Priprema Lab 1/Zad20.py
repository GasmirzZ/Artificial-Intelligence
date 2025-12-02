def boje(rgb):
    rez = {"Red": 0, "Green": 0, "Blue": 0}
    reds = rgb[1:3]
    greens = rgb[3:5]
    blues = rgb[5:]
    red = int(reds, 16)
    green = int(greens, 16)
    blue = int(blues, 16)
    rez.update({"Red": red, "Green": green, "Blue": blue})
    return rez


print(boje("#FA1AA0"))
