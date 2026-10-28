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

Sayıların anlamı: Kanal kesme kullanmıyor. 5 videoda tek çekim süresi videonun kendi süresine eşit, örneğin [V2](https://youtu.be/J1f5b4vcxCQ) 795 sn ve [V5](https://youtu.be/hxGOiiR9ZKg) 600 sn. Ekrandaki değişimi kesmeler değil animasyonlar sağlıyor: yazının kelime kelime belirmesi, kod satırlarının eklenmesi, diyagramlar. Bu değişimler ortalama 8–9 saniyede bir geliyor. Uç değerler de var. En sık değişen video, hareketli oyun sahnesi olan [V8](https://youtu.be/rQlMtztiAoA) (dakikada 10,9). En seyrek değişen video, uzun kod ekranlarıyla ilerleyen [V6](https://youtu.be/CFRhGnuXG-4) (dakikada 2,2). [V1](https://youtu.be/nuML9SmdbJ4)'in 1,98 sn'lik medyan çekim süresi, kelime kelime açılan metnin kesme sayılmasından kaynaklanıyor olabilir; bu bir tahmin. Konuşma ilk saniyede başlıyor ve açılışta biraz hızlı (ilk 3 sn medyanı 180). İlk 10–30 saniyede ise genel hızın altına iniyor. [V3](https://youtu.be/tKbV6BpH-C8) bunun en belirgin örneği: ilk 10 sn'de dakikada 78 kelime. Yani tempo kurgudan değil, sözlü yoğunluktan geliyor.

## Paketleme (başlık + kapak)
- **Kapakta yüz yok, koyu zemin üzerinde yalnızca tipografi ve şekil var:** 8/8. Sunucu hiçbir kapakta görünmüyor.
- **Mor veya lavanta vurgu kelimesi:** 6/8. Örnekler: [V1](https://youtu.be/nuML9SmdbJ4)'de "Functional", [V2](https://youtu.be/J1f5b4vcxCQ)'de "Dependency", [V4](https://youtu.be/Bf7vDBBOBUA)'te "Don't Write", [V5](https://youtu.be/hxGOiiR9ZKg)'te "Composition >", [V6](https://youtu.be/CFRhGnuXG-4)'da "I'm a", [V8](https://youtu.be/rQlMtztiAoA)'de "vs coupling". [V3](https://youtu.be/tKbV6BpH-C8)'te kırmızı-pembe fırça yazı, [V7](https://youtu.be/-J3wNP6u5YU)'de yeşilimsi "how not to" kullanılmış.
- **Kavramı simgeleyen renkli kare/kutu diyagramı:** 5/8 ([V1](https://youtu.be/nuML9SmdbJ4), [V2](https://youtu.be/J1f5b4vcxCQ), [V5](https://youtu.be/hxGOiiR9ZKg), [V6](https://youtu.be/CFRhGnuXG-4), [V8](https://youtu.be/rQlMtztiAoA)). [V6](https://youtu.be/CFRhGnuXG-4)'daki basamaklı kareler girintiyi, [V5](https://youtu.be/hxGOiiR9ZKg)'teki küp ağacı kalıtımı gösteriyor. [V7](https://youtu.be/-J3wNP6u5YU)'nin kapağında kod satırları var (int d; int delay; int delaySeconds; TimeSpan delay;) ve "BaseObject" üstü çizili.
- **Kapak metni başlığı tekrar ediyor:** 4/8 ([V1](https://youtu.be/nuML9SmdbJ4), [V3](https://youtu.be/tKbV6BpH-C8), [V4](https://youtu.be/Bf7vDBBOBUA) birebir; [V2](https://youtu.be/J1f5b4vcxCQ) "The Best Pattern" kısmı çıkarılmış hâliyle).
- **Kapak başlığa yeni bir açı ekliyor:** 4/8. [V5](https://youtu.be/hxGOiiR9ZKg): başlık "The Flaws of Inheritance", kapak "Composition > Inheritance". [V6](https://youtu.be/CFRhGnuXG-4): başlık "Why You Shouldn't Nest Your Code", kapak "I'm a Never Nester {". [V7](https://youtu.be/-J3wNP6u5YU): kapakta "how not to Name Things". [V8](https://youtu.be/rQlMtztiAoA): kapakta "ABSTRACTION vs coupling".
- **Sözün türü, yani alışkanlığa karşı çıkan, olumsuz ya da kural koyan bir çerçeve:** 6/8 ([V2](https://youtu.be/J1f5b4vcxCQ), [V4](https://youtu.be/Bf7vDBBOBUA), [V5](https://youtu.be/hxGOiiR9ZKg), [V6](https://youtu.be/CFRhGnuXG-4), [V7](https://youtu.be/-J3wNP6u5YU), [V8](https://youtu.be/rQlMtztiAoA)). Kalan iki video da görüş bildiriyor: [V1](https://youtu.be/nuML9SmdbJ4) belli bir kitleye sesleniyor, [V3](https://youtu.be/tKbV6BpH-C8) ünlü "root of all evil" iddiasına dayanıyor.
- **Merak boşluğu:** Neredeyse hepsinde aynı soru var: "Bu neden kötü ya da iyi, ne zaman geçerli?" [V8](https://youtu.be/rQlMtztiAoA)'deki "vs coupling" ikinci kavramı adlandırıp açıklamıyor. [V6](https://youtu.be/CFRhGnuXG-4) "never nester" diye yeni bir kimlik uyduruyor.

## İlk 3, 10 ve 30 saniye
**Sıra genelde şöyle:** 0. saniyede konuşma başlıyor ve iddia söyleniyor (8/8) → ekranda başlık ya da iddianın kendisi kelime kelime beliriyor → 10–30 saniye arasında tanım veya bağlam geliyor → 30. saniye civarında ilk kod ya da örnek ekrana çıkıyor.

- **İlk cümlenin türü:**
  - Görüş veya tartışmalı iddia: 4/8. [V2 0:00](https://youtu.be/J1f5b4vcxCQ?t=0) "Dependency injection is a term I don't love…", [V3 0:00](https://youtu.be/tKbV6BpH-C8?t=0) "…root of all evil.", [V4 0:00](https://youtu.be/Bf7vDBBOBUA?t=0) "It's time to get a bit controversial.", [V6 0:00](https://youtu.be/CFRhGnuXG-4?t=0) itiraf.
  - Bilinen bir söz veya alıntı: 2/8. [V5 0:00](https://youtu.be/hxGOiiR9ZKg?t=0) "prefer composition over inheritance", [V7 0:00](https://youtu.be/-J3wNP6u5YU?t=0) "two hard things". [V3](https://youtu.be/tKbV6BpH-C8)'te Knuth alıntısı 5. saniyede ekrana geliyor.
  - Kitleye doğrudan hitap: 1/8 ([V1 0:00](https://youtu.be/nuML9SmdbJ4?t=0)).
  - Somut bir senaryo: 1/8 ([V8 0:00](https://youtu.be/rQlMtztiAoA?t=0), oyun sahnesi).
- **Ekranda konuşmayla eşzamanlı açılan metin:** 5/8 ([V1](https://youtu.be/nuML9SmdbJ4), [V3](https://youtu.be/tKbV6BpH-C8), [V5](https://youtu.be/hxGOiiR9ZKg), [V6](https://youtu.be/CFRhGnuXG-4), [V7](https://youtu.be/-J3wNP6u5YU)). [V2](https://youtu.be/J1f5b4vcxCQ)'de sabit bir başlık kartı var, [V4](https://youtu.be/Bf7vDBBOBUA)'te ilk 3 sn ekran boş, [V8](https://youtu.be/rQlMtztiAoA)'de uzay gemisi çizimi beliriyor.
- **Açılış görüntüsü kapakla örtüşüyor:** 4/8 ([V1](https://youtu.be/nuML9SmdbJ4), [V2](https://youtu.be/J1f5b4vcxCQ), [V3](https://youtu.be/tKbV6BpH-C8), [V6](https://youtu.be/CFRhGnuXG-4)).
- **Kapak sözü ekranda ilk ne zaman görünüyor:** medyan 0 sn (aralık 0–46). En geç [V8 0:46](https://youtu.be/rQlMtztiAoA?t=46): "But there's a hidden trade-off… Coupling."
- **Kapak sözü ne zaman karşılanıyor:** medyan 285 sn, video süresinin medyan %80'i. 8 videonun 6'sı vaadi son çeyrekte ya da ona yakın ödüyor. Örnekler: [V1 14:18](https://youtu.be/nuML9SmdbJ4?t=858) "voila" pipeline, [V2 10:40](https://youtu.be/J1f5b4vcxCQ?t=640) mock'larla test, [V3 11:37](https://youtu.be/tKbV6BpH-C8?t=697) dört adımlı kural, [V8 4:52](https://youtu.be/rQlMtztiAoA?t=292) değer–bağlılık kuralı. [V7 0:31](https://youtu.be/-J3wNP6u5YU?t=31) ve [V6 0:40](https://youtu.be/CFRhGnuXG-4?t=40) vaadi erken karşılıyor. Ama [V6](https://youtu.be/CFRhGnuXG-4) asıl merak sorusunu (Linus da never nester mı?) [V6 7:35](https://youtu.be/CFRhGnuXG-4?t=455)'de kapatıyor.
- **Kendini tanıtma:** 0/8. Kanal adı hiç söylenmiyor; yalnızca [V5 0:20](https://youtu.be/hxGOiiR9ZKg?t=20) ve [V7 0:30](https://youtu.be/-J3wNP6u5YU?t=30)'de ekranda logo kartı var.
- **İlk 30 saniyede ilk kod veya somut örnek:** [V2 0:12](https://youtu.be/J1f5b4vcxCQ?t=12) Storage sınıfı, [V4 0:20](https://youtu.be/Bf7vDBBOBUA?t=20) "if status == 5", [V5 0:30](https://youtu.be/hxGOiiR9ZKg?t=30) User/Administrator, [V8](https://youtu.be/rQlMtztiAoA) oyun sahnesi ilk saniyelerden itibaren.

## Yapı ve yeniden kancalar
**Ortak sıra:** iddia → tanım → tek bir çalışan örnek → yeni gereksinim veya sorun ("But now we want…") → çözüm ve adlandırma → ters köşe veya istisna → özet → kapanış sorusu ya da Patreon.

- **Yeni gereksinimle sorunu büyütmek:**
  - [V2 1:40](https://youtu.be/J1f5b4vcxCQ?t=100) "Unfortunately…" ve [V2 6:18](https://youtu.be/J1f5b4vcxCQ?t=378) Synergy anlaşmasının tamamlanmamış olması.
  - [V5 1:40](https://youtu.be/hxGOiiR9ZKg?t=100) dosyadan gelmeyen görüntü.
  - [V6 5:00](https://youtu.be/CFRhGnuXG-4?t=300) "But things get interesting if we hit an error."
  - [V1 3:35](https://youtu.be/nuML9SmdbJ4?t=215) sonsuz özyineleme.
- **Kendi önerisini tersine çevirmek:** [V8 2:33](https://youtu.be/rQlMtztiAoA?t=153) "But this is a bad idea", [V3 8:40](https://youtu.be/tKbV6BpH-C8?t=520) set'in ölçülünce daha yavaş çıkması, [V1 15:35](https://youtu.be/nuML9SmdbJ4?t=935) "The issue is it's fake."
- **Yeniden kanca sıklığı:** Model açıklamalarına göre aralıklar videoya göre 15–130 sn. Çoğu videoda kabaca 30–90 sn. En sık [V7](https://youtu.be/-J3wNP6u5YU)'de (20–40 sn), en seyrek [V2](https://youtu.be/J1f5b4vcxCQ)'de (10–130 sn). [V1](https://youtu.be/nuML9SmdbJ4)'de büyük kancalar 2–3 dakikada bir, araya giren küçük "But/So/Okay" geçişleri 40–80 sn'de bir geliyor. Kancaların hepsi sözlü; görsel bir hileye dayanan kanca yok.
- **Ekranda bölüm başlıkları:** 3/8 ([V4](https://youtu.be/Bf7vDBBOBUA), [V5](https://youtu.be/hxGOiiR9ZKg), [V7](https://youtu.be/-J3wNP6u5YU)). [V7](https://youtu.be/-J3wNP6u5YU)'de her yeni kötü alışkanlık 60–90 sn'de bir yeni bölüm olarak açılıyor.
- **Açık döngüler:** video başına medyan 5 (aralık 4–6). En uzunu her zaman kapak sorusu. [V6](https://youtu.be/CFRhGnuXG-4)'daki Linus döngüsü 14. saniyede açılıp 455. saniyede kapanıyor. 5 videoda en az bir döngü bilerek açık bırakılıyor: [V4](https://youtu.be/Bf7vDBBOBUA)'te "There's your startup idea.", [V7](https://youtu.be/-J3wNP6u5YU)'de "What would you add?"
- **Kuralı sonda yumuşatmak:** 5/8.
  - [V1 15:35](https://youtu.be/nuML9SmdbJ4?t=935): saf fonksiyonel programlama "sahte".
  - [V4 4:38](https://youtu.be/Bf7vDBBOBUA?t=278): istisnalar.
  - [V5 8:25](https://youtu.be/hxGOiiR9ZKg?t=505): "I won't say that inheritance is as evil…"
  - [V6 7:58](https://youtu.be/CFRhGnuXG-4?t=478): "not that committed".
  - [V8 4:15](https://youtu.be/rQlMtztiAoA?t=255): soyutlamanın değdiği iki durum.
- **Sponsor:** 0/8.
- **Kanal dışı çağrı (Patreon veya site):** 3/8 ([V1 14:40](https://youtu.be/nuML9SmdbJ4?t=880), [V2 12:32](https://youtu.be/J1f5b4vcxCQ?t=752), [V3 11:55](https://youtu.be/tKbV6BpH-C8?t=715)). Hepsi son %10–15'lik dilimde.
- **Yorum sorusuyla kapanış:** 4/8 ([V4 5:54](https://youtu.be/Bf7vDBBOBUA?t=354), [V6 8:20](https://youtu.be/CFRhGnuXG-4?t=500), [V7 7:15](https://youtu.be/-J3wNP6u5YU?t=435), [V8 5:06](https://youtu.be/rQlMtztiAoA?t=306)). [V5](https://youtu.be/hxGOiiR9ZKg) yalnızca teşekkür ederek bitiyor.
- **Abone ol çağrısı:** hiçbir videoda sözlü olarak yapılmıyor.

## Nasıl öğretiyor
- **Video başına kavram sayısı:** medyan 8,5 (aralık 6–12). En azı [V8](https://youtu.be/rQlMtztiAoA) (6), en fazlası [V3](https://youtu.be/tKbV6BpH-C8) (12).
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
  - [V8 0:28](https://youtu.be/rQlMtztiAoA?t=28) "You just created an abstraction."
  - [V5 8:10](https://youtu.be/hxGOiiR9ZKg?t=490) "There's a name for what we just did there, dependency injection."
  - [V1 9:50](https://youtu.be/nuML9SmdbJ4?t=590) "We'll call this function map…"
- **Tek çalışan örnek:** 5/8 videoda tek bir senaryo bütün videoyu taşıyor.
  - [V1](https://youtu.be/nuML9SmdbJ4): makbuz ve fintech uygulaması.
  - [V2](https://youtu.be/J1f5b4vcxCQ): chat uygulamasının dosya yükleme servisi.
  - [V5](https://youtu.be/hxGOiiR9ZKg): görüntü kütüphanesi.
  - [V6](https://youtu.be/CFRhGnuXG-4): indirme yöneticisi.
  - [V8](https://youtu.be/rQlMtztiAoA): oyun ve XML/JSON kayıt sistemi.

  [V7](https://youtu.be/-J3wNP6u5YU) bölüm bölüm ilerliyor ama kamyon ve film uygulaması vakalarıyla bitiyor. [V3](https://youtu.be/tKbV6BpH-C8) ve [V4](https://youtu.be/Bf7vDBBOBUA) her bölümde yeni bir örnek kullanıyor.
- **Gerçek vakalar:**
  - [V3 2:30](https://youtu.be/tKbV6BpH-C8?t=150) Facebook'un PHP ile yazılması.
  - [V3 10:30](https://youtu.be/tKbV6BpH-C8?t=630) GTA 5 ve Tost'un profiler ile bulduğu sorun.
  - [V6 7:35](https://youtu.be/CFRhGnuXG-4?t=455) Linux kernel stil kılavuzu.
  - [V4 4:50](https://youtu.be/Bf7vDBBOBUA?t=290) CommitStrip karikatürü.

  Kurgu vakalar mizahla kuruluyor: [V1 11:46](https://youtu.be/nuML9SmdbJ4?t=706) satirik fintech fikri, [V2](https://youtu.be/J1f5b4vcxCQ)'de "we were hacked, by the way".
- **Benzetmeler az ama akılda kalıyor:**
  - [V1 7:55](https://youtu.be/nuML9SmdbJ4?t=475) "secret extra parameter".
  - [V1 15:05](https://youtu.be/nuML9SmdbJ4?t=905) "sophisticated plumbers".
  - [V8 1:16](https://youtu.be/rQlMtztiAoA?t=76) "equal and opposite reaction".
  - [V7 0:45](https://youtu.be/-J3wNP6u5YU?t=45) matematikte kısalığın erdem olması.
  - [V5 6:25](https://youtu.be/hxGOiiR9ZKg?t=385) sözleşme (kontrat).
- **Ön bilgi ve jargon:** Hedef, sınıf, döngü ve arayüz bilen bir izleyici. Yeni terimler ayrı bir sözlük bölümünde değil, ilk geçtikleri yerde ve kod üzerinde tanımlanıyor. [V6](https://youtu.be/CFRhGnuXG-4)'da nesting, extraction, inversion; [V7](https://youtu.be/-J3wNP6u5YU)'de Macar notasyonu. [V1 0:20](https://youtu.be/nuML9SmdbJ4?t=20) jargonu bir terim bulutunda gösterip alaycı bir tonla geçiyor. Bazı terimler hiç tanımlanmıyor: [V8](https://youtu.be/rQlMtztiAoA)'de interface ve factory, [V7](https://youtu.be/-J3wNP6u5YU)'de anti-pattern.
- **Yanlış inançlar:** 8/8 videoda var, video başına medyan 3 (aralık 2–6; en çok [V7](https://youtu.be/-J3wNP6u5YU)'de, 6 tane). Yöntem şu: yaygın inanç izleyicinin ağzından söyleniyor, sonra ölçümle ya da kodla çürütülüyor.
  - [V4 2:35](https://youtu.be/Bf7vDBBOBUA?t=155) "Isn't more comments just better?"
  - [V3 4:31](https://youtu.be/tKbV6BpH-C8?t=271) ++i/i++, sonuç 3,4 nanosaniye.
  - [V8 0:36](https://youtu.be/rQlMtztiAoA?t=36) "tekrar kötüdür".
- **"Önce sen düşün" anları:** 8/8, video başına medyan 4.
  - [V7 1:16](https://youtu.be/-J3wNP6u5YU?t=76) "Can you tell me its purpose?"
  - [V8 2:55](https://youtu.be/rQlMtztiAoA?t=175) "What does this abstraction save us?"
  - [V2 10:10](https://youtu.be/J1f5b4vcxCQ?t=610) tek implementasyon varken arayüz neden gerekli?
  - [V1 2:39](https://youtu.be/nuML9SmdbJ4?t=159) "So how do you do a loop in a pure functional way?"
- **En zor kısım:** Parçalara bölünüyor ve ekranda katman katman kuruluyor.
  - [V6](https://youtu.be/CFRhGnuXG-4)'da refactor dört adımda yapılıyor ve arka plandaki kod bulanıklaştırılıyor.
  - [V2](https://youtu.be/J1f5b4vcxCQ)'de zincir önce "Then… Then… Lastly" diye sayılıyor, sonra kutu diyagramına dökülüyor.
  - [V1](https://youtu.be/nuML9SmdbJ4)'de "This is a little weird" diyerek zorluk kabul ediliyor.
- **Özet:**
  - Sonda açık özet: 6/8 ([V1](https://youtu.be/nuML9SmdbJ4), [V3 11:37](https://youtu.be/tKbV6BpH-C8?t=697) dört adımlı kural, [V4](https://youtu.be/Bf7vDBBOBUA), [V6 8:05](https://youtu.be/CFRhGnuXG-4?t=485), [V7 7:09](https://youtu.be/-J3wNP6u5YU?t=429), [V8 4:52](https://youtu.be/rQlMtztiAoA?t=292)).
  - Yalnızca videonun ortasında ara özet: [V2 9:40](https://youtu.be/J1f5b4vcxCQ?t=580) "puzzle pieces".
  - Tek cümlelik özet: [V5 8:50](https://youtu.be/hxGOiiR9ZKg?t=530).

## Senaryo dili
Ton sakin, sohbet havasında ve kişisel: "I'd argue", "for me", "Maybe it's just me". Kendisiyle dalga geçen bir mizah var ama abartılı bir heyecan yok. Cümleler kısa (medyan 13 kelime). Geçişlerin çoğu "But", "So", "Okay", "Well" ile yapılıyor. Senaryo izleyiciyle "you" diye konuşuyor, adım adım ilerlerken "let's/we" kullanıyor. Vurgu için tek kelimelik cümleler ("Coupling.") ve kesinlik bildiren "period." gibi ifadeler var. Sayılar ve somut ölçüler sık kullanılıyor: "three deep", "3.4 nanosaniye", "%70", "80% moves".

Örnek satırlar:
- "It's time to get a bit controversial." [V4 0:00](https://youtu.be/Bf7vDBBOBUA?t=0)
- "I have to admit, I'm a never nester. I know, shocking." [V6 0:00](https://youtu.be/CFRhGnuXG-4?t=0)
- "Comments can lie, but code cannot." [V4](https://youtu.be/Bf7vDBBOBUA)
- "So now the answer is a thorough and totally satisfying maybe. We must measure." [V3 5:53](https://youtu.be/tKbV6BpH-C8?t=353)
- "But this is a bad idea. We've now coupled both of these classes to the same input." [V8 2:33](https://youtu.be/rQlMtztiAoA?t=153)
- "A lot of the time, we're just sophisticated plumbers." [V1 15:05](https://youtu.be/nuML9SmdbJ4?t=905)

## Sınırlar
- **Örneklem:** Tek bir kanalın 28.10.2026 itibarıyla en son 8 uzun videosu (2022-11-20 ile 2023-12-23 arası yüklenmiş). Bu sonuçlar kanalın genel çizgisini ya da başka kanalları temsil etmeyebilir.
- **Ölçülenler:** Kesme sayıları, çekim süreleri, görsel değişimler, konuşma hızı ve ilk konuşma saniyesi kodla hesaplandı ve güvenilir.
- **Model açıklamaları:** Paketleme, vuruşlar, yeniden kancalar, öğretim araçları ve alıntılar bir modelin transkript, kapak ve örnek karelerden yaptığı yorumlar. Bazı açıklamalardaki konuşma hızı rakamları (örneğin ilk 3 sn için "360" ya da "340 kelime/dk") ölçümlerle çelişiyor. Bu raporda yalnızca ölçülen değerler kullanıldı.
- **İzlenme verisi:** Videonun nerede bırakıldığını gösteren izlenme verisi yok, çünkü YouTube bunu yayımlamıyor. "İzleyiciyi tutuyor" yorumu yapıya bakılarak yapılan bir çıkarım, ölçülmüş bir sonuç değil.
- **Tarih:** Rapor 28.10.2026 tarihindeki durumu yansıtıyor.


---

## Video başına ölçümler

360p görüntü ve metinden kodla hesaplandı: kesme = ffmpeg sahne değişimi, kelime/dk = dakikadaki kelime. Otomatik yazıya dökülen seste konuşma hızı yaklaşıktır.

| # | Video | İzlenme | Kesme/dk | Kesme 0-3 sn | Kesme 0-10 sn | Kesme 0-30 sn | Ortanca çekim (sn) | Değişim/dk | Değişim 0-30 sn | Ortanca değişim arası (sn) | Kelime/dk | Kelime/dk 0-10 sn | Kelime/dk 0-30 sn | İlk kelime (sn) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | [Dear Functional Bros](https://youtu.be/nuML9SmdbJ4) | 759168 | 1.0 | 0 | 0 | 0 | 1.98 | 3.4 | 4 | 5.5 | 167.9 | 114.0 | 132.0 | 0.0 |
| V2 | [Dependency Injection, The Best Pattern](https://youtu.be/J1f5b4vcxCQ) | 1163826 | 0.0 | 0 | 0 | 0 | 795.0 | 3.9 | 2 | 8.53 | 157.0 | 204.0 | 198.0 | 0.0 |
| V3 | [Premature Optimization](https://youtu.be/tKbV6BpH-C8) | 1030732 | 0.6 | 0 | 0 | 0 | 57.98 | 4.8 | 4 | 8.85 | 174.0 | 78.0 | 88.0 | 0.0 |
| V4 | [Don't Write Comments](https://youtu.be/Bf7vDBBOBUA) | 976293 | 0.3 | 0 | 0 | 0 | 31.7 | 4.4 | 2 | 11.93 | 168.0 | 138.0 | 154.0 | 0.0 |
| V5 | [The Flaws of Inheritance](https://youtu.be/hxGOiiR9ZKg) | 1313214 | 0.0 | 0 | 0 | 0 | 600.0 | 3.5 | 4 | 12.05 | 166.4 | 180.0 | 152.0 | 0.0 |
| V6 | [Why You Shouldn't Nest Your Code](https://youtu.be/CFRhGnuXG-4) | 3373823 | 0.0 | 0 | 0 | 0 | 509.0 | 2.2 | 2 | 16.68 | 139.8 | 126.0 | 154.0 | 0.0 |
| V7 | [Naming Things in Code](https://youtu.be/-J3wNP6u5YU) | 2976078 | 0.0 | 0 | 0 | 0 | 444.0 | 5.4 | 2 | 6.27 | 149.4 | 156.0 | 138.0 | 0.0 |
| V8 | [Abstraction Can Make Your Code Worse](https://youtu.be/rQlMtztiAoA) | 847659 | 0.0 | 0 | 0 | 0 | 313.0 | 10.9 | 3 | 3.67 | 149.1 | 186.0 | 166.0 | 0.0 |
| | **Ortanca** | | 0.0 | 0.0 | 0.0 | 0.0 | 378.5 | 4.2 | 2.5 | 8.7 | 161.7 | 147.0 | 153.0 | 0.0 |
