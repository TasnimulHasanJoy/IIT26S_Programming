
import os
import codecs

PROGRESS_FILE = "player_progress.txt"

locations = {
    0: "Home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}

def rot13(text):
    return codecs.decode(text, "rot_13")


def main():
    if not os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "w") as file:
            file.write("current_location;next_location;passphrase\n")
            file.write("0;1;qvfpvcyvar\n")

    with open(PROGRESS_FILE, "r") as file:
        lines = file.readlines()

    if len(lines) < 2:
        print("No travel progress found.")
        return

    current, next_location, encrypted_password = lines[-1].strip().split(";")

    current = int(current)
    next_location = int(next_location)

    if next_location > 4:
        print("All Emperor messages collected!")
        return

    password = rot13(encrypted_password)

    print("Travel starting.")
    print(f"Currently at {locations[current]}.")
    print(f"Travelling to {locations[next_location]}...")
    print(f"...Arriving to the {locations[next_location]}.")
    print("Passing the guard at the entrance.")
    print(f'"{password}"')

    print("Looking for the message in the palace...")

    message_file = f"{next_location}_{password}.gkg"

    if not os.path.exists(message_file):
        print(f"Message file not found: {message_file}")
        return

    with open(message_file, "r") as file:
        encrypted_message = file.readline().strip()

    plain_message = rot13(encrypted_message)

    with open(PROGRESS_FILE, "a") as file:
        file.write(f"{next_location};{next_location + 1};")

        if next_location < 4:
            file.write(rot13("next_password"))
        else:
            file.write("DONE")

        file.write("\n")

    output_file = f"{next_location}-{password}.txt"

    with open(output_file, "w") as file:
        file.write(plain_message)

    print("Message saved successfully!")
    print("Travel ending.")


if __name__ == "__main__":
    main()
