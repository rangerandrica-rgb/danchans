import streamlit as st
import random
from PIL import Image
import os

st.title("あなたのだんちゃんレベルは？")

questions = [
    {"image": "danchan/danchan1.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan2.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan3.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/dandan1.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan2.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/danchan4.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan5.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan6.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan7.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan8.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan9.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan10.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan11.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan12.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan13.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/danchan14.jpg", "options": ["動物", "人間"], "answer": "人間"},
    {"image": "danchan/dandan3.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan4.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan5.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan6.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan7.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan8.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan9.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan10.jpg", "options": ["動物", "人間"], "answer": "動物"},
    {"image": "danchan/dandan11.jpg", "options": ["動物", "人間"], "answer": "動物"},

]

# セッションごとにランダム5問を選ぶ
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(questions, 5)
    st.session_state.q_index = 0
    st.session_state.score = 0

# answered がまだなければ作る
if "answered" not in st.session_state:
    st.session_state.answered = False


questions = st.session_state.questions

if st.session_state.q_index < len(questions):
    q = st.session_state.questions[st.session_state.q_index]
    st.write("画像パス:",q["image"])
    img = Image.open(q["image"])
    st.image(img, caption="このだんちゃんはどっち？", use_container_width=True)
    choice = st.radio("答えを選んでください:", q["options"], key=f"q{st.session_state.q_index}")

    if not st.session_state.answered:
        if st.button("回答する"):
            if choice == q["answer"]:
                st.success("正解！さすがだね🤓")
                st.session_state.score += 1
            else:
                st.error(f"あれれちょっと違ったみたい… 正解は「{q['answer']}」だよ")
            st.session_state.answered = True  # 回答済みにする

# 次の問題へボタン
    if st.session_state.answered:
        if st.button("次の問題へ"):
            st.session_state.q_index += 1
            st.session_state.answered = False

else:
    st.subheader("🎉 チャレンジ終了！ 🎉")
    st.write(f"あなたのスコア: {st.session_state.score} / {len(questions)}")
    if st.button("もう一度だんちゃんと向き合ってみる"):
# ランダムに新しい問題を選び直す
        st.session_state.questions = random.sample(questions, 5)
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.answered = False













