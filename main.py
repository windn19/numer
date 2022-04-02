from tkinter import Tk, Button, Label, Text, Frame, Entry, TOP, END
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror
import logging


def evalute():
    m = cobm_month.get().strip()
    d = cobm_day.get().strip()
    y = cobm_year.get().strip()
    if not m:
        showerror(title='Ошибка значения', message='Введено пустое значение месяца')
        cobm_month.focus_set()
    elif not d:
        showerror(title='Ошибка значения', message='Введено пустое значение дня')
        cobm_day.focus_set()
    elif not y:
        showerror(title='Ошибка значения', message='Введено пустое значение года')
        cobm_year.focus_set()
    else:
        d = m + d + y
        s = 0
        try:
            for ch in d:
                s += int(ch)
        except:
            log.exception('Error!')
        lbl_text['text'] = s
        log.debug('Сумма чисел - ' + s)
        s = str(s)
        while len(s) > 1:
            s1 = 0
            for ch in s:
                s1 += int(ch)
            s = str(s1)
        log.debug('Результат - ' + s)
        lbl_text1['text'] = s


def change_day():
    # log.info(f'{cobm_month.get()} {type(cobm_month.get())}')
    if cobm_month.get():
        m = int(cobm_month.get())
        if m == 2:
            cobm_day['values'] = list(range(1, 29))
        elif not m % 2:
            cobm_day['values'] = list(range(1, 31))
        else:
            cobm_day['values'] = list(range(1, 32))


log = logging.getLogger('Start')
log.setLevel(logging.DEBUG)
fh = logging.FileHandler('new.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)

window = Tk()
window.title('Numeric')
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = Text(window)
fr_btns = Frame(window)
# field = Entry(fr_btns, width=10)
btn_open = Button(fr_btns, text='Open', command=evalute)
lbl_text = Label(fr_btns, text='NN')
lbl_text1 = Label(fr_btns, text='NN1')

fr_comb = Frame(fr_btns)
lbl_month = Label(fr_comb, text='Месяц рождения:')
cobm_month = Combobox(fr_comb, values=list(range(1, 13)))
lbl_day = Label(fr_comb, text='День:')
cobm_day = Combobox(fr_comb, values=list(range(1, 32)), postcommand=change_day)
lbl_year = Label(fr_comb, text='Год:')
cobm_year = Combobox(fr_comb, values=list(range(1940, 2020)))

lbl_month.pack(side=TOP)
cobm_month.pack(side=TOP)
lbl_day.pack(side=TOP)
cobm_day.pack(side=TOP)
lbl_year.pack(side=TOP)
cobm_year.pack(side=TOP)

cobm_month.focus_set()
cobm_day.current(0)
cobm_month.current(0)
cobm_year.current(0)
# cobm_month.select_to('2')

cobm_month.bind('<Return>', func=lambda x: cobm_day.focus_set())
cobm_day.bind('<Return>', func=lambda x: cobm_year.focus_set())
cobm_year.bind('<Return>', func=lambda x: evalute())

# field.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
fr_btns.grid(row=0, column=0, sticky='ns')
btn_open.grid(row=2, column=0, sticky='ew', padx=5)
lbl_text.grid(row=3, column=0, sticky='ew', padx=5)
lbl_text1.grid(row=4, column=0, sticky='ew', padx=5)
fr_comb.grid(row=1, column=0, sticky='ew', padx=5)

txt_edit.grid(row=0, column=1, sticky='nsew')

btn_close = Button(window, text='Close', command=window.destroy)
btn_close.grid(row=1, column=1, sticky='e', padx=5)
window.bind('<Escape>', func=lambda x: window.destroy())
log.info('start')

window.mainloop()
