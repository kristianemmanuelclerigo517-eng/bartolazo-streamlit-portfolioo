
import streamlit as st
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Jamycha P. Bartolazo | Portfolio",
    page_icon="🎵",
    layout="wide"
)

# IMAGE DIRECTORY
IMAGE_DIR = Path(__file__).parent / "images"

def show_image(filename, caption=None, width=None):
    image_path = IMAGE_DIR / filename

    if image_path.exists():
        if width:
            st.image(str(image_path), caption=caption, width=width)
        else:
            st.image(str(image_path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: {filename}")

# CUSTOM DESIGN
st.markdown("""
<style>
.stApp {
    background-color: #faf7ff;
    color: #292238 !important;
}

.stApp p, .stApp span, .stApp li,
.stApp label, [data-testid="stMarkdownContainer"] p {
    color: #292238 !important;
}

h1, h2, h3, h4, h5, h6 {
    color: #7546a5 !important;
}

[data-testid="stSidebar"] {
    background-color: #eee5fa;
}

[data-testid="stSidebar"] * {
    color: #292238 !important;
}

.stButton button {
    background-color: #8e63b6;
    color: white !important;
    border: none;
    border-radius: 10px;
}

[data-testid="stCaptionContainer"] {
    color: #62566f !important;
}

hr {
    border-color: #d9c8eb;
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION
st.sidebar.title("🎵 My Portfolio")
st.sidebar.write("Jamycha P. Bartolazo")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Personal Information",
        "Education",
        "Hobbies",
        "Interests",
        "STEM & Engineering"
    ]
)

# HOME
if page == "Home":

    left, right = st.columns([2, 1], gap="large")

    with left:
        st.title("Jamycha P. Bartolazo")
        st.subheader("Welcome to My Personal Portfolio! 🎶")

        st.write("""
        Hello! I'm Jamycha P. Bartolazo. Welcome to my personal
        portfolio, where you can learn more about my hobbies,
        interests, education, and passion for discovering new things.
        """)

    with right:
        show_image("profile.jpg", width=220)

    st.markdown("---")
    st.header("A Little About Me")

    st.write("""
    I enjoy expressing myself through music, especially by playing
    musical instruments and composing my own songs. I also love
    spending time with my cats.

    I believe that learning is a continuous journey, and I enjoy
    exploring new experiences and discovering things that interest me.
    """)

# PERSONAL INFORMATION
elif page == "Personal Information":

    st.title("Personal Information")

    st.write("**Full Name:** Jamycha P. Bartolazo")
    st.write("**Senior High School:** Bislig City National High School")
    st.write("**Strand:** STEM")
    st.write("**College:** North Eastern Mindanao State University (NEMSU)")

    st.markdown("---")
    st.subheader("My Personality and Values")

    st.write("""
    I enjoy creativity, learning, and discovering new things.
    Music gives me a way to express myself, while my curiosity
    encourages me to explore different ideas and experiences.
    """)

# EDUCATION
elif page == "Education":

    st.title("Educational Attainment")

    st.subheader("Senior High School")
    st.write("**School:** Bislig City National High School")
    st.write("**Strand:** Science, Technology, Engineering, and Mathematics (STEM)")

    st.markdown("---")

    st.subheader("College")
    st.write("**School:** North Eastern Mindanao State University (NEMSU)")
    st.write("**Level:** College")

    st.write("""
    Continuing my education at NEMSU gives me opportunities
    to gain more knowledge, develop new skills, and prepare
    for my future career.
    """)

    show_image("engineering.jpg", "Science, Technology, Engineering, and Mathematics")

# HOBBIES
elif page == "Hobbies":

    st.title("My Hobbies")

    st.subheader("🎸 Playing the Ukulele and Guitar")

    st.write("""
    I enjoy playing the ukulele and guitar because music allows
    me to express my feelings and creativity.
    """)

    show_image("hobbies.jpg")

    st.markdown("---")

    st.subheader("🎼 Composing My Own Songs")

    st.write("""
    I love creating and composing my own songs. It gives me the
    opportunity to turn my thoughts and emotions into music.
    """)

    st.markdown("---")

    st.subheader("🐱 Spending Time with My Cats")

    st.write("""
    I also enjoy playing and spending time with my cats.
    They make my free time more enjoyable and meaningful.
    """)

# INTERESTS
elif page == "Interests":

    st.title("My Interests")

    st.subheader("🎵 Music")

    st.write("""
    Music is one of my biggest interests. I enjoy listening to
    different kinds of music, playing instruments, and discovering
    new ways to express myself through songs.
    """)

    show_image("interest.jpg")

    st.markdown("---")

    st.subheader("🌱 Learning and Exploring New Things")

    st.write("""
    I am interested in learning new skills, gaining knowledge,
    and exploring unfamiliar things. I believe every new experience
    is an opportunity to grow and improve myself.
    """)

# STEM AND ENGINEERING
elif page == "STEM & Engineering":

    st.title("STEM & Engineering")
    st.subheader("Exploring Science, Technology, and Innovation")

    show_image("engineering.jpg")

    st.write("""
    As a STEM student, I am introduced to different concepts
    involving science, technology, engineering, and mathematics.
    These fields help me understand how ideas can be transformed
    into practical solutions.
    """)

    st.markdown("---")

    st.subheader("⚙️ My Interest in Engineering")

    st.write("""
    Engineering interests me because it combines creativity,
    mathematics, and problem-solving to design and improve things.

    I find it interesting how engineers use scientific knowledge
    and technology to create machines, structures, and useful
    innovations that make everyday life better.
    """)

    st.markdown("---")

    st.subheader("🔬 Skills I Want to Develop")

    st.write("""
    - Critical and logical thinking
    - Problem-solving
    - Creativity and innovation
    - Scientific and mathematical understanding
    - Learning how technology and machines work
    """)

    st.markdown("---")

    st.subheader("My Goal")

    st.write("""
    I want to continue learning, improving my skills, and exploring
    opportunities in science, technology, and engineering.
    """)

# FOOTER
st.markdown("---")
st.caption("© 2026 Jamycha P. Bartolazo | Personal Portfolio")
