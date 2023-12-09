

def legit(full_line):
    # Game 4:
    
    # 4 blue, 11 green, 6 red; 4 green, 2 red; 12 red, 1 blue, 3 green
    line = full_line.split(":")[1]
    curr = True
    # 4 blue, 11 green, 6 red
    balls = line.split(";")
    color_count = {
        "blue": 14,
        "green": 13,
        "red": 12,
    } # color -> number of balls
    for ball in balls:
        # 4 blue
        colors = ball.split(",")
        for color in colors:
            color_num_word = color.strip().split(" ")
            print(color_num_word)
            if (color_count[color_num_word[1]] < int(color_num_word[0])):
                return False
    return curr

with open("input2.txt", "r") as f:
    i = 0
    val = 0
    for l in f:
        print(f"processing line {i}: {l}", end="")
        possible = legit(l)
        val += int(l.split(":")[0].split(" ")[1]) if possible else 0
        print(f"found code {possible}")
        i += 1
        

print(f'final {val}')	