from flask import Flask, render_template, request, session, redirect, url_for
import google.generativeai as genai
from dotenv import load_dotenv
import os
import markdown

# --- API Anahtarını yükleme ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Hata: GEMINI_API_KEY bulunamadı.")
    exit()

# --- Gemini'yi yapılandırma ---
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("Gemini modeli başarıyla yüklendi.")
except Exception as e:
    print(f"Hata: Gemini API ya da modeli yüklenemedi. Detay: {e}")
    model = None

# --- Flask uygulaması başlat ---
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sadece_bana_ozel_cok_gizli_anahtar'

# --- Ana sayfa ---
@app.route('/')
def index():
    if 'chat_history' not in session:
        session['chat_history'] = []
    return render_template('index.html', chat_history=session['chat_history'])

# --- Mesaj gönderme ---
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.form.get('user_input', '').strip()
    if user_message == '':
        return redirect(url_for('index'))

    # Geçmişi getir
    chat_history = session.get('chat_history', [])
    chat_history.append({"sender": "user", "message": user_message})

    ai_response = "Üzgünüm şu anda size cevap veremiyorum. Bir sorun oluştu."
    if model:
        try:
            prompt = f"""
            Sen akıllı bir e-ticaret ürün asistanısın. Kullanıcının isteklerini anla ve bütçe, ürün tipi, kişi (kardeş, arkadaş vb.) gibi kriterlere göre ürün önerileri yap. 
            Eğer kullanıcı birden fazla ürün linki verirse (şimdilik sadece ürün adlarını/açıklamalarını varsayalım), bu ürünleri analiz et, avantaj ve dezavantajlarını belirt ve daha iyi alternatifler sun.
            Cevaplarını kullanıcıya faydalı olacak şekilde kullanıcının seninle konuştuğu dilde samimi bir şekilde ver. 
            Direkt olarak güncel, hala kullanılan satın alınabilen ürünlerin linklerini ver.
            Kullanıcının sorusu: "{user_message}"
            """
            response = model.generate_content(prompt)
            ai_response = response.text
            # Markdown metni HTML'e çevir
            ai_response = markdown.markdown(ai_response)
        except Exception as e:
            print(f"Hata: Gemini API'den cevap alınırken sorun oluştu: {e}")
            ai_response = "Bir hata oluştuğu için şu an cevap veremiyorum. (Gemini API hatası)"

    # Cevabı geçmişe ekle
    chat_history.append({"sender": "ai", "message": ai_response})
    session['chat_history'] = chat_history  # yeniden ata
    session.modified = True

    return redirect(url_for('index'))

# --- Sohbeti temizleme ---
@app.route('/clear_chat')
def clear_chat():
    session.pop('chat_history', None)
    return redirect(url_for('index'))

# --- Uygulamayı çalıştır ---
if __name__ == '__main__':
    app.run(debug=True)


