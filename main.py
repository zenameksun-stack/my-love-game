import streamlit as st
import os

st.set_page_config(page_title="Наш секретный сайт", page_icon="❤️", layout="centered")

# --- КРАСИВЫЙ СТИЛЬ САЙТА ---
st.markdown(
    """
    <style>
        @import url('https://googleapis.com');
        .stApp { background-color: #f3e8ff !important; color: #4a1d96 !important; font-family: "Montserrat", sans-serif; }
        .main-title { color: #6b21a8 !important; font-family: 'Caveat', cursive !important; font-size: 50px !important; text-align: center; font-weight: bold; margin-top: -10px; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(107, 33, 168, 0.15); }
        h2 { color: #7c3aed !important; font-size: 30px !important; font-weight: bold; }
        p, span, label, div[data-baseweb="radio"] { color: #3b0764 !important; font-size: 24px !important; font-weight: 500 !important; }
        div[data-testid="stWidgetLabel"] p { color: #6b21a8 !important; font-size: 26px !important; font-weight: bold !important; }
        .stImage img { border: none !important; border-radius: 0px !important; box-shadow: none !important; }
        .big-success { font-size: 24px !important; color: #db2777 !important; font-weight: bold; text-align: center; background-color: #fce7f3; padding: 10px; border-radius: 12px; margin: 10px 0; }
        .big-error { font-size: 24px !important; color: #b91c1c !important; font-weight: bold; text-align: center; background-color: #fee2e2; padding: 10px; border-radius: 12px; margin: 10px 0; }
        div[data-testid="stSelectbox"] label p { font-size: 26px !important; color: #4a1d96 !important; font-weight: bold !important; }
        div[data-baseweb="select"] div { font-size: 18px !important; font-weight: bold !important; color: #6b21a8 !important; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">❤️ Наш секретный сайт ❤️</div>', unsafe_allow_html=True)
st.divider()


# Ультра-надежная функция поиска любого формата фото
def smart_photo3():
    possible_names = [
        "photo3.jpg", "photo3.JPG", "photo3.jpeg", "photo3.JPEG",
        "photo3.png", "photo3.PNG", "photo3.jfif", "photo3.webp",
        "photo 3.jpg", "photo 3.JPG", "photo 3.jpeg", "photo 3.JPEG",
        "photo 3.png", "photo 3.PNG"
    ]
    for name in possible_names:
        if os.path.exists(name):
            st.image(name, caption="Самая лучшая пара во Вселенной! 🔒❤️")
            return
    st.error("⚠️ Файл photo3 не найден! Проверьте, что вы перетащили его в PyCharm.")


levels = ["легенький уровень❤️", "средний уровень💘", "сложний уровень💖"]
mode = st.selectbox("Выбери уровень сложности:", levels)

# ==========================================
# 1. ЛЕГЕНЕНЬКИЙ УРОВЕНЬ ❤️
# ==========================================
if mode == "легенький уровень❤️":
    st.markdown("<h2>✨ Насколько добре ти пам'ятаєш наші моменти?</h2>", unsafe_allow_html=True)

    a1 = st.radio("1. В каком году мы начали встречаться?", ["2024", "2025", "2026", "2027"], index=None, key="l1")
    if a1 == "2026":
        st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
        a2 = st.radio("2. Какого числа ты предложил мне стать твоей девушкой?", ["9", "12", "13", "14"], index=None,
                      key="l2")
        if a2 == "13":
            st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
            a3 = st.radio("3. Куда мы пошли на первой нашей прогулке?",
                          ["в Эпицентр", "в Голливуд", "на Золотой Пляж", "на Земснаряд"], index=None, key="l3")
            if a3 == "в Голливуд":
                st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
                a4 = st.radio("4. Какую фразу ты запомнишь навсегда от меня?",
                              ["канешна", "хорошо", "окей", "как скажешь"], index=None, key="l4")
                if a4 == "канешна":
                    st.balloons()
                    st.markdown('<div class="big-success">🎉 ТЫ ПРОШЕЛ ЛЕГЕНЬКИЙ УРОВЕНЬ! 🎉</div>',
                                unsafe_allow_html=True)
                    try:
                        st.image("photo1.JPG", caption="Наш первый уровень пройден 🥰")
                    except:
                        st.image("photo1.jpg", caption="Наш первый уровень пройден 🥰")
                    st.info(
                        "Солнышко, поздравляю, ты прошел первый уровень! Теперь ты можешь выбрать 'средний уровень💘' в списке самого верха страницы! ❤️")
                elif a4 is not None:
                    st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
            elif a3 is not None:
                st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
        elif a2 is not None:
            st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
    elif a1 is not None:
        st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)

# ==========================================
# 2. СРЕДНИЙ УРОВЕНЬ 💘
# ==========================================
elif mode == "средний уровень💘":
    st.markdown("<h2>✨ Уровень 2: Наши общие воспоминания и шутки</h2>", unsafe_allow_html=True)

    b1 = st.radio("1. Какое АТБ самое легендарное?", ["на Сиверском", "на Козацокой", "на Цуме", "на Бобровице"],
                  index=None, key="m1")
    if b1 == "на Бобровице":
        st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
        b2 = st.radio("2. Что произошло в Голливуде 16.01.2026 г.?",
                      ["первый раз взялись за ручку", "обменялись резинками", "первый раз поцеловались",
                       "первый раз обнялись"], index=None, key="m2")
        if b2 == "обменялись резинками":
            st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
            b3 = st.radio("3. Каким играм ты учил меня играть 26.01.2026 г.?",
                          ["в доту", "в раст", "в кс", "в бравл старс"], index=None, key="m3")
            if b3 == "в кс":
                st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
                b4 = st.radio("4. Когда мы поиграли в маску с поцелуями?",
                              ["14.01.2026", "16.01.2026", "15.01.2026", "12.01.2026"], index=None, key="m4")
                if b4 == "16.01.2026":
                    st.balloons()
                    st.markdown('<div class="big-success">🎉 ТЫ СУПЕР, СРЕДНИЙ УРОВЕНЬ ПРОЙДЕН! 🎉</div>',
                                unsafe_allow_html=True)
                    try:
                        st.image("photo2.JPG", caption="Мы становимся ещё ближе 🥰")
                    except:
                        st.image("photo2.jpg", caption="Мы становимся ещё ближе 🥰")
                    st.info(
                        "Зайка, умничка мояя, ты большой молодец💋 Теперь выбери 'сложний уровень💖' в списке самого верха страницы!")
                elif b4 is not None:
                    st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
            elif b3 is not None:
                st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
        elif b2 is not None:
            st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
    elif b1 is not None:
        st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)

# ==========================================
# 3. СЛОЖНИЙ УРОВЕНЬ 💖
# ==========================================
elif mode == "сложний уровень💖":
    st.markdown("<h2>🔥 Уровень 3: Проверка на максимальную внимательность!</h2>", unsafe_allow_html=True)

    c1 = st.radio("1. Какого числа мы первый раз поцеловались?",
                  ["14.01.2026", "17.01.2026", "13.01.2026", "18.01.2026"], index=None, key="h1")
    if c1 == "18.01.2026":
        st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
        c2 = st.radio("2. Какого числа мы первый раз созвонились в дс?",
                      ["07.01.2026", "08.01.2026", "09.01.2026", "10.01.2026"], index=None, key="h2")
        if c2 == "08.01.2026":
            st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
            c3 = st.radio("3. Когда мы первый раз списались?", ["утром", "днем", "вечером", "ночью"], index=None,
                          key="h3")
            if c3 == "ночью":
                st.markdown('<div class="big-success">Умница, ты ответил правильно!🌸💖</div>', unsafe_allow_html=True)
                c4 = st.radio("4. Что было 25.01.2026 г.?",
                              ["Эпицентр + знакомство с санечкой и соней", "Прогулка в Голливуде", "Пошли в Яловщину",
                               "Поехали на Земснаряд"], index=None, key="h4")
                if c4 == "Эпицентр + знакомство с санечкой и соней":
                    st.balloons()
                    st.markdown('<div class="big-success">👑 ТЫ ПРОШЕЛ ВСЮ ИГРУ! Абсолютный Победитель! 👑</div>',
                                unsafe_allow_html=True)

                    # Запуск умной функции вывода фото сердечка
                    smart_photo3()

                    st.info(
                        "Любименьй мой мальчик, я тебя очень сильно люблю, пасиба что прошел эту мини игру, и не забывай что самый лучший!💘")
                elif c4 is not None:
                    st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
            elif c3 is not None:
                st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
        elif c2 is not None:
            st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
    elif c1 is not None:
        st.markdown('<div class="big-error">подумай еще😉😘</div>', unsafe_allow_html=True)
