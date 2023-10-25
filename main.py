import customtkinter
import mec

customtkinter.set_appearance_mode("light")

class Interface():
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Mecânica Deon")
        self.app.geometry("400x370")

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=1)

        #Comando do botão
        def capturar_Valor():
            texto = self.textbox.get("0.0", "end")
            mec.calcular_valor(texto, self.resultado)

        #Criando os widgets

        #Label
        self.label = customtkinter.CTkLabel(self.app, text="Mecânica Deon", font=("Arial", 20, "bold"), text_color='#214697')
        self.resultado = customtkinter.CTkLabel(self.app, text="", font=("Arial", 20), text_color='#214697')
        self.pedro = customtkinter.CTkLabel(self.app, text="By: Pedro Leocir - Vers 2.0", font=("Arial", 12), text_color='#214697')

        #Text area
        self.textbox = customtkinter.CTkTextbox(self.app, text_color='#214697', font=("Arial", 18), fg_color='#E6E6FA')

        #Buttons
        self.button = customtkinter.CTkButton(self.app, text='Calcular horas', font=("Arial", 15), fg_color=("#214697"), hover_color='#131c23', command=capturar_Valor)

        #Grid
        self.label.grid(row=0, column=0, pady=10, sticky='we', padx=20)
        self.textbox.grid(row=1, column=0, sticky='we', padx=20)
        self.button.grid(row=2, column=0, sticky='we', padx=20, pady=10)
        self.resultado.grid(row=3, column=0)
        self.pedro.grid(row=4, column=0)

if __name__ == "__main__":
    interface = Interface()
    interface.app.mainloop()