# Rules: Shift + X to quit
# .txt cotent: name,6.78 (no spaces)


def preamble():
    \"\"\"Preamble for rhythm game\"\"\"
    for i in range(3, 0, -1):
        print(i)
        time.sleep(0.5)
    print(\"Go!\")


def game():
    \"\"\"Main function for rhythm game\"\"\"
    notes = 20
    count = 0
    start = time.perf_counter()
    mapped_keys = {\"d\": 1, \"f\": 2, \"j\": 3, \"k\": 4}
    for i in range(notes):
        s = \"| | | | |\"
        music_note = random.randint(1, 4)
        index = music_note * 2 - 1
        s = list(s)
        s[index] = \"o\"
        s = \"\".join(s)
        print(s)
        key = msvcrt.getch().decode()
        if key in mapped_keys and mapped_keys[key] == music_note:
            count += 1
        elif key == \"X\":
            print(\"User Quit.\")
            exit(0) 

    end = time.perf_counter()
    accuracy = (count / notes) * 100
    time_taken = round(end - start, 2)
    print(f\"\"\"
Time Taken: {time_taken}s
Accuracy: {accuracy}%\"\"\")
    if accuracy == 100:
        with open(\"record.txt\") as in_file:
            name, record = in_file.readlines()[-1].split(\",\")
            if time_taken < float(record):
                print(f\"\"\"Congratulations, you beat {name} whose record was {float(record)}s!\"\"\")
                name = input(\"Enter your name for the leaderboards: \")
                with open(\"record.txt\") as out_file:
                    out_file.write(f\"{name},{time_taken}\")


def main():
    if len(sys.argv) == 2 and sys.argv[1] == \"- start\":
        preamble()
        game()
    else:
        print(\"Usage: python rhythm_game.py -start\")


if __name__ == \"__main__\":
    main()"
