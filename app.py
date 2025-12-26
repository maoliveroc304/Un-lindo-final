import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Nuestra Historia - Edición Navidad",
    page_icon="🎄",
    layout="wide"
)

# --- CSS PERSONALIZADO (LA MAGIA VISUAL) ---
# Aquí definimos las animaciones (temblor) y el efecto 3D (giro)
st.markdown("""
<style>
    /* 1. FONDO Y TIPOGRAFÍA */
    .stApp {
        background-color: #1a1515; /* Fondo oscuro tipo chocolate amargo */
        background-image: radial-gradient(#3e2b2b 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    h1, h2, h3 {
        color: #D4AF37 !important; /* Dorado elegante */
        font-family: 'Playfair Display', serif;
        text-align: center;
    }
    
    p {
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }

    /* 2. EFECTO DE NIEVE (CSS PURO) */
    .snowflake {
        color: #fff;
        font-size: 1em;
        font-family: Arial;
        text-shadow: 0 0 1px #000;
    }
    
    @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}
    @-webkit-keyframes snowflakes-shake{0%{-webkit-transform:translateX(0px);transform:translateX(0px)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}100%{-webkit-transform:translateX(0px);transform:translateX(0px)}}
    .snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s}

    /* 3. CONTENEDOR DE LA TARJETA (FLIP CARD) */
    .flip-card {
        background-color: transparent;
        width: 300px;
        height: 400px;
        perspective: 1000px; /* Necesario para el efecto 3D */
        margin: auto;
        margin-bottom: 30px;
    }

    /* Contenedor interior que agrupa frente y dorso */
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
        box-shadow: 0 4px 8px 0 rgba(255,215,0,0.2);
        border-radius: 15px;
    }

    /* ANIMACIÓN 1: TEMBLOR CÓMICO AL PASAR EL MOUSE (HOVER) */
    @keyframes shake {
        0% { transform: translate(1px, 1px) rotate(0deg); }
        10% { transform: translate(-1px, -2px) rotate(-1deg); }
        20% { transform: translate(-3px, 0px) rotate(1deg); }
        30% { transform: translate(3px, 2px) rotate(0deg); }
        40% { transform: translate(1px, -1px) rotate(1deg); }
        50% { transform: translate(-1px, 2px) rotate(-1deg); }
        60% { transform: translate(-3px, 1px) rotate(0deg); }
        70% { transform: translate(3px, 1px) rotate(-1deg); }
        80% { transform: translate(-1px, -1px) rotate(1deg); }
        90% { transform: translate(1px, 2px) rotate(0deg); }
        100% { transform: translate(1px, -2px) rotate(-1deg); }
    }

    .flip-card:hover .flip-card-inner {
        animation: shake 0.5s; /* Aplica el temblor */
        animation-iteration-count: infinite; /* Tiembla por siempre mientras esté el mouse */
        cursor: pointer;
    }

    /* ANIMACIÓN 2: GIRAR AL HACER CLIC (ACTIVE) */
    /* Usamos la pseudoclase :active para simular el clic mantenido */
    .flip-card:active .flip-card-inner {
        transform: rotateY(180deg);
        animation: none; /* Detiene el temblor al girar */
    }

    /* Cara frontal y trasera */
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 15px;
    }

    /* Estilo del Frente (Imagen) */
    .flip-card-front {
        background-color: #bbb;
        color: black;
    }
    
    .flip-card-front img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 15px;
    }

    /* Estilo del Dorso (Texto) */
    .flip-card-back {
        background-color: #2c2c2c; /* Gris oscuro elegante */
        color: #D4AF37; /* Letras doradas */
        transform: rotateY(180deg);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        border: 2px solid #D4AF37;
    }

</style>
""", unsafe_allow_html=True)

# --- EFECTO DE NIEVE HTML ---
st.markdown("""
<div class="snowflakes" aria-hidden="true">
  <div class="snowflake">❅</div><div class="snowflake">❅</div>
  <div class="snowflake">❆</div><div class="snowflake">❄</div>
  <div class="snowflake">❅</div><div class="snowflake">❆</div>
  <div class="snowflake">❄</div><div class="snowflake">❅</div>
  <div class="snowflake">❆</div><div class="snowflake">❄</div>
</div>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1>✨ Nuestra Historia: Edición Navidad ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Una colección de momentos que brillan tanto como tú.<br><i>(Pasa el mouse para verlas temblar de emoción, mantén presionado el clic para revelar el secreto)</i></p>", unsafe_allow_html=True)
st.markdown("---")

# --- FUNCIÓN PARA CREAR TARJETAS ---
def crear_tarjeta_html(imagen_url, titulo, descripcion):
    return f"""
    <div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img src="{imagen_url}" alt="Foto">
        </div>
        <div class="flip-card-back">
          <h3>{titulo}</h3>
          <p>{descripcion}</p>
          <p>❤️</p>
        </div>
      </div>
    </div>
    """

# --- GRILLA DE FOTOS ---
# Usamos columnas de Streamlit para organizar las tarjetas
col1, col2, col3 = st.columns(3)

with col1:
    # Tarjeta 1
    # Nota: Puedes cambiar estas URL por fotos reales subidas a tu GitHub o Imgur
    html_card = crear_tarjeta_html(
        "https://images.unsplash.com/photo-1511895426328-dc8714191300?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "Nuestra Primera Cena",
        "¿Recuerdas que se nos quemó el postre? Pero igual fue la noche perfecta porque estaba contigo."
    )
    st.markdown(html_card, unsafe_allow_html=True)

with col2:
    # Tarjeta 2
    html_card = crear_tarjeta_html(
        "https://images.unsplash.com/photo-1543589077-47d81606c1bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "Ese Viaje Inolvidable",
        "Tú, yo y ese atardecer que parecía pintado. No necesito más regalos esta Navidad."
    )
    st.markdown(html_card, unsafe_allow_html=True)

with col3:
    # Tarjeta 3
    html_card = crear_tarjeta_html(
        "https://images.unsplash.com/photo-1512474932049-78ac69ede12c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
        "Tu Sonrisa",
        "El adorno más bonito de todas mis Navidades. Gracias por hacerme tan feliz cada mes."
    )
    st.markdown(html_card, unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D4AF37;'>Para Mariana, con todo mi amor. Miguel ❤️</h4>", unsafe_allow_html=True)
