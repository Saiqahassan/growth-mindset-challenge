import streamlit as st

st.set_page_config(page_title='Growth Mindset Challenge', page_icon='🌱', layout='wide')
st.title('🌱 Growth Mindset Challenge')
st.write("This is a simple app that will help you develop a growth mindset. A growth mindset is the belief that you can develop your abilities through hard work, dedication, and perseverance. People with a growth mindset are more likely to succeed in life because they are willing to take on challenges, learn from their mistakes, and keep going even when things get tough. Are you ready to take on the challenge? Let's get started!")

# Challenge 1: Embrace Failure
st.header('💘 Challenge 1: Embrace Failure')
st.write("Failure is a natural part of the learning process. It's not a sign that you're not good enough, it's a sign that you're trying something new and pushing yourself out of your comfort zone. Embrace failure as an opportunity to learn and grow.")
user_input = st.text_area("Share a time when you failed at something and what you learned from the experience:")

# Challenge 2: Learn from Mistakes
st.header('📝 Challenge 2: Learn from Mistakes')
st.write("Mistakes are a valuable source of information that can help you improve and grow. Instead of beating yourself up over your mistakes, take the time to reflect on what went wrong and what you can do differently next time.")
user_input = st.text_area("Share a mistake you made recently and what you learned from it:")

# Challenge 3: Take on Challenges
st.header('🚀 Challenge 3: Take on Challenges')
st.write("Challenges are an opportunity to test your limits and discover what you're capable of. Instead of shying away from challenges, embrace them as a chance to learn and grow.")
user_input = st.text_area("Share a challenge you're currently facing and how you plan to overcome it:")

# Challenge 4: Persist through difficulties
st.header('🏃 Challenge 4: Persist through difficulties')
st.write("Persistence is the key to success. When things get tough, it's easy to give up and walk away. But if you want to achieve your goals, you need to keep going even when the going gets tough.")
user_input = st.text_area("Share a time when you faced a difficult situation and how you persevered through it:")

# Challenge 5: Celebrate your effort or success
st.header('🎉 Challenge 5: Celebrate your effort or success')
st.write("It's important to celebrate your efforts and successes, no matter how small they may seem. Recognizing your hard work and progress can help you stay motivated and focused on your goals.")
user_input = st.text_area("Share a recent accomplishment or effort that you're proud of:")

# Footer
st.write("- - -")
st.write("**Congratulations on completing the Growth Mindset Challenge! Remember, developing a growth mindset is an ongoing process that takes time and effort. Keep challenging yourself, learning from your mistakes, and celebrating your successes. You've got this! 🌱**")
