# Xodon Tools

**Xodon Tools - X ve Mastodon arasında kesintisiz iletim için bir köprü aracı**

Xodon Tools, X (Twitter) ve Mastodon hesaplarınızı birleştiren Python tabanlı bir yardımcı programdır. X'teki gönderilerinizi otomatik olarak Mastodon'a yansıtır ve X'teki takip listenizi Mastodon'da arayarak ve takip ederek senkronize eder. Her iki platformda da manuel çaba harcamadan varlık sürdürmek isteyen kullanıcılar için tasarlanmış olan Xodon Tools, platformlar arası etkileşimi basitleştirir.

## Özellikler

- **Gönderi Senkronizasyonu**: X'teki tweetlerinizi gerçek zamanlıya yakın bir şekilde (anket yöntemiyle) otomatik olarak Mastodon'a gönderir.
- **Takip Senkronizasyonu**: X'teki arkadaşlarınızı Mastodon'da bulur ve takip eder, sosyal ağlarınızı birleştirir.
- **Özelleştirilebilir Anket**: Uygulamanın X'teki yeni gönderileri kontrol etme sıklığını ayarlayabilirsiniz.
- **Hafif**: Python ile inşa edilmiştir, basitlik ve verimlilik için `tweepy` ve `requests` kullanır.

## Kurulum

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/makalin/Xodon-Tools.git
   cd Xodon-Tools
   ```

2. **Bağımlılıkları Yükleyin**:
   Python 3.x'in yüklü olduğundan emin olun, ardından şunu çalıştırın:
   ```bash
   pip install tweepy requests
   ```

3. **API Kimlik Bilgilerini Ayarlayın**:
   - **X (Twitter)**: [X Developer Portal](https://developer.twitter.com/) üzerinden API Anahtarı, API Sırrı, Erişim Belirteci ve Erişim Belirteci Sırrı alın.
   - **Mastodon**: Mastodon örneğinizden bir Erişim Belirteci oluşturun (örneğin, Ayarlar > Geliştirme yoluyla).

## Yapılandırma

Proje kök dizininde bir `.env` dosyası oluşturun ve kimlik bilgilerinizi ekleyin:

```env
X_API_KEY=sizin-api-anahtarınız
X_API_SECRET=sizin-api-sırrınız
X_ACCESS_TOKEN=sizin-erişim-belirteciniz
X_ACCESS_SECRET=sizin-erişim-belirteci-sırrınız
MASTODON_INSTANCE=https://mastodon.social  # Örneğinizin URL'si ile değiştirin
MASTODON_TOKEN=sizin-mastodon-erişim-belirteciniz
```

Bu bilgileri `.env` dosyasından yüklemek için betiği güncelleyin (bunun için `python-dotenv` gereklidir):
```bash
pip install python-dotenv
```

Betiğin üst kısmını şu şekilde değiştirin:
```python
from dotenv import load_dotenv
import os

load_dotenv()
X_API_KEY = os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")
MASTODON_INSTANCE = os.getenv("MASTODON_INSTANCE")
MASTODON_TOKEN = os.getenv("MASTODON_TOKEN")
```

## Kullanım

1. **Uygulamayı Çalıştırın**:
   ```bash
   python xodon.py
   ```
2. **Detayları Girin**:
   - X kullanıcı adınız (@ olmadan).
   - Anket aralığı saniye cinsinden (örneğin, 60).

3. **Neler Oluyor**:
   - Uygulama başlangıçta X takip listenizi Mastodon'a senkronize eder.
   - Ardından X hesabınızı yeni gönderiler için izler ve bunları Mastodon'a yansıtır.

### Örnek Çıktı
```
X kullanıcı adınızı girin (@ olmadan): benimxkullanıcım
Anket aralığını saniye cinsinden girin (örneğin, 60): 60
Xodon Tools - X ve Mastodon arasında kesintisiz iletim için bir köprü aracı
Benimxkullanıcım için uygulama başlatılıyor...
Benimxkullanıcım için takip listesi senkronize ediliyor...
X'te 50 kullanıcı bulundu.
Kullanıcı1, Mastodon'da @kullanıcı1@mastodon.social olarak takip edildi
X gönderileri her 60 saniyede bir izleniyor...
Yeni tweet tespit edildi: Merhaba dünya!...
Mastodon'a gönderildi: Merhaba dünya!...
```

## Sınırlamalar

- **API Hız Sınırlamaları**: X'in ücretsiz katmanı okuma ve gönderme işlemlerini sınırlar; Mastodon sınırları örneğe göre değişir. Anket aralıklarını buna göre ayarlayın.
- **Kullanıcı Eşleştirme**: X kullanıcı adlarını Mastodon ile eşleştirir, bu her zaman doğru olmayabilir. Biyografi veya isim eşleştirme bunu iyileştirebilir (gelecekteki özellik).
- **Tek Örnek**: Şu anda tek bir Mastodon örneğini destekler. Çoklu örnek desteği planlanmaktadır.

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Başlamak için:

1. Repoyu çatallayın.
2. Bir dal oluşturun (`git checkout -b özellik/sizin-özelliğiniz`).
3. Değişikliklerinizi kaydedin (`git commit -m "Özelliğinizi ekleyin"`).
4. Dalınıza itin (`git push origin özellik/sizin-özelliğiniz`).
5. Bir Çekme İsteği açın.

### İyileştirme Fikirleri
- X güncellemeleri için gerçek zamanlı webhook desteği (premium X API erişimi gerektirir).
- Çoklu Mastodon örneği desteği.
- Kolay yapılandırma için GUI arayüzü.
- Geliştirilmiş kullanıcı eşleştirme mantığı.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## Teşekkürler

- X API entegrasyonu için [Tweepy](https://github.com/tweepy/tweepy) ile inşa edilmiştir.
- Mastodon etkileşimleri için [Mastodon API](https://docs.joinmastodon.org/api/) kullanılır.
