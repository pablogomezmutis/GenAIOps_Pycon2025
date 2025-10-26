# app/dashboard.py

import mlflow
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard General de Evaluación", layout="wide")
st.title("Evaluación Completa del Chatbot por Pregunta")

client = mlflow.tracking.MlflowClient()
experiments = [exp for exp in client.search_experiments() if exp.name.startswith("eval_")]

if not experiments:
    st.warning("No se encontraron experimentos de evaluación.")
    st.stop()

exp_names = [exp.name for exp in experiments]
selected_exp_name = st.selectbox("Selecciona un experimento para visualizar:", exp_names)

experiment = client.get_experiment_by_name(selected_exp_name)
runs = client.search_runs(experiment_ids=[experiment.experiment_id], order_by=["start_time DESC"])

if not runs:
    st.warning("No hay ejecuciones registradas en este experimento.")
    st.stop()

data = []
for run in runs:
    params = getattr(run.data, "params", {}) or {}
    metrics = getattr(run.data, "metrics", {}) or {}

    def safe_int(x, default=0):
        try:
            return int(x)
        except Exception:
            return default

    def safe_float(x, default=0.0):
        try:
            return float(x)
        except Exception:
            return default

    pregunta = params.get("question") or params.get("pregunta") or ""
    prompt_version = params.get("prompt_version") or params.get("prompt") or "default"
    chunk_size = safe_int(params.get("chunk_size", 0))
    chunk_overlap = safe_int(params.get("chunk_overlap", 0))

    data.append({
        "pregunta": pregunta,
        "prompt_version": str(prompt_version),
        "chunk_size": chunk_size,
        "chunk_overlap": chunk_overlap,
        "correctness": safe_float(metrics.get("correctness", metrics.get("correctness_score", 0))),
        "relevance": safe_float(metrics.get("relevance", 0)),
        "coherence": safe_float(metrics.get("coherence", 0)),
        "toxicity": safe_float(metrics.get("toxicity", 0)),
        "harmfulness": safe_float(metrics.get("harmfulness", 0)),
        "razonamiento": params.get("reasoning") or params.get("razonamiento") or ""
    })

df = pd.DataFrame(data)

st.subheader("Resultados individuales por pregunta")
if df.empty:
    st.info("No hay datos para mostrar en la tabla.")
else:
    st.dataframe(df)

metricas = ["correctness", "relevance", "coherence", "toxicity", "harmfulness"]
st.subheader("Comparación de criterios")
criterios = st.multiselect("Selecciona los criterios para comparar:", metricas, default=["correctness", "relevance", "coherence"])

if not criterios:
    st.info("Selecciona al menos un criterio para visualizar los gráficos.")
else:
    # Mostrar medias en un gráfico de barras
    medios = df[criterios].mean().reset_index()
    medios.columns = ["criterio", "puntaje_promedio"]
    st.markdown("**Puntaje promedio por criterio**")
    st.bar_chart(medios.set_index("criterio")["puntaje_promedio"])

st.subheader("Evolución de métricas por configuración")
if df.empty:
    st.info("No hay datos para agrupar por configuración.")
else:
    df_grouped = df.groupby(["prompt_version", "chunk_size"])[metricas].mean().reset_index()
    df_grouped["config"] = df_grouped["prompt_version"].astype(str) + " | " + df_grouped["chunk_size"].astype(str)
    st.dataframe(df_grouped)
    if criterios:
        try:
            st.markdown("**Métricas promedio por configuración (selección actual de criterios)**")
            st.bar_chart(df_grouped.set_index("config")[criterios])
        except Exception:
            st.warning("No se pudieron graficar las métricas por configuración con la selección actual.")

if "razonamiento" in df.columns and df["razonamiento"].notna().any():
    st.subheader("Razonamientos del modelo")
    for idx, row in df.iterrows():
        razon = row.get("razonamiento") or ""
        pregunta = row.get("pregunta") or f"item {idx}"
        if razon:
            with st.expander(f"Pregunta: {pregunta}"):
                st.write(razon)
