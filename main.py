import streamlit as st
import random
import matplotlib.pyplot as plt

# ------------------- CONFIGURACIÓN PÁGINA ------------------- #
st.set_page_config(
    page_title="Calculadora de Indicadores Dinegma",
    layout="centered"
)

# ------------------- ESTILOS PERSONALIZADOS ------------------- #
st.markdown("""
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
""", unsafe_allow_html=True)

# ------------------- TÍTULO ------------------- #
st.markdown('<div class="title">🧮 Calculadora de Indicadores Dinegma</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">💼 Herramienta para evaluar desempeño comercial</div>', unsafe_allow_html=True)

# ------------------- CAMPO ADMIN ------------------- #
modo_admin = st.text_input("🔐 Ingresar contraseña para activar modo Admin (opcional)", type="password")
es_admin = modo_admin == "Formacion.2025"

# ------------------- ENTRADAS ------------------- #
asesor = st.text_input("👤 Nombre del asesor o asesora", max_chars=30)
ventas = st.number_input("👉 Ventas realizadas", min_value=1)
articulos = st.number_input("🧾 Artículos vendidos", min_value=0)
valor_total = st.number_input("💰 Valor total vendido (Q)", min_value=0.0)
clientes = st.number_input("🚶‍♂️ Clientes que ingresaron", min_value=1)
fidelizados = st.number_input("📈 Clientes Fidelizados", min_value=0)

# ------------------- FRASES MOTIVADORAS ------------------- #
frases = [
    "¡Cada venta suma, cada indicador cuenta! 💪",
    "¡Vamos por más! Tu esfuerzo impacta en el equipo 🔥",
    "¡Los buenos resultados no se improvisan, se construyen! 🚀",
    "¡Un asesor motivado hace la diferencia! 🎯",
    "¡Hoy puede ser tu mejor día en tienda! 🌟"
]

# ------------------- CÁLCULOS ------------------- #
if st.button("🎯 Calcular Indicadores"):
    axf = round(articulos / ventas, 2)
    vxf = round(valor_total / ventas, 2)
    tc = round((ventas / clientes) * 100, 2)
    tasa_fidel = round((fidelizados / ventas) * 100, 2)

    st.balloons()
    st.success(f"📊 Resultados para {asesor or 'asesor/a'}:")

    st.write(f"🔸 Artículos por Factura (AxF): `{axf}`")
    st.write(f"🔸 Valor por Factura (VxF): `Q{vxf}`")
    st.write(f"🔸 Tasa de Conversión (TC): `{tc}%`")
    st.write(f"🔸 Tasa de Fidelización: `{tasa_fidel}%`")

    # Frase motivadora
    st.markdown(f"### ✨ {random.choice(frases)}")

    # ------------------- GRÁFICA ------------------- #
    indicadores = ["AxF", "VxF", "TC", "Fidelización"]
    valores = [axf, vxf, tc, tasa_fidel]

    fig, ax = plt.subplots()
    ax.bar(indicadores, valores, color=["#0277BD", "#29B6F6", "#4FC3F7", "#81D4FA"])
    ax.set_ylabel("Valor")
    ax.set_title("Comparativa de Indicadores")
    st.pyplot(fig)

    # ------------------- MODO ADMIN ------------------- #
    if es_admin:
        st.markdown("---")
        st.info("🔐 **Modo Admin Activado**")
        st.write(f"📌 Asesor/a: `{asesor}`")
        st.write(f"📌 Ventas: `{ventas}`, Artículos: `{articulos}`, Valor: `Q{valor_total}`")
        st.write(f"📌 Clientes: `{clientes}`, Fidelizados: `{fidelizados}`")

# ------------------- BOTÓN PARA REINICIAR ------------------- #
if st.button("🔄 Evaluar otro asesor"):
    st.rerun()

# ------------------- FOOTER ------------------- #
st.markdown("---")
st.caption("🦁 Desarrollado por Edgar Urrutia • Proyecto Formación Dinegma • 2025")
