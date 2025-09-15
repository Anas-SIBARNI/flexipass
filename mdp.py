import string
import customtkinter
from tkinter import *
import tkinter.messagebox
import pyperclip
import random

#Apparence - Dark Mode -> Moderne UI
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_widget_scaling(1)

#Fenêtre - "Window" Principale
window = customtkinter.CTk()
window.title("Générateur - Mot de Passe")
window.geometry(f"{565}x{370}")
#window.iconbitmap(...)

# configuration grille (Frame(2x2))
window.grid_columnconfigure((1), weight=1)
window.grid_columnconfigure((2), weight=1)
window.grid_rowconfigure((1), weight=0)
window.grid_rowconfigure((2), weight=1)

# configuration Frame Secondaire
frame_main = customtkinter.CTkFrame(master=window, corner_radius=0)
frame_main.grid(row=1, column=1, pady=2, padx=2, sticky="n")
frame_main.grid_rowconfigure(7, weight=1)
frame_main.grid_columnconfigure((1,2), weight=1)
frame_settings = customtkinter.CTkFrame(master=window, corner_radius=0)
frame_settings.grid(row=1, column=2, pady=2, padx=2, sticky="w")
frame_settings.grid_rowconfigure(4, weight=1)
frame_settings.grid_columnconfigure((1,2), weight=1)


#Fonction - Toute les fonctions du programme

#Fonction - Générer un mot de Passe
def generateur():
    """
    Cette fonction génère un mot de passe solide d'une taille de 16 caractères
    >>> generateur()
    (pas de return) : génère un mot de passe
    """
    liste = ""

    min="abcdefghijklmnopqrstuvwxyz"
    majs="ABCDEFGHIJKLMONPQRSTUVWXYZ"
    chif="0123456789"
    carac="#$%&'()*+,-/?[]"
    ponc="!.?;:"
    
    if  switch_min.get()== "Avec":
        liste = liste + min
    if  switch_majs.get()== "Avec":
        liste = liste + majs
    if  switch_chif.get() == "Avec":
        liste = liste + chif
    if  switch_carac.get() == "Avec":
        liste = liste + carac
    if  switch_ponc.get() == "Avec":
        liste = liste + ponc
    mdp = "".join(random.choices(liste,k=int(enter_len.get())))  
    enter_pwd.delete(0, END)
    enter_pwd.insert(0, mdp)

#Fonction - Vérrification de la dificulté du Mot de Passe (?)
def verif()-> int :
    """
    Cette fonction la Verrification et Aprobation de la veracité de la dificulté du Mot de Passe
    >>> verif()
    un nombre (=le score)
    """
    str_maj = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    str_min = "abcdefghijklmnopqrstuvwxyz"
    str_punct = "!.?;:"
    str_caract ="#$%&'()*+,-/?[]"
    str_digit = "0123456789"

    score = 0
    mdp = enter_pwd.get()
    score = score + len(mdp)
    multiplicateur = 0

    for str_maj in mdp :
        if str_maj in mdp : 
            score = score + 2
    for str_min in mdp :
        if str_min in mdp: 
            score = score + 3
    for str_punct in mdp : 
        if str_punct in mdp : 
            score = score + 7
    for str_caract in mdp :
        if str_caract in mdp : 
            score = score + 4
    for str_digit in mdp :
        if str_digit in mdp : 
            score = score + 8
    
    if  switch_min.get()== "Avec":
        multiplicateur = multiplicateur + 1 
    if  switch_majs.get()== "Avec":
        multiplicateur = multiplicateur + 1 
    if  switch_chif.get() == "Avec":
        multiplicateur = multiplicateur + 1 
    if  switch_carac.get() == "Avec":
        multiplicateur = multiplicateur + 1 
    if  switch_ponc.get() == "Avec":
        multiplicateur = multiplicateur + 1 
    
    score = score * multiplicateur
    score = progressbar_1.set


#Fonction - Copie du Mot de Passe dans la Presse-Papier
def copier():
  """
  Cette fonction sert à copier le mot de passe généré par la fonction generateur
  >>> copier()
  (pas de return) copie le mot de passe généré
  """
  pyperclip.copy(enter_pwd.get())

#Fonction - Enregistrement Du Mot de Passe dans un Fichier dédié
def enregistrer()-> None : 
    """
    Cette fonction sert à enregister le Mot de Passe dans un Fichier dédié
    >>> enregistrer()
    (pas de return) : enregistre le mdp dans le fichier txt
    """
    fichier = "mots_de_passe.txt"
    fich = open(fichier,'a')
    fich.write(enter_site.get() + " : " + enter_pwd.get() + "\n")
    fich.close()

#Fonction - Retour du Nombre de Caractère du Mot de Passe à Générer
def slider_event(value):
    """
    Cette fonction sert à retourner le Nombre de Caractère du (Taille) Mot de Passe à Générer
    >>> slider_event(14)
    14
    """
    return_pwd.delete(0, END)
    return_pwd.insert(0, int(enter_len.get()))
    return value

#Fonction - Changement de l'Apparence
def change_appearance_mode_event(new_appearance_mode: str):
    """
    Cette fonction sert à changer l'apparence du générateur de mot de passe
    >>> change_appearance_mode_event("Dark")
    (pas de return) change l'apparence en sombre
    """
    customtkinter.set_appearance_mode(new_appearance_mode)

#Fonction - Changement de l'Echelle
def change_scaling_event(new_scaling: str):
    """
    cette fonction sert à afficher la difficulté du mot de passe (plus  la jauge est remplie plus le mot de passe est sécurisé)
    >>> change_scaling_event("100")
    (pas de return) : initialise la taille à l'échelle 1 sur 1 
    """
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)


# Switch - Paramtère Fonction Generateur
# Switch - Paramtère 'Majuscule' Fonction Generateur
switch_majs = customtkinter.StringVar(value="Avec")
switch_majs = customtkinter.CTkSwitch(master=frame_settings, text="Majuscules", progress_color="#537895", variable=switch_majs, onvalue="Avec", offvalue="Sans")
switch_majs.grid(row=1, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")

# Switch - Paramtère 'Minuscule' Fonction Generateur
switch_min = customtkinter.StringVar(value="Avec")
switch_min = customtkinter.CTkSwitch(master=frame_settings, text="Minuscules", progress_color="#537895", variable=switch_min, onvalue="Avec", offvalue="Sans")
switch_min.grid(row=2, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")

# Switch - Paramtère 'Chiffre' Fonction Generateur
switch_chif = customtkinter.StringVar(value="Avec")
switch_chif = customtkinter.CTkSwitch(master=frame_settings, text="Chiffres", progress_color="#537895", variable=switch_chif, onvalue="Avec", offvalue="Sans")
switch_chif.grid(row=3, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")

# Switch - Paramtère 'Caractère' Fonction Generateur
switch_carac = customtkinter.StringVar(value="Avec")
switch_carac = customtkinter.CTkSwitch(master=frame_settings, text="Caractères speciaux", progress_color="#537895", variable=switch_carac, onvalue="Avec", offvalue="Sans")
switch_carac.grid(row=4, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")

# Switch - Paramtère 'Ponctuation' Fonction Generateur
switch_ponc = customtkinter.StringVar(value="Avec")
switch_ponc = customtkinter.CTkSwitch(master=frame_settings, text="Simple Ponctuation", progress_color="#537895", variable=switch_ponc, onvalue="Avec", offvalue="Sans")
switch_ponc.grid(row=5, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")


#Champ - Champ de Text (Entry)
#Champ - Generation du Mot de Passe
enter_pwd = customtkinter.CTkEntry(master=frame_main, width=240, placeholder_text="Mot de passe généré")
enter_pwd.grid(row=1, column=1, columnspan=2, pady=2, padx=2, sticky="w")

#Champ - (Taille) Nombre de Caractère dans le Mot de Passe
return_pwd = customtkinter.CTkEntry(master=frame_main, width=50, placeholder_text="Taille")
return_pwd.grid(row=1, column=2, pady=5, padx=2, sticky="e")
#Champ - Insertion du Nom du Service asocié au Mot de Passe
site = StringVar
enter_site =customtkinter.CTkEntry(master=frame_main, placeholder_text="Nom du srvice")
enter_site.grid(row=2, column=1, pady=2, padx=2)

#Slider - Barre Variable -> int(float)
#Slider - Retour du Nombre de Caractère du Mot de Passe à générer
enter_len = customtkinter.CTkSlider(master=frame_main, from_=4, to=32, fg_color="#537895", button_color="#537895", button_hover_color="#517fa4", number_of_steps=28, width=155, height=18, command=slider_event)
enter_len.grid(row=4, column=1, pady=1)


#Bouton - Execution des  Fonction Principale
#Bouton - Génération du Mot de Passe
generate_pwd_button = customtkinter.CTkButton(master=frame_main, text="Générer", fg_color="#537895", hover_color="#517fa4", command=generateur)
generate_pwd_button.grid(row=3, column=1, ipady=25, pady=5, padx=5)
#Bouton - Enregistrement du Mot de Passe dans un Fichier (TXT) dédié
save_pwd_button = customtkinter.CTkButton(master=frame_main, text="Enregistrer", fg_color="#537895", hover_color="#517fa4", command=enregistrer)
save_pwd_button.grid(row=2, column=2, ipady=5, pady=5, padx=5)
#Bouton - Copie du Mot de Passse dans le Press-Papier
generate_pwd_button = customtkinter.CTkButton(master=frame_main, text="Copier", fg_color="#537895", hover_color="#517fa4", command=copier)
generate_pwd_button.grid(row=3, column=2, ipady=25, pady=3, padx=5)
#Bouton - Changement du Mode d'apparence
button_appearance= customtkinter.CTkOptionMenu(master=frame_settings, values=["Dark", "light"], fg_color="#537895", button_color="#537895", button_hover_color="#517fa4", command=change_appearance_mode_event)
button_appearance.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")


#TextBox - Text de Desciption du Programme
textbox = customtkinter.CTkTextbox(master=window)
textbox.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")
textbox.insert("0.0", "Bienvenue sur le généreteur de mot de passe FlexiPass ! \nVous pouvez choisir si vous voulez des majuscules, minuscules, chiffres, caractères spéciaux ainsi que de la ponctuation pour améliorer la robustesse de votre mot de passe. \Le cuseur sert à modifier la taille de votre mot de passe. \nLe bouton copier sert à copier le mot de passe généré dans votre presse-papier. \n\nLe bouton enregistrer sert à enregistrer le  mot de passe généré dans un \nfichier text à côté du nom de service renseigné. \n\nVous pouvez aussi choisir l'apparence de FlexiPass dans l'onglet 'Option' (Sombre ou Clair).")
text = textbox.get("0.0", "end")  # prendre le texte du premier caractère au dernier
textbox.configure(state="disable")  # le text ne peut que être lu


#ProgressBar - Animation -> Verrification de la dificulté du Mot de Passe
progressbar_1 = customtkinter.CTkProgressBar(master = frame_main, indeterminate_speed=2, width=155, height=15, progress_color="#537895")
progressbar_1.configure(mode="indeterminnate")
progressbar_1.grid(row=4, column=2, padx=(20, 10), pady=(10, 10), sticky="ew")
progressbar_1.start()


#OptionMenu - Levier d'option
#OptionMenu - Levier d'option -> Echelle du menu
scaling_optionemenu = customtkinter.CTkOptionMenu(master=frame_settings, fg_color="#537895", button_color="#537895", button_hover_color="#517fa4", values=["80%", "90%", "100%", "110%", "120%"],command=change_scaling_event)
scaling_optionemenu.grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")
scaling_optionemenu.set("100%")

#OptionMenu - Levier d'option -> Apparence du menu
titre_generateur = customtkinter.CTkLabel(master = frame_main, text="FlexiPass", font=customtkinter.CTkFont(size=20, weight="bold"))
titre_generateur.grid(row=0, column=1, columnspan=2, pady=8, padx=2, sticky="nsew") 
titre_option = customtkinter.CTkLabel(master =
frame_settings, text="Options", font=customtkinter.CTkFont(size=20, weight="bold"))
titre_option.grid(row=0, column=1, columnspan=2, pady=5, padx=2, sticky="nsew")

window.mainloop()