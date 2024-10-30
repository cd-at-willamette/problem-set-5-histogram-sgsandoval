from pgl import *

#1a
def create_histogram_array(data:list[int])->list[int]:
    max_value = max(data) if data else 0
    histogram = [0] * (max_value + 1)
    for number in data:
        histogram[number] += 1
    return histogram
    pass

#1b
def print_histogram(hist:list[int]) -> None:
    for index, value in enumerate(hist):
        print(f"{index}: {'*' * value}")
    pass

#1c
def graph_histogram(hist:list[int], width:int, height:int) -> None:
    gw = GWindow(width,height)

    def my_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    max_value = max(hist) if hist else 1
    w = width / len(hist)

    for i, value in enumerate(hist):
        h = (value / max_value) * height

        x = i * w
        y = height - h

    gw.add(my_rect(x,y,w,h,"Blue"))

    


    pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
#print_histogram(hist) # uncomment to test
#graph_histogram(hist, 400, 400) # uncomment to test

