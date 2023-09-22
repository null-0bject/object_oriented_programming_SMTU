import csv
import tkinter as tk
import tkinter.ttk as ttk


def add_old_data():
    with open('expenses.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            tree.insert('', tk.END, values=row)


def sum_calculations(sum_label):
    sum_of_all = 0
    with open('expenses.csv') as f:
        sum_reader = csv.reader(f)
        if list[csv.reader(f,delimiter=',')]:
            for row in sum_reader:
                sum_of_all += int(row[3])
    sum_label.configure(text=f'Общая сумма расходов: {sum_of_all}')


def create_input_frame(label_name):
    frame = ttk.Frame(borderwidth=1, padding=[8, 10])

    label = ttk.Label(frame, text=label_name, font=('Ubuntu', 14))
    label.pack(anchor='nw', side='left', pady=5, padx=50)

    entry = ttk.Entry(frame, width=50)
    entry.pack(anchor='nw', side='right', fill='both', pady=5, padx=30)

    frame.pack(fill='x', anchor='nw', padx=5, pady=5)

    return entry


def validate_datas(data, category, money_sum):
    if not(data and category and money_sum):
        error_msg('Ошибка при вводе данных, перепроверьте данные!')
        return False
    elif len(data) != 10:
        error_msg('Неправильно введена дата')
        return False
    elif not(data[0:2].isdigit() and data[2] == '.' and data[3:5].isdigit()
             and data[5] == '.' and data[6:10].isdigit()):
        error_msg('Неправильно введена дата')
        return False
    elif not(category.isalpha()):
        error_msg('Неправильно введена категория')
        return False
    elif not(money_sum.isdigit()):
        error_msg('Неправильно введена сумма')
        return False
    return True


def error_msg(errtext):
    error_window = tk.Toplevel()

    error_window.title('ERROR validating data')
    errortext = ttk.Label(error_window, text=errtext,
                          font=('Ubuntu', 20),
                          foreground='Black', padding=[15, 40])
    errortext.pack(anchor='n')
    error_window.grab_set()


def clear_all():
   for item in tree.get_children():
      tree.delete(item)


def csv_add_data():
    data = data_entry.get()
    category = category_entry.get()
    money_sum = sum_entry.get()
    if not(validate_datas(data, category, money_sum)):
        return 0
    with open('expenses.csv', 'r') as f:
        row_count = sum(1 for row in f)
    with open('expenses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([row_count, data, category, money_sum])
    tree.insert('', tk.END, values=[row_count, data, category, money_sum])
    sum_calculations(sum_label)


def delete_item():
    selected_items = tree.selection()
    with open('expenses.csv', 'r') as f:
        datas = list(csv.reader(f, delimiter=','))
    print(tree.item(selected_items[0]))
    values = (tree.item(selected_items[0]))['values']

    datas.pop(int(values[0]))

    for selected_item in selected_items:
        tree.delete(selected_item)

    for i in range(len(datas)):
        datas[i][0] = f'{i}'

    with open('expenses.csv', 'w', newline='') as f:
        csvwriter = csv.writer(f)
        for row in datas:
            csvwriter.writerow(row)
    sum_calculations(sum_label=sum_label)
    clear_all()
    add_old_data()


root = tk.Tk()
root.geometry('850x600')
root.title('Учёт расходов')

data_entry = create_input_frame('Дата(ДД.ММ.ГГГГ)')
category_entry = create_input_frame('Категория')
sum_entry = create_input_frame('Сумма')

button_style = ttk.Style()
button_style.configure('My.TButton', font=('Ubuntu', 10))
add_button = ttk.Button(text='Добавить', width=20, style='My.TButton', command=csv_add_data)
add_button.pack(pady=10)

columns = ('#0', '#1', '#2','#3')
ysb = ttk.Scrollbar(root, orient='vertical')

tree = ttk.Treeview(root, columns=columns, show='headings', displaycolumns=columns[1:], yscrollcommand=ysb.set)
tree.heading('#0', text='Позиция')
tree.heading('#1', text='Дата')
tree.heading('#2', text='Категория')
tree.heading('#3', text='Сумма')

ysb.pack(side='right', anchor='e')

add_old_data()

tree.pack()
ysb.config(command=tree.yview)

delete_button = ttk.Button(text='Удалить',width=20,command=delete_item)
delete_button.pack(pady=30)

sum_label = ttk.Label(text=f'Общая сумма расходов: 0')
sum_label.pack(side='bottom')
sum_calculations(sum_label)

root.mainloop()