import os
import subprocess
<<<<<<< HEAD
=======
import sys

def LINENO():
    return currentframe().f_back.f_lineno

>>>>>>> a3f9920 (Initial commit)
def ffmpegEncode(folder_path, file_name, action):
    if action == 0: #不轉檔
        return
    elif action == 1: #GPU轉檔
        os.chdir(folder_path)
        try:
<<<<<<< HEAD
            subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4','-c:v', 'h264_nvenc', '-b:v', '10000K',
                                '-threads', '5', f'f_{file_name}.mp4'])
            os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
            os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
            print("轉檔成功!")
        
        except:
            print("轉檔失敗!")
    elif action == 2: #CPU轉檔
        os.chdir(folder_path)
        try:
            subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4', '-c:v', 'libx264', '-b:v', '3M',
                            '-threads', '5', '-preset', 'superfast', f'f_{file_name}.mp4'])
            os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
            os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
            print("轉檔成功!")
        
        except:
            print("轉檔失敗!")
=======
            subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4','-c:v', 'h264_videotoolbox', '-b:v', '10M',
                                '-threads', '5', f'f_{file_name}.mp4'])
        except:
            try:
                subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4','-c:v', 'h264_nvenc', '-b:v', '10M',
                                    '-threads', '5', f'f_{file_name}.mp4'])
            except:
                print(f'！[{LINENO()}] ffmpeg convertion failed with GPU libraries: h264_videotoolbox and h264_nvenc.')
                print('Fallback to convert with CPU library: libx264.')
                try:
                    subprocess.call(['ffmpeg', '-i', f'{file_name}.mp4', '-c:v', 'libx264', '-b:v', '3M',
                                    '-threads', '5', '-preset', 'superfast', f'f_{file_name}.mp4'])
                except:
                    sys.exit('轉檔失敗!')
        os.remove(os.path.join(folder_path, f'{file_name}.mp4'))
        os.rename(os.path.join(folder_path, f'f_{file_name}.mp4'), os.path.join(folder_path, f'{file_name}.mp4'))
        print("轉檔成功!")
>>>>>>> a3f9920 (Initial commit)
    else:
        return
