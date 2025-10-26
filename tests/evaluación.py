import mlflow
import json
from pathlib import Path

# Cargar dataset de evaluación
eval_path = Path("tests/eval_dataset.json")
with open(eval_path, "r") as f:
    eval_data = json.load(f)

# Simular respuestas del RAG (en la práctica aquí iría tu llamada al modelo)
def rag_answer(question, context):
    # Lógica del RAG simulada
    # Podrías reemplazar esto con tu verdadero modelo, por ahora algo simple
    return context[:100]

# Iniciar experimento de MLflow
mlflow.set_experiment("eval_rag_eafit")

with mlflow.start_run():
    total = len(eval_data)
    correct = 0

    for item in eval_data:
        question = item["question"]
        expected = item["answer"]
        context = item.get("context", "")
        pred = rag_answer(question, context)

        # Métrica simple: acierto si la respuesta esperada aparece en la predicción
        if expected.lower() in pred.lower():
            correct += 1

    accuracy = correct / total
    print(f"Precisión simulada: {accuracy:.2f}")

    # Registrar métrica
    mlflow.log_metric("lc_is_correct", accuracy)
