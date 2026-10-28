# Code Aesthetic: Kesmesiz anlatım, tartışmalı iddia ve tek kod örneği

## Kısa cevap
Bu sekiz video tıklamayı tartışmalı ya da kendinden emin bir iddiayla kazanıyor. Başlıklarda "Don't", "Shouldn't", "Flaws", "Can Make Your Code Worse", "The Best Pattern" gibi ifadeler var. Kapaklarda yüz yok; koyu zemin üzerinde tipografi ve renkli kutular kullanılıyor. İzleyiciyi tutan şey kurgu değil: 8 videonun 5'inde hiç kesme yok. Konuşma her videoda 0. saniyede başlıyor ve ilk cümle doğrudan iddiayı söylüyor. Dikkat, yaklaşık her 30–90 saniyede gelen "But…" cümleleriyle tazeleniyor. Bunlar yeni bir gereksinim, bir sorun ya da önceki önerinin tersine dönmesi oluyor. Öğretim çoğunlukla tek bir kod örneği üzerinden adım adım ilerliyor. Videoların çoğu kesin kuralı sonunda yumuşatıyor. Kalıp oldukça tutarlı; açılış cümlesinin türü ve kapak sözünün karşılandığı an ise videodan videoya değişiyor.

## Ölçülen kalıp

| Ölçü | Medyan | Aralık |
|---|---|---|
| Süre | 554,5 sn (~9,2 dk) | 313–1010 sn |
| Dakikada kesme | 0 | 0–1,0 |
| İlk 3 / 10 / 30 sn'de kesme | 0 / 0 / 0 | 8 videonun hepsinde 0 |
| Medyan çekim süresi | 378,5 sn | 1,98–795 sn |
| Dakikada görsel değişim | 4,15 | 2,2–10,9 |
| Görsel değişimler arası medyan süre | 8,69 sn | 3,67–16,68 sn |
| İlk 30 sn'de görsel değişim | 2,5 | 2–4 |
| Kelime/dk (genel) | 161,7 | 139,8–174,0 |
| Kelime/dk (ilk 3 sn) | 180 | 120–220 |
| Kelime/dk (ilk 10 sn) | 147 | 78–204 |
| Kelime/dk (ilk 30 sn) | 153 | 88–198 |
| İlk konuşma saniyesi | 0,0 | 8 videonun hepsinde 0,0 |
| Cümle uzunluğu (medyan kelime) | 13 | 10–14 |

Sayıların anlamı: Kanal kesme kullanmıyor. 5 videoda tek çekim süresi videonun kendi süresine eşit, örneğin [V2] 795 sn ve [V5] 600 sn. Ekrandaki değişimi kesmeler değil animasyonlar sağlıyor: yazının kelime kelime belirmesi, kod satırlarının eklenmesi, diyagramlar. Bu değişimler ortalama 8–9 saniyede bir geliyor. Uç değerler de var. En sık değişen video, hareketli oyun sahnesi olan [V8] (dakikada 10,9). En seyrek değişen video, uzun kod ekranlarıyla ilerleyen [V6] (dakikada 2,2). [V1]'in 1,98 sn'lik medyan çekim süresi, kelime kelime açılan metnin kesme sayılmasından kaynaklanıyor olabilir; bu bir tahmin. Konuşma ilk saniyede başlıyor ve açılışta biraz hızlı (ilk 3 sn medyanı 180). İlk 10–30 saniyede ise genel hızın altına iniyor. [V3] bunun en belirgin örneği: ilk 10 sn'de dakikada 78 kelime. Yani tempo kurgudan değil, sözlü yoğunluktan geliyor.

## Paketleme (başlık + kapak)
- **Kapakta yüz yok, koyu zemin üzerinde yalnızca tipografi ve şekil var:** 8/8. Sunucu hiçbir kapakta görünmüyor.
- **Mor veya lavanta vurgu kelimesi:** 6/8. Örnekler: [V1]'de "Functional", [V2]'de "Dependency", [V4]'te "Don't Write", [V5]'te "Composition >", [V6]'da "I'm a", [V8]'de "vs coupling". [V3]'te kırmızı-pembe fırça yazı, [V7]'de yeşilimsi "how not to" kullanılmış.
- **Kavramı simgeleyen renkli kare/kutu diyagramı:** 5/8 ([V1], [V2], [V5], [V6], [V8]). [V6]'daki basamaklı kareler girintiyi, [V5]'teki küp ağacı kalıtımı gösteriyor. [V7]'nin kapağında kod satırları var (int d; int delay; int delaySeconds; TimeSpan delay;) ve "BaseObject" üstü çizili.
- **Kapak metni başlığı tekrar ediyor:** 4/8 ([V1], [V3], [V4] birebir; [V2] "The Best Pattern" kısmı çıkarılmış hâliyle).
- **Kapak başlığa yeni bir açı ekliyor:** 4/8. [V5]: başlık "The Flaws of Inheritance", kapak "Composition > Inheritance". [V6]: başlık "Why You Shouldn't Nest Your Code", kapak "I'm a Never Nester {". [V7]: kapakta "how not to Name Things". [V8]: kapakta "ABSTRACTION vs coupling".
- **Sözün türü, yani alışkanlığa karşı çıkan, olumsuz ya da kural koyan bir çerçeve:** 6/8 ([V2], [V4], [V5], [V6], [V7], [V8]). Kalan iki video da görüş bildiriyor: [V1] belli bir kitleye sesleniyor, [V3] ünlü "root of all evil" iddiasına dayanıyor.
- **Merak boşluğu:** Neredeyse hepsinde aynı soru var: "Bu neden kötü ya da iyi, ne zaman geçerli?" [V8]'deki "vs coupling" ikinci kavramı adlandırıp açıklamıyor. [V6] "never nester" diye yeni bir kimlik uyduruyor.

## İlk 3, 10 ve 30 saniye
**Sıra genelde şöyle:** 0. saniyede konuşma başlıyor ve iddia söyleniyor (8/8) → ekranda başlık ya da iddianın kendisi kelime kelime beliriyor → 10–30 saniye arasında tanım veya bağlam geliyor → 30. saniye civarında ilk kod ya da örnek ekrana çıkıyor.

- **İlk cümlenin türü:**
  - Görüş veya tartışmalı iddia: 4/8. [V2 0s] "Dependency injection is a term I don't love…", [V3 0s] "…root of all evil.", [V4 0s] "It's time to get a bit controversial.", [V6 0s] itiraf.
  - Bilinen bir söz veya alıntı: 2/8. [V5 0s] "prefer composition over inheritance", [V7 0s] "two hard things". [V3]'te Knuth alıntısı 5. saniyede ekrana geliyor.
  - Kitleye doğrudan hitap: 1/8 ([V1 0s]).
  - Somut bir senaryo: 1/8 ([V8 0s], oyun sahnesi).
- **Ekranda konuşmayla eşzamanlı açılan metin:** 5/8 ([V1], [V3], [V5], [V6], [V7]). [V2]'de sabit bir başlık kartı var, [V4]'te ilk 3 sn ekran boş, [V8]'de uzay gemisi çizimi beliriyor.
- **Açılış görüntüsü kapakla örtüşüyor:** 4/8 ([V1], [V2], [V3], [V6]).
- **Kapak sözü ekranda ilk ne zaman görünüyor:** medyan 0 sn (aralık 0–46). En geç [V8 46s]: "But there's a hidden trade-off… Coupling."
- **Kapak sözü ne zaman karşılanıyor:** medyan 285 sn, video süresinin medyan %80'i. 8 videonun 6'sı vaadi son çeyrekte ya da ona yakın ödüyor. Örnekler: [V1 858s] "voila" pipeline, [V2 640s] mock'larla test, [V3 697s] dört adımlı kural, [V8 292s] değer–bağlılık kuralı. [V7 31s] ve [V6 40s] vaadi erken karşılıyor. Ama [V6] asıl merak sorusunu (Linus da never nester mı?) [V6 455s]'de kapatıyor.
- **Kendini tanıtma:** 0/8. Kanal adı hiç söylenmiyor; yalnızca [V5 20s] ve [V7 30s]'de ekranda logo kartı var.
- **İlk 30 saniyede ilk kod veya somut örnek:** [V2 12s] Storage sınıfı, [V4 20s] "if status == 5", [V5 30s] User/Administrator, [V8] oyun sahnesi ilk saniyelerden itibaren.

## Yapı ve yeniden kancalar
**Ortak sıra:** iddia → tanım → tek bir çalışan örnek → yeni gereksinim veya sorun ("But now we want…") → çözüm ve adlandırma → ters köşe veya istisna → özet → kapanış sorusu ya da Patreon.

- **Yeni gereksinimle sorunu büyütmek:**
  - [V2 100s] "Unfortunately…" ve [V2 378s] Synergy anlaşmasının tamamlanmamış olması.
  - [V5 100s] dosyadan gelmeyen görüntü.
  - [V6 300s] "But things get interesting if we hit an error."
  - [V1 215s] sonsuz özyineleme.
- **Kendi önerisini tersine çevirmek:** [V8 153s] "But this is a bad idea", [V3 520s] set'in ölçülünce daha yavaş çıkması, [V1 935s] "The issue is it's fake."
- **Yeniden kanca sıklığı:** Model açıklamalarına göre aralıklar videoya göre 15–130 sn. Çoğu videoda kabaca 30–90 sn. En sık [V7]'de (20–40 sn), en seyrek [V2]'de (10–130 sn). [V1]'de büyük kancalar 2–3 dakikada bir, araya giren küçük "But/So/Okay" geçişleri 40–80 sn'de bir geliyor. Kancaların hepsi sözlü; görsel bir hileye dayanan kanca yok.
- **Ekranda bölüm başlıkları:** 3/8 ([V4], [V5], [V7]). [V7]'de her yeni kötü alışkanlık 60–90 sn'de bir yeni bölüm olarak açılıyor.
- **Açık döngüler:** video başına medyan 5 (aralık 4–6). En uzunu her zaman kapak sorusu. [V6]'daki Linus döngüsü 14. saniyede açılıp 455. saniyede kapanıyor. 5 videoda en az bir döngü bilerek açık bırakılıyor: [V4]'te "There's your startup idea.", [V7]'de "What would you add?"
- **Kuralı sonda yumuşatmak:** 5/8.
  - [V1 935s]: saf fonksiyonel programlama "sahte".
  - [V4 278s]: istisnalar.
  - [V5 505s]: "I won't say that inheritance is as evil…"
  - [V6 478s]: "not that committed".
  - [V8 255s]: soyutlamanın değdiği iki durum.
- **Sponsor:** 0/8.
- **Kanal dışı çağrı (Patreon veya site):** 3/8 ([V1 880s], [V2 752s], [V3 715s]). Hepsi son %10–15'lik dilimde.
- **Yorum sorusuyla kapanış:** 4/8 ([V4 354s], [V6 500s], [V7 435s], [V8 306s]). [V5] yalnızca teşekkür ederek bitiyor.
- **Abone ol çağrısı:** hiçbir videoda sözlü olarak yapılmıyor.

## Nasıl öğretiyor
- **Video başına kavram sayısı:** medyan 8,5 (aralık 6–12). En azı [V8] (6), en fazlası [V3] (12).
- **Kavramları taşıyan araçlar (toplam 72 kavram, birincil araca göre):**

| Araç | Kavram sayısı | Bulunduğu video sayısı |
|---|---|---|
| Tanım | 21 | 8 |
| Örnek | 18 | 7 |
| Hikâye veya vaka | 9 | 7 |
| Kod demosu | 8 | 6 |
| Görsel | 6 | 4 |
| Benzetme | 4 | 3 |
| Soru | 3 | 3 |
| Yanlış inanç | 3 | 3 |

  Bu etiket yalnızca birincil aracı gösteriyor. Kod ekranı neredeyse her kavramın arka planında duruyor.
- **Tipik sıra:** sorun veya soru → küçük bir kod parçası → gösterme → **adı sonra koyma**.
  - [V8 28s] "You just created an abstraction."
  - [V5 490s] "There's a name for what we just did there, dependency injection."
  - [V1 590s] "We'll call this function map…"
- **Tek çalışan örnek:** 5/8 videoda tek bir senaryo bütün videoyu taşıyor.
  - [V1]: makbuz ve fintech uygulaması.
  - [V2]: chat uygulamasının dosya yükleme servisi.
  - [V5]: görüntü kütüphanesi.
  - [V6]: indirme yöneticisi.
  - [V8]: oyun ve XML/JSON kayıt sistemi.

  [V7] bölüm bölüm ilerliyor ama kamyon ve film uygulaması vakalarıyla bitiyor. [V3] ve [V4] her bölümde yeni bir örnek kullanıyor.
- **Gerçek vakalar:**
  - [V3 150s] Facebook'un PHP ile yazılması.
  - [V3 630s] GTA 5 ve Tost'un profiler ile bulduğu sorun.
  - [V6 455s] Linux kernel stil kılavuzu.
  - [V4 290s] CommitStrip karikatürü.

  Kurgu vakalar mizahla kuruluyor: [V1 706s] satirik fintech fikri, [V2]'de "we were hacked, by the way".
- **Benzetmeler az ama akılda kalıyor:**
  - [V1 475s] "secret extra parameter".
  - [V1 905s] "sophisticated plumbers".
  - [V8 76s] "equal and opposite reaction".
  - [V7 45s] matematikte kısalığın erdem olması.
  - [V5 385s] sözleşme (kontrat).
- **Ön bilgi ve jargon:** Hedef, sınıf, döngü ve arayüz bilen bir izleyici. Yeni terimler ayrı bir sözlük bölümünde değil, ilk geçtikleri yerde ve kod üzerinde tanımlanıyor. [V6]'da nesting, extraction, inversion; [V7]'de Macar notasyonu. [V1 20s] jargonu bir terim bulutunda gösterip alaycı bir tonla geçiyor. Bazı terimler hiç tanımlanmıyor: [V8]'de interface ve factory, [V7]'de anti-pattern.
- **Yanlış inançlar:** 8/8 videoda var, video başına medyan 3 (aralık 2–6; en çok [V7]'de, 6 tane). Yöntem şu: yaygın inanç izleyicinin ağzından söyleniyor, sonra ölçümle ya da kodla çürütülüyor.
  - [V4 155s] "Isn't more comments just better?"
  - [V3 271s] ++i/i++, sonuç 3,4 nanosaniye.
  - [V8 36s] "tekrar kötüdür".
- **"Önce sen düşün" anları:** 8/8, video başına medyan 4.
  - [V7 76s] "Can you tell me its purpose?"
  - [V8 175s] "What does this abstraction save us?"
  - [V2 610s] tek implementasyon varken arayüz neden gerekli?
  - [V1 159s] "So how do you do a loop in a pure functional way?"
- **En zor kısım:** Parçalara bölünüyor ve ekranda katman katman kuruluyor.
  - [V6]'da refactor dört adımda yapılıyor ve arka plandaki kod bulanıklaştırılıyor.
  - [V2]'de zincir önce "Then… Then… Lastly" diye sayılıyor, sonra kutu diyagramına dökülüyor.
  - [V1]'de "This is a little weird" diyerek zorluk kabul ediliyor.
- **Özet:**
  - Sonda açık özet: 6/8 ([V1], [V3 697s] dört adımlı kural, [V4], [V6 485s], [V7 429s], [V8 292s]).
  - Yalnızca videonun ortasında ara özet: [V2 580s] "puzzle pieces".
  - Tek cümlelik özet: [V5 530s].

## Senaryo dili
Ton sakin, sohbet havasında ve kişisel: "I'd argue", "for me", "Maybe it's just me". Kendisiyle dalga geçen bir mizah var ama abartılı bir heyecan yok. Cümleler kısa (medyan 13 kelime). Geçişlerin çoğu "But", "So", "Okay", "Well" ile yapılıyor. Senaryo izleyiciyle "you" diye konuşuyor, adım adım ilerlerken "let's/we" kullanıyor. Vurgu için tek kelimelik cümleler ("Coupling.") ve kesinlik bildiren "period." gibi ifadeler var. Sayılar ve somut ölçüler sık kullanılıyor: "three deep", "3.4 nanosaniye", "%70", "80% moves".

Örnek satırlar:
- "It's time to get a bit controversial." [V4 0s]
- "I have to admit, I'm a never nester. I know, shocking." [V6 0s]
- "Comments can lie, but code cannot." [V4]
- "So now the answer is a thorough and totally satisfying maybe. We must measure." [V3 353s]
- "But this is a bad idea. We've now coupled both of these classes to the same input." [V8 153s]
- "A lot of the time, we're just sophisticated plumbers." [V1 905s]

## Sınırlar
- **Örneklem:** Tek bir kanalın 28.10.2026 itibarıyla en son 8 uzun videosu (2022-11-20 ile 2023-12-23 arası yüklenmiş). Bu sonuçlar kanalın genel çizgisini ya da başka kanalları temsil etmeyebilir.
- **Ölçülenler:** Kesme sayıları, çekim süreleri, görsel değişimler, konuşma hızı ve ilk konuşma saniyesi kodla hesaplandı ve güvenilir.
- **Model açıklamaları:** Paketleme, vuruşlar, yeniden kancalar, öğretim araçları ve alıntılar bir modelin transkript, kapak ve örnek karelerden yaptığı yorumlar. Bazı açıklamalardaki konuşma hızı rakamları (örneğin ilk 3 sn için "360" ya da "340 kelime/dk") ölçümlerle çelişiyor. Bu raporda yalnızca ölçülen değerler kullanıldı.
- **İzlenme verisi:** Videonun nerede bırakıldığını gösteren izlenme verisi yok, çünkü YouTube bunu yayımlamıyor. "İzleyiciyi tutuyor" yorumu yapıya bakılarak yapılan bir çıkarım, ölçülmüş bir sonuç değil.
- **Tarih:** Rapor 28.10.2026 tarihindeki durumu yansıtıyor.
