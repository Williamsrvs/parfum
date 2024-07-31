import streamlit as st
from PIL import Image


#Projeto de Cartão de Visita digital
st.sidebar.image('Parfum.png')
st.sidebar.header("Aqui você encontra os melhores produtos, venha conferir")
st.sidebar.markdown("Village das Fontes, 770 Bloco R Apto 206")
st.sidebar.markdown("Tel.(082) 98109-0042")
# Definindo o CSS para centralizar o cabeçalho
header_css = """
<style>
.header {
    text-align: center;
    font-family: Arial, sans-serif;
    font-size: 40px;
}
</style>
"""

# Aplicando o CSS no cabeçalho
st.markdown(header_css, unsafe_allow_html=True)

# Usando o CSS customizado no cabeçalho

# Definindo o título com HTML e CSS
title_html = """
<h6 class="header">PERFUMARIA E COSMÉTICOS - PARFUM</h6>
"""

# Aplicando o CSS
css_style = """
<style>
.header {
    text-align: center;
    color: #F1F1F2; /* Altere a cor conforme necessário */
}
</style>
"""

# Exibir o título e aplicar o CSS
st.markdown(css_style, unsafe_allow_html=True)
st.markdown(title_html, unsafe_allow_html=True)
st.markdown("_______________________________________________________________")

col1,col2,col3,col4,col5,col6,col7=st.tabs(["Whatsapp","Instagram","Telegram","Loja O boticário","Loja Natura","Ir para Localização","Pronta Entrega"])

# Definindo o CSS para centralizar o cabeçalho
header_css = """
<style>
.header {
    text-align: center;
    font-family: Arial, sans-serif;
    font-size: 30px;
}
</style>
"""

# Aplicando o CSS no cabeçalho
st.markdown(header_css, unsafe_allow_html=True)

# Definindo o CSS para o fundo de cor gradiente
page_bg_css = """
<style>
.stApp {
    background: linear-gradient(to right, #5A5398, #33646E);
}
</style>
"""
# Aplicando o CSS no aplicativo
st.markdown(page_bg_css, unsafe_allow_html=True)

# Conteúdo da aba WhatsApp
with col1:
    st.markdown("""
        <a href="http://wa.me/5582981090042" target="_blank">
            <button style="background-color: #25D366; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para WhatsApp
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Instagram
with col2:
    st.markdown("""
        <a href="https://www.instagram.com/parfum_wr" target="_blank">
            <button style="background-color: #E1306C; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para Instagram
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Telegram
with col3:
    st.markdown("""
        <a href="https://t.me/82981090042" target="_blank">
            <button style="background-color: #0088cc; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para Telegram
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Loja O Boticário
with col4:
    st.markdown("""
        <a href="https://minhaloja.grupoboticario.com.br/loja-williams-rodrigues-vieira-silva--7116272" target="_blank">
            <button style="background-color: #006400; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para Loja O Boticário
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Loja Natura
with col5:
    st.markdown("""
        <a href="https://www.natura.com.br/consultoria/doralices0606" target="_blank">
            <button style="background-color: #EB5E28; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para Loja Natura
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Localização
with col6:
    st.markdown("""
        <a href="https://www.google.com/maps/dir/-9.543113,-35.7375994/Perfumaria+e+Cosm%C3%A9ticos-+PARFUM/@-9.5430305,-35.7398643,17z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x701391ca6d5e037:0x23938b53ee4b9d48!2m2!1d-35.7369753!2d-9.5428977?hl=pt-BR&entry=ttu" target="_blank">
            <button style="background-color: #2206F5; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Ir para Localização
            </button>
        </a>
    """, unsafe_allow_html=True)

# Conteúdo da aba Localização
with col7:
    st.markdown("""
        <a href="https://wa.me/c/5582981090042">
            <button style="background-color: #DF138D; color: white; padding: 1px 2px; border: none; border-radius: 5px; cursor: pointer;">
                Pronta Entrega
            </button>
        </a>
    """, unsafe_allow_html=True)


st.video('video.mp4')

st.markdown("""
    <div style="text-align: center;">
        © Autor deste Projeto dateanalytics - Soluções em tecnologia
            
Solicite agora mesmo o seu projeto   
Tel.(082) 98863-9394
    </div>
""", unsafe_allow_html=True)
