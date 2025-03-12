from operator import itemgetter
import csv

LEARNED = 'l'
UNLEARNED = 'u'


# Load songs from CSV file
def load_songs(filename):
    songs = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                songs.append([row[0], row[1], int(row[2]), row[3]])
    except FileNotFoundError:
        print("File not found. Starting with an empty song list.")
    return songs


# Display songs
def display_songs(songs):
    sorted_songs = sorted(songs, key=itemgetter(2))

    # 计算最大列宽，确保格式对齐（可选）
    title_width = max(len(song[0]) for song in songs)
    artist_width = max(len(song[1]) for song in songs)
    year_width = max(len(str(song[2])) for song in songs)

    # 遍历排序后的歌曲列表
    for idx, song in enumerate(sorted_songs, start=1):  # 直接从1开始索引
        learned_status = '*' if song[3] == UNLEARNED else ''
        print(f"{idx:2}. {learned_status:2} {song[0]:<{title_width}} - {song[1]:<{artist_width}} ({song[2]:>{year_width}})")

    # 统计已学和未学的歌曲数量
    learned_count = sum(1 for song in songs if song[3] == LEARNED)
    unlearned_count = len(songs) - learned_count
    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")


# Save songs to CSV file

def save_songs(filename, songs):
    sorted_songs = sorted(songs, key=itemgetter(2))
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for song in sorted_songs:
            writer.writerow([song[0], song[1], song[2], LEARNED if song[3] == LEARNED else UNLEARNED])


# Complete a song
def complete_song(songs):
    """Allow the user to complete a song and mark it as learned."""
    if not any(song[3] == UNLEARNED for song in songs):
        print("No more songs to learn!")
        return

    sorted_songs = sorted(songs, key=lambda x: (x[2], x[0]))  # 和 display_songs() 保持一致的排序
    print("Enter the number of a song to mark as learned.")

    while True:
        try:
            print(">>> ", end="")
            song_number = int(input())
            if song_number < 1:
                print("Number must be > 0.")
            elif song_number > len(songs):
                print("Invalid song number")
            else:
                original_index = songs.index(sorted_songs[song_number - 1])

                if songs[original_index][3] == LEARNED:
                    print(f"You have already learned {songs[original_index][0]}")
                else:
                    songs[original_index][3] = LEARNED
                    print(f"{songs[original_index][0]} by {songs[original_index][1]} learned")
                break
        except ValueError:
            print("Invalid input; please enter a number.")



# Add new song
def add_song(songs):
    print("Enter details for a new song.")
    title = input("Title: ").strip()
    while not title:
        print("Input can not be blank.")
        title = input("Title: ").strip()

    artist = input("Artist: ").strip()
    while not artist:
        print("Input can not be blank.")
        artist = input("Artist: ").strip()

    while True:
        try:
            year = int(input("Year: "))
            if year <= 0:
                print("Number must be > 0.")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number.")

    song = [title, artist, year, UNLEARNED]
    songs.append(song)
    print(f'{title} by {artist} ({year}) added to song list.')


# Main program loop
def main():
    filename = 'songs.csv'
    songs = load_songs(filename)
    print("Song List 1.0 - by Lindsay Ward")
    print(f"{len(songs)} songs loaded.")
    while True:
        print("Menu:")
        print("D - Display songs")
        print("A - Add new song")
        print("C - Complete a song")
        print("Q - Quit")
        choice = input(">>> ").strip().lower()
        if choice == 'd':
            display_songs(songs)
        elif choice == 'a':
            add_song(songs)
        elif choice == 'c':
            complete_song(songs)
        elif choice == 'q':
            save_songs(filename, songs)
            print(f"{len(songs)} songs saved to {filename}")
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()

