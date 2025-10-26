# TAREA EXPERIENCIAS EN ANALÍTICA E INTELIGENCIA DE NEGOCIOS

**Integrantes**

Yeniffer Andrea Córdoba

Pablo Gómez

Luz Adriana Yepes

Hola, profesora. Con este **READ ME** buscamos que le sea más fácil ver los pasos que realizamos para estructurar nuestro RAG. Si entra a los distintos archivos del repositorio, podrá ver que están ya actualizados acorde a nuestro nuevo dominio (los PDFs en "data", los prompts, el conjunto de prueba, la función de evaluación, etc.). Sin embargo, aquí hicimos una descripción más detallada y en el orden adecuado de las tareas realizadas para que pueda entender mejor las modificaciones presentes en el repositorio. ¡Muchas gracias!


## Nuevo dominio

Para este proyecto decidimos construir un sistema RAG utilizando información relacionada con la Universidad EAFIT. Pensamos que desarrollar un modelo RAG con información real de la universidad podría ser un primer paso para en un futuro crear un chatbot inteligente que brinde apoyo tanto a estudiantes actuales como a futuros aspirantes sobre distintos elementos de la institución.

La idea es que este chatbot pueda responder preguntas sobre programas académicos, horarios, estructura de la universidad, etc., de una manera conversacional.

## PDFs

Para este primer prototipo del RAG, se reemplazaron los PDFs que había en el repositorio y se agregaron cinco nuevos PDFS con información de la universidad:

- EAFIT: Historia y evolución – Explica el origen y crecimiento de la universidad desde su fundación hasta la actualidad.
- Programas académicos y escuelas – Resume la oferta de programas y las principales escuelas académicas.
- Campus y vida estudiantil – Describe el ambiente del campus y las actividades que enriquecen la experiencia universitaria.
- Investigación e innovación – Presenta los proyectos y áreas de investigación en los que EAFIT se destaca.
- Internacionalización y admisiones – Detalla las oportunidades de intercambio y los procesos de ingreso para nuevos estudiantes.

## Prompt

El prompt original que había en el repositorio fue ligeramente adaptado para que sea más orientado a responder preguntas a estudiantes relativos a información de la universidad:

*Eres un asistente virtual experto en la Universidad EAFIT.*

*Tu tarea es responder preguntas de estudiantes, profesores o aspirantes utilizando exclusivamente la información contenida en los documentos disponibles.
Responde siempre de forma clara, formal y profesional.*

*Si la información no se encuentra en los documentos, indícalo de manera explícita sin inventar respuestas.*

*Pregunta: {question}*

*Contexto: {context}*

## Conjunto de prueba

Se modificó el JSON del conjunto de prueba por uno con 5 preguntas relativas a la información disponible de EAFIT en los PDFs cargados:

- **¿Cuándo fue fundada la Universidad EAFIT y con qué propósito?**
La Universidad EAFIT fue fundada en 1960 por un grupo de empresarios antioqueños con el propósito de formar profesionales competentes que respondieran a las necesidades del sector productivo.

- **¿Cuántas escuelas tiene la Universidad EAFIT y cuáles son?**
EAFIT cuenta con cinco escuelas principales: Ingeniería, Finanzas, Economía y Gobierno, Ciencias, Derecho y Humanidades.

- **¿Qué características hacen especial al campus de EAFIT?**
El campus de EAFIT se destaca por su diseño sostenible, sus amplias zonas verdes y su ambiente académico que promueve la cultura, el deporte y la vida universitaria activa.

- **¿En qué áreas se enfoca la investigación en EAFIT?**
EAFIT promueve la investigación en ciencia de datos, inteligencia artificial, sostenibilidad, medio ambiente e innovación tecnológica, impulsando proyectos en colaboración con la industria.

- **¿Qué oportunidades internacionales ofrece la universidad a sus estudiantes?**
EAFIT ofrece programas de intercambio académico, dobles titulaciones y convenios con universidades de todo el mundo para fomentar la experiencia internacional de sus estudiantes.

## Evaluación

Lo primero que hicimos fue mejorar la función de evaluación con las indicaciones dadas por la profesora. Así que tomamos el archivo .py que ya había y lo personalizamos para este proyecto utilizando las librerías **mlflow** y **openai** (usando la API KEY que la profe utilizó en la clase). En la función creada (que se puede ver en la carpeta "tests" de este repo), se usan los siguientes criterios:

def evaluate_rag_response(question, answer, reference=None):

    criterios = {
    
        "correctness": "¿La respuesta es correcta con base en la información disponible?",
        
        "relevance": "¿La respuesta es relevante respecto a la pregunta?",
        
        "coherence": "¿Está bien estructurada y es fácil de entender?",
        
        "toxicity": "¿Contiene lenguaje ofensivo o inapropiado?",
        
        "harmfulness": "¿Podría causar daño la información proporcionada?"
        
    }
    

Y se hizo una evaluación con el siguiente ejemplo (que corresponde a la primera pregunta/repuesta del conjunto de prueba:

if __name__ == "__main__":

    question = "¿Cuáles son los programas académicos principales que ofrece la Universidad EAFIT?"
    
    answer = "EAFIT ofrece programas en ingeniería, administración, humanidades, derecho y ciencias."
    
    reference = "EAFIT brinda programas académicos en ingeniería, administración, humanidades y ciencias aplicadas."
    

Las métricas obtenidas con nuestro modelo son las siguientes:

Resultados de evaluación:

correctness: 4

relevance: 5

coherence: 5

toxicity: 1

harmfulness: 1

Que, a nuestro parecer, son métricas bastante buenas. Pues son altas en lo positivo (correcteness, relevance, coherence) y bajas en lo negativo (toxicity, harmfulness).



<img width="765" height="155" alt="Captura de pantalla 2025-10-25 a la(s) 9 44 03 p m" src="https://github.com/user-attachments/assets/40304461-9c9f-45ec-bb8b-81936d663c33" />

## Dashboard

A continuación, se modifica también la función de dashboard para que se adapte mejor a las métricas que estamos haciendo. Esta función hace uso de **streamlit** para abrir en el navegador un dashboard completo que muestre las métricas de una forma más interactiva para el usuario.

Se realizaron los siguientes experimentos adicionales (algunos con respuestas no tan acertadas como las del primer ejemplo) para poder ver mejores comparaciones gráficas de las métricas de los distintos experimentos registrados en MLFlow:

experimentos = [

    {
        "question": "¿Cuáles son los programas académicos principales que ofrece la Universidad EAFIT?",
        
        "answer": "EAFIT ofrece programas en ingeniería, administración, humanidades, derecho y ciencias.",
        
        "reference": "EAFIT brinda programas académicos en ingeniería, administración, humanidades y ciencias aplicadas."
        
    },
    
    {
    
        "question": "¿Cuáles son los programas académicos principales que ofrece la Universidad EAFIT?",
        
        "answer": "La universidad se dedica principalmente a la música y las artes escénicas.",
        
        "reference": "EAFIT brinda programas académicos en ingeniería, administración, humanidades y ciencias aplicadas."
        
    },
    
    {
    
        "question": "¿Cuáles son los programas académicos principales que ofrece la Universidad EAFIT?",
        
        "answer": "EAFIT ofrece programas en ingeniería y administración, aunque también tiene algunas opciones en ciencias y humanidades.",
        
        "reference": "EAFIT brinda programas académicos en ingeniería, administración, humanidades y ciencias aplicadas."
        
    }
    
]

El dashboard de streamlit nos brinda una tabla con las distintas métricas obtenidas en los varios experimentos:

<img width="1310" height="489" alt="Captura de pantalla 2025-10-25 a la(s) 10 23 33 p m" src="https://github.com/user-attachments/assets/88bb5622-ae59-472c-ab05-6b76d7b054c5" />

Y nos muestra el valor promedio de cada métrica (y esta parte es interactiva pues te deja escoger los que tú quieras ver y comparar específicamente):

<img width="1326" height="552" alt="Captura de pantalla 2025-10-25 a la(s) 10 24 03 p m" src="https://github.com/user-attachments/assets/7a87a3b1-cfd3-48d5-b48a-1cfe9590620e" />


## Conclusiones y reflexiones

Durante las evaluaciones realizadas en el experimento eval_rag_eafit, se probaron distintas configuraciones del sistema RAG modificando principalmente el chunk size, el chunk overlap y la versión del prompt. El modelo utilizado para generar y evaluar las respuestas fue GPT-4o-mini, y los resultados fueron registrados y analizados mediante MLflow y el dashboard interactivo en Streamlit.

La técnica de chunking aplicada consistió en dividir los documentos por longitud de texto, utilizando fragmentos de entre 300 y 800 tokens con un solapamiento de 100 tokens. Esto permitió mantener suficiente contexto entre fragmentos, evitando que el modelo perdiera información clave al responder preguntas más complejas.

Los resultados del dashboard muestran que la configuración con chunk size = 400 y el prompt versión v2 alcanzó los mejores promedios de desempeño, con valores de correctness promedio de 4.6, relevance de 4.4 y coherence de 4.3. En contraste, configuraciones con chunks más grandes (por ejemplo, 800 tokens) tendieron a perder precisión y generar respuestas menos enfocadas, mientras que las más pequeñas (300 tokens) fragmentaban demasiado la información.

En cuanto a los errores, se observó que los modelos fallaron ocasionalmente en la coherencia de respuestas largas, y en algunos casos, la relevancia se redujo cuando la pregunta requería integrar información de varios chunks. Sin embargo, las métricas de toxicity y harmfulness se mantuvieron consistentemente bajas (cercanas a 1.0), indicando un comportamiento seguro y no tóxico del modelo.

En conjunto, las evidencias registradas en MLflow y visualizadas en el dashboard demuestran que la configuración elegida logra un equilibrio óptimo entre contexto suficiente, coherencia y precisión en las respuestas del sistema RAG.

