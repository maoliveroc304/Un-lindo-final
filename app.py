import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Nuestra Historia - Edición Navidad",
    page_icon="🎄",
    layout="wide"
)

# --- CSS PERSONALIZADO ---
st.markdown("""
<style>
    /* 1. ESTILOS GENERALES */
    .stApp {
        background-color: #1a1515;
        background-image: radial-gradient(#3e2b2b 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    h1 {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        text-align: left;
        margin-top: 0px;
    }
    
    h3, h4 {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
    }
    
    p, div {
        color: #E0E0E0;
        font-family: 'Montserrat', sans-serif;
    }

    /* 2. EFECTO NIEVE */
    .snowflake { color: #fff; font-size: 1em; font-family: Arial; text-shadow: 0 0 1px #000; }
    @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}
    @-webkit-keyframes snowflakes-shake{0%{-webkit-transform:translateX(0px);transform:translateX(0px)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}100%{-webkit-transform:translateX(0px);transform:translateX(0px)}}
    .snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s}

    /* 3. FLIP CARD Y VIDEO */
    input[type=checkbox] { display: none; }
    
    .card-container { 
        perspective: 1000px; 
        width: 300px; 
        height: 400px; 
        margin: auto; 
        margin-bottom: 30px; 
        cursor: pointer; 
        display: block; 
        position: relative; 
    }
    
    .card-flip-inner { 
        position: relative; 
        width: 100%; 
        height: 100%; 
        text-align: center; 
        transition: transform 0.8s; 
        transform-style: preserve-3d; 
        box-shadow: 0 4px 8px 0 rgba(255,215,0,0.2); 
        border-radius: 15px; 
    }
    
    input:checked + .card-container .card-flip-inner { transform: rotateY(180deg); }
    
    @keyframes shake { 0% { transform: translate(1px, 1px) rotate(0deg); } 10% { transform: translate(-1px, -2px) rotate(-1deg); } 20% { transform: translate(-3px, 0px) rotate(1deg); } 30% { transform: translate(3px, 2px) rotate(0deg); } 40% { transform: translate(1px, -1px) rotate(1deg); } 50% { transform: translate(-1px, 2px) rotate(-1deg); } 60% { transform: translate(-3px, 1px) rotate(0deg); } 70% { transform: translate(3px, 1px) rotate(-1deg); } 80% { transform: translate(-1px, -1px) rotate(1deg); } 90% { transform: translate(1px, 2px) rotate(0deg); } 100% { transform: translate(1px, -2px) rotate(-1deg); } }
    
    .card-container:hover .card-flip-inner { animation: shake 0.5s; animation-iteration-count: infinite; }
    input:checked + .card-container:hover .card-flip-inner { animation: none; }
    
    .flip-front, .flip-back { 
        position: absolute; 
        width: 100%; 
        height: 100%; 
        -webkit-backface-visibility: hidden; 
        backface-visibility: hidden; 
        border-radius: 15px; 
        top: 0; 
        left: 0; 
    }
    
    .flip-front { 
        background-color: #222; 
        color: black; 
        z-index: 2; 
        transform: rotateY(0deg); 
    }
    
    .flip-front img { 
        width: 100%; 
        height: 100%; 
        object-fit: cover; 
        border-radius: 15px; 
        display: block; 
    }
    
    /* AQUÍ ESTÁ LA CORRECCIÓN CLAVE */
    .flip-back { 
        background-color: #2c2c2c; 
        color: #D4AF37; 
        transform: rotateY(180deg); 
        z-index: 1; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        align-items: center; 
        text-align: center; /* <-- ESTO ASEGURA QUE EL TEXTO ESTÉ CENTRADO */
        padding: 20px; 
        border: 2px solid #D4AF37; 
    }

    /* Centrar cosas verticalmente en columnas */
    div[data-testid="stColumn"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
</style>
""", unsafe_allow_html=True)

# --- HTML DEL REPRODUCTOR PERSONALIZADO ---
music_player_html = """
<!DOCTYPE html>
<html>
<head>
<style>
    body { margin: 0; padding: 0; background-color: transparent; font-family: 'Montserrat', sans-serif; overflow: hidden;}
    
    .player-container {
        background: rgba(44, 44, 44, 0.9);
        border: 1px solid #D4AF37;
        border-radius: 15px;
        padding: 10px 15px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 90%;
        margin: auto;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .song-title {
        color: #D4AF37;
        font-size: 14px;
        margin-bottom: 8px;
        font-weight: bold;
        text-align: center;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 100%;
    }
    
    audio {
        width: 100%;
        height: 30px;
        filter: invert(100%) sepia(100%) saturate(500%) hue-rotate(360deg) brightness(90%) contrast(85%);
        outline: none;
    }
    
    .controls {
        display: flex;
        justify-content: space-between;
        width: 100%;
        margin-top: 5px;
    }
    
    .btn {
        background: none;
        border: 1px solid #D4AF37;
        color: #D4AF37;
        border-radius: 5px;
        cursor: pointer;
        font-size: 10px;
        padding: 2px 8px;
        transition: 0.3s;
    }
    
    .btn:hover {
        background: #D4AF37;
        color: #000;
    }
</style>
</head>
<body>

<div class="player-container">
    <div class="song-title" id="songTitle">Cargando música... 🎵</div>
    <audio id="audioPlayer" controls autoplay>
        Tu navegador no soporta audio.
    </audio>
    <div class="controls">
        <button class="btn" onclick="prevSong()">⏮ Ant</button>
        <button class="btn" onclick="nextSong()">Sig ⏭</button>
    </div>
</div>

<script>
    const playlist = [
        { title: "💑 Nuestra Canción Especial", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Kygo%20-%20Firestone%20ft.%20Conrad%20Sewell.mp3" },
        { title: "🐱 Jaja, muchos recuerdos", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Yung%20Kai%20ft%20Oiia%20Cat%20-%20Blue.mp3" },
        { title: "✨ Siempre te tengo presente", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Sleeping%20With%20Sirens%20-%20James%20Dean%20%26%20Audrey%20Hepburn%20(Acoustic%20version).mp3" },
        { title: "🕒 Soñemos juntos, por siempre, mi amor", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Amor%20De%20Papel%20-%20Jorge%20Cuellar.mp3" },
        { title: "🏡 Eres mi hogar", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Edith%20Whiskers%20-%20Home.mp3" },
        { title: "😆 Algo random no cae mal jaja", src: "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/canciones/Party%20Tunes%20%20Brainrot%20Rap.mp3" }
    ];

    let currentTrack = 0;
    const audio = document.getElementById('audioPlayer');
    const titleLabel = document.getElementById('songTitle');

    function loadSong(index) {
        if (index < 0) index = playlist.length - 1;
        if (index >= playlist.length) index = 0;
        
        currentTrack = index;
        audio.src = playlist[currentTrack].src;
        titleLabel.innerText = "🎶 " + playlist[currentTrack].title;
        audio.play().catch(e => console.log("Autoplay bloqueado por navegador hasta interactuar"));
    }

    function nextSong() {
        loadSong(currentTrack + 1);
    }

    function prevSong() {
        loadSong(currentTrack - 1);
    }

    audio.addEventListener('ended', nextSong);

    window.onload = () => {
        loadSong(0); 
    };
</script>

</body>
</html>
"""

# --- EFECTO NIEVE ---
st.markdown("""<div class="snowflakes" aria-hidden="true"><div class="snowflake">❅</div><div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div><div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div><div class="snowflake">❅</div><div class="snowflake">❆</div><div class="snowflake">❄</div></div>""", unsafe_allow_html=True)

# ==========================================
# 🎵 CABECERA + REPRODUCTOR 🎵
# ==========================================

col_text, col_player = st.columns([3, 1.2])

with col_text:
    st.markdown("<h1>✨ Nuestra Historia: Edición Navidad ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: left; font-size: 1.1em;'>Una colección de momentos que brillan e iluminaron tanto mi corazón, que los recordaré por siempre<3<br><i>(Haz clic en las fotos para descubrir el mensaje secreto)</i></p>", unsafe_allow_html=True)

with col_player:
    components.html(music_player_html, height=130)

st.markdown("---")

# ==========================================
# 🎥 VIDEO CENTRAL 🎥
# ==========================================
col_vid1, col_vid2, col_vid3 = st.columns([1, 2, 1])

with col_vid2:
    st.markdown("<h3 style='margin-bottom: 10px; text-align: center;'>🎥 Nuestro Mensaje de Amor</h3>", unsafe_allow_html=True)
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    st.video(video_url)
    st.markdown("<p style='text-align: center; font-size: 0.9em; margin-top: 5px;'>Dale play al video para ver la dedicatoria visual 🎬</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 🃏 TARJETAS (GRILLA DE 9 MOMENTOS) 🃏
# ==========================================

def crear_tarjeta_html(id_unico, imagen_url, titulo, descripcion):
    # HE AGREGADO text-align: center EXPLÍCITAMENTE EN EL H3 Y EL P TAMBIÉN POR SEGURIDAD
    return f"""
    <div style="margin-top: 20px; margin-bottom: 20px;">
        <input type="checkbox" id="{id_unico}">
        <label class="card-container" for="{id_unico}">
            <div class="card-flip-inner">
                <div class="flip-front">
                    <img src="{imagen_url}" alt="Foto">
                </div>
                <div class="flip-back">
                    <h3 style="font-size: 1.2em; text-align: center; margin-bottom: 10px;">{titulo}</h3>
                    <p style="font-size: 0.9em; padding: 0 10px; text-align: center;">{descripcion}</p>
                    <p>❤️</p>
                </div>
            </div>
        </label>
    </div>
    """

# --- FILA 1 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(crear_tarjeta_html(
        "card1",
        "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600",
        "Las canciones",
        "Fueron nuestro lenguaje de amor, nuestra forma de demostrar esta hermosa conexión."
    ), unsafe_allow_html=True)

with col2:
    st.markdown(crear_tarjeta_html(
        "card2",
        "https://images.unsplash.com/photo-1513205770146-2f168f2379d7?w=600",
        "Tenemos el humor más roto",
        "Podemos reírnos de nuestras locuras, de nuestras normalidades y de todo. Tu sonrisa era mi mayor regalo."
    ), unsafe_allow_html=True)

with col3:
    st.markdown(crear_tarjeta_html(
        "card3",
        "https://images.unsplash.com/photo-1472120435266-53107fd0c44a?w=600",
        "Los atardeceres",
        "Siempre guardaré en mi memoria los muchos atardeceres que nos enviamos, y donde podíamos sentirnos cerca sólo con mirar el horizonte."
    ), unsafe_allow_html=True)

# --- FILA 2 ---
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(crear_tarjeta_html(
        "card4",
        "https://images.unsplash.com/photo-1632501641765-e568d28b0015?w=600",
        "Nuestros juegos",
        "Jaja, hicimos un poco de todo, no? desde lindos dibujos, partidas épicas de Monopoly, hasta mis humillaciones en Plato :v"
    ), unsafe_allow_html=True)

with col5:
    st.markdown(crear_tarjeta_html(
        "card5",
        "https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=600",
        "Formas de llamarnos",
        "Cajita de sorpresas, mi tralalera, mi gran y lindo amor, el amor de mi vida, y mi más hermosa coincidencia."
    ), unsafe_allow_html=True)

with col6:
    st.markdown(crear_tarjeta_html(
        "card6",
        "https://images.unsplash.com/photo-1518133835878-5a93cc3f89e5?w=600",
        "Llama a la llama en llamas",
        "No necesita más explicación :v"
    ), unsafe_allow_html=True)

# --- FILA 3 ---
col7, col8, col9 = st.columns(3)

with col7:
    st.markdown(crear_tarjeta_html(
        "card7",
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=600",
        "La única peli que vimos",
        "Aún tengo el pendiente de ir al cine algún día contigo, y te aseguro que será toda una experiencia :)"
    ), unsafe_allow_html=True)

with col8:
    st.markdown(crear_tarjeta_html(
        "card8",
        "https://images.unsplash.com/photo-1623945202652-327c59c5d72a?w=600",
        "La promesa de amarnos",
        "El destino se encargó de encontrarnos y te prometo que será este destino el que nos volverá a juntar."
    ), unsafe_allow_html=True)

with col9:
    st.markdown(crear_tarjeta_html(
        "card9",
        "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?w=600",
        "Amo amarte",
        "Gracias por amarme como lo hiciste cada día, y por haberme hecho sentir cómo es amar a alguien con toda el alma."
    ), unsafe_allow_html=True)

# ==========================================
# 🎞️ CINTA DE FOTOS INFINITA (CORREGIDA) 🎞️
# ==========================================

st.markdown("<br><h3 style='text-align: center; color: #D4AF37;'>🎞️ Un viaje por nuestros momentos 🎞️</h3>", unsafe_allow_html=True)

# 1. Lista de Imágenes (Asegúrate de que esta variable exista)
cinta_imagenes = [
    "https://images.unsplash.com/photo-1529619768328-e37af76c6fe5?w=600",
    "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?w=600",
    "https://images.unsplash.com/photo-1523438885200-e635ba2c371e?w=600",
    "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=600", 
    "https://images.unsplash.com/photo-1543589077-47d81606c1bf?w=600",
    "https://images.unsplash.com/photo-1512474932049-78ac69ede12c?w=600",
    "https://images.unsplash.com/photo-1623945202652-327c59c5d72a?w=600",
    "https://images.unsplash.com/photo-1518199266791-5375a83190b7?w=600"
]

# 2. Cálculos en Python (Más seguro que CSS)
full_list = cinta_imagenes * 2  # Duplicamos para efecto infinito
cantidad_fotos = len(full_list)
ancho_foto = 250
ancho_total_track = cantidad_fotos * ancho_foto  # Ancho total en pixeles
distancia_scroll = len(cinta_imagenes) * ancho_foto # Cuánto debe moverse para el loop

# 3. Generación HTML de las fotos
html_imgs = ""
for i, img_url in enumerate(full_list):
    html_imgs += f'<div class="slide"><img src="{img_url}" onclick="openModal({i})" alt="Foto {i}"></div>'

# Lista JS para el modal
js_img_list = str(full_list) 

cinta_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ margin: 0; background-color: transparent; font-family: 'Montserrat', sans-serif; overflow: hidden; }}
    
    /* CONTENEDOR PRINCIPAL */
    .slider {{
        height: 220px;
        margin: auto;
        position: relative;
        width: 100%;
        display: flex;
        align-items: center;
        overflow: hidden;
    }}
    
    /* PISTA QUE SE MUEVE */
    .slide-track {{
        display: flex;
        width: {ancho_total_track}px; /* Ancho calculado en Python */
        animation: scroll 40s linear infinite;
    }}
    
    .slide-track:hover {{
        animation-play-state: paused;
    }}
    
    /* ANIMACIÓN */
    @keyframes scroll {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-{distancia_scroll}px); }} /* Distancia calculada en Python */
    }}
    
    /* FOTOS INDIVIDUALES */
    .slide {{
        height: 180px;
        width: {ancho_foto}px;
        display: flex;
        align-items: center;
        padding: 10px;
        box-sizing: border-box; /* Importante para que el padding no rompa el ancho */
    }}
    
    .slide img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 10px;
        cursor: pointer;
        transition: transform 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        border: 2px solid #D4AF37;
    }}
    
    .slide img:hover {{
        transform: scale(1.1);
        z-index: 10;
    }}

    /* MODAL (Pantalla Completa dentro del Iframe) */
    .modal {{
        display: none;
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0,0,0,0.95);
    }}

    .modal-content {{
        margin: auto;
        display: block;
        max-width: 90%;
        max-height: 80%;
        margin-top: 20px;
        border: 2px solid #D4AF37;
        border-radius: 10px;
        box-shadow: 0 0 20px #D4AF37;
    }}

    .close {{
        position: absolute;
        top: 10px;
        right: 25px;
        color: #f1f1f1;
        font-size: 35px;
        font-weight: bold;
        cursor: pointer;
        z-index: 1001;
    }}

    .prev, .next {{
        cursor: pointer;
        position: absolute;
        top: 50%;
        width: auto;
        padding: 16px;
        margin-top: -50px;
        color: white;
        font-weight: bold;
        font-size: 24px;
        transition: 0.6s ease;
        border-radius: 0 3px 3px 0;
        user-select: none;
        background-color: rgba(0,0,0,0.5);
    }}

    .next {{ right: 0; border-radius: 3px 0 0 3px; }}
    .prev:hover, .next:hover {{ background-color: #D4AF37; color: black; }}

</style>
</head>
<body>

<div class="slider">
    <div class="slide-track">
        {html_imgs}
    </div>
</div>

<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="img01">
  <a class="prev" onclick="changeSlide(-1)">&#10094;</a>
  <a class="next" onclick="changeSlide(1)">&#10095;</a>
</div>

<script>
    const images = {js_img_list};
    let currentIndex = 0;
    const modal = document.getElementById("myModal");
    const modalImg = document.getElementById("img01");

    function openModal(index) {{
        modal.style.display = "block";
        currentIndex = index;
        modalImg.src = images[currentIndex];
    }}

    function closeModal() {{
        modal.style.display = "none";
    }}

    function changeSlide(n) {{
        currentIndex += n;
        if (currentIndex >= images.length) {{ currentIndex = 0; }}
        if (currentIndex < 0) {{ currentIndex = images.length - 1; }}
        modalImg.src = images[currentIndex];
    }}
    
    // Cerrar al hacer clic fuera
    window.onclick = function(event) {{
        if (event.target == modal) {{ closeModal(); }}
    }}
</script>

</body>
</html>
"""

# Renderizamos el componente con altura suficiente
# 600px es para asegurar que cuando abras la foto grande, quepa bien.
components.html(cinta_html, height=600)

# --- PIE DE PÁGINA ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D4AF37;'>Para Mariana, con todo mi amor. Miguel ❤️</h4>", unsafe_allow_html=True)
