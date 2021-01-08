import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeat = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text='00:00')
	break_label.config(text='')
	check_mark.config(text='')
	global repeat
	repeat = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_start():
	global repeat
	repeat += 1
	if repeat == 1 or repeat == 3 or repeat == 5 or repeat == 7:
		counter(WORK_MIN * 60)
	elif repeat == 2 or repeat == 4 or repeat == 6:
		break_label.config(text='BREAK', fg=RED)
		counter(SHORT_BREAK_MIN * 60)
	elif repeat == 8:
		break_label.config(text='BREAK', fg='black')
		counter(LONG_BREAK_MIN * 60)
	else:
		repeat = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(count):
	minutes = math.floor(count / 60)
	seconds = count % 60
	if 0 <= seconds < 10:
		seconds = f'0{seconds}'
	canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
	if count > 0:
		global timer
		timer = window.after(1000, counter, count - 1)
	else:
		timer_start()
		global repeat
		if repeat in [3, 5, 7]:
			check_mark.config(text='✔')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Принцип "Помидоро"')
window.config(padx=100, pady=50, bg=GREEN)

# Image adding
canvas = tkinter.Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
image = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 115, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=2, column=2)

# Break Label
break_label = tkinter.Label()
break_label.configure(bg=GREEN, font=(FONT_NAME, 20, 'bold'), highlightthickness=0)
break_label.grid(column=2, row=0)

# Start Button
start_button = tkinter.Button()
start_button.config(text='Start', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=timer_start)
start_button.grid(row=3, column=1)

# Reset Button
reset_button = tkinter.Button()
reset_button.config(text='Reset', font=(FONT_NAME, 10, 'bold'), highlightthickness=0, command=timer_reset)
reset_button.grid(row=3, column=3)

# Check Mark
check_mark = tkinter.Label()
check_mark.config(bg=GREEN, fg=RED, font=(FONT_NAME, 20, 'bold'))
check_mark.grid(row=4, column=2)

window.mainloop()
