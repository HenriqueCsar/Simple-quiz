import json
from tkinter import *
from tkinter import filedialog, messagebox

####Gui
class program:
    def __init__(self):
        super().__init__()

        self.app = Tk()
        self.app.title('Simple Quiz')
        self.app.geometry('230x100')
        self.app.iconbitmap('icone.ico')
        self.app.configure(bg='#292f3b')
        self.app.resizable(height=0, width=0)

        self.create_question = Button(self.app, text='Create question', fg='gray', bg='#292f3a',font=' 20', command=self.gui_question)
        self.create_question.place(x="20", y="10")

        self.run_question = Button(self.app, text='Run question', fg='gray', bg='#292f3a',font=' 20', command=self.run_question)
        self.run_question.place(x="20", y="50")

        self.app.mainloop()




####Gui question
    def gui_question(self):
        self.app.destroy()
        self.window_gui_question = Tk()
        self.window_gui_question.title('Gui Question')
        self.window_gui_question.geometry('700x400')
        self.window_gui_question.resizable(height=0, width=0)
        self.window_gui_question.iconbitmap('icone.ico')
        self.window_gui_question.configure(bg='#292f3b')
        self.window_gui_question.mainloop()





#####Run question
    def run_question(self):
        import pygame
        try:
            self.file = filedialog.askopenfilename(initialdir = "/", title='Selecione o Arquivo.quiz', filetypes=[(("Quiz files","*"))])
        except:
            messagebox.showerror(title="Erro", message="Erro ao abrir o quiz")

        if(self.file):
            self.app.destroy()
            self.window_run_question = Tk()
            self.window_run_question.title('Quiz')
            self.window_run_question.configure(bg='#292f3b')
            self.window_run_question.iconbitmap('icone.ico')
            self.window_run_question.geometry('700x400')
            pygame.mixer.init(1100)
            pygame.mixer.music.load("music.mp3")
            pygame.mixer.music.play(loops=0)
            self.window_run_question.resizable(height=0, width=0)


            ###Buttons from run_question

            self.button_run_question_






            self.window_run_question.mainloop()






####Questions

    def questions(self):
        self.data = {}
        self.data[f'{n_after_vef}'] = []
        self.data[f'{n_after_vef}'].append({
            'question': f'{_question}',
            'answer': f'{_answer}'
            })

        with open('data.quiz', 'w') as out:
            json.dump(self.data, out)


#####Checker
    def checker(self):
        pass

program()
