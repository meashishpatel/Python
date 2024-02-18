import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    con.commit()

def update_video(video_id, name, time):
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    con.commit()


def main():
    while True:
        print('\n Youtube manager app with DB')
        print('1. List Videos')
        print('2. Add Video')
        print('3. Update Video')
        print('4. Delete Video')
        print('5. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            add_video(name, time)
        elif choice == '3':
            video_id = input('Enter video id to update: ')
            name = input('Enter video name: ')
            time = input('Enter video time: ')
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input('Enter video id to delete: ')
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid choice! Try again.')

    con.close()



if __name__ == '__main__':
    main()