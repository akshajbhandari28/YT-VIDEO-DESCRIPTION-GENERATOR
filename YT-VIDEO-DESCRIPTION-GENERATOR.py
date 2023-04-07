import tkinter as tk
import openai
import pyperclip as pc

root = tk.Tk()

root.geometry('1024x700')
root.title('VIDEO DESCRIPTION GENERATOR')


label = tk.Label(root, text="WELCOME TO VIDEO DESCRIPTION GENERATOR!", font=('Arial', 30))
label.pack(padx=20, pady=20)


def Myclick():
    maybe_prompt = e.get()
    actual_prompt = maybe_prompt.replace('Please Enter Video Name: ', '')
    openai.api_key = "OPEN-AI-API-KEY"
    model_engine = "text-davinci-003"
    prompt = f"give me a possible description of a video titled, {actual_prompt}"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    global response
    response = completion.choices[0].text
    text = tk.Text(root, width=75, height=10)
    text.place(x=205, y=250)
    text.insert('1.0', f'{response}')


button = tk.Button(root, text='GENERATE VIDEO DESCRIPTION', font=('Arial', 20),command=Myclick)
button.place(x=275, y=150)


e = tk.Entry(root, width=100, borderwidth=7)
e.pack()
e.insert(0, 'Please Enter Video Name: ')


def CopyToClipboard():
    hastags = response
    pc.copy(hastags)
    completed_label = tk.Label(root, text='VIDEO DESCRIPTION SUCCESSFULLY COPIED TO CLIPBOARD!', font=('Arial', 25))
    completed_label.place(x=5, y=540)


button = tk.Button(root, text='COPY VIDEO DESCRIPTION TO CLIPBOARD', font=('Arial', 20), command=CopyToClipboard)
button.place(x=210, y=450)


def exit():
    root.destroy()


exit_button = tk.Button(root, text='EXIT', font=('Arial', 20), command=exit)
exit_button.place(x=475, y=600)


root.mainloop()
