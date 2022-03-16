import tkinter as tk
from pypresence import Presence
import time

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
    time.sleep(60)
    exit(0)

def show_entry_fields():
    a1=int(e1.get())
    a2=int(e2.get())
    a3=int(e3.get())
    master.withdraw()
    pomodori(a1,a2,a3)


master = tk.Tk()
master.title("Pomodoro")
#master.iconbitmap('tomato.ico')
tk.Label(master,text="Length of work session(min):").grid(row=0)
tk.Label(master, text="Length of break(min):").grid(row=1)
tk.Label(master,text="Number of sessions:").grid(row=2)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
tk.Button(master, text='Quit',command=master.destroy).grid(row=3, column=0,sticky=tk.W, pady=4)
tk.Button(master,text='START!',command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
