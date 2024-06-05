from pytube import YouTube
import os
import subprocess

def download_audio(url, output_path, filename):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_file_path = os.path.join(output_path, filename)
        audio_stream.download(output_path=output_path, filename=filename)
        print("Audio downloaded successfully! Saved as:", audio_file_path)

        # Convert to desired bitrate
        input_file_path = os.path.join(output_path, filename)
        output_file_path = os.path.join(output_path, filename.split('.')[0] + "_192kbps.mp3")
        subprocess.run(['ffmpeg', '-i', input_file_path, '-b:a', '192k', output_file_path])

        print("Audio converted to 192kbps successfully! Saved as:", output_file_path)
        os.remove(input_file_path)  # Remove the original file
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    url = "<Youtube Link>"
    output_path = "<File location>"
    filename = "audio_file.m4a"
    download_audio(url, output_path, filename)
