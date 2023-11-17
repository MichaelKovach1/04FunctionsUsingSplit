def meal_time(time):
    h, m = time.split(":")
    h = int(h)
    m = int(m)
    if h >= 7 and h <= 8:
      if h == 8 and m == 0:
        return "breakfast"
      elif h == 8 and m > 0:
        return "nothing right now"
      else:
        return "breakfast"
    elif h >= 12 and h <= 13:
      if h == 13 and m == 0:
        return "lunch"
      elif h == 13 and m > 0:
        return "nothing right now"
      else:
        return "lunch"
    elif h >= 18 and h <= 19:
      if h == 19 and m == 0:
        return "dinner"
      elif h == 19 and m > 0:
        return "nothing right now"
      else:
        return "dinner"
    else:
      return "nothing right now"
print("meal_time")
print("07:32 =>", meal_time("07:32"))
print("13:42 =>", meal_time("13:42"))
print("12:47 =>", meal_time("12:47"))
print("19:00 =>", meal_time("19:00"))
print("09:18 =>", meal_time("09:18"))
print("19:01 =>", meal_time("19:01"))


def get_filename_extension(namestring):
  name, extension = namestring.split(".")
  return extension
print("get_filename_extension")
print("shark.png =>", get_filename_extension("shark.png"))
print("index.csv =>", get_filename_extension("index.csv"))

def is_image_file(namestring):
  extension = get_filename_extension(namestring)
  if extension == "png" or extension == "jpg" or extension == "jpeg" or extension == "gif" or extension == "tiff":
    return True
  else:
    return False

print("is_image_file")
print("shark.png =>", is_image_file("shark.png"))
print("index.mp3 =>", is_image_file("index.mp3"))