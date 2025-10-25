import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Aprendizaje por Recompensa", layout="centered")

st.title("🤖 Aprendizaje por Recompensa (Q-Learning)")
st.markdown("El agente aprende a llegar a la meta 🏆 moviéndose en una línea de 5 posiciones mediante **prueba y error**.")

# --- Parámetros ---
states = [0, 1, 2, 3, 4]
actions = [0, 1]  # 0=izquierda, 1=derecha
goal_state = 4

alpha = st.sidebar.slider("Tasa de aprendizaje (α)", 0.0, 1.0, 0.1, 0.05)
gamma = st.sidebar.slider("Factor de descuento (γ)", 0.0, 1.0, 0.9, 0.05)
epsilon = st.sidebar.slider("Exploración (ε)", 0.0, 1.0, 0.2, 0.05)
episodes = st.sidebar.slider("Número de episodios", 5, 100, 20, 5)

# --- Inicializamos la tabla Q ---
Q = np.zeros((len(states), len(actions)))

# --- Función de recompensa ---
def get_reward(state):
    return 10 if state == goal_state else -1

# --- Función para mostrar entorno ---
def show_environment(state):
    cells = ["⬜"] * len(states)
    cells[state] = "🤖"
    cells[goal_state] = "🏆"
    st.markdown(" ".join(cells))

# --- Entrenamiento ---
start = st.button("🚀 Iniciar entrenamiento")

if start:
    progress = st.progress(0)
    for episode in range(episodes):
        state = 0
        done = False
        step = 0

        st.subheader(f"Episodio {episode+1}")
        placeholder = st.empty()

        while not done:
            with placeholder.container():
                show_environment(state)
                st.write(f"➡️ Estado: {state} | Paso: {step}")

            # Elegir acción (explorar o explotar)
            if np.random.rand() < epsilon:
                action = np.random.choice(actions)
            else:
                action = np.argmax(Q[state])

            # Ejecutar acción
            if action == 0:
                next_state = max(0, state - 1)
            else:
                next_state = min(goal_state, state + 1)

            reward = get_reward(next_state)

            # Actualizar Q-table
            Q[state, action] = Q[state, action] + alpha * (
                reward + gamma * np.max(Q[next_state]) - Q[state, action]
            )

            state = next_state
            step += 1

            if state == goal_state:
                done = True
                with placeholder.container():
                    show_environment(state)
                    st.success(f"🎉 ¡Meta alcanzada en {step} pasos!")
                time.sleep(0.5)
            else:
                time.sleep(0.2)

        progress.progress((episode + 1) / episodes)
        time.sleep(0.2)

    st.subheader("📊 Tabla Q aprendida:")
    st.dataframe(Q, use_container_width=True)
    st.success("Entrenamiento completado ✅")
