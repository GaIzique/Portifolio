import streamlit as st
from PIL import Image

# Função para exibir o currículo
def exibir_curriculo():
    st.header("Currículo Profissional")
    
    # Foto de perfil
    imagem_perfil = Image.open("perfil.jpg")  # Substitua o caminho para a foto do desenvolvedor
    st.image(imagem_perfil, width=150)
    
    st.subheader("Resumo das Qualificações")
    st.write("""
        - Compreensão de habilidades de estoque e  gestão de estoque, com experiência em gerenciar estoques de produtos, opereção de sistemas de marketplace como Iberis.
        - Conhecimento em tecnologias de desenvolvimento de software, como Python, C#.
        - Conhecimento de manipulação e manutenção em empresoras Epson.
        - Pacote office basico.
        

    """)
    
    st.subheader("Experiência Profissional")
    st.write("""
        **Auxiliar de estamparia, empresa Pepito Criativo (2024 - Atual)**
             - Recolhimento e organização de pedidos,  manutenção de estoque e controle de estoque, operação de impressoras de estampas Epson.



    """)
    
    st.subheader("Educação")
    st.write("""
        - Formado em Design de jogos .
    """)
    
    st.subheader("Habilidades Técnicas")
    st.write("""
        - Linguagens: Python, C#
        - Frameworks: 
        - Bancos de dados: 
        - Ferramentas: Unity
    """)
    
    st.subheader("Projetos e Realizações")
    st.write("""
        - Nenhuma no momento.
    """)
    
    st.subheader("Idiomas")
    st.write("""
        - Português: Nativo
        - Inglês: Médio
    """)
    
    st.subheader("Cursos e Treinamentos")
    st.write("""
        - Curso de Python básico.
        - Inglês Avançado.
        - Curso de administração.
    """)
    
    st.subheader("Referências Profissionais")
    st.write("""

    """)
    
    st.subheader("Contatos")
    st.write("""
        - Email: giziqui@gmail.com
        - Telefone: (16) 98858-2433

             
    """)

# Função para exibir o portfólio de projetos
def exibir_portfolio():
    st.header("Portfólio de Projetos")
    
    st.subheader("   ")
    st.write("""

    """)
    
# Configurações do Streamlit
st.set_page_config(page_title="Portfólio de Desenvolvimento", layout="wide")

# Sidebar para navegação
st.sidebar.title("Menu de Navegação")
opcao = st.sidebar.radio("Escolha uma seção", ["Currículo", "Portfólio"])

# Exibir conteúdo conforme a escolha do menu
if opcao == "Currículo":
    exibir_curriculo()
elif opcao == "Portfólio":
    exibir_portfolio()

