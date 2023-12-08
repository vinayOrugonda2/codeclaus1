import os
import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        self.playlist = []
        self.current_index = 0

        pygame.init()
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.playlistbox = tk.Listbox(self.master, selectmode=tk.SINGLE, bg="black", fg="white", selectbackground="gray")
        self.playlistbox.pack(pady=20)

        add_button = tk.Button(self.master, text="Add Song", command=self.add_song)
        add_button.pack(pady=10)

        play_button = tk.Button(self.master, text="Play", command=self.play_song)
        play_button.pack(pady=10)

        pause_button = tk.Button(self.master, text="Pause", command=self.pause_song)
        pause_button.pack(pady=10)

        stop_button = tk.Button(self.master, text="Stop", command=self.stop_song)
        stop_button.pack(pady=10)

        next_button = tk.Button(self.master, text="Next", command=self.next_song)
        next_button.pack(pady=10)

        prev_button = tk.Button(self.master, text="Previous", command=self.prev_song)
        prev_button.pack(pady=10)

    def add_song(self):
        song = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select A Song", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        if song:
            self.playlist.append(song)
            self.playlistbox.insert(tk.END, os.path.basename(song))

    def play_song(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_song()

    def prev_song(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_song()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
