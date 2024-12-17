from abc import ABC, abstractmethod

# Target interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, filename: str):
        pass

# Adaptee interface
class AdvancedMediaPlayer(ABC):
    @abstractmethod
    def play_vlc(self, filename: str):
        pass
    
    @abstractmethod
    def play_mp4(self, filename: str):
        pass

# Concrete Adaptee implementations
class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, filename: str):
        print(f"Playing vlc file: {filename}")
    
    def play_mp4(self, filename: str):
        # Do nothing
        pass

class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, filename: str):
        # Do nothing
        pass
    
    def play_mp4(self, filename: str):
        print(f"Playing mp4 file: {filename}")

# Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        if audio_type.lower() == "vlc":
            self.advanced_media_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_media_player = Mp4Player()
    
    def play(self, audio_type: str, filename: str):
        if audio_type.lower() == "vlc":
            self.advanced_media_player.play_vlc(filename)
        elif audio_type.lower() == "mp4":
            self.advanced_media_player.play_mp4(filename)

# Concrete implementation of the target interface
class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, filename: str):
        # Built-in support for mp3 files
        if audio_type.lower() == "mp3":
            print(f"Playing mp3 file: {filename}")
        
        # MediaAdapter provides support for other formats
        elif audio_type.lower() in ["vlc", "mp4"]:
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, filename)
        
        else:
            print(f"Invalid media type: {audio_type}")

# Client code
def main():
    audio_player = AudioPlayer()
    
    # Test with different formats
    audio_player.play("mp3", "song.mp3")
    audio_player.play("mp4", "movie.mp4")
    audio_player.play("vlc", "video.vlc")
    audio_player.play("avi", "video.avi")  # Invalid format

if __name__ == "__main__":
    main() 