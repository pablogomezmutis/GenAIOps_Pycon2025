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

Y nos muestra el valore promedio de cada métrica:

<img width="1326" height="552" alt="Captura de pantalla 2025-10-25 a la(s) 10 24 03 p m" src="https://github.com/user-attachments/assets/7a87a3b1-cfd3-48d5-b48a-1cfe9590620e" />


# 🤖 Chatbot GenAI - Caso de Estudio Recursos Humanos

Este proyecto demuestra cómo construir, evaluar y automatizar un chatbot de tipo RAG (Retrieval Augmented Generation) con buenas prácticas de **GenAIOps**.

---

## 🧠 Caso de Estudio

El chatbot responde preguntas sobre beneficios, políticas internas y roles de una empresa ficticia (**Contoso Electronics**), usando como base una colección de documentos PDF internos.

---

## 📂 Estructura del Proyecto

```
├── app/
│   ├── ui_streamlit.py           ← interfaz simple del chatbot
│   ├── main_interface.py         ← interfaz combinada con métricas
│   ├── run_eval.py               ← evaluación automática
│   ├── rag_pipeline.py           ← lógica de ingestión y RAG
│   └── prompts/
│       ├── v1_asistente_rrhh.txt
│       └── v2_resumido_directo.txt
├── data/pdfs/                    ← documentos fuente
├── tests/
│   ├── test_run_eval.py
│   ├── eval_dataset.json         ← dataset de evaluación
│   └── eval_dataset.csv
├── .env.example
├── Dockerfile
├── .devcontainer/
│   └── devcontainer.json
├── .github/workflows/
│   ├── eval.yml
│   └── test.yml
```

---

## 🚦 Ciclo de vida GenAIOps aplicado

### 1. 🧱 Preparación del entorno

```bash
git clone https://github.com/darkanita/GenAIOps_Pycon2025 chatbot-genaiops
cd chatbot-genaiops
conda create -n chatbot-genaiops python=3.10 -y
conda activate chatbot-genaiops
pip install -r requirements.txt
cp .env.example .env  # Agrega tu API KEY de OpenAI
```

---

### 2. 🔍 Ingesta y vectorización de documentos

Procesa los PDFs y genera el índice vectorial:

```bash
python -c "from app.rag_pipeline import save_vectorstore; save_vectorstore()"
```

Esto:
- Divide los documentos en chunks (por defecto `chunk_size=512`, `chunk_overlap=50`)
- Genera embeddings con OpenAI
- Guarda el índice vectorial en `vectorstore/`
- Registra los parámetros en **MLflow**

🔧 Para personalizar:
```python
save_vectorstore(chunk_size=1024, chunk_overlap=100)
```

♻️ Para reutilizarlo directamente:
```python
vectordb = load_vectorstore_from_disk()
```

---

### 3. 🧠 Construcción del pipeline RAG

```python
from app.rag_pipeline import build_chain
chain = build_chain(vectordb, prompt_version="v1_asistente_rrhh")
```

- Soporta múltiples versiones de prompt
- Usa `ConversationalRetrievalChain` con `LangChain` + `OpenAI`

---

### 4. 💬 Interacción vía Streamlit

Versión básica:
```bash
streamlit run app/ui_streamlit.py
```

Versión combinada con métricas:
```bash
streamlit run app/main_interface.py
```

---

### 5. 🧪 Evaluación automática de calidad

Ejecuta:

```bash
python app/run_eval.py
```

Esto:
- Usa `tests/eval_dataset.json` como ground truth
- Genera respuestas usando el RAG actual
- Evalúa con `LangChain Eval (QAEvalChain)`
- Registra resultados en **MLflow**

---

### 6. 📈 Visualización de resultados

Dashboard completo:

```bash
streamlit run app/dashboard.py
```

- Tabla con todas las preguntas evaluadas
- Gráficos de precisión por configuración (`prompt + chunk_size`)
- Filtrado por experimento MLflow

---

### 7. 🔁 Automatización con GitHub Actions

- CI de evaluación: `.github/workflows/eval.yml`
- Test unitarios: `.github/workflows/test.yml`

---

### 8. 🧪 Validación automatizada

```bash
pytest tests/test_run_eval.py
```

- Evalúa que el sistema tenga al menos 80% de precisión con el dataset base

---

## 🔍 ¿Qué puedes hacer?

- 💬 Hacer preguntas al chatbot
- 🔁 Evaluar diferentes estrategias de chunking y prompts
- 📊 Comparar desempeño con métricas semánticas
- 🧪 Trazar todo en MLflow
- 🔄 Adaptar a otros dominios (legal, salud, educación…)

---

## ⚙️ Stack Tecnológico

- **OpenAI + LangChain** – LLM + RAG
- **FAISS** – Vectorstore
- **Streamlit** – UI
- **MLflow** – Registro de experimentos
- **LangChain Eval** – Evaluación semántica
- **GitHub Actions** – CI/CD
- **DevContainer** – Desarrollo portable

---

## 🎓 Desafío para estudiantes

🧩 Parte 1: Personalización

1. Elige un nuevo dominio
Ejemplos: salud, educación, legal, bancario, etc.

2. Reemplaza los documentos PDF
Ubícalos en data/pdfs/.

3. Modifica o crea tus prompts
Edita los archivos en app/prompts/.

4. Crea un conjunto de pruebas
En tests/eval_dataset.json, define preguntas y respuestas esperadas para evaluar a tu chatbot.

✅ Parte 2: Evaluación Automática

1. Ejecuta run_eval.py para probar tu sistema actual.
Actualmente, la evaluación está basada en QAEvalChain de LangChain, que devuelve una métrica binaria: correcto / incorrecto.

🔧 Parte 3: ¡Tu reto! (👨‍🔬 nivel investigador)

1. Mejora el sistema de evaluación:

    * Agrega evaluación con LabeledCriteriaEvalChain usando al menos los siguientes criterios:

        * "correctness" – ¿Es correcta la respuesta?
        * "relevance" – ¿Es relevante respecto a la pregunta?
        * "coherence" – ¿Está bien estructurada la respuesta?
        * "toxicity" – ¿Contiene lenguaje ofensivo o riesgoso?
        * "harmfulness" – ¿Podría causar daño la información?

    * Cada criterio debe registrar:

        * Una métrica en MLflow (score)

    * Y opcionalmente, un razonamiento como artefacto (reasoning)

    📚 Revisa la [documentación de LabeledCriteriaEvalChain](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.LabeledCriteriaEvalChain.html) para implementarlo.

📊 Parte 4: Mejora el dashboard

1. Extiende dashboard.py o main_interface.py para visualizar:

    * Las métricas por criterio (correctness_score, toxicity_score, etc.).
    * Una opción para seleccionar y comparar diferentes criterios en gráficos.
    * (Opcional) Razonamientos del modelo como texto.    

🧪 Parte 5: Presenta y reflexiona
1. Compara configuraciones distintas (chunk size, prompt) y justifica tu selección.
    * ¿Cuál configuración genera mejores respuestas?
    * ¿En qué fallan los modelos? ¿Fueron tóxicos o incoherentes?
    * Usa evidencias desde MLflow y capturas del dashboard.

🚀 Bonus

- ¿Te animas a crear un nuevo criterio como "claridad" o "creatividad"? Puedes definirlo tú mismo y usarlo con LabeledCriteriaEvalChain.

---

¡Listo para ser usado en clase, investigación o producción educativa! 🚀
