import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Calculadora de Indicadores",
    layout="centered"
)

# Estilos personalizados en tonos azul/celeste
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .title {
        color: #02577A;
        font-size: 32px;
        font-weight: bold;
    }
    .sub {
        color: #0277BD;
        font-size: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título personalizado
st.markdown('<div class="title">🧮 Calculadora de Indicadores Comerciales</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">💼 Herramienta para evaluar desempeño comercial</div>', unsafe_allow_html=True)

# Entradas
ventas = st.number_input("👉 Ventas realizadas", min_value=1)
articulos = st.number_input("🧾 Artículos vendidos", min_value=0)
valor_total = st.number_input("💰 Valor total vendido (Q)", min_value=0.0)
clientes = st.number_input("🚶‍♂️ Clientes que ingresaron", min_value=1)
fidelizados = st.number_input("📈 Tasa de Fidelización", min_value=0)

# Botón para calcular
if st.button("🎯 Calcular Indicadores"):
    axf = round(articulos / ventas, 2)
    vxf = round(valor_total / ventas, 2)
    tc = round((ventas / clientes) * 100, 2)
    tasa_fidel = round((fidelizados / ventas) * 100, 2)

    st.success("📊 Resultados:")
    st.write(f"🔸 Artículos por Factura (AxF): `{axf}`")
    st.write(f"🔸 Valor por Factura (VxF): `Q{vxf}`")
    st.write(f"🔸 Tasa de Conversión: `{tc}%`")
    st.write(f"🔸 Tasa de Fidelización: `{tasa_fidel}%`")

# Footer
st.markdown("---")
st.caption("🦁 Desarrollado por Edgar Urrutia • Proyecto Formación & Fidelización • 2025")
