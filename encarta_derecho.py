import customtkinter as ctk
from PIL import Image
import os
from datetime import datetime
import ctypes
# =================================================================
# CONFIGURACIÓN VISUAL
# =================================================================
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

# =================================================================
# 1. BASE DE DATOS DE CONTENIDO (AMPLIADA Y DETALLADA)
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
        "1. ETIMOLOGÍA\n"
        "La palabra Derecho proviene del vocablo latino 'directum', que significa «no apartarse del buen camino», «seguir el sendero señalado por la ley» o «lo que está conforme a la regla».\n\n"
        "2. DEFINICIÓN\n"
        "En sentido general, el Derecho es el conjunto de normas jurídicas, creadas por el Estado, para regular la conducta externa de los hombres en sociedad. A diferencia de otras normas, estas cuentan con la posibilidad de imponerse por la fuerza en caso de incumplimiento.\n\n"
        "3. LOS FINES DEL DERECHO\n"
        "El Derecho no es un fin en sí mismo, sino un medio para alcanzar valores superiores:\n"
        "• Justicia: Es la voluntad constante de dar a cada quien lo que le corresponde.\n"
        "• Seguridad Jurídica: Es la garantía que tiene el individuo de que su persona, sus bienes y sus derechos no serán objeto de ataques violentos o que, si estos llegan a producirse, le serán asegurados por la sociedad (certeza de la ley).\n"
        "• Bien Común: Es el conjunto de condiciones sociales que permiten y favorecen en los seres humanos el desarrollo integral de todos y cada uno de los miembros de la comunidad.",

    "1.2 Normas Jurídicas vs. Normas Morales": 
        "DIFERENCIAS FUNDAMENTALES\n\n"
        "Para comprender el Derecho, es vital distinguirlo de la Moral. Aunque ambas regulan la conducta humana, sus características son opuestas en puntos clave:\n\n"
        "A. NORMAS MORALES\n"
        "• Unilaterales: Imponen deberes pero no conceden derechos. Nadie puede exigir su cumplimiento.\n"
        "• Internas: Regulan las intenciones y la conciencia del individuo (pensamientos).\n"
        "• Incoercibles: No se puede usar la fuerza pública para obligar a cumplirlas. Su sanción es el remordimiento o el rechazo social (como no saludar a un vecino).\n\n"
        "B. NORMAS JURÍDICAS\n"
        "• Bilaterales: Imponen deberes y conceden derechos (si yo te vendo, tú tienes derecho a recibir y yo a cobrar).\n"
        "• Externas: Regulan la conducta manifestada exteriormente (actos), no los pensamientos.\n"
        "• COERCIBLES: Esta es su característica principal. Significa que, si no se cumplen voluntariamente, el Estado tiene la facultad de obligar su cumplimiento por la fuerza pública (policía, jueces, embargos).",

    "1.3 Fuentes del Derecho": 
        "¿DE DÓNDE NACE LA LEY?\n"
        "Se denomina 'Fuentes del Derecho' a los acontecimientos, documentos y procesos de los cuales surgen las normas jurídicas. Se clasifican en tres:\n\n"
        "1. FUENTES REALES\n"
        "Son los factores y elementos (sociales, políticos, económicos, culturales) que determinan el contenido de las normas. Ejemplo: Una crisis económica o una revolución que obliga a crear nuevas leyes.\n\n"
        "2. FUENTES HISTÓRICAS\n"
        "Son los documentos del pasado (papiros, inscripciones, libros) que contienen textos de leyes antiguas y que sirven de base para las actuales. El ejemplo más famoso es el Derecho Romano.\n\n"
        "3. FUENTES FORMALES\n"
        "Son los procesos de creación de las normas jurídicas. En Guatemala, la fuente formal por excelencia es la Legislación (el proceso de crear leyes), el cual es competencia exclusiva del Organismo Legislativo (Congreso).",

    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": 
        "EL ORDENAMIENTO JURÍDICO\n"
        "Las leyes no tienen el mismo valor; existe una jerarquía. Hans Kelsen ideó una pirámide para explicar que una norma inferior no puede contradecir a una superior.\n\n"
        "NIVEL 1: CONSTITUCIONAL (La Cúspide)\n"
        "Es la norma suprema. Incluye la Constitución Política de la República de Guatemala (CPRG) y los tratados internacionales sobre Derechos Humanos. Ninguna ley puede estar por encima de ella.\n\n"
        "NIVEL 2: ORDINARIO\n"
        "Son las leyes creadas por el Congreso de la República (Organismo Legislativo). Ejemplos: Código Civil, Código Penal, Código de Trabajo.\n\n"
        "NIVEL 3: REGLAMENTARIO\n"
        "Son disposiciones creadas por el Organismo Ejecutivo (Presidente y Ministros) para facilitar la aplicación de las leyes ordinarias. Ejemplo: Reglamento de Tránsito.\n\n"
        "NIVEL 4: INDIVIDUALIZADO\n"
        "Normas que aplican a personas específicas: Sentencias judiciales o contratos.",

    "2.1 ¿Qué es la Constitución?": 
        "LA CARTA MAGNA\n"
        "Es la ley suprema y fundamental de un Estado. La actual Constitución de Guatemala fue promulgada el 31 de mayo de 1985 y entró en vigencia en 1986.\n\n"
        "ESTRUCTURA DE LA CONSTITUCIÓN\n"
        "Se divide técnicamente en tres partes:\n\n"
        "1. PARTE DOGMÁTICA (Arts. 1-139)\n"
        "Contiene los derechos humanos fundamentales y las libertades de los ciudadanos. Es la parte que protege a la persona frente al Estado.\n\n"
        "2. PARTE ORGÁNICA (Arts. 140-262)\n"
        "Establece la estructura y organización del Estado, dividiendo los poderes (Ejecutivo, Legislativo y Judicial) para evitar abusos.\n\n"
        "3. PARTE PRÁCTICA (Arts. 263-281)\n"
        "Establece las Garantías Constitucionales, que son los mecanismos para defender la Constitución (Amparo, Exhibición Personal, Inconstitucionalidad).",

    "2.2 Derechos Humanos Individuales": 
        "DERECHOS INHERENTES\n"
        "Son facultades y libertades propias de la persona humana por el simple hecho de serlo; el Estado no los 'regala', solo los reconoce y garantiza.\n\n"
        "PRINCIPALES DERECHOS EN LA CPRG:\n"
        "• Derecho a la Vida (Art. 3): El Estado garantiza y protege la vida humana desde su concepción.\n"
        "• Libertad e Igualdad (Art. 4): En Guatemala todos los seres humanos son libres e iguales en dignidad y derechos.\n"
        "• Derecho de Defensa (Art. 12): Nadie podrá ser condenado, ni privado de sus derechos, sin haber sido citado, oído y vencido en proceso legal.\n"
        "• Presunción de Inocencia (Art. 14): Toda persona es inocente mientras no se le haya declarado responsable judicialmente en sentencia debidamente ejecutoriada.",

    "2.3 La Organización del Estado": 
        "SEPARACIÓN DE PODERES\n"
        "Guatemala es una república soberana. Para evitar la tiranía, el poder público proviene del pueblo y se divide en tres organismos independientes (Teoría de Pesos y Contrapesos):\n\n"
        "1. ORGANISMO LEGISLATIVO\n"
        "Su función esencial es crear, reformar y derogar las leyes. Está representado por el Congreso de la República, compuesto por diputados electos por el pueblo.\n\n"
        "2. ORGANISMO EJECUTIVO\n"
        "Su función es administrativa y política; se encarga de administrar el Estado y ejecutar las políticas públicas. Lo encabeza el Presidente de la República, el Vicepresidente y los Ministros.\n\n"
        "3. ORGANISMO JUDICIAL\n"
        "Su función exclusiva es juzgar y promover la ejecución de lo juzgado (impartir justicia). Lo ejerce la Corte Suprema de Justicia y los demás tribunales.",

    "2.4 Corte de Constitucionalidad": 
        "EL GUARDIÁN DE LA CONSTITUCIÓN\n"
        "La Corte de Constitucionalidad (CC) es un tribunal permanente de jurisdicción privativa. Es el máximo tribunal en materia constitucional en Guatemala.\n\n"
        "FUNCIONES CLAVE:\n"
        "• Su función esencial es la defensa del orden constitucional.\n"
        "• Actúa como un tribunal independiente de los demás organismos del Estado (no depende del Congreso ni del Presidente).\n"
        "• Conoce amparos e inconstitucionalidades de leyes que atenten contra la Carta Magna.\n"
        "• Sus magistrados son designados por los tres poderes del Estado, la USAC y el Colegio de Abogados."
}

# =================================================================
# 2. BASE DE DATOS DE QUIZZES
# =================================================================

BASE_DE_DATOS_QUIZZES = {
    "1.1 Origen y Definición del Derecho": [
        {"pregunta": "¿Qué significa el vocablo latino 'directum'?", "opciones": ["Torcido", "No apartarse del buen camino", "Ley de Talión"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Cuál es el fin del Derecho que busca dar a cada quien lo suyo?", "opciones": ["Bien Común", "Justicia", "Seguridad"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Quién crea las normas jurídicas?", "opciones": ["El Estado", "La Iglesia", "La Familia"], "respuestaCorrecta": 0 }
    ],
    "1.2 Normas Jurídicas vs. Normas Morales": [
        {"pregunta": "¿Qué característica permite al Estado usar la fuerza si no cumples la ley?", "opciones": ["Unilateralidad", "Coercibilidad", "Interioridad"], "respuestaCorrecta": 1 },
        {"pregunta": "Si no saludo a mi vecino, incumplo una norma:", "opciones": ["Jurídica", "Penal", "Moral o de trato social"], "respuestaCorrecta": 2 },
        {"pregunta": "Las normas jurídicas regulan la conducta:", "opciones": ["Interna (pensamientos)", "Externa (actos)", "Sentimental"], "respuestaCorrecta": 1 }
    ],
    "1.3 Fuentes del Derecho": [
        {"pregunta": "¿Qué fuente del Derecho describe el proceso legislativo de creación de la ley?", "opciones": ["Reales", "Históricas", "Formales"], "respuestaCorrecta": 2 },
        {"pregunta": "El Derecho Romano (documentos antiguos) es un ejemplo de fuente:", "opciones": ["Histórica", "Real", "Formal"], "respuestaCorrecta": 0 },
        {"pregunta": "¿Qué organismo tiene la competencia de crear leyes (legislación)?", "opciones": ["Ejecutivo", "Legislativo (Congreso)", "Judicial"], "respuestaCorrecta": 1 }
    ],
    "1.4 Jerarquía Normativa (Pirámide de Kelsen)": [
        {"pregunta": "Según la pirámide de Kelsen, ¿cuál es la norma suprema?", "opciones": ["Código Civil", "Constitución (CPRG)", "Reglamentos"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Puede una ley ordinaria contradecir a la Constitución?", "opciones": ["Sí, siempre", "No, nunca", "A veces"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué nivel ocupan los reglamentos creados por el Ejecutivo?", "opciones": ["Nivel 1 (Constitucional)", "Nivel 2 (Ordinario)", "Nivel 3 (Reglamentario)"], "respuestaCorrecta": 2 }
    ],
    "2.1 ¿Qué es la Constitución?": [
        {"pregunta": "¿En qué año fue promulgada la Constitución actual de Guatemala?", "opciones": ["1944", "1985", "2020"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué parte de la Constitución organiza el Estado y divide poderes?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué parte contiene los Derechos Humanos fundamentales?", "opciones": ["Dogmática", "Orgánica", "Práctica"], "respuestaCorrecta": 0 }
    ],
    "2.2 Derechos Humanos Individuales": [
        {"pregunta": "¿En qué artículo de la CPRG se garantiza el derecho a la vida?", "opciones": ["Artículo 1", "Artículo 3", "Artículo 10"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué derecho implica que nadie puede ser condenado sin ser oído y vencido?", "opciones": ["Derecho de Petición", "Libertad de Emoción", "Derecho de Defensa"], "respuestaCorrecta": 2 },
        {"pregunta": "¿Hasta cuándo se considera inocente a una persona?", "opciones": ["Hasta que la policía lo detiene", "Hasta que es citado", "Hasta ser declarado responsable en sentencia"], "respuestaCorrecta": 2 }
    ],
    "2.3 La Organización del Estado": [
        {"pregunta": "¿Qué organismo tiene la función de crear leyes?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Qué organismo administra el Estado y ejecuta políticas?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 0 },
        {"pregunta": "¿Qué organismo tiene la función exclusiva de juzgar?", "opciones": ["Ejecutivo", "Legislativo", "Judicial"], "respuestaCorrecta": 2 }
    ],
    "2.4 Corte de Constitucionalidad": [
        {"pregunta": "¿Cuál es la función esencial de la CC?", "opciones": ["Aprobar leyes ordinarias", "Defensa del orden constitucional", "Juzgar delitos comunes"], "respuestaCorrecta": 1 },
        {"pregunta": "¿La CC depende del Presidente para tomar decisiones?", "opciones": ["Sí", "No, es independiente", "A veces"], "respuestaCorrecta": 1 },
        {"pregunta": "¿Es la CC el máximo tribunal en materia constitucional?", "opciones": ["Sí", "No", "Depende"], "respuestaCorrecta": 0 }
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
        
        # El archivo logo.ico debe estar en la misma carpeta
        if os.path.exists("derecho.ico"):
            self.iconbitmap("derecho.ico")
        # --- Variables de Lógica ---
        self.PUNTAJE_PARA_DIPLOMA = 170
        self.puntajeTotal = 0
        self.temaActual = ""
        self.quizzesCompletados = set()
        self.nombre_usuario = ""
        
        # Almacenará las variables IntVars de los radiobuttons
        self.respuestas_usuario = [] 

        # --- DICCIONARIO PARA BOTONES ---
        self.botones_temas = {} 

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
        """Crea el logo en la esquina inferior derecha que persiste."""
        try:
            if os.path.exists("logo.png"):
                pil_img = Image.open("logo.png")
                logo_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(100, 100))
                
                self.lbl_watermark = ctk.CTkLabel(self, text="", image=logo_img)
                self.lbl_watermark.place(relx=0.98, rely=0.98, anchor="se")
            else:
                print("Advertencia: No se encontró 'logo.png'.")
        except Exception as e:
            print(f"Error cargando marca de agua: {e}")

    def crear_frames(self):
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
        
        # Control de Logo: Ocultar solo en diploma
        if hasattr(self, 'lbl_watermark'):
            if nombre == "diploma":
                self.lbl_watermark.place_forget() 
            else:
                self.lbl_watermark.place(relx=0.98, rely=0.98, anchor="se")
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
            return 
        self.nombre_usuario = nombre
        self.lbl_saludo_menu.configure(text=f"¡Bienvenido, {nombre}!")
        self.mostrar_frame("menu")

    # =================================================================
    # 2. PANTALLA MENÚ
    # =================================================================
    def setup_menu(self, frame):
        # Header
        header = ctk.CTkFrame(frame, height=80, corner_radius=0, fg_color="#1a1a1a")
        header.pack(fill="x", side="top")
        
        ctk.CTkLabel(header, text="MENÚ PRINCIPAL", font=("Roboto", 24, "bold")).pack(side="left", padx=30, pady=20)
        self.lbl_saludo_menu = ctk.CTkLabel(header, text="", font=("Roboto", 16), text_color="#3498db")
        self.lbl_saludo_menu.pack(side="right", padx=30)

        # Contenido
        scroll = ctk.CTkScrollableFrame(frame, width=900)
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        for modulo in MODULOS:
            ctk.CTkLabel(scroll, text=modulo["titulo"], font=("Roboto", 22, "bold"), anchor="w", text_color="#ecf0f1").pack(fill="x", pady=(20, 10))
            
            grid_frame = ctk.CTkFrame(scroll, fg_color="transparent")
            grid_frame.pack(fill="x")
            
            for i, tema in enumerate(modulo["temas"]):
                btn = ctk.CTkButton(grid_frame, text=tema, command=lambda t=tema: self.cargar_teoria(t), 
                                    height=60, font=("Roboto", 14), fg_color="#2c3e50", hover_color="#34495e")
                btn.grid(row=i//2, column=i%2, padx=10, pady=10, sticky="ew")
                
                # GUARDAR REFERENCIA AL BOTÓN
                self.botones_temas[tema] = btn
            
            grid_frame.grid_columnconfigure(0, weight=1)
            grid_frame.grid_columnconfigure(1, weight=1)

        # Footer
        footer = ctk.CTkFrame(frame, height=80, fg_color="transparent")
        footer.pack(fill="x", pady=20, padx=20)
        
        self.btn_diploma = ctk.CTkButton(footer, text="🏆 VER DIPLOMA (Bloqueado)", state="disabled", 
                                         command=self.ver_diploma, fg_color="#7f8c8d", height=50)
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
        for widget in self.scroll_quiz.winfo_children():
            widget.destroy()
        
        self.lbl_titulo_quiz.configure(text=f"Evaluación: {self.temaActual}")
        self.lbl_resultado.configure(text="")
        self.btn_calificar.configure(state="normal", text="CALIFICAR RESPUESTAS")
        self.respuestas_usuario = [] 

        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas:
             ctk.CTkLabel(self.scroll_quiz, text="No hay preguntas disponibles.").pack(pady=20)
             self.btn_calificar.configure(state="disabled")
             self.mostrar_frame("quiz")
             return

        for i, p in enumerate(preguntas):
            card = ctk.CTkFrame(self.scroll_quiz, fg_color="#2b2b2b", border_width=1, border_color="#333")
            card.pack(fill="x", pady=10, padx=10)
            
            ctk.CTkLabel(card, text=f"{i+1}. {p['pregunta']}", font=("Roboto", 15, "bold"), wraplength=750, justify="left").pack(anchor="w", padx=15, pady=(15, 10))
            
            var = ctk.IntVar(value=-1) 
            self.respuestas_usuario.append(var)
            
            for j, op in enumerate(p['opciones']):
                rb = ctk.CTkRadioButton(card, text=op, variable=var, value=j, font=("Roboto", 14))
                rb.pack(anchor="w", padx=25, pady=5)
            
            ctk.CTkLabel(card, text="").pack(pady=2)

        self.mostrar_frame("quiz")

    def calificar(self):
        preguntas = BASE_DE_DATOS_QUIZZES.get(self.temaActual, [])
        if not preguntas: return

        correctas = 0
        minimo_aprobar = 2 
        total_preguntas = len(preguntas)
        
        for i, p in enumerate(preguntas):
            seleccion = self.respuestas_usuario[i].get()
            if seleccion == p['respuestaCorrecta']:
                correctas += 1
        
        if self.temaActual in self.quizzesCompletados:
             self.lbl_resultado.configure(text=f"Resultado: {correctas}/{total_preguntas}. (Ya completado previamente)", text_color="gray")
        else:
            if correctas >= minimo_aprobar:
                puntos_ganados = correctas * 10
                self.puntajeTotal += puntos_ganados
                self.quizzesCompletados.add(self.temaActual)
                self.lbl_resultado.configure(text=f"¡APROBADO! ✅ {correctas}/{total_preguntas} correctas. (+{puntos_ganados} pts)", text_color="#2ecc71")
                
                # --- CAMBIAR COLOR DEL BOTÓN DEL MENÚ ---
                if self.temaActual in self.botones_temas:
                    self.botones_temas[self.temaActual].configure(fg_color="#27ae60", hover_color="#2ecc71")
                
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
        # Fondo papel
        bg = ctk.CTkFrame(frame, fg_color="#ecf0f1", corner_radius=10) 
        bg.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.85)

        # Contenido
        ctk.CTkLabel(bg, text="⚖️", font=("Arial", 80)).pack(pady=(40, 10))
        ctk.CTkLabel(bg, text="UNIVERSIDAD DE SAN CARLOS DE GUATEMALA", font=("Times New Roman", 20, "bold"), text_color="black").pack()
        ctk.CTkLabel(bg, text="FACULTAD DE CIENCIAS JURÍDICAS Y SOCIALES", font=("Times New Roman", 14), text_color="#2c3e50").pack(pady=5)
        
        ctk.CTkLabel(bg, text="OTORGA EL PRESENTE", font=("Arial", 12), text_color="#7f8c8d").pack(pady=(30, 5))
        ctk.CTkLabel(bg, text="DIPLOMA DE MÉRITO", font=("Times New Roman", 40, "bold"), text_color="#c0392b").pack(pady=5)
        
        ctk.CTkLabel(bg, text="A:", font=("Arial", 14), text_color="#7f8c8d").pack(pady=5)
        
        self.lbl_nombre_diploma = ctk.CTkLabel(bg, text="NOMBRE ESTUDIANTE", font=("Arial", 30, "bold"), text_color="#2980b9")
        self.lbl_nombre_diploma.pack(pady=10)

        texto_cuerpo = "Por haber completado satisfactoriamente los módulos de aprendizaje interactivo de Introducción al Derecho."
        ctk.CTkLabel(bg, text=texto_cuerpo, font=("Arial", 16), text_color="black", wraplength=600).pack(pady=20)

        self.lbl_fecha_diploma = ctk.CTkLabel(bg, text="Fecha", font=("Arial", 12), text_color="black")
        self.lbl_fecha_diploma.pack(pady=(30, 10))

        ctk.CTkButton(frame, text="Volver al Menú", command=lambda: self.mostrar_frame("menu"), fg_color="#2c3e50").place(relx=0.5, rely=0.92, anchor="center")

    def ver_diploma(self):
        nombre_final = self.nombre_usuario if self.nombre_usuario else "Estudiante de Derecho"
        self.lbl_nombre_diploma.configure(text=nombre_final.upper())

        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        now = datetime.now()
        fecha_str = f"Guatemala, {now.day} de {meses[now.month-1]} de {now.year}"
        self.lbl_fecha_diploma.configure(text=fecha_str)

        self.mostrar_frame("diploma")

    # =================================================================
    # 6. PANTALLA EQUIPO
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
            card = ctk.CTkFrame(self.frame_integrantes, fg_color="#2b2b2b")
            card.pack(fill="x", pady=15, padx=10)
            
            try:
                if os.path.exists(dev["foto"]):
                    pil_image = Image.open(dev["foto"])
                    ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(120, 150))
                    lbl_img = ctk.CTkLabel(card, text="", image=ctk_image)
                else:
                    lbl_img = ctk.CTkLabel(card, text="[Sin Foto]", width=120, height=150, fg_color="#444", corner_radius=5)
                lbl_img.pack(side="left", padx=20, pady=20)
            except Exception as e:
                print(f"Error imagen {dev['nombre']}: {e}")
                ctk.CTkLabel(card, text="Err", width=120, height=150, fg_color="red").pack(side="left", padx=20)

            info_frame = ctk.CTkFrame(card, fg_color="transparent")
            info_frame.pack(side="left", fill="both", expand=True, pady=20, padx=10)

            ctk.CTkLabel(info_frame, text=dev["nombre"], font=("Roboto", 20, "bold"), anchor="w", text_color="#3498db").pack(fill="x")
            ctk.CTkLabel(info_frame, text=dev["rol"], font=("Roboto", 16, "italic"), anchor="w").pack(fill="x", pady=(5, 0))
            ctk.CTkLabel(info_frame, text=f"Carné USAC: {dev['carnet']}", font=("Roboto", 14), anchor="w").pack(fill="x", pady=(10, 0))
            ctk.CTkLabel(info_frame, text=f"Contacto: {dev['correo']}", font=("Roboto", 14), anchor="w", text_color="gray").pack(fill="x")

        self.mostrar_frame("equipo")

if __name__ == "__main__":
    try:
        
        my_appid = 'usac.derecho.proyecto.encarta.v1' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_appid)
    except Exception as e:
        pass 
    app = EncartaFinalApp()
    app.mainloop()