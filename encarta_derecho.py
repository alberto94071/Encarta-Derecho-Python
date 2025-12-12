import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime

# =================================================================
# --- 1. BASES DE DATOS DEL PROYECTO ---
# =================================================================

# --- 1.1 Definición de Módulos y Temas (DERECHO) ---
MODULOS = [
    {
        "titulo": "Módulo 1: Introducción al Derecho",
        "temas": [
            "1.1 Origen y Definición del Derecho",
            "1.2 Normas Jurídicas vs. Normas Morales",
            "1.3 Fuentes del Derecho",
            "1.4 Jerarquía Normativa (Pirámide de Kelsen)"
        ]
    },
    {
        "titulo": "Módulo 2: Derecho Constitucional",
        "temas": [
            "2.1 ¿Qué es la Constitución?",
            "2.2 Derechos Humanos Individuales",
            "2.3 La Organización del Estado",
            "2.4 Corte de Constitucionalidad"
        ]
    }
]

# --- 1.2 BASE DE DATOS DE CONTENIDO (DERECHO) ---
BASE_DE_DATOS_CONTENIDO = {
    "1.1 Origen y Definición del Derecho": 
        "La palabra Derecho proviene del vocablo latino directum, que significa 'no apartarse del buen camino' o 'seguir el sendero señalado por la ley'.\n\n"
        "En general se entiende como el conjunto de normas jurídicas, creadas por el Estado, para regular la conducta externa de los hombres.\n\n"
        "Fines del Derecho:\n"
        "- Justicia: Dar a cada quien lo que le corresponde.\n"
        "- Seguridad Jurídica: La certeza de que la ley se cumplirá.\n"
        "- Bien Común: El bienestar de la mayoría de la sociedad.",
    
    "1.2 Normas Jurídicas vs. Normas Morales": 
        "Es fundamental distinguir entre los tipos de reglas.\n\n"
        "Normas Morales: Unilaterales, internas e incoercibles. El castigo es el remordimiento.\n\n"
        "Normas Jurídicas: Bilaterales, externas y coercibles. El Estado puede obligarte a cumplirlas por la fuerza (multas, prisión, etc.).",
    
    "1.3 Fuentes del Derecho": 
        "Se refiere al origen de donde nacen las normas jurídicas:\n"
        "- Fuentes Reales: Fenómenos sociales, políticos o económicos.\n"
        "- Fuentes Históricas: Documentos antiguos (ej. El Derecho Romano).\n"
        "- Fuentes Formales: El proceso legislativo para crear la ley.",
    
    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": 
        "El ordenamiento jurídico tiene jerarquía. Ninguna ley inferior puede contradecir a una superior. \n"
        "1. Nivel Constitucional (CPRG y DDHH).\n"
        "2. Nivel Ordinario (Códigos, leyes del Congreso).\n"
        "3. Nivel Reglamentario (Reglamentos del Ejecutivo).\n"
        "4. Nivel Individualizado (Sentencias, contratos).",
    
    "2.1 ¿Qué es la Constitución?": 
        "Es la ley suprema de un Estado. La de Guatemala fue promulgada en 1985.\n\n"
        "Partes:\n"
        "- Dogmática: Derechos humanos.\n"
        "- Orgánica: Estructura y organización del Estado (Organismos Ejecutivo, Legislativo y Judicial).\n"
        "- Práctica: Garantías constitucionales (Amparo, Exhibición Personal).",

    "2.2 Derechos Humanos Individuales":
        "Derechos inherentes a la persona humana. Ejemplos:\n"
        "- Derecho a la Vida (Art. 3 CPRG)\n"
        "- Libertad e Igualdad\n"
        "- Derecho de Defensa\n"
        "- Presunción de Inocencia",
        
    "2.3 La Organización del Estado":
        "El poder se divide en tres organismos para evitar el abuso (Teoría de Pesos y Contrapesos):\n"
        "- Ejecutivo: Administra (Presidente).\n"
        "- Legislativo: Crea leyes (Congreso).\n"
        "- Judicial: Juzga (Corte Suprema de Justicia).",
        
    "2.4 Corte de Constitucionalidad":
        "Es el máximo tribunal en materia constitucional. Su función principal es la defensa del orden constitucional. Actúa como un tribunal independiente de los demás organismos del Estado."
}

# --- 1.3 BASE DE DATOS DE QUIZZES (DERECHO) ---
BASE_DE_DATOS_QUIZZES = {
    "1.1 Origen y Definición del Derecho": [
        {"pregunta": "¿Qué significa el vocablo latino 'directum'?", "opciones": ["Torcido", "Directo o conforme a la regla", "Ley de Talión"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Cuál NO es uno de los fines del Derecho?", "opciones": ["Bien Común", "Justicia", "Venganza Privada"], "respuestaCorrecta": 2 },
    ],
    "1.2 Normas Jurídicas vs. Normas Morales": [
        {"pregunta": "Las normas jurídicas son 'coercibles'. ¿Qué significa?", "opciones": ["Que son opcionales", "Que se pueden imponer por la fuerza", "Que dependen de la religión"], "respuestaCorrecta": 1 },
        {"pregunta": "Las normas jurídicas regulan la conducta:", "opciones": ["Interna (pensamientos)", "Externa (actos)", "Sentimental"], "respuestaCorrecta": 1 }
    ],
    "1.3 Fuentes del Derecho": [
        {"pregunta": "¿Cuáles son las fuentes que describen el proceso de creación de la ley?", "opciones": ["Reales", "Históricas", "Formales"], "respuestaCorrecta": 2 },
        {"pregunta": "El Derecho Romano es un ejemplo de fuente:", "opciones": ["Histórica", "Real", "Formal"], "respuestaCorrecta": 0 },
    ],
    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": [
        {"pregunta": "¿Cuál es la norma suprema en la jerarquía?", "opciones": ["El Código Civil", "La Constitución (CPRG)", "El Reglamento de Tránsito"], "respuestaCorrecta": 1 },
        {"pregunta": "Una ley ordinaria NO puede contradecir a:", "opciones": ["Un reglamento", "Una sentencia", "La Constitución"], "respuestaCorrecta": 2 },
    ],
    "2.1 ¿Qué es la Constitución?": [
        {"pregunta": "¿Qué parte de la Constitución organiza el Estado?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué parte contiene los Derechos Humanos?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 0 }
    ],
    "2.2 Derechos Humanos Individuales": [
        {"pregunta": "¿En qué artículo de la CPRG inicia el derecho a la vida?", "opciones": ["Artículo 1", "Artículo 3", "Artículo 10"], "respuestaCorrecta": 1 },
        {"pregunta": "Los Derechos Humanos son:", "opciones": ["Inherentes a la persona", "Regalos del Estado", "Comprables"], "respuestaCorrecta": 0 }
    ],
    "2.3 La Organización del Estado": [
        {"pregunta": "¿Qué organismo crea las leyes?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué organismo juzga?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 2 }
    ],
    "2.4 Corte de Constitucionalidad": [
        {"pregunta": "¿Cuál es la función principal de la CC?", "opciones": ["Aprobar el presupuesto", "Defensa del orden constitucional", "Juzgar delitos comunes"], "respuestaCorrecta": 1 },
        {"pregunta": "¿La CC es el máximo tribunal en materia constitucional?", "opciones": ["Sí", "No", "Depende del caso"], "respuestaCorrecta": 0 }
    ]
}

# --- 1.4 BASE DE DATOS DEL EQUIPO (ACTUALIZADA) ---
INFO_EQUIPO = {
    "proyecto": "Encarta Interactiva de Introducción al Derecho",
    "universidad": "Universidad de San Carlos de Guatemala (USAC)",
    "catedra": "Fundamentos Jurídicos", 
    "desarrolladores": [
        {"nombre": "Tania Vanessa Vásquez Morales", "carnet": "201946345", "rol": "Desarrollador", "contacto": "estudiante1@gmail.com"},
        {"nombre": "Yenifer Marisol Fuentes Velásquez", "carnet": "202145889", "rol": "Desarrollador", "contacto": "estudiante2@gmail.com / Cel: +(502) 40517154"},
        {"nombre": "Nazzary Jasmin Rubio Rodríguez", "carnet": "202141942", "rol": "Desarrollador", "contacto": "estudiante3@gmail.com"},
        {"nombre": "Mariela Lisbeth Navarro Alvarado", "carnet": "202146575", "rol": "Desarrollador", "contacto": "estudiante4@gmail.com"},
    ],
    "fecha_creacion": datetime.now().strftime('%B, %Y')
}

# =================================================================
# --- CLASE PRINCIPAL DE LA APLICACIÓN (TKINTER) ---
# =================================================================
class EncartaDerechoApp:
    def __init__(self, master):
        self.master = master
        master.title("Encarta de Derecho - USAC")
        master.geometry("800x600")

        # Variables de Estado
        self.PUNTAJE_PARA_DIPLOMA = 50
        self.puntajeTotal = 0
        self.temaActual = ""
        self.quizzesCompletados = set()
        self.nombre_usuario = ""
        
        # Diccionario para almacenar las pantallas (Frames)
        self.frames = {}
        self.crear_frames()
        self.mostrar_frame("inicio")
        
    def crear_frames(self):
        self.frames["inicio"] = tk.Frame(self.master)
        self.crear_pantalla_inicio(self.frames["inicio"])
        
        self.frames["menu"] = tk.Frame(self.master)
        self.frames["menu"].grid_columnconfigure(0, weight=1)
        self.crear_pantalla_menu(self.frames["menu"])
        
        self.frames["teoria"] = tk.Frame(self.master)
        self.crear_pantalla_teoria(self.frames["teoria"])

        self.frames["quiz"] = tk.Frame(self.master)
        self.crear_pantalla_quiz(self.frames["quiz"])
        
        self.frames["diploma"] = tk.Frame(self.master)
        self.crear_pantalla_diploma(self.frames["diploma"])
        
        self.frames["equipo"] = tk.Frame(self.master)
        self.crear_pantalla_equipo(self.frames["equipo"])

        for frame_name, frame in self.frames.items():
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def mostrar_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    # --- PANTALLA DE INICIO ---
    def crear_pantalla_inicio(self, frame):
        tk.Label(frame, text="APRENDIENDO DERECHO CON LA USAC 🎓", font=("Arial", 18, "bold")).pack(pady=50)
        tk.Label(frame, text="Refuerza las leyes de forma interactiva.", font=("Arial", 12)).pack(pady=5)
        
        tk.Label(frame, text="Escribe el nombre para tu diploma:").pack(pady=15)
        self.inputNombre = tk.Entry(frame, width=40)
        self.inputNombre.pack(pady=5)
        
        tk.Button(frame, text="¡Comenzar Aventura!", command=self.comenzar_estudio, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white").pack(pady=20)
    
    def comenzar_estudio(self):
        nombre = self.inputNombre.get().strip()
        if not nombre:
            messagebox.showwarning("Error", "Por favor, ingresa tu nombre para continuar.")
            return
        
        self.nombre_usuario = nombre
        self.cargar_menu()
        self.mostrar_frame("menu")

    # --- PANTALLA DE MENÚ ---
    def crear_pantalla_menu(self, frame):
        tk.Label(frame, text="Menú Principal", font=("Arial", 16, "bold")).pack(pady=20)
        self.saludoNombre = tk.Label(frame, text="", font=("Arial", 12))
        self.saludoNombre.pack(pady=5)
        
        self.menuOpciones = tk.Frame(frame)
        self.menuOpciones.pack(pady=10, fill='x', padx=50)

    def cargar_menu(self):
        self.saludoNombre.config(text=f"Hola, {self.nombre_usuario}. ¡Bienvenido futuro abogado!")
        
        for widget in self.menuOpciones.winfo_children():
            widget.destroy()

        for modulo in MODULOS:
            tk.Label(self.menuOpciones, text=modulo["titulo"], font=("Arial", 12, "bold")).pack(anchor='w', pady=(15, 5))
            
            contenedorBotones = tk.Frame(self.menuOpciones)
            contenedorBotones.pack(fill='x', padx=10)
            
            for i, tema in enumerate(modulo["temas"]):
                boton = tk.Button(contenedorBotones, text=tema, command=lambda t=tema: self.mostrar_teoria(t), width=30)
                if tema in self.quizzesCompletados:
                    boton.config(bg="#A5D6A7")
                boton.grid(row=i // 2, column=i % 2, padx=5, pady=5, sticky='ew')

        # Botón de Diploma
        if self.puntajeTotal >= self.PUNTAJE_PARA_DIPLOMA:
            texto_diploma = "🏆 ¡Ver mi Diploma!"
            estado = tk.NORMAL
            color = "#FFC107"
        else:
            texto_diploma = f"🏆 Diploma (Faltan {self.PUNTAJE_PARA_DIPLOMA - self.puntajeTotal} pts)"
            estado = tk.DISABLED
            color = "gray"
            
        tk.Button(self.menuOpciones, text=texto_diploma, command=self.mostrar_diploma, state=estado, bg=color, font=("Arial", 10, "bold")).pack(pady=(20, 5), fill='x', padx=50)

        # Botón de Equipo
        tk.Button(self.menuOpciones, text="⚖️ Equipo de Desarrollo", command=lambda: self.mostrar_frame("equipo"), bg="#E0E0E0").pack(pady=5, fill='x', padx=50)


    # --- PANTALLA DE TEORÍA ---
    def crear_pantalla_teoria(self, frame):
        self.teoriaTitulo = tk.Label(frame, text="", font=("Arial", 16, "bold"), wraplength=700)
        self.teoriaTitulo.pack(pady=20)
        
        self.teoriaContenido = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=90, height=20, font=("Arial", 11))
        self.teoriaContenido.pack(pady=10, padx=20)
        
        contenedor_botones = tk.Frame(frame)
        contenedor_botones.pack(pady=10)

        tk.Button(contenedor_botones, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu"), bg="#FFCDD2").pack(side=tk.LEFT, padx=10)
        tk.Button(contenedor_botones, text="Ir al Quiz →", command=self.ir_al_quiz, bg="#C8E6C9").pack(side=tk.LEFT, padx=10)

    def mostrar_teoria(self, tema):
        self.temaActual = tema
        self.teoriaTitulo.config(text=tema)
        
        self.teoriaContenido.config(state=tk.NORMAL)
        self.teoriaContenido.delete(1.0, tk.END)
        contenido = BASE_DE_DATOS_CONTENIDO.get(tema, "Contenido próximamente.")
        self.teoriaContenido.insert(tk.END, contenido)
        self.teoriaContenido.config(state=tk.DISABLED)
        
        self.mostrar_frame("teoria")
        
    def ir_al_quiz(self):
        self.cargar_quiz(self.temaActual)
        self.mostrar_frame("quiz")
        
    # --- PANTALLA DE QUIZ ---
    def crear_pantalla_quiz(self, frame):
        tk.Label(frame, text="EVALUACIÓN DEL TEMA", font=("Arial", 14, "bold")).pack(pady=(10, 5))
        self.quizTitulo = tk.Label(frame, text="", font=("Arial", 12))
        self.quizTitulo.pack(pady=(5, 10))

        quiz_canvas = tk.Canvas(frame)
        quiz_canvas.pack(side="left", fill="both", expand=True, padx=20, pady=5)
        
        quiz_scrollbar = tk.Scrollbar(frame, orient="vertical", command=quiz_canvas.yview)
        quiz_scrollbar.pack(side="right", fill="y")
        
        quiz_canvas.configure(yscrollcommand=quiz_scrollbar.set)
        quiz_canvas.bind('<Configure>', lambda e: quiz_canvas.configure(scrollregion = quiz_canvas.bbox("all")))

        self.quizContenedor = tk.Frame(quiz_canvas)
        quiz_canvas.create_window((0, 0), window=self.quizContenedor, anchor="nw", width=740)
        
        # Resultados y Botones
        self.quizResultados = tk.Label(frame, text="", font=("Arial", 12, "italic"))
        self.quizResultados.pack(pady=10)
        
        self.btnCalificarQuiz = tk.Button(frame, text="Calificar Examen", command=self.calificar_quiz, bg="#81C784", fg="white")
        self.btnCalificarQuiz.pack(pady=5)
        
        tk.Button(frame, text="Volver al Menú Principal", command=lambda: self.mostrar_frame("menu")).pack(pady=5)

    def cargar_quiz(self, tema):
        self.quizTitulo.config(text=f"Quiz: {tema}")
        self.quizResultados.config(text="")
        self.btnCalificarQuiz.config(state=tk.NORMAL)
        
        for widget in self.quizContenedor.winfo_children():
            widget.destroy()
            
        preguntas = BASE_DE_DATOS_QUIZZES.get(tema, [])
        if not preguntas:
            tk.Label(self.quizContenedor, text="Quiz próximamente.").pack(pady=20)
            self.btnCalificarQuiz.config(state=tk.DISABLED)
            return
            
        self.respuestas_usuario = []
        
        for indice, pregunta in enumerate(preguntas):
            bloque = tk.Frame(self.quizContenedor, padx=10, pady=5, borderwidth=1, relief="groove")
            bloque.pack(fill='x', pady=5)
            
            tk.Label(bloque, text=f"{indice + 1}. {pregunta['pregunta']}", font=("Arial", 10, "bold"), justify=tk.LEFT, wraplength=700).pack(anchor='w', pady=(5, 2))
            
            var_opcion = tk.IntVar()
            self.respuestas_usuario.append(var_opcion)
            
            for indice_opcion, opcion in enumerate(pregunta['opciones']):
                tk.Radiobutton(bloque, text=opcion, variable=var_opcion, value=indice_opcion, justify=tk.LEFT).pack(anchor='w')
                
    def calificar_quiz(self):
        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas: return

        correctas = 0
        correctas_para_ganar = 2
        
        for i, pregunta in enumerate(preguntas):
            try:
                respuesta_usuario_index = self.respuestas_usuario[i].get()
                if respuesta_usuario_index == pregunta['respuestaCorrecta']:
                    correctas += 1
            except tk.TclError:
                pass

        puntos_ganados = 0
        mensaje_puntos = ""

        if self.temaActual in self.quizzesCompletados:
            mensaje_puntos = f"Resultado: {correctas}/{len(preguntas)}. (Quiz ya completado. Puntos no sumados. Total: {self.puntajeTotal})"
            clase_color = "#E0E0E0"
        else:
            if correctas >= correctas_para_ganar:
                puntos_ganados = correctas * 10
                self.puntajeTotal += puntos_ganados
                self.quizzesCompletados.add(self.temaActual)
                self.cargar_menu()
                mensaje_puntos = f"¡Aprobado! Ganaste {puntos_ganados} puntos. (Total: {self.puntajeTotal})"
                clase_color = "#4CAF50"
            else:
                mensaje_puntos = f"Resultado: {correctas}/{len(preguntas)}. Necesitas al menos {correctas_para_ganar} para aprobar. ¡Inténtalo de nuevo!"
                clase_color = "#F44336"

        self.quizResultados.config(text=mensaje_puntos, fg=clase_color)
        self.btnCalificarQuiz.config(state=tk.DISABLED)


    # --- PANTALLA DE DIPLOMA ---
    def crear_pantalla_diploma(self, frame):
        tk.Label(frame, text="¡Felicitaciones!", font=("Arial", 20, "bold"), fg="#FFC107").pack(pady=30)
        tk.Label(frame, text="Se otorga el presente", font=("Arial", 14)).pack()
        tk.Label(frame, text="DIPLOMA DE MÉRITO", font=("Arial", 18, "italic")).pack(pady=10)
        
        tk.Label(frame, text="Otorgado a:", font=("Arial", 12)).pack(pady=5)
        self.diplomaNombre = tk.Label(frame, text="[Nombre del Estudiante]", font=("Arial", 24, "underline"), fg="#3F51B5")
        self.diplomaNombre.pack(pady=10)
        
        tk.Label(frame, text="Por haber completado exitosamente todos los módulos de Introducción al Derecho y demostrar un dominio excepcional de los fundamentos jurídicos guatemaltecos.", 
                 font=("Arial", 14), wraplength=600).pack(pady=10)
        
        self.diplomaFecha = tk.Label(frame, text="[Fecha]", font=("Arial", 12))
        self.diplomaFecha.pack(pady=20)

        tk.Label(frame, text="FACULTAD DE DERECHO", font=("Arial", 14, "bold")).pack(pady=5)
        
        tk.Button(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu")).pack(pady=20)
    
    def mostrar_diploma(self):
        nombre = self.nombre_usuario or "Estudiante de Derecho"
        self.diplomaNombre.config(text=nombre)
        self.diplomaFecha.config(text=f"Guatemala, {datetime.now().strftime('%d de %B de %Y')}")
        self.mostrar_frame("diploma")

    # --- PANTALLA DE EQUIPO (ACTUALIZADA) ---
    def crear_pantalla_equipo(self, frame):
        tk.Label(frame, text="⚖️ Equipo de Desarrollo ⚖️", font=("Arial", 18, "bold")).pack(pady=30)
        
        tk.Label(frame, text=f"Proyecto: {INFO_EQUIPO['proyecto']}", font=("Arial", 14, "italic")).pack(pady=(0, 10))
        tk.Label(frame, text=f"Universidad: {INFO_EQUIPO['universidad']} | Cátedra: {INFO_EQUIPO['catedra']}", font=("Arial", 12)).pack(pady=5)

        tk.Label(frame, text="--- INTEGRANTES ---", font=("Arial", 12, "bold")).pack(pady=15)
        
        # Contenedor para los desarrolladores (usando un Frame para agrupar)
        dev_frame = tk.Frame(frame)
        dev_frame.pack(padx=20, pady=10)

        for i, dev in enumerate(INFO_EQUIPO["desarrolladores"]):
            # Tarjeta de Desarrollador
            card = tk.Frame(dev_frame, borderwidth=2, relief="groove", padx=15, pady=10)
            
            # Usaremos 2 columnas para una mejor presentación
            row = i // 2
            col = i % 2
            
            card.grid(row=row, column=col, padx=10, pady=10, sticky="n")

            tk.Label(card, text=dev['nombre'], font=("Arial", 12, "bold")).pack(pady=2)
            tk.Label(card, text=f"Rol: {dev['rol']}", font=("Arial", 10)).pack(pady=2)
            tk.Label(card, text=f"Carné USAC: {dev['carnet']}", font=("Arial", 10)).pack(pady=2)
            tk.Label(card, text=f"Contacto: {dev['contacto']}", font=("Arial", 10)).pack(pady=2)
        
        tk.Label(frame, text=f"Fecha: {INFO_EQUIPO['fecha_creacion']}", font=("Arial", 10, "italic")).pack(pady=20)

        tk.Button(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu")).pack(pady=10)

# --- INICIO DE LA APLICACIÓN ---
if __name__ == "__main__":
    root = tk.Tk()
    app = EncartaDerechoApp(root)
    root.mainloop()