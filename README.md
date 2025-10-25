https://learning-nhhcmb5ov9i96v5b9twxya.streamlit.app/

🤖 Aprendizaje por Recompensa (Q-Learning)

Este proyecto es una simulación visual e interactiva del algoritmo Q-Learning desarrollada con Python y Streamlit.
El agente aprende, mediante prueba y error, a alcanzar una meta moviéndose en una línea de 5 posiciones.

🎯 Objetivo

Demostrar de forma sencilla cómo un agente puede aprender por refuerzo utilizando una tabla Q (Q-Table), donde se almacenan los valores de acción-recompensa que guían al agente hacia la meta 🏆.

🧩 Descripción del entorno

El entorno está representado por una línea de 5 posiciones:
⬜ ⬜ ⬜ ⬜ 🏆

El agente 🤖 comienza en la posición inicial (izquierda) y debe llegar al objetivo (derecha).

En cada paso:

Puede moverse a la izquierda (0) o a la derecha (1).

Recibe una recompensa negativa (-1) si no llega a la meta.

Recibe una recompensa positiva (+10) al alcanzar la meta.

