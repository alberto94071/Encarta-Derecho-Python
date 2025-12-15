import customtkinter as ctk
from PIL import Image
import os
from datetime import datetime

# =================================================================
# CONFIGURACIÓN VISUAL
# =================================================================
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

# =================================================================
# 1. BASE DE DATOS DE CONTENIDO (COMPLETA Y LIMPIA)
# =================================================================

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

BASE_DE_DATOS_CONTENIDO = {
    "1.1 Origen y Definición del Derecho": 
        "ORIGEN Y DEFINICIÓN\n\n"
        "La palabra Derecho proviene del vocablo latino 'directum', que significa \"no apartarse del buen camino\" o \"seguir el sendero señalado por la ley\".\n\n"
        "En general se entiende como el conjunto de normas jurídicas, creadas por el Estado, para regular la conducta externa de los hombres y, en caso de incumplimiento, está prevista una sanción judicial.\n\n"
        "FINES DEL DERECHO:\n"
        "• Justicia: Dar a cada quien lo que le corresponde.\n"
        "• Seguridad Jurídica: La certeza de que la ley se cumplirá.\n"
        "• Bien Común: El bienestar de la mayoría de la sociedad.",

    "1.2 Normas Jurídicas vs. Normas Morales": 
        "DIFERENCIA ENTRE NORMAS\n\n"
        "Es fundamental distinguir entre los tipos de reglas que rigen nuestra vida.\n\n"
        "NORMAS MORALES:\n"
        "Son unilaterales, internas e incoercibles. Si no las cumples, el castigo es el remordimiento o el rechazo social, pero nadie te puede obligar por la fuerza.\n\n"
        "NORMAS JURÍDICAS:\n"
        "Son bilaterales, externas y COERCIBLES. Esto significa que si no las cumples voluntariamente, el Estado tiene la facultad de obligarte a cumplirlas por la fuerza (multas, prisión, embargo).",

    "1.3 Fuentes del Derecho": 
        "FUENTES DEL DERECHO\n\n"
        "Se refiere al origen de donde nacen las normas jurídicas. Se clasifican tradicionalmente en:\n\n"
        "1. Fuentes Reales: Son los fenómenos sociales, políticos o económicos que motivan la creación de una norma (ej. una revolución, una crisis económica).\n"
        "2. Fuentes Históricas: Documentos antiguos que sirven de base (ej. El Derecho Romano).\n"
        "3. Fuentes Formales: El proceso legislativo mediante el cual se crea la ley (Iniciativa, Discusión, Aprobación, Sanción, Promulgación).",

    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": 
        "JERARQUÍA NORMATIVA\n\n"
        "El ordenamiento jurídico no es plano, tiene jerarquía. Ninguna ley inferior puede contradecir a una superior.\n\n"
        "1. Nivel Constitucional: La Constitución Política de la República (CPRG) y tratados de DDHH. Es la ley suprema.\n"
        "2. Nivel Ordinario: Leyes creadas por el Congreso (Código Civil, Penal, Laboral).\n"
        "3. Nivel Reglamentario: Reglamentos creados por el Ejecutivo para aplicar las leyes ordinarias.\n"
        "4. Nivel Individualizado: Sentencias o contratos que aplican a personas específicas.",

    "2.1 ¿Qué es la Constitución?": 
        "LA CONSTITUCIÓN POLÍTICA\n\n"
        "Es la ley suprema de un Estado. En Guatemala, nuestra constitución actual fue promulgada en 1985.\n\n"
        "Se divide en tres partes:\n"
        "• Parte Dogmática: Contiene los derechos humanos y libertades fundamentales.\n"
        "• Parte Orgánica: Establece la estructura y organización del Estado (Organismos Ejecutivo, Legislativo y Judicial).\n"
        "• Parte Práctica: Garantías constitucionales (Amparo, Exhibición Personal).",

    "2.2 Derechos Humanos Individuales": 
        "DERECHOS HUMANOS INDIVIDUALES\n\n"
        "Son los derechos inherentes a la persona humana. En la Constitución de Guatemala inician desde el Artículo 3 (Derecho a la vida).\n\n"
        "Principales Derechos:\n"
        "• Derecho a la Vida\n"
        "• Libertad e Igualdad\n"
        "• Derecho de Defensa\n"
        "• Presunción de Inocencia",

    "2.3 La Organización del Estado": 
        "ORGANIZACIÓN DEL ESTADO\n\n"
        "Guatemala es una república soberana. El poder proviene del pueblo y se divide en tres organismos para evitar el abuso de poder (Teoría de Pesos y Contrapesos):\n\n"
        "• Ejecutivo: Administra el Estado (Presidente, Vicepresidente, Ministros).\n"
        "• Legislativo: Crea las leyes (Congreso de la República).\n"
        "• Judicial: Juzga y promueve la ejecución de lo juzgado (Corte Suprema de Justicia, Tribunales).",

    "2.4 Corte de Constitucionalidad": 
        "CORTE DE CONSTITUCIONALIDAD (CC)\n\n"
        "La Corte de Constitucionalidad es el máximo tribunal en materia constitucional.\n\n"
        "Su función principal es la defensa del orden constitucional. Actúa como un tribunal independiente de los demás organismos del Estado."
}

# =================================================================
# 2. BASE DE DATOS DE QUIZZES (COMPLETA)
# =================================================================

BASE_DE_DATOS_QUIZZES = {
    "1.1 Origen y Definición del Derecho": [
        {"pregunta": "¿Qué significa el vocablo latino 'directum'?", "opciones": ["Torcido", "Directo o conforme a la regla", "Ley de Talión"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Cuál NO es uno de los fines del Derecho?", "opciones": ["Bien Común", "Justicia", "Venganza Privada"], "respuestaCorrecta": 2 },
        {"pregunta": "¿Quién crea las normas jurídicas principalmente?", "opciones": ["El Estado", "La Iglesia", "La Familia"], "respuestaCorrecta": 0 }
    ],
    "1.2 Normas Jurídicas vs. Normas Morales": [
        {"pregunta": "Las normas jurídicas son 'coercibles'. ¿Qué significa?", "opciones": ["Que son opcionales", "Que se pueden imponer por la fuerza", "Que dependen de la religión"], "respuestaCorrecta": 1 },
        {"pregunta": "Si no saludo a mi vecino, incumplo una norma:", "opciones": ["Jurídica", "Penal", "Moral o de trato social"], "respuestaCorrecta": 2 },
        {"pregunta": "Las normas jurídicas regulan la conducta:", "opciones": ["Interna (pensamientos)", "Externa (actos)", "Sentimental"], "respuestaCorrecta": 1 }
    ],
    "1.3 Fuentes del Derecho": [
        {"pregunta": "¿Cuáles son las fuentes que describen el proceso de creación de la ley?", "opciones": ["Reales", "Históricas", "Formales"], "respuestaCorrecta": 2 },
        {"pregunta": "El Derecho Romano es un ejemplo de fuente:", "opciones": ["Histórica", "Real", "Formal"], "respuestaCorrecta": 0 },
        {"pregunta": "¿Qué organismo del Estado aprueba las leyes ordinarias?", "opciones": ["Ejecutivo", "Legislativo (Congreso)", "Judicial"], "respuestaCorrecta": 1 }
    ],
    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": [
        {"pregunta": "¿Cuál es la norma suprema en la jerarquía?", "opciones": ["El Código Civil", "La Constitución (CPRG)", "El Reglamento de Tránsito"], "respuestaCorrecta": 1 },
        {"pregunta": "Una ley ordinaria NO puede contradecir a:", "opciones": ["Un reglamento", "Una sentencia", "La Constitución"], "respuestaCorrecta": 2 },
        {"pregunta": "¿En qué año se promulgó la Constitución actual de Guatemala?", "opciones": ["1944", "1985", "2020"], "respuestaCorrecta": 1 }
    ],
    "2.1 ¿Qué es la Constitución?": [
        {"pregunta": "¿Qué parte de la Constitución organiza el Estado?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué parte contiene los Derechos Humanos?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 0 },
        {"pregunta": "¿Es la Constitución superior a las leyes del Congreso?", "opciones": ["Sí", "No", "Son iguales"], "respuestaCorrecta": 0 }
    ],
    "2.2 Derechos Humanos Individuales": [
        {"pregunta": "¿En qué artículo de la CPRG inicia el derecho a la vida?", "opciones": ["Artículo 1", "Artículo 3", "Artículo 10"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué es la presunción de inocencia?", "opciones": ["Ser culpable hasta demostrar lo contrario", "Ser inocente hasta ser citado", "Ser inocente hasta que una sentencia declare lo contrario"], "respuestaCorrecta": 2 },
        {"pregunta": "Los Derechos Humanos son:", "opciones": ["Inherentes a la persona", "Regalos del Estado", "Comprables"], "respuestaCorrecta": 0 }
    ],
    "2.3 La Organización del Estado": [
        {"pregunta": "¿Qué organismo crea las leyes?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué organismo administra el Estado?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 0 },
        {"pregunta": "¿Qué organismo juzga?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 2 }
    ],
    "2.4 Corte de Constitucionalidad": [
        {"pregunta": "¿Cuál es la función principal de la CC?", "opciones": ["Aprobar el presupuesto", "Defensa del orden constitucional", "Juzgar delitos comunes"], "respuestaCorrecta": 1 },
        {"pregunta": "La CC es un tribunal:", "opciones": ["Dependiente del Congreso", "Independiente", "Militar"], "respuestaCorrecta": 1 },
        {"pregunta": "¿La CC es el máximo tribunal en materia constitucional?", "opciones": ["Sí", "No", "Depende del caso"], "respuestaCorrecta": 0 }
    ]
}

# =================================================================
# 3. INFO EQUIPO
# =================================================================

INFO_EQUIPO = {
    "proyecto": "Encarta Interactiva de Derecho",
    "universidad": "Universidad de San Carlos de Guatemala (USAC)",
    "catedra": "Fundamentos Jurídicos", 
    "desarrolladores": [
        {"nombre": "Tania Vanessa Vásquez Morales", "carnet": "201946345", "rol": "Desarrollador", "correo": "estudiante1@gmail.com", "foto": "Tania.jpeg"},
        {"nombre": "Yenifer Marisol Fuentes Velásquez", "carnet": "202145889", "rol": "Desarrollador", "correo": "estudiante2@gmail.com", "foto": "Marisol.jpeg"},
        {"nombre": "Nazzary Jasmin Rubio Rodríguez", "carnet": "202141942", "rol": "Desarrollador", "correo": "estudiante3@gmail.com", "foto": "Nazzary.jpeg"},
        {"nombre": "Mariela Lisbeth Navarro Alvarado", "carnet": "202146575", "rol": "Desarrollador", "correo": "estudiante4@gmail.com", "foto": "Mariela.jpeg"},
    ],
    "fecha_creacion": datetime.now().strftime('%B, %Y')
}

# =================================================================
# CLASE PRINCIPAL
# =================================================================

class EncartaFinalApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuración Ventana ---
        self.title("Aprende Derecho | USAC - Proyecto Final")
        self.geometry("1000x700")
        
        # --- Variables de Lógica ---
        self.PUNTAJE_PARA_DIPLOMA = 50
        self.puntajeTotal = 0
        self.temaActual = ""
        self.quizzesCompletados = set()
        self.nombre_usuario = ""
        
        # Almacenará las variables IntVars de los radiobuttons
        self.respuestas_usuario = [] 

        # --- Layout Principal ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Inicialización de Frames ---
        self.frames = {}
        self.crear_frames()
        
        # --- MARCA DE AGUA (LOGO) ---
        self.crear_marca_agua()

        # Mostrar inicio
        self.mostrar_frame("inicio")

    def crear_marca_agua(self):
        """Crea el logo en la esquina inferior derecha que persiste sobre todo."""
        try:
            if os.path.exists("logo.png"):
                # Cargamos la imagen
                pil_img = Image.open("logo.png")
                # Ajusta el tamaño del logo si es necesario (ej. 100x100)
                logo_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(100, 100))
                
                self.lbl_watermark = ctk.CTkLabel(self, text="", image=logo_img)
                # Usamos place con coordenadas relativas (1.0, 1.0 es abajo derecha)
                self.lbl_watermark.place(relx=0.98, rely=0.98, anchor="se")
            else:
                print("Advertencia: No se encontró 'logo.png'. La marca de agua no se mostrará.")
        except Exception as e:
            print(f"Error cargando marca de agua: {e}")

    def crear_frames(self):
        # Creamos los contenedores para cada pantalla
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
        """Trae el frame al frente y asegura que la marca de agua quede arriba."""
        self.frames[nombre].tkraise()
        
        # IMPORTANTE: Traer la marca de agua al frente de nuevo
        if hasattr(self, 'lbl_watermark'):
            self.lbl_watermark.lift()

    # =================================================================
    # 1. PANTALLA INICIO
    # =================================================================
    def setup_inicio(self, frame):
        inner_frame = ctk.CTkFrame(frame, width=600, height=450, corner_radius=20)
        inner_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(inner_frame, text="APRENDE DERECHO", font=("Roboto", 40, "bold")).pack(pady=(50, 10))
        ctk.CTkLabel(inner_frame, text="USAC - Facultad de Ciencias Jurídicas y Sociales", font=("Roboto", 18), text_color="gray").pack(pady=5)
        
        ctk.CTkLabel(inner_frame, text="Escribe el nombre para tu diploma:", font=("Roboto", 14)).pack(pady=(40, 5))
        self.entry_nombre = ctk.CTkEntry(inner_frame, placeholder_text="Tu nombre completo...", width=350, height=40)
        self.entry_nombre.pack(pady=10)

        ctk.CTkButton(inner_frame, text="COMENZAR AVENTURA", command=self.comenzar, width=250, height=50, 
                      font=("Roboto", 15, "bold"), fg_color="#27ae60", hover_color="#2ecc71").pack(pady=40)

    def comenzar(self):
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            return # No hace nada si está vacío
        self.nombre_usuario = nombre
        self.lbl_saludo_menu.configure(text=f"¡Bienvenido, {nombre}!")
        self.mostrar_frame("menu")

    # =================================================================
    # 2. PANTALLA MENÚ
    # =================================================================
    def setup_menu(self, frame):
        # --- Header ---
        header = ctk.CTkFrame(frame, height=80, corner_radius=0, fg_color="#1a1a1a")
        header.pack(fill="x", side="top")
        
        ctk.CTkLabel(header, text="MENÚ PRINCIPAL", font=("Roboto", 24, "bold")).pack(side="left", padx=30, pady=20)
        self.lbl_saludo_menu = ctk.CTkLabel(header, text="", font=("Roboto", 16), text_color="#3498db")
        self.lbl_saludo_menu.pack(side="right", padx=30)

        # --- Contenido ---
        scroll = ctk.CTkScrollableFrame(frame, width=900)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # Generar botones dinámicamente
        for modulo in MODULOS:
            ctk.CTkLabel(scroll, text=modulo["titulo"], font=("Roboto", 22, "bold"), anchor="w", text_color="#ecf0f1").pack(fill="x", pady=(20, 10))
            
            grid_frame = ctk.CTkFrame(scroll, fg_color="transparent")
            grid_frame.pack(fill="x")
            
            for i, tema in enumerate(modulo["temas"]):
                # Crear botón
                btn = ctk.CTkButton(grid_frame, text=tema, command=lambda t=tema: self.cargar_teoria(t), 
                                    height=60, font=("Roboto", 14), fg_color="#2c3e50", hover_color="#34495e")
                
                # Posición Grid (2 columnas)
                btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
            
            grid_frame.grid_columnconfigure(0, weight=1)
            grid_frame.grid_columnconfigure(1, weight=1)

        # --- Footer ---
        footer = ctk.CTkFrame(frame, height=80, fg_color="transparent")
        footer.pack(fill="x", pady=20, padx=20)
        
        self.btn_diploma = ctk.CTkButton(footer, text="🏆 VER DIPLOMA (Bloqueado)", state="disabled", 
                                         command=lambda: self.mostrar_frame("diploma"), fg_color="#7f8c8d", height=50)
        self.btn_diploma.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        ctk.CTkButton(footer, text="👥 EQUIPO DE DESARROLLO", command=self.cargar_equipo, 
                      fg_color="#8e44ad", hover_color="#9b59b6", height=50).pack(side="right", fill="x", expand=True, padx=(10, 0))

    # =================================================================
    # 3. PANTALLA TEORÍA
    # =================================================================
    def setup_teoria(self, frame):
        ctk.CTkButton(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu"), width=120, height=35, fg_color="#e74c3c", hover_color="#c0392b").pack(anchor="nw", padx=30, pady=20)
        
        self.lbl_titulo_teoria = ctk.CTkLabel(frame, text="Titulo", font=("Roboto", 28, "bold"), wraplength=800)
        self.lbl_titulo_teoria.pack(pady=(0, 20))

        # Textbox de solo lectura
        self.txt_contenido = ctk.CTkTextbox(frame, width=850, height=450, font=("Roboto", 16))
        self.txt_contenido.pack(pady=10)

        ctk.CTkButton(frame, text="IR A LA EVALUACIÓN →", command=self.cargar_quiz, width=250, height=50, 
                      fg_color="#27ae60", hover_color="#2ecc71", font=("Roboto", 15, "bold")).pack(pady=20)

    def cargar_teoria(self, tema):
        self.temaActual = tema
        self.lbl_titulo_teoria.configure(text=tema)
        
        contenido = BASE_DE_DATOS_CONTENIDO.get(tema, "Contenido en construcción.")
        
        self.txt_contenido.configure(state="normal")
        self.txt_contenido.delete("0.0", "end")
        self.txt_contenido.insert("0.0", contenido)
        self.txt_contenido.configure(state="disabled")
        
        self.mostrar_frame("teoria")

    # =================================================================
    # 4. PANTALLA QUIZ
    # =================================================================
    def setup_quiz(self, frame):
        ctk.CTkButton(frame, text="← Cancelar Quiz", command=lambda: self.mostrar_frame("menu"), width=120, fg_color="#95a5a6").pack(anchor="nw", padx=30, pady=20)
        
        self.lbl_titulo_quiz = ctk.CTkLabel(frame, text="Quiz", font=("Roboto", 24, "bold"))
        self.lbl_titulo_quiz.pack(pady=10)

        self.scroll_quiz = ctk.CTkScrollableFrame(frame, width=850, height=400)
        self.scroll_quiz.pack(pady=10)

        self.lbl_resultado = ctk.CTkLabel(frame, text="", font=("Roboto", 18, "bold"))
        self.lbl_resultado.pack(pady=10)

        self.btn_calificar = ctk.CTkButton(frame, text="CALIFICAR RESPUESTAS", command=self.calificar, width=250, height=50, fg_color="#e67e22", hover_color="#d35400")
        self.btn_calificar.pack(pady=10)

    def cargar_quiz(self):
        # Limpiar
        for widget in self.scroll_quiz.winfo_children():
            widget.destroy()
        
        self.lbl_titulo_quiz.configure(text=f"Evaluación: {self.temaActual}")
        self.lbl_resultado.configure(text="")
        self.btn_calificar.configure(state="normal", text="CALIFICAR RESPUESTAS")
        
        # Reiniciar lista de respuestas
        self.respuestas_usuario = [] 

        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas:
             ctk.CTkLabel(self.scroll_quiz, text="No hay preguntas disponibles para este tema.").pack(pady=20)
             self.btn_calificar.configure(state="disabled")
             self.mostrar_frame("quiz")
             return

        for i, p in enumerate(preguntas):
            card = ctk.CTkFrame(self.scroll_quiz, fg_color="#2b2b2b", border_width=1, border_color="#333")
            card.pack(fill="x", pady=10, padx=10)
            
            ctk.CTkLabel(card, text=f"{i+1}. {p['pregunta']}", font=("Roboto", 15, "bold"), wraplength=750, justify="left").pack(anchor="w", padx=15, pady=(15, 10))
            
            # Variable entera para guardar selección (value=0, 1, 2...)
            var = ctk.IntVar(value=-1) 
            self.respuestas_usuario.append(var)
            
            for j, op in enumerate(p['opciones']):
                # Radio button
                rb = ctk.CTkRadioButton(card, text=op, variable=var, value=j, font=("Roboto", 14))
                rb.pack(anchor="w", padx=25, pady=5)
            
            # Espacio extra abajo
            ctk.CTkLabel(card, text="").pack(pady=2)

        self.mostrar_frame("quiz")

    def calificar(self):
        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas: return

        correctas = 0
        minimo_aprobar = 2 # Según JS original
        total_preguntas = len(preguntas)
        
        sin_responder = False
        
        for i, p in enumerate(preguntas):
            seleccion = self.respuestas_usuario[i].get()
            if seleccion == -1:
                sin_responder = True
            elif seleccion == p['respuestaCorrecta']:
                correctas += 1
        
        if sin_responder:
            # Opcional: Avisar si faltan
            pass 

        # Lógica de Puntos
        if self.temaActual in self.quizzesCompletados:
             self.lbl_resultado.configure(text=f"Resultado: {correctas}/{total_preguntas}. (Ya completado previamente)", text_color="gray")
        else:
            if correctas >= minimo_aprobar:
                puntos_ganados = correctas * 10
                self.puntajeTotal += puntos_ganados
                self.quizzesCompletados.add(self.temaActual)
                
                self.lbl_resultado.configure(text=f"¡APROBADO! ✅ {correctas}/{total_preguntas} correctas. (+{puntos_ganados} pts)", text_color="#2ecc71")
                
                # Actualizar estado del Diploma
                self.actualizar_boton_diploma()
                
            else:
                self.lbl_resultado.configure(text=f"REPROBADO ❌ {correctas}/{total_preguntas}. Necesitas {minimo_aprobar} buenas.", text_color="#e74c3c")
        
        self.btn_calificar.configure(state="disabled", text="EVALUACIÓN FINALIZADA")

    def actualizar_boton_diploma(self):
        if self.puntajeTotal >= self.PUNTAJE_PARA_DIPLOMA:
            self.btn_diploma.configure(state="normal", text="🏆 ¡VER MI DIPLOMA! (Meta Alcanzada)", fg_color="#f1c40f", text_color="black")
        else:
             self.btn_diploma.configure(text=f"🏆 Diploma ({self.puntajeTotal}/{self.PUNTAJE_PARA_DIPLOMA} pts)")

    # =================================================================
    # 5. PANTALLA DIPLOMA
    # =================================================================
    def setup_diploma(self, frame):
        # Fondo tipo papel
        bg = ctk.CTkFrame(frame, fg_color="#ecf0f1", corner_radius=10) 
        bg.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.85)

        # Contenido del diploma (Texto oscuro sobre fondo claro)
        ctk.CTkLabel(bg, text="⚖️", font=("Arial", 80)).pack(pady=(40, 10))
        ctk.CTkLabel(bg, text="UNIVERSIDAD DE SAN CARLOS DE GUATEMALA", font=("Times New Roman", 20, "bold"), text_color="black").pack()
        ctk.CTkLabel(bg, text="FACULTAD DE CIENCIAS JURÍDICAS Y SOCIALES", font=("Times New Roman", 14), text_color="#2c3e50").pack(pady=5)
        
        ctk.CTkLabel(bg, text="OTORGA EL PRESENTE", font=("Arial", 12), text_color="#7f8c8d").pack(pady=(30, 5))
        ctk.CTkLabel(bg, text="DIPLOMA DE MÉRITO", font=("Times New Roman", 40, "bold"), text_color="#c0392b").pack(pady=5)
        
        ctk.CTkLabel(bg, text="A:", font=("Arial", 14), text_color="#7f8c8d").pack(pady=5)
        self.lbl_nombre_diploma = ctk.CTkLabel(bg, text="NOMBRE ESTUDIANTE", font=("Zapfino", 30, "bold"), text_color="#2980b9") # Fuente script si disponible o cursiva
        self.lbl_nombre_diploma.pack(pady=10)

        texto_cuerpo = "Por haber completado satisfactoriamente los módulos de aprendizaje interactivo de Introducción al Derecho."
        ctk.CTkLabel(bg, text=texto_cuerpo, font=("Arial", 16), text_color="black", wraplength=600).pack(pady=20)

        self.lbl_fecha_diploma = ctk.CTkLabel(bg, text="Fecha", font=("Arial", 12), text_color="black")
        self.lbl_fecha_diploma.pack(pady=(30, 10))

        # Botón Volver
        ctk.CTkButton(frame, text="Volver al Menú", command=lambda: self.mostrar_frame("menu"), fg_color="#2c3e50").place(relx=0.5, rely=0.92, anchor="center")

    def cargar_diploma_datos(self):
        # Método auxiliar si se necesitara actualizar algo específico antes de mostrar
        pass

    # =================================================================
    # 6. PANTALLA EQUIPO (MODERNA)
    # =================================================================
    def setup_equipo(self, frame):
        ctk.CTkButton(frame, text="← Volver al Menú", command=lambda: self.mostrar_frame("menu"), width=120, fg_color="#7f8c8d").pack(anchor="nw", padx=30, pady=20)
        
        ctk.CTkLabel(frame, text="EQUIPO DE DESARROLLO", font=("Roboto", 30, "bold")).pack(pady=(0, 20))
        
        scroll = ctk.CTkScrollableFrame(frame, width=900)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        self.frame_integrantes = scroll 

    def cargar_equipo(self):
        for widget in self.frame_integrantes.winfo_children():
            widget.destroy()

        for dev in INFO_EQUIPO["desarrolladores"]:
            # Tarjeta
            card = ctk.CTkFrame(self.frame_integrantes, fg_color="#2b2b2b")
            card.pack(fill="x", pady=15, padx=10)
            
            # --- IMAGEN (Lado Izquierdo) ---
            try:
                if os.path.exists(dev["foto"]):
                    pil_image = Image.open(dev["foto"])
                    # TAMAÑO AUMENTADO PARA VERSE MEJOR (120x150 vertical o 120x120 cuadrado)
                    # Usamos 120x150 para que parezca foto tipo carnet/retrato
                    ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(120, 150))
                    lbl_img = ctk.CTkLabel(card, text="", image=ctk_image)
                else:
                    # Placeholder si no hay foto
                    lbl_img = ctk.CTkLabel(card, text="[Sin Foto]", width=120, height=150, fg_color="#444", corner_radius=5)
                
                lbl_img.pack(side="left", padx=20, pady=20)
            except Exception as e:
                print(f"Error imagen {dev['nombre']}: {e}")
                ctk.CTkLabel(card, text="Err", width=120, height=150, fg_color="red").pack(side="left", padx=20)

            # --- INFO (Lado Derecho) ---
            info_frame = ctk.CTkFrame(card, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, pady=20, padx=10)

            ctk.CTkLabel(info_frame, text=dev["nombre"], font=("Roboto", 20, "bold"), anchor="w", text_color="#3498db").pack(fill="x")
            ctk.CTkLabel(info_frame, text=dev["rol"], font=("Roboto", 16, "italic"), anchor="w").pack(fill="x", pady=(5, 0))
            
            # Datos extra
            ctk.CTkLabel(info_frame, text=f"Carné USAC: {dev['carnet']}", font=("Roboto", 14), anchor="w").pack(fill="x", pady=(10, 0))
            ctk.CTkLabel(info_frame, text=f"Contacto: {dev['correo']}", font=("Roboto", 14), anchor="w", text_color="gray").pack(fill="x")

        self.mostrar_frame("equipo")


if __name__ == "__main__":
    app = EncartaFinalApp()
    app.mainloop()
