import customtkinter
import mec

customtkinter.set_appearance_mode("light")

class Interface():
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Mecânica Deon")
        self.app.geometry("500x370")

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure((0, 1), weight=1)

        #Comando do botão
        def capturar_Valor():
            texto = self.textbox.get("0.0", "end")
            mec.calcular_valor(texto, self.resultado)

        def capturar_material():
            material = self.textbox2.get("0.0", "end")
            mec.calcular_material(material, self.resultado2)

        #Criando os widgets 1

        #Label
        self.label = customtkinter.CTkLabel(self.app, text="Mecânica Deon", font=("Arial", 20, "bold"), text_color='#214697')

        self.resultado = customtkinter.CTkLabel(self.app, text="", font=("Arial", 20), text_color='#214697')
        self.resultado2 = customtkinter.CTkLabel(self.app, text="", font=("Arial", 20), text_color='#214697')


        self.pedro = customtkinter.CTkLabel(self.app, text="By: Pedro Leocir - Vers 2.1", font=("Arial", 14), text_color='#214697')

        #Text area
        self.textbox = customtkinter.CTkTextbox(self.app, text_color='#214697', font=("Arial", 18), fg_color='#dcdcdc')

        #Buttons
        self.button = customtkinter.CTkButton(self.app, text='Calcular horas', font=("Arial", 15), fg_color=("#214697"), hover_color='#131c23', command=capturar_Valor)

        #Criando os widgets 2

        #Text area
        self.textbox2 = customtkinter.CTkTextbox(self.app, text_color='#214697', font=("Arial", 18), fg_color='#dcdcdc')

         #Buttons
        self.button2 = customtkinter.CTkButton(self.app, text='Calcular material', font=("Arial", 15), fg_color=("#214697"), hover_color='#131c23', command=capturar_material)

        #Grid
        self.label.grid(row=0, column=0, pady=10, sticky='ew', padx=20, columnspan=2)

        self.textbox.grid(row=1, column=0, sticky='ew', padx=10)
        self.textbox2.grid(row=1, column=1, sticky='ew', padx=10)

        self.button.grid(row=2, column=0, sticky='ew', padx=20, pady=10)
        self.button2.grid(row=2, column=1, sticky='ew', padx=20, pady=10)

        self.resultado.grid(row=3, column=0)
        self.resultado2.grid(row=3, column=1)

        self.pedro.grid(row=4, column=0, columnspan=2)

if __name__ == "__main__":
    interface = Interface()
    interface.app.mainloop()
