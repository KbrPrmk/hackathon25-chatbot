<h1 align="center">Akıllı Ürün Asistanı</h1>
<p align="center"><b>Hackathon 2025 için yapay zeka kullanılarak geliştirilmiş web tabanlı bir chatbottur. Kullanıcılara ürünler hakkında bilgi vermek, istenirse link vermek ve sorularını yanıtlamak amacıyla tasarlanmıştır.</b></p>

## Özellikler
* **Doğal Dil İşleme (NLP) Yeteneği:** Gelişmiş dil modelleri sayesinde, kullanıcıların metin tabanlı sorularını anlamlandırabilir ve bu sorulara bağlamına uygun, akıcı cevaplar üretebilir. Basit anahtar kelime eşleştirmesinden ziyade, cümlenin amacını ve niyetini kavrayarak daha doğal bir sohbet deneyimi sunar.
* **Akıllı Ürün ve Bütçe Önerisi:** Chatbot'un en güçlü özelliği, kullanıcıların "5000 TL altı bir laptop öner" veya "fotoğraf çekimi için iyi bir kamera" gibi doğal dil komutlarını anlayabilmesidir. Bu komutlar doğrultusunda, belirlediğiniz kriterlere en uygun ürünleri akıllıca önerir.
* **Doğrudan Ürün Bağlantıları Sağlama:** Sorgulanan ürün hakkında detaylı bilgi verdikten sonra, ilgili ürünün doğrudan satın alma veya detay sayfasının linkini sağlayabilmesidir. Bu sayede, kullanıcılar sohbetten ayrılmadan, istedikleri ürüne anında ulaşabilirler.
* **Kullanıcı Dostu ve Etkileşimli Arayüz:** Minimalist ve sezgisel bir arayüzle tasarlanmıştır. Kullanıcılar, kolayca sohbet başlatabilir ve chatbot'un yanıtlarını açık ve anlaşılır bir formatta alabilirler. Ayrıca, sohbet geçmişi gibi özellikler, etkileşimi daha akıcı hale getirir.

## Kullanılan Teknolojiler
* **Frontend:**
  * **HTML:** Uygulamanın iskeletini ve sayfa yapısını oluşturmak için kullanılmıştır. Chatbot'un mesaj kutuları, giriş alanı, başlık gibi tüm yapısal elemanları HTML etiketleriyle tanımlanmıştır.
  * **CSS:** Chatbot'un görsel tasarımını, stilini ve düzenini sağlamak için kullanılmıştır. Renkler, yazı tipleri, sohbet balonlarının şekli, animasyonlar ve responsive (farklı ekran boyutlarına uyumlu) tasarım gibi tüm estetik unsurlar CSS kodlarıyla belirlenmiştir.

* **Backend:**
  * **Python:** Uygulamanın sunucu tarafı mantığı tamamen Python programlama dili ile yazılmıştır.
  * **Flask:** Hafif ve esnek bir Python web framework'üdür. Projenin ana yapısı, oturum (session) yönetimi ve kullanıcı isteklerinin işlenmesi Flask ile sağlanmıştır.
  * **Jinja2:** Flask'in varsayılan şablon motorudur. Kullanıcı arayüzünün (HTML) dinamik olarak oluşturulması ve sohbet geçmişinin sayfaya yerleştirilmesi Jinja2 şablonları kullanılarak gerçekleştirilmiştir.
  * **Python-dotenv:** Hassas bilgileri (Gemini API anahtarı gibi) güvenli bir şekilde yönetmek ve ortam değişkenlerinden okumak için bu kütüphane kullanılmıştır.

* **Yapay Zeka (AI) ve API:**
  * **Google Gemini API:** Chatbot'un temel yapay zeka motorudur. Kullanıcıdan gelen soruları anlama, ürün önerileri oluşturma ve ilgili linkleri bulma gibi tüm akıllı işlevler Gemini API ile sağlanmıştır.
