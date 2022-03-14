from pypresence import Presence
import time
from PyQt5.QtWidgets import QLabel

def pomodori(pomodoro_time,break_time,total_tomatoes):
    pomodoro_time_int=pomodoro_time*60
    break_time_int=break_time*60
    start = int(time.time())
    client_id = "952663821946880081" 
    RPC = Presence(client_id=client_id)
    RPC.connect()


    for i in range(total_tomatoes):
        RPC.update(large_image="toomato", large_text="Working for "+str(pomodoro_time)+" minutes",start=start,small_image="color", small_text=str(i+1)+" out of "+str(total_tomatoes)+" pomos")
        time.sleep(pomodoro_time_int) 
        RPC.update(large_image="sleep", large_text="Resting for "+str(break_time)+" minutes",start=start,small_image="color", small_text=str(i+1)+" out of "+str(total_tomatoes)+" pomos")
        time.sleep(break_time_int)
    
    RPC.update(large_image="toomato", large_text="Session finished!",start=start,small_image="color", small_text="Session finished!")
    sleep(60)
    exit(0)

num1=int(input("How long will the study parts be? (minutes)"))
num2=int(input("How long will the breaks be? (minutes)"))
num3=int(input("How many separate sessions will you have this tomato?"))
useless=input("Press ENTER when you are ready to start.")
pomodori(num1,num2,num3)
