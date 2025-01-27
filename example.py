from time import sleep as wait
import audiobox

# Generate example files
audiobox.generate_example_files()

# Play sound effect in a separate thread
audiobox.sfx(filename="example_sfx", times=1, volume=0.5)
wait(audiobox.get_audio_length(filename="example_sfx"))

# Play music with looping enabled
audiobox.play_music(filename="example_music", stop_other=True, loop=True)

# Wait for the duration of the music
wait(audiobox.get_audio_length(filename="example_music"))

# Manage playlist: Add, Remove, Clear
audiobox.add_to_playlist(filename="example_music")
audiobox.play_playlist()
audiobox.remove_from_playlist(filename="example_music")
audiobox.clear_playlist()