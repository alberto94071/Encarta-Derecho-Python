import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
from datetime import datetime

# Configuración Inicial de Diseño
ctk.set_appearance_mode("Dark")  # Modo: "System" (estándar), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Tema: "blue" (estándar), "green", "dark-blue"

# =================================================================
# --- 1. BASES DE DATOS (Mismos datos, nueva presentación) ---
# =================================================================

MODULOS = [
    {
        "titulo": "Módulo 1: Introducción al Derecho",
        "temas": ["1.1 Origen y Definición", "1.2 Normas Jurídicas vs Morales", "1.3 Fuentes del Derecho", "1.4 Jerarquía Normativa"]
    },
    {
        "titulo": "Módulo 2: Derecho Constitucional",
        "temas": ["2.1 ¿Qué es la Constitución?", "2.2 Derechos Humanos", "2.3 Organización del Estado", "2.4 Corte de Constitucionalidad"]
    }
]

BASE_DE_DATOS_CONTENIDO = {
    "1.1 Origen y Definición": "La palabra Derecho proviene del vocablo latino directum...\n\n(Contenido resumido para demo visual modernizada)...",
    "1.2 Normas Jurídicas vs Morales": "Diferencia entre normas coercibles e incoercibles...",
    "1.3 Fuentes del Derecho": "Fuentes Reales, Históricas y Formales...",
    "1.4 Jerarquía Normativa": "La Pirámide de Kelsen establece la jerarquía de las leyes...",
    "2.1 ¿Qué es la Constitución?": "Ley suprema del Estado promulgada en 1985...",
    "2.2 Derechos Humanos": "Derechos inherentes a la persona (Vida, Libertad)...",
    "2.3 Organización del Estado": "Ejecutivo, Legislativo y Judicial...",
    "2.4 Corte de Constitucionalidad": "Máximo tribunal en materia constitucional..."
}

BASE_DE_DATOS_QUIZZES = {
    "1.1 Origen y Definición": [
        {"pregunta": "¿Qué significa 'directum'?", "opciones": ["Torcido", "Directo/Regla", "Talión"], "respuestaCorrecta": 1},
        {"pregunta": "¿Cuál NO es un fin del Derecho?", "opciones": ["Bien Común", "Justicia", "Venganza"], "respuestaCorrecta": 2},
    ],
    # ... (Puedes agregar el resto de preguntas aquí)
}

# Aquí definimos los nombres de archivo de las fotos
INFO_EQUIPO = {
    "proyecto": "Encarta Interactiva de Derecho",
    "universidad": "Universidad de San Carlos de Guatemala (USAC)",
    "catedra": "Fundamentos Jurídicos", 
    "desarrolladores": [
        {"nombre": "Tania Vásquez", "carnet": "201946345", "rol": "Desarrollador", "foto": "Tania.jpeg"},
        {"nombre": "Yenifer Fuentes", "carnet": "202145889", "rol": "Desarrollador", "foto": "Marisol.jpeg"},
        {"nombre": "Nazzary Rubio", "carnet": "202141942", "rol": "Desarrollador", "foto": "Nazzary.jpeg"},
        {"nombre": "Mariela Navarro", "carnet": "202146575", "rol": "Desarrollador", "foto": "Mariela.jpeg"},
    ],
    "fecha_creacion": datetime.now().strftime('%B, %Y')
}

# =================================================================
# --- CLASE PRINCIPAL ---
# =================================================================
class EncartaModernaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de Ventana
        self.title("Encarta Derecho USAC - Edición Profesional")
        self.geometry("900x700")
        
        # Variables
        self.PUNTAJE_PARA_DIPLOMA = 50
        self.puntajeTotal = 0
        self.temaActual = ""
        self.quizzesCompletados = set()
        self.nombre_usuario = ""
        self.respuestas_usuario = [] # Para guardar vars de quiz

        # Grid Layout Principal (1 columna, 1 fila que ocupa todo)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Diccionario de Frames
        self.frames = {}
        self.crear_frames()
        self.mostrar_frame("inicio")

    def crear_frames(self):
        # Crear todos los frames y apilarlos
        for nombre in ["inicio", "menu", "teoria", "quiz", "diploma", "equipo"]:
            frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[nombre] = frame

        self.setup_inicio(self.frames["inicio"])
        self.setup_menu(self.frames["menu"])
        self.setup_teoria(self.frames["teoria"])
        self.setup_quiz(self.frames["quiz"])
        self.setup_diploma(self.frames["diploma"])
        self.setup_equipo(self.frames["equipo"])

    def mostrar_frame(self, nombre):
        self.frames[nombre].tkraise()

    # --- 1. PANTALLA INICIO ---
    def setup_inicio(self, frame):
        # Fondo decorativo o color sólido
        inner_frame = ctk.CTkFrame(frame, width=600, height=400, corner_radius=20)
        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(inner_frame, text="APRENDE DERECHO", font=("Roboto Medium", 30)).pack(pady=(40, 10))
        ctk.CTkLabel(inner_frame, text="USAC - Facultad de Derecho", font=("Roboto", 16), text_color="gray").pack(pady=5)
        
        ctk.CTkLabel(inner_frame, text="Ingresa tu nombre para el Diploma:", font=("Roboto", 14)).pack(pady=(30, 5))
        self.entry_nombre = ctk.CTkEntry(inner_frame, placeholder_text="Tu nombre aquí...", width=300)
        self.entry_nombre.pack(pady=10)

        ctk.CTkButton(inner_frame, text="COMENZAR AVENTURA", command=self.comenzar, width=200, height=40, fg_color="#2ecc71", hover_color="#27ae60").pack(pady=30)

    def comenzar(self):
        nombre = self.entry_nombre.get()
        if not nombre:
            return
        self.nombre_usuario = nombre
        self.lbl_saludo_menu.configure(text=f"¡Hola, {nombre}!")
        self.mostrar_frame("menu")

    # --- 2. PANTALLA MENÚ ---
    def setup_menu(self, frame):
        # Header
        header = ctk.CTkFrame(frame, height=80, corner_radius=0, fg_color="#1f2530") # Color oscuro
        header.pack(fill="x", side="top")
        
        ctk.CTkLabel(header, text="MENÚ PRINCIPAL", font=("Roboto Medium", 24)).pack(side="left", padx=30, pady=20)
        self.lbl_saludo_menu = ctk.CTkLabel(header, text="", font=("Roboto", 16), text_color="#3498db")
        self.lbl_saludo_menu.pack(side="right", padx=30)

        # Contenido Scrollable
        scroll = ctk.CTkScrollableFrame(frame, width=800)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        for modulo in MODULOS:
            ctk.CTkLabel(scroll, text=modulo["titulo"], font=("Roboto", 20, "bold"), anchor="w").pack(fill="x", pady=(20, 10))
            
            # Grid de botones para temas
            grid_frame = ctk.CTkFrame(scroll, fg_color="transparent")
            grid_frame.pack(fill="x")
            
            for i, tema in enumerate(modulo["temas"]):
                btn = ctk.CTkButton(grid_frame, text=tema, command=lambda t=tema: self.cargar_teoria(t), 
                                    height=50, fg_color="#2980b9", hover_color="#3498db")
                btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
            
            grid_frame.grid_columnconfigure(0, weight=1)
            grid_frame.grid_columnconfigure(1, weight=1)

        # Footer botones
        footer = ctk.CTkFrame(frame, height=80, fg_color="transparent")
        footer.pack(fill="x", pady=20, padx=20)
        
        self.btn_diploma = ctk.CTkButton(footer, text="🏆 VER DIPLOMA (Bloqueado)", state="disabled", command=lambda: self.mostrar_frame("diploma"), fg_color="#f39c12")
        self.btn_diploma.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        ctk.CTkButton(footer, text="👥 EQUIPO DE DESARROLLO", command=self.cargar_equipo, fg_color="#8e44ad").pack(side="right", fill="x", expand=True, padx=(10, 0))

    # --- 3. PANTALLA TEORÍA ---
    def setup_teoria(self, frame):
        # Botón volver flotante
        ctk.CTkButton(frame, text="← Volver", command=lambda: self.mostrar_frame("menu"), width=80, height=30, fg_color="gray").pack(anchor="nw", padx=20, pady=20)
        
        self.lbl_titulo_teoria = ctk.CTkLabel(frame, text="Titulo", font=("Roboto Medium", 28), wraplength=800)
        self.lbl_titulo_teoria.pack(pady=(0, 20))

        self.txt_contenido = ctk.CTkTextbox(frame, width=800, height=400, font=("Roboto", 14))
        self.txt_contenido.pack(pady=10)

        ctk.CTkButton(frame, text="IR A LA EVALUACIÓN →", command=self.cargar_quiz, width=200, height=50, fg_color="#e74c3c", hover_color="#c0392b").pack(pady=20)

    def cargar_teoria(self, tema):
        self.temaActual = tema
        self.lbl_titulo_teoria.configure(text=tema)
        contenido = BASE_DE_DATOS_CONTENIDO.get(tema, "Contenido en construcción.")
        self.txt_contenido.configure(state="normal")
        self.txt_contenido.delete("0.0", "end")
        self.txt_contenido.insert("0.0", contenido)
        self.txt_contenido.configure(state="disabled")
        self.mostrar_frame("teoria")

    # --- 4. PANTALLA QUIZ ---
    def setup_quiz(self, frame):
        ctk.CTkButton(frame, text="← Cancelar", command=lambda: self.mostrar_frame("menu"), width=80, fg_color="gray").pack(anchor="nw", padx=20, pady=20)
        
        self.lbl_titulo_quiz = ctk.CTkLabel(frame, text="Quiz", font=("Roboto Medium", 24))
        self.lbl_titulo_quiz.pack(pady=10)

        self.scroll_quiz = ctk.CTkScrollableFrame(frame, width=800, height=400)
        self.scroll_quiz.pack(pady=10)

        self.lbl_resultado = ctk.CTkLabel(frame, text="", font=("Roboto", 16))
        self.lbl_resultado.pack(pady=10)

        self.btn_calificar = ctk.CTkButton(frame, text="CALIFICAR", command=self.calificar, width=200, height=50, fg_color="#27ae60")
        self.btn_calificar.pack(pady=10)

    def cargar_quiz(self):
        # Limpiar anterior
        for widget in self.scroll_quiz.winfo_children():
            widget.destroy()
        
        self.lbl_titulo_quiz.configure(text=f"Evaluación: {self.temaActual}")
        self.lbl_resultado.configure(text="")
        self.btn_calificar.configure(state="normal")
        self.respuestas_usuario = []

        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas:
             ctk.CTkLabel(self.scroll_quiz, text="No hay preguntas disponibles.").pack()
             return

        for i, p in enumerate(preguntas):
            card = ctk.CTkFrame(self.scroll_quiz)
            card.pack(fill="x", pady=10, padx=10)
            
            ctk.CTkLabel(card, text=f"{i+1}. {p['pregunta']}", font=("Roboto", 14, "bold")).pack(anchor="w", padx=10, pady=5)
            
            var = ctk.IntVar(value=-1)
            self.respuestas_usuario.append(var)
            
            for j, op in enumerate(p['opciones']):
                ctk.CTkRadioButton(card, text=op, variable=var, value=j).pack(anchor="w", padx=20, pady=2)

        self.mostrar_frame("quiz")

    def calificar(self):
        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        correctas = 0
        for i, p in enumerate(preguntas):
            if self.respuestas_usuario[i].get() == p['respuestaCorrecta']:
                correctas += 1
        
        if correctas >= 2: # Lógica simple
            self.puntajeTotal += (correctas * 10)
            self.quizzesCompletados.add(self.temaActual)
            self.lbl_resultado.configure(text=f"¡Aprobado! {correctas}/{len(preguntas)} correctas.", text_color="#2ecc71")
            # Actualizar botón diploma si aplica
            if self.puntajeTotal >= 50:
                self.btn_diploma.configure(state="normal", text="🏆 VER DIPLOMA ¡LISTO!", fg_color="#f1c40f")
            else:
                self.btn_diploma.configure(text=f"🏆 Diploma ({self.puntajeTotal}/50 pts)")
        else:
            self.lbl_resultado.configure(text=f"Reprobado. {correctas}/{len(preguntas)}. Intenta de nuevo.", text_color="#e74c3c")
        
        self.btn_calificar.configure(state="disabled")

    # --- 5. PANTALLA DIPLOMA ---
    def setup_diploma(self, frame):
        bg = ctk.CTkFrame(frame, fg_color="#ecf0f1", corner_radius=20) # Fondo claro tipo papel
        bg.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

        ctk.CTkLabel(bg, text="⚖️", font=("Arial", 60)).pack(pady=20)
        ctk.CTkLabel(bg, text="UNIVERSIDAD DE SAN CARLOS DE GUATEMALA", font=("Times New Roman", 18, "bold"), text_color="black").pack()
        ctk.CTkLabel(bg, text="DIPLOMA DE MÉRITO", font=("Times New Roman", 30, "bold"), text_color="#c0392b").pack(pady=20)
        
        ctk.CTkLabel(bg, text="Otorgado a:", font=("Arial", 14), text_color="gray").pack()
        self.lbl_nombre_diploma = ctk.CTkLabel(bg, text="NOMBRE ESTUDIANTE", font=("Times New Roman", 24, "bold"), text_color="#2c3e50")
        self.lbl_nombre_diploma.pack(pady=10)

        self.lbl_fecha_diploma = ctk.CTkLabel(bg, text="Fecha", text_color="black")
        self.lbl_fecha_diploma.pack(pady=20)

        ctk.CTkButton(frame, text="Volver al Menú", command=lambda: self.mostrar_frame("menu")).place(relx=0.5, rely=0.9, anchor="center")

    # --- 6. PANTALLA EQUIPO (CON FOTOS) ---
    def setup_equipo(self, frame):
        # Header Equipo
        ctk.CTkButton(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu"), width=100, fg_color="gray").pack(anchor="nw", padx=20, pady=20)
        
        ctk.CTkLabel(frame, text="EQUIPO DE DESARROLLO", font=("Roboto Medium", 26)).pack(pady=(0, 20))
        
        # Area scrollable para las tarjetas
        scroll = ctk.CTkScrollableFrame(frame, width=800)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        self.frame_integrantes = scroll # Guardamos referencia

    def cargar_equipo(self):
        # Limpiar tarjetas anteriores para no duplicar
        for widget in self.frame_integrantes.winfo_children():
            widget.destroy()

        for dev in INFO_EQUIPO["desarrolladores"]:
            card = ctk.CTkFrame(self.frame_integrantes)
            card.pack(fill="x", pady=10, padx=10)
            
            # Cargar Imagen
            try:
                # Intentamos abrir la imagen. Si no existe, usamos placeholder
                if os.path.exists(dev["foto"]):
                    pil_image = Image.open(dev["foto"])
                    ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(80, 80))
                    lbl_img = ctk.CTkLabel(card, text="", image=ctk_image)
                else:
                    lbl_img = ctk.CTkLabel(card, text="[Sin Foto]", width=80, height=80, fg_color="gray")
                
                lbl_img.pack(side="left", padx=20, pady=10)
            except Exception as e:
                print(f"Error cargando imagen: {e}")
                ctk.CTkLabel(card, text="[Error Img]", width=80, height=80, fg_color="gray").pack(side="left", padx=20)

            # Info Texto
            info_frame = ctk.CTkFrame(card, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True)

            ctk.CTkLabel(info_frame, text=dev["nombre"], font=("Roboto", 18, "bold"), anchor="w").pack(fill="x")
            ctk.CTkLabel(info_frame, text=f"{dev['rol']} | Carné: {dev['carnet']}", font=("Roboto", 14), anchor="w").pack(fill="x")
            
        self.mostrar_frame("equipo")

if __name__ == "__main__":
    app = EncartaModernaApp()
    app.mainloop()