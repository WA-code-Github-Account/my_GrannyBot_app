import streamlit as st
import random
from gtts import gTTS
import os

# ✅ Set page config FIRST!
st.set_page_config(page_title="GrannyBot - Pyari Dadi", layout="centered")

# ✅ Background image setup
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://images.unsplash.com/photo-1526045478516-99145907023c");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; color: #B22222;'>🧕 GrannyBot</h1>
    <h3 style='text-align: center; color: #555;'>Pyari Dadi Ki Awaaz Mein 🎙️</h3>
    <hr>
""", unsafe_allow_html=True)

# ---------- Lists with 10 items each ----------

totkay = [
    "🧂 Sar dard mein arrq-e-gulab mathay par lagana mufeed hay.",
    "🥗 Zaytun ka tail chehre ki jild ke liye behtareen hay.",
    "🌿 Haldi aur doodh ka mixure haddi k dard ke liye acha hay.",
    "🍵 Adrak ka kehwa zukaam mein bohat faida deta hay.",
    "🌱 Neem kay patto ka lep daano ke liye behtareen hay.",
    "🧴 Multani mitti chehre ke liye natural cleanser hay.",
    "🖤 Kalonji har marz ka ilaj hai siwae maut ke.",
    "🥛 Raat ko doodh mein badam bhigo kar khana dimagh ke liye acha hay.",
    "🌿 Munh se badbu dur karne ke liye sauf ka istemal karein.",
    "✨ Gharelu ubtan chehre ko chamakdaar banata hay."
]

kahaniyan = [
    "📖 Ek baar ka zikr hai, ek chor ne buddhi aurat ki maded ki aur bedleay mein uska dil badel gaya.",
    "🐦 Pyaasay kaway ne kankar daal kar paani uthaya aur sabit kiya ke soch jeet jati hai,taqqat nahi.",
    "👞 Ek mochi ne apne kaam se izzat kamai aur logon ka dil jeeta.",
    "👧 Ek larki har roz ek budhi aurat ko khana dayti thi aur ussay  dua milti thi.",
    "🦁 Ek sher aur chuhe ki dosti ne sabko hayrran kar diya.",
    "🌸 Ek nanhi si bachi ne sabak diya ke ahankaar kabhi acha nahi hota.",
    "👴 Ek buzrug ne bachon ko sabr ka matlab samjhayaa.",
    "🐦 Ek Choti si chirya ne tootay hue par ke saath bhi parwaaz ka khwab nahi chhoda." , 
    "🐢 Sab kachway ki raftaar ka mazak uratay rahe, or wohi kharghos say pahlay manzil par pohanch gaya.",
    "🙏 Ek waqt tha jab ek choti se maddad nay kisi ki zindagi baddal di."
]

nasihatain = [
    "⏳ Beta, waqt ki qadr karo, ye dobara nahi milta.",
    "🗣️ hamesha sach bolo or jhoot se doori ikhtiyar karo.",
    "🕌 Namaaz ki pabandi zindagi mein barkat laati hay.",
    "💞 Apno se pyar se baat karo, zindagi choti si hay.",
    "🙏 Hamesha shukar guzar raho, jitna hay usi mein khushi dhoondo.",
    "📚 Parhne ki aadat daalo, eilm kabhi zay nahi jaata.",
    "💫 Buron ka jawab achai se do, Allah sab dekhta hay.",
    "💔 Kisi ka dil mat dukhao, dil Allah ka ghar hota hay.",
    "👵 Buzurgon ki izzat karo, dua milegi.",
    "🌱 Rozana kuch naya seekhne ki koshish karo."
]

duaein = [
    "🛡️ Allah tumhe har burai se mehfooz rakhe.",
    "😊 Khosh raho mere bachay, har mod pe kaamiyabi milay.",
    "🌟 Tumhara naseeb chamak uthe, Ameen.",
    "🤝 Jahan bhi jao, log tumse pyar karein.",
    "❤️ Tumhara dil kabhi udaas na ho.",
    "🌈 Har mushkil asaan ho jaye, Ameen.",
    "🧕 Allah tumhe sehat aur lambi zindagi de.",
    "🚪 Tumhe har manzil asaani se mil jaye.",
    "☀️ Tumhara har din khushi wala ho.",
    "👵 Dadi ki duaon mein tum hamesha shaamil ho."
]

# ---------- Response selection based on keyword ----------

def get_response(user_input):
    text = user_input.lower()
    if "totka" in text:
        return random.choice(totkay)
    elif "kahani" in text:
        return random.choice(kahaniyan)
    elif "nasihat" in text:
        return random.choice(nasihatain)
    elif "dua" in text:
        return random.choice(duaein)
    else:
        return "❓ Beta, main samajh nahi paayi. Totka, kahani, nasihat ya dua poochho."

# ---------- Voice output using gTTS ----------

def speak_text(text):
    tts = gTTS(text=text, lang='ur')
    filename = "granny_voice.mp3"
    tts.save(filename)
    audio_file = open(filename, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    audio_file.close()
    os.remove(filename)

# ---------- Streamlit UI ----------

st.markdown("""
    <div style='text-align: center; margin-bottom: 1em;'>
        <input type='text' id='userInput' placeholder='Apna paighaam likhein (e.g., dadi koi kahani/totka/dua/nasihat sunao)' style='width: 90%; padding: 0.5em; font-size: 16px;'>
    </div>
""", unsafe_allow_html=True)

user_input = st.text_input("", label_visibility="collapsed")

if st.button("🎧 Suniye!") and user_input:
    response = get_response(user_input)
    st.markdown(f"<h5 style='color:#222;'>👵 <i>Dadi:</i> {response}</h5>", unsafe_allow_html=True)
    speak_text(response)

# ---------- Footer Branding ----------
st.markdown("---")
st.markdown(
    "<h4 style='text-align: center; color: #888;'>💖 Made with love by <span style='color:#B22222;'><b>Aziza Siddiqui®</b></span></h4>",
    unsafe_allow_html=True
)
