import customtkinter
from mec import Mec

customtkinter.set_appearance_mode("light")

class Interface():
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.title("Mecânica Deon")
        self.app.geometry("600x400")
        self.app.resizable(False, False)

        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure((0, 1), weight=1)

        #Comando do botão
        def capturar_Valor():
            texto = self.textbox.get("0.0", "end")
            
            if mec_instance.STATUS_BOTAO == 2:
                mec_instance.calcular_valor(texto, self.resultado)
            elif mec_instance.STATUS_BOTAO == 3:
                mec_instance.somar_horas(texto, self.resultado)
            else:
                self.resultado.configure(text="Selecione uma opções!")

        def capturar_material():
            material = self.textbox2.get("0.0", "end")

            if mec_instance.STATUS_BOTAO == 2:
                mec_instance.calcular_material(material, self.resultado2)
            elif mec_instance.STATUS_BOTAO == 3:
                mec_instance.calcular_chapas(material, self.resultado2)
            else:
                self.resultado2.configure(text="Selecione uma opções!")

        #Checkbox command
        def checkbox_event_calcular():
            status = self.check_var_calcular.get()
            status_check2 = self.check_var_soma.get()
            mec_instance.verificar_status(status, status_check2, self.checkbox_calcular, self.checkbox_soma)

        #Checkbox command
        def checkbox_event_calcular_materiais():
            status = self.check_var_materiais.get()
            status_check2 = self.check_var_chapas.get()
            mec_instance.verificar_status(status, status_check2, self.checkbox_calcular_materiais, self.checkbox_calcular_chapas)

        #Criando os widgets 1

        #Label
        self.label = customtkinter.CTkLabel(self.app, text="Mecânica Deon", font=("Arial", 20, "bold"), text_color='#214697')

        self.resultado = customtkinter.CTkLabel(self.app, text="", font=("Arial", 20), text_color='#214697')
        self.resultado2 = customtkinter.CTkLabel(self.app, text="", font=("Arial", 20), text_color='#214697')


        self.pedro = customtkinter.CTkLabel(self.app, text="By: Pedro Leocir - Vers 2.3", font=("Arial", 14), text_color='#214697')

        #Text area
        self.textbox = customtkinter.CTkTextbox(self.app, text_color='#214697', font=("Arial", 18), fg_color='#dcdcdc')

        #Buttons
        self.button = customtkinter.CTkButton(self.app, text='Calcular', font=("Arial", 15), fg_color=("#214697"), hover_color='#131c23', command=capturar_Valor)

        #CheckBox das horas
        self.check_var_calcular = customtkinter.StringVar(value="off")
        self.checkbox_calcular = customtkinter.CTkCheckBox(self.app, text="Calcular horas", command=checkbox_event_calcular,
                                             variable=self.check_var_calcular, onvalue="on", offvalue="off",
                                             fg_color='#214697', border_color='#214697')
        #CheckBox das somas das horas
        self.check_var_soma = customtkinter.StringVar(value="off")
        self.checkbox_soma = customtkinter.CTkCheckBox(self.app, text="Somar horas", command=checkbox_event_calcular,
                                             variable=self.check_var_soma, onvalue="on", offvalue="off",
                                             fg_color='#214697', border_color='#214697')

        #Criando os widgets 2

        #Text area
        self.textbox2 = customtkinter.CTkTextbox(self.app, text_color='#214697', font=("Arial", 18), fg_color='#dcdcdc')

         #Buttons
        self.button2 = customtkinter.CTkButton(self.app, text='Calcular material', font=("Arial", 15), fg_color=("#214697"), hover_color='#131c23', command=capturar_material)

        #CheckBox dos materiais
        self.check_var_materiais = customtkinter.StringVar(value="off")
        self.checkbox_calcular_materiais = customtkinter.CTkCheckBox(self.app, text="Calcular materiais", command=checkbox_event_calcular_materiais,
                                             variable=self.check_var_materiais, onvalue="on", offvalue="off",
                                             fg_color='#214697', border_color='#214697')
        #CheckBox das chapas
        self.check_var_chapas = customtkinter.StringVar(value="off")
        self.checkbox_calcular_chapas = customtkinter.CTkCheckBox(self.app, text="Calcular chapas", command=checkbox_event_calcular_materiais,
                                             variable=self.check_var_chapas, onvalue="on", offvalue="off",
                                             fg_color='#214697', border_color='#214697')


        #Grid
        self.label.grid(row=0, column=0, pady=10, sticky='ew', padx=20, columnspan=2)

        self.checkbox_calcular.grid(row=1, column=0, sticky='we', padx=10, pady=10)
        self.checkbox_soma.grid(row=1, column=0, sticky='ne', padx=10, pady=10)
        self.checkbox_calcular_materiais.grid(row=1, column=1, sticky='we', padx=10, pady=10)
        self.checkbox_calcular_chapas.grid(row=1, column=1, sticky='ne', padx=10, pady=10)

        self.textbox.grid(row=2, column=0, sticky='ew', padx=10)
        self.textbox2.grid(row=2, column=1, sticky='ew', padx=10)

        self.button.grid(row=3, column=0, sticky='ew', padx=20, pady=10)
        self.button2.grid(row=3, column=1, sticky='ew', padx=20, pady=10)

        self.resultado.grid(row=4, column=0)
        self.resultado2.grid(row=4, column=1)

        self.pedro.grid(row=5, column=0, columnspan=2)

if __name__ == "__main__":
    interface = Interface()
    mec_instance = Mec()
    interface.app.mainloop()
