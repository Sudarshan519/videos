import subprocess
import threading

def convert_video():
    try:
        input_file = 'Shingeki_no_Kyojin_S2_-_11.mkv'
        output_file = 'output.m3u8'
        
        # FFmpeg command to convert video (modify as needed)
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_file,
            '-c:v', 'h264',
            # '-c:a', 'aac',
            # '-scodec', 'webvtt',
           '-hls_time', '10', 
           '-hls_list_size', '0',
          '-hls_segment_filename', 'segment%d.ts',
            'index.m3u8'
        ]
        
        # Run FFmpeg command in a subprocess
        subprocess.run(ffmpeg_command, check=True)
        
        print(f'Video conversion complete: {output_file}')
    except Exception as e:
        print(f'Error during video conversion: {str(e)}')

# Create a thread for the conversion process
conversion_thread = threading.Thread(target=convert_video)

# Start the thread
conversion_thread.start()

# Optionally, you can join the thread to wait for it to finish
# conversion_thread.join()

# Continue with other tasks in your main program
print('Main program continues executing...')
