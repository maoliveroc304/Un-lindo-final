import streamlit as st
import streamlit.components.v1 as components
import time
import random

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
    
    .flip-back { 
        background-color: #2c2c2c; 
        color: #D4AF37; 
        transform: rotateY(180deg); 
        z-index: 1; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        align-items: center; 
        text-align: center; 
        padding: 20px; 
        border: 2px solid #D4AF37; 
    }

    /* Centrar cosas verticalmente en columnas */
    div[data-testid="stColumn"] {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    /* ========================================== */
    /* 🧠 ESTILOS ESPECÍFICOS PARA JUEGO DE MEMORIA 🧠 */
    /* ========================================== */
    
    /* 1. Forzar que las IMÁGENES (Cartas boca arriba) sean del mismo tamaño */
    div[data-testid="stImage"] img {
        height: 180px !important;       /* Alto fijo */
        width: 100% !important;         /* Ancho se adapta a la columna */
        object-fit: cover !important;   /* Recorta la imagen */
        border-radius: 10px !important;
        border: 2px solid #D4AF37;      /* Borde dorado */
    }

    /* 2. Forzar que los BOTONES (Cartas boca abajo) sean del mismo tamaño */
    div[data-testid="stButton"] button {
        height: 180px !important;       /* Mismo alto que la imagen */
        width: 100% !important;
        border-radius: 10px !important;
        border: 2px dashed #D4AF37 !important; 
        background-color: #2c2c2c !important;
        color: #D4AF37 !important;
        font-size: 40px !important;     
        transition: transform 0.2s;
    }

    div[data-testid="stButton"] button:hover {
        transform: scale(1.05);
        border: 2px solid #D4AF37 !important;
        background-color: #3e2b2b !important;
    }
    
    /* Ajustar el espaciado de las columnas del juego */
    div[data-testid="stVerticalBlock"] > div {
        gap: 1rem;
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
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Las_canciones.png",
        "Las canciones",
        "Fueron nuestro lenguaje de amor, nuestra forma de demostrar esta hermosa conexión."
    ), unsafe_allow_html=True)

with col2:
    st.markdown(crear_tarjeta_html(
        "card2",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Humor_rotisimo.png",
        "Tenemos el humor más roto",
        "Podemos reírnos de nuestras locuras, de nuestras normalidades y de todo. Tu sonrisa era mi mayor regalo."
    ), unsafe_allow_html=True)

with col3:
    st.markdown(crear_tarjeta_html(
        "card3",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Atardeceres.png",
        "Los atardeceres",
        "Siempre guardaré en mi memoria los muchos atardeceres que nos enviamos, y donde podíamos sentirnos cerca sólo con mirar el horizonte."
    ), unsafe_allow_html=True)

# --- FILA 2 ---
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown(crear_tarjeta_html(
        "card4",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Nuestros_juegos.png",
        "Nuestros juegos",
        "Jaja, hicimos un poco de todo, no? desde lindos dibujos, partidas épicas de Monopoly, hasta mis humillaciones en Plato :v"
    ), unsafe_allow_html=True)

with col5:
    st.markdown(crear_tarjeta_html(
        "card5",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Formas_llamarnos.jpg",
        "Formas de llamarnos",
        "Cajita de sorpresas, mi tralalera, mi gran y lindo amor, el amor de mi vida, y mi más hermosa coincidencia."
    ), unsafe_allow_html=True)

with col6:
    st.markdown(crear_tarjeta_html(
        "card6",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Llama_llama_llamas.png",
        "Llama a la llama en llamas",
        "No necesita más explicación :v"
    ), unsafe_allow_html=True)

# --- FILA 3 ---
col7, col8, col9 = st.columns(3)

with col7:
    st.markdown(crear_tarjeta_html(
        "card7",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Unica_pelicula.jpg",
        "La única peli que vimos",
        "Aún tengo el pendiente de ir al cine algún día contigo, y te aseguro que será toda una experiencia :)"
    ), unsafe_allow_html=True)

with col8:
    st.markdown(crear_tarjeta_html(
        "card8",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/La_promesa.jpg",
        "La promesa de amarnos",
        "El destino se encargó de encontrarnos y te prometo que será este destino el que nos volverá a juntar."
    ), unsafe_allow_html=True)

with col9:
    st.markdown(crear_tarjeta_html(
        "card9",
        "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/Amo_amarte.jpg",
        "Amo amarte",
        "Gracias por amarme como lo hiciste cada día, y por haberme hecho sentir cómo es amar a alguien con toda el alma."
    ), unsafe_allow_html=True)

# ==========================================
# 🧠 JUEGO DE MEMORIA: NUESTROS RECUERDOS 🧠
# ==========================================

st.markdown("<br><h3 style='text-align: center; color: #D4AF37;'>🧠 Encuentra los Pares: Nuestros Recuerdos 🧠</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 0.9em;'>Dale la vuelta a las cartas y encuentra los momentos gemelos. ¿Podrás desbloquearlos todos?</p>", unsafe_allow_html=True)

# 1. LISTA DE FOTOS PARA EL JUEGO (12 en total)
all_memory_photos = [
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/1.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/2.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/3.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/4.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/5.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/6.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/7.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/8.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/9.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/10.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/11.jpg",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/memoria/12.jpg"
]

# 2. INICIALIZACIÓN DEL ESTADO DEL JUEGO
if 'memory_initialized' not in st.session_state:
    st.session_state.memory_initialized = True
    st.session_state.seen_photos = set()
    st.session_state.game_over = False
    st.session_state.current_deck = []
    st.session_state.flipped = []
    st.session_state.matched = set()
    st.session_state.moves = 0

def init_game():
    unseen = [p for p in all_memory_photos if p not in st.session_state.seen_photos]
    needed = 6
    selection = []
    
    if len(unseen) >= needed:
        selection = random.sample(unseen, needed)
    else:
        remaining = needed - len(unseen)
        selection = unseen + random.sample(list(st.session_state.seen_photos), remaining)
    
    st.session_state.seen_photos.update(selection)
    
    deck_images = selection * 2
    random.shuffle(deck_images)
    
    st.session_state.current_deck = [{"id": i, "url": url} for i, url in enumerate(deck_images)]
    st.session_state.flipped = []
    st.session_state.matched = set()
    st.session_state.moves = 0
    st.session_state.game_over = False

if not st.session_state.current_deck:
    init_game()

def handle_click(card_id):
    if len(st.session_state.flipped) == 2:
        st.session_state.flipped = []
    
    st.session_state.flipped.append(card_id)
    
    if len(st.session_state.flipped) == 2:
        st.session_state.moves += 1
        id1 = st.session_state.flipped[0]
        id2 = st.session_state.flipped[1]
        
        url1 = next(c['url'] for c in st.session_state.current_deck if c['id'] == id1)
        url2 = next(c['url'] for c in st.session_state.current_deck if c['id'] == id2)
        
        if url1 == url2:
            st.session_state.matched.add(id1)
            st.session_state.matched.add(id2)
            st.session_state.flipped = []
            
            if len(st.session_state.matched) == len(st.session_state.current_deck):
                st.session_state.game_over = True
                st.balloons()

# 3. INTERFAZ DEL JUEGO
col_info1, col_info2 = st.columns([3, 1])
with col_info1:
    if len(st.session_state.seen_photos) < len(all_memory_photos):
        st.caption(f"🕵️‍♂️ Aún quedan fotos nuevas por descubrir... ({len(st.session_state.seen_photos)}/{len(all_memory_photos)} vistas)")
    else:
        st.caption("✨ ¡Ya has desbloqueado todos los recuerdos!")

with col_info2:
    if st.button("🔄 Barajar"):
        init_game()
        st.rerun()

if st.session_state.game_over:
    st.success(f"¡Ganaste! 🎉 Intentos: {st.session_state.moves}. Reiniciando...")
    time.sleep(3)
    init_game()
    st.rerun()

cols = st.columns(4)
for i, card in enumerate(st.session_state.current_deck):
    is_flipped = card['id'] in st.session_state.flipped
    is_matched = card['id'] in st.session_state.matched
    
    with cols[i % 4]:
        if is_flipped or is_matched:
            st.image(card['url'], use_container_width=True)
        else:
            if st.button("❤️", key=f"btn_{card['id']}", use_container_width=True):
                handle_click(card['id'])
                st.rerun()

st.markdown("---")

# ==========================================
# 🎞️ CINTA DE FOTOS: TODOS NUESTROS MOMENTOS 🎞️
# ==========================================

st.markdown("<h3 style='text-align: center; color: #D4AF37; margin-top: 20px; margin-bottom: 0px;'>🎞️ Un viaje por nuestros momentos 🎞️</h3>", unsafe_allow_html=True)

# 1. LISTA ACTUALIZADA CON TUS FOTOS DE LA CARPETA 'RULETA'
cinta_imagenes = [
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R1.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R2.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R3.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R4.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R5.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R6.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R7.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R8.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R9.png",
    "https://raw.githubusercontent.com/maoliveroc304/Un-lindo-final/main/fotos/ruleta/R10.png"
]

# 2. Cálculos Python
full_list = cinta_imagenes * 2
cantidad_fotos = len(full_list)
ancho_foto = 250
ancho_total_track = cantidad_fotos * ancho_foto
distancia_scroll = len(cinta_imagenes) * ancho_foto

# 3. Generar HTML de imágenes
html_imgs = ""
for i, img_url in enumerate(full_list):
    html_imgs += f'<div class="slide"><img src="{img_url}" onclick="expandViewer({i})" alt="Foto {i}"></div>'

js_img_list = str(full_list) 

# 4. Código HTML/CSS/JS (Inyección directa flexible)
cinta_html = f"""
<style>
    .slider {{
        height: 180px;
        margin: 0 auto;
        position: relative;
        width: 100%;
        display: flex;
        align-items: center;
        overflow: hidden;
        padding: 10px 0;
    }}
    
    .slide-track {{
        display: flex;
        width: {ancho_total_track}px;
        animation: scroll 40s linear infinite;
    }}
    
    .slide-track:hover {{ animation-play-state: paused; }}
    
    @keyframes scroll {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-{distancia_scroll}px); }}
    }}
    
    .slide {{
        height: 150px;
        width: {ancho_foto}px;
        display: flex;
        align-items: center;
        padding: 0 10px;
        box-sizing: border-box;
    }}
    
    .slide img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.3s, border 0.3s;
        box-shadow: 0 2px 4px rgba(0,0,0,0.5);
        border: 1px solid #D4AF37;
        opacity: 0.8;
    }}
    
    .slide img:hover {{ 
        transform: scale(1.1); 
        opacity: 1;
        border: 2px solid #fff;
        z-index: 10;
    }}

    /* --- CONTENEDOR EXPANDIBLE (CERO ALTURA POR DEFECTO) --- */
    #expandable-container {{
        display: none;
        width: 100%;
        background-color: rgba(0,0,0,0.3);
        border-top: 1px solid #D4AF37;
        border-bottom: 1px solid #D4AF37;
        margin: 10px 0;
        position: relative;
        text-align: center;
        padding: 20px 0;
        transition: height 0.3s ease;
    }}

    #big-image {{
        max-width: 90%;
        max-height: 450px;
        border-radius: 8px;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.4);
        display: block;
        margin: 0 auto;
    }}

    .close-exp {{
        position: absolute;
        top: 5px;
        right: 15px;
        color: #ddd;
        font-size: 24px;
        font-weight: bold;
        cursor: pointer;
        z-index: 100;
    }}
    .close-exp:hover {{ color: #D4AF37; }}

    .nav-btn {{
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        font-size: 30px;
        color: rgba(255,255,255,0.7);
        cursor: pointer;
        padding: 10px;
        user-select: none;
        transition: 0.2s;
    }}
    .nav-btn:hover {{ color: #D4AF37; scale: 1.2; }}
    .prev-exp {{ left: 10px; }}
    .next-exp {{ right: 10px; }}
</style>

<div class="slider">
    <div class="slide-track">
        {html_imgs}
    </div>
</div>

<div id="expandable-container">
    <span class="close-exp" onclick="closeViewer()">&times;</span>
    <div class="nav-btn prev-exp" onclick="changeBigImage(-1)">&#10094;</div>
    <div class="nav-btn next-exp" onclick="changeBigImage(1)">&#10095;</div>
    <img id="big-image" src="" alt="Vista Previa">
</div>

<script>
    var imgList = {js_img_list};
    var currIdx = 0;
    var container = document.getElementById("expandable-container");
    var bigImg = document.getElementById("big-image");

    function expandViewer(index) {{
        container.style.display = "block";
        currIdx = index;
        bigImg.src = imgList[currIdx];
        setTimeout(() => {{
             container.scrollIntoView({{behavior: "smooth", block: "center"}});
        }}, 100);
    }}

    function closeViewer() {{
        container.style.display = "none";
    }}

    function changeBigImage(n) {{
        currIdx += n;
        if (currIdx >= imgList.length) {{ currIdx = 0; }}
        if (currIdx < 0) {{ currIdx = imgList.length - 1; }}
        bigImg.src = imgList[currIdx];
    }}
</script>
"""

st.markdown(cinta_html, unsafe_allow_html=True)

# ==========================================
# 🔒 CANDADO FINAL: LA ÚLTIMA SORPRESA 🔒
# ==========================================

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #D4AF37;'>Y como última sorpresa de hoy quisiera darte esto:</h3>", unsafe_allow_html=True)

# Contenedor para centrar el desplegable del candado
col_pad1, col_pad2, col_pad3 = st.columns([1, 2, 1])

with col_pad2:
    with st.expander("🔒 Haz clic aquí para abrir el candado secreto"):
        code = st.text_input("Ingresa la clave secreta:", type="password")
        # Pista 1 (Siempre visible)
        st.markdown("<p style='text-align: center; font-style: italic; font-size: 0.8em; color: #888; margin-top: -10px;'>Pista: es una fecha muy especial</p>", unsafe_allow_html=True)

        if code == "2604":
            st.balloons()
            # Botón con enlace al Poema (ESTILO BOTÓN DORADO)
            st.markdown("""
            <div style='text-align: center; margin-top: 20px;'>
                <a href="PON_AQUI_TU_LINK_DEL_POEMA" target="_blank" style="background-color: #D4AF37; color: black; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; border-radius: 10px; font-weight: bold; border: 2px solid #fff; box-shadow: 0 0 15px #D4AF37;">
                    💌 Abrir 💌
                </a>
            </div>
            """, unsafe_allow_html=True)
        elif code:
            # Si falla, sale el error y la Pista 2
            st.error("Esa no es la clave... ¿Quizás el día que empezó todo? ❤️")
            st.warning("Pista 2: Son 4 dígitos :v\n\nNota: Creo que debí indicar esta pista primero xd")

# --- PIE DE PÁGINA ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D4AF37;'>Para Mariana, con todo mi amor. Miguel ❤️</h4>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
