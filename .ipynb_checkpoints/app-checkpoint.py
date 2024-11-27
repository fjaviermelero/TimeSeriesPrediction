import streamlit as st







# Título de la aplicación
st.title("Mi Página Básica con Streamlit")

# Encabezado
st.header("¡Bienvenido a mi aplicación!")

# Texto introductorio
st.write("""
Esta es una página de ejemplo creada con Streamlit.
Puedes usar este marco para crear aplicaciones web interactivas de manera sencilla.
""")

# Agregar un cuadro de texto
nombre = st.text_input("Introduce tu nombre:")

# Agregar un botón
if st.button("Saludar"):
    st.write(f"¡Hola, {nombre}!")

# Agregar un gráfico de barras
st.subheader("Gráfico de barras de ejemplo")
datos = {'Eje X': ['A', 'B', 'C', 'D'], 'Eje Y': [3, 6, 9, 12]}
st.bar_chart(datos)

# Agregar un slider
numero = st.slider("Selecciona un número:", 0, 100)
st.write(f"Número seleccionado: {numero}")

# Agregar una imagen
st.image("https://www.streamlit.io/images/brand/streamlit-mark-light.svg", caption="Streamlit Logo")
