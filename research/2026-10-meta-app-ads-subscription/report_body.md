# Meta Advantage+ app ile abonelikli B2B uygulamaya düşük bütçede deneme ve ödeyen müşteri getirmek

## Kısa cevap

Kanıtlar birkaç konuda net. Abonelikli bir uygulamada kampanyayı yüklemeye (install) optimize etmek ucuz yükleme getirir, ama bu yüklemeler denemeye ve ödemeye nadiren dönüşür. StartTrial gibi daha derin bir olaya optimize etmek daha iyi sonuç verir [K4] [K381]. Öte yandan Meta'nın öğrenebilmesi için reklam seti başına haftada yaklaşık 50 optimizasyon olayı gerekir. Bu yüzden düşük bütçede Purchase yerine StartTrial seçmek, yapıyı tek reklam setinde toplamak ve geniş hedefleme kullanmak en tutarlı öneri [K8] [K11] [K3]. Kurulum tarafında önce Meta SDK ile olayları doğru göndermek, sonra birbirinden belirgin biçimde farklı kreatifler test etmek, değerlendirmeyi 7 günlük pencerelerle yapmak ve bütçeyi kademeli artırmak destekleniyor [K18] [K24] [K15] [K7].

Kanıtın zayıf kaldığı yerler de var. Çoğu kaynak ajans ya da kurs satıyor ve kendi verisini göstermiyor. B2B'ye özgü, düşük bütçeli bir Advantage+ app vakası corpus'ta neredeyse hiç yok; örneklerin çoğu B2C (fitness, bebek uygulaması) ya da B2B lead kampanyası. "Ödeyen müşteri maliyeti" konusunda güvenilir bir kıyas değeri bulunmuyor. Bunu kendi verinizle ölçmeniz gerekecek.

## Platformun söyledikleri ve uygulayıcıların aktardıkları

Aşağıdaki maddelerde uygulayıcı kanıtı var ama resmi dokümanlar konuda sessiz (practice_only). Dokümanla doğrudan çelişen pratik bir bulgu yok. Dokümanla çelişen iki iddia ayrıca not edildi.

| Konu | Platform / dokümanlar | Uygulayıcılar (kendi deneyimi) | Hangisi ne zaman geçerli | Kümeler |
|---|---|---|---|---|
| Ham deneme yerine "nitelikli deneme" olayı | Optimize ettiğiniz olayı yapacak kişileri bulur; deneme ile ödeme arasında ayrım yapmaz | Denemeden 1–3 saat sonra hâlâ aktif olan kullanıcıyı ayrı olay olarak gönderip ona optimize etmek, hemen iptal edenleri eler | Olay hacmi yetiyorsa nitelikli deneme. Hacim düşükse pencereyi kısaltın ya da ham StartTrial'da kalın | [K13] [K381] |
| Hedefleme genişliği | Advantage+ audience'ı tarif ediyor, performans hakkında bir şey demiyor | Tek ülke ve geniş hedefleme, dar segmentasyondan iyi | Kitle havuzu büyükse geniş. Çok niş B2B kitlede belirsiz | [K31] [K147] |
| Tıklama/etkileşime optimizasyon | Yalnızca "optimizasyon olayına göre dağıtım" ilkesi var | Tıklayan ama dönüşmeyen kişileri getirir | Hedef deneme ya da ödemeyse dönüşüm olayına optimize edin | [K10] |
| Bütçenin kolay dönüşüme yığılması | Sessiz | CBO veya tek sette harcama tek kreatife ya da kolay dönüşüme toplanabiliyor | Küçük bütçe ve çok kreatifli tek sette risk daha yüksek | [K47] |
| Öğrenme süresi | Haftada ~50 olay eşiği | Süre hacme bağlı; düşük bütçede setler uzun süre "öğrenme sınırlı" kalabiliyor | Düşük bütçeli StartTrial kampanyasında sabit bir süre beklemeyin | [K32] [K8] |
| Onboarding içinde paywall | Konu Meta'nın alanı değil | Deneme başlangıcını artırıyor; ancak denemeden ödemeye oranı ayrıca izlenmeli | Uygulama içi taktik; kampanyadan bağımsız test edin | [K17] |
| Web quiz'e yönlendirme | Sessiz; Advantage+ app trafiği doğrudan mağazaya götürür | B2C'de doğrudan mağazaya göre daha iyi dönüşüm | Yalnızca B2C'de görülmüş. Web dönüşüm kampanyası gerektirir | [K68] |
| LTV:CAC hedefi | Eşik vermiyor | Kabaca 3:1 (en az 2–3 kat) | LTV verisi olan, orta ve yüksek bütçeli hesaplar | [K1] |
| Organik içeriği reklamda yeniden kullanmak | Sessiz | Organikte iyi giden içerik reklamda da çoğunlukla iyi çalışır | Organik etkileşimle deneme dönüşümü aynı şey değil; test edin | [K29] |
| Kazanan kreatif oranı | Yalnızca çeşitlilik öneriyor | Ayda çok sayıda kreatif test ediliyor, ~%5–10'u kazanıyor | Yüksek bütçe; düşük bütçeye doğrudan aktarılamaz | [K21] |

**Dokümanla çelişen iddialar:** "SDK ve sunucudan aynı event_id ile gönderilirse pLTV, ATT'ye rağmen çalışır" iddiası, Meta'nın pLTV rehberiyle çelişiyor. Rehbere göre pLTV şu an uygulama olaylarını desteklemiyor [K462]. "Andromeda ile 100 kat daha kısa yanıt süresi" de resmi yazıyla uyuşmuyor; resmi yazıda %6 recall artışı ve 10 kat verimlilik geçiyor [K348].

**Pratik ile dokümanın örtüştüğü yerler:** Birbirinden belirgin biçimde farklı konseptlerle test etmek [K24]. Reklam incelemesinin genelde 24 saat içinde bitmesi [K23]. Günlük dalgalanmalara tepki vermemek [K39].

## Kaldıraçlar (etkisine göre sıralı)

1. **Optimizasyon olayını StartTrial (ya da nitelikli deneme) yapmak.**
   - Ne yapılır: Install yerine StartTrial'a optimize edin. Hacim yeterliyse nitelikli deneme olayına geçin.
   - Beklenen etki: Yükleme maliyeti artar, ama ödeyen müşteri başına maliyet (CAC) düşmesi beklenir. Tek kaynaklı bir ilk el örnekte deneme optimizasyonu yükleme maliyetini yaklaşık iki katına çıkarmış, buna rağmen kampanya toplamda daha kârlı çıkmış [K448].
   - Kanıt: güçlü [K4] [K11] [K381] [K457]. Nitelikli deneme için olası [K13].

2. **Olay hacmine göre bütçe ve yapı kurmak.**
   - Ne yapılır: Reklam seti başına haftada ~50 olay hedefleyin. Bütçe kaba olarak "olay maliyeti × 50 / hafta" (günde ×7–10) eder.
   - Beklenen etki: Set öğrenme aşamasından çıkabilir ve maliyetler istikrar kazanır.
   - Kanıt: güçlü, docs destekli [K8] [K11] [K492]. Tek set ve konsolidasyon için [K3] [K53].

3. **Sinyal ve ölçüm kalitesi.**
   - Ne yapılır: Önce Meta SDK ile StartTrial ve abonelik olaylarını gönderin. Events Manager, Ads Manager ve mağaza sayılarını birbiriyle karşılaştırın.
   - Beklenen etki: Yanlış olaya optimize etmenin ve yanlış bütçe kararlarının önüne geçer.
   - Kanıt: güçlü [K18] [K457] [K288] [K54]. "Önce sinyal, sonra kreatif" sıralaması olası düzeyde [K35].

4. **Kreatif çeşitliliği.**
   - Ne yapılır: Kanca, format ve açı olarak birbirinden ayrışan 5–10 konsept kullanın. Varyasyonlara ancak kazanan konsept çıktıktan sonra geçin.
   - Beklenen etki: Andromeda sonrası dağıtımda kreatif, reklamı kimin göreceğini belirleyen ana sinyallerden biri.
   - Kanıt: güçlü [K24] [K2] [K5] [K262] [K69]. Kesin sayılar tartışmalı.

5. **Geniş hedefleme, Advantage+ yerleşim, en yüksek hacim teklifi.**
   - Ne yapılır: Hedefleme ve yerleşimi Meta'ya bırakın. Başlangıçta teklif sınırı ya da maliyet hedefi koymayın.
   - Kanıt: güçlü ya da olası [K28] [K65] [K31].

6. **Sabır ve düzenleme disiplini.**
   - Ne yapılır: Değerlendirmeyi 7 günlük pencerede yapın, önemli düzenlemeleri seyrek tutun.
   - Beklenen etki: Öğrenme aşamasının tekrar tekrar sıfırlanmasını önler.
   - Kanıt: olası [K15] [K39] [K36] [K66].

7. **Kademeli ölçekleme.**
   - Ne yapılır: Bütçeyi adım başına %10–20 artırın, 2–4 günde bir. Küçük bütçede aralığı 7–10 güne uzatın.
   - Kanıt: güçlü, ama rakamlar sektör pratiği [K7].

8. **Uygulama içi dönüşüm.**
   - Ne yapılır: Paywall'u onboarding içine alın, deneme teklifini açık sunun.
   - Kanıt: olası, B2C kaynaklı [K17].

## Pratik tarif

1. Uygulamanız gerçekten mobilse Uygulama Tanıtımı / Advantage+ app hedefini kullanın. iOS 14+ ayarlarını yapın [K6]. Reklam hesabını açarken para birimi ve saat dilimini doğru seçin [K12].
2. Meta SDK'yı kurun. Install, StartTrial ve abonelik/satın alma olaylarını gönderin [K18] [K457]. MMP'yi birden fazla mecra ölçecekseniz ya da bütçe büyüdüğünde ekleyin [K18].
3. Ölçümü doğrulayın. Events Manager ile Ads Manager arasında fark çıkması normaldir [K288]. iOS'ta ATT'yi reddeden kullanıcılar toplulaştırılmış ve modellenmiş biçimde, gecikmeli ölçülür [K54]. Ads Manager'daki rakamı tek başına doğru kabul etmeyin [K199].
4. Beklenen deneme maliyetinizle bütçeyi hesaplayın: haftalık bütçe ≈ deneme maliyeti × 50, günlük karşılığı ≈ deneme maliyeti × 7–10 [K8] [K11] [K492].
   - Bu bütçe karşılanabiliyorsa ya da ona yakın bir bütçeniz varsa StartTrial'a optimize edin [K4] [K11].
   - Purchase ancak haftada ~50 satın alma çıkıyorsa mantıklı [K11].
5. Tek kampanya ve tek reklam seti kurun. Hedeflemeyi geniş, yerleşimleri Advantage+ (varsayılan) bırakın [K3] [K31] [K65]. Reklam setini bölmeyin [K53].
6. Teklif stratejisi olarak en yüksek hacmi (varsayılan) seçin. Gerçek maliyeti öğrenene kadar maliyet hedefi ya da teklif sınırı koymayın [K28].
7. Birbirinden belirgin biçimde farklı 5–10 konseptle başlayın [K24] [K5] [K262]. Düşük bütçede bu sayının alt ucunda kalın, çünkü Meta harcamayı birkaç kreatife topluyor [K5] [K47]. Reklam yapısında kanca, sorun/çözüm, kanıt ve CTA bulunsun; mağaza sayfası reklamla uyumlu olsun [K26].
8. 7 gün dolmadan karar vermeyin [K15] [K39]. Kreatifleri gün sayısına göre değil harcamaya göre değerlendirin. Hedef CPA'ya göre önceden bir harcama eşiği koyun; eşiği geçip hedefin açıkça kötüsünde kalan kreatifi kapatın [K19] [K20]. Önemli düzenlemeleri seyrek yapın [K36] [K66].
9. Kreatifleri 2–4 haftada bir, ya da maliyet ve sıklık yükselince yenileyin. Haftalık yenileme yüksek bütçe içindir [K262] [K30].
10. Kampanya öğrenme aşamasından çıkıp kazanmaya başlayınca bütçeyi adım başına %10–20 artırın. Küçük bütçede bu aralığı 7–10 güne uzatın [K7].
11. Başarıyı deneme başına maliyetle değil, ödeyen müşteri başına maliyetle (CAC) ölçün. LTV verisi biriktikçe LTV:CAC ≈ 3:1 hedefini kendi kohortunuzla kontrol edin [K1] [K381].
12. Uygulama içinde paywall'u onboarding'e alın, ama denemeden ödemeye oranını ayrıca izleyin [K17].

## Kendi verinizle doğrulama

Aşağıdaki testler önem sırasıyla dizildi. Her test için kendi panelinizdeki StartTrial ve ödeme verisini kullanın.

1. **Install mi, StartTrial mı? [K4 testi] [K8 testi]**
   - Ne değişir: Aynı kitle ve bütçeyle iki kampanya; biri Install'a, biri StartTrial'a optimize.
   - Süre: en az 7–14 gün.
   - Ölçüt: deneme başına maliyet ve CAC.
   - Karar: CPI'ya göre değil CAC'ye göre verin. StartTrial kolunun CAC'si düşükse ona geçin. StartTrial kolu "öğrenme sınırlı"da takılıp hiç teslimat alamıyorsa bütçeyi artırın ya da setleri birleştirin.
2. **Ham deneme mi, nitelikli deneme mi? [K13 testi]**
   - Ne değişir: Bir kol "StartTrial"a, diğeri "1–2 saat sonra hâlâ aktif" olayına optimize.
   - Süre: en az 2 hafta ya da kol başına ~50 olay.
   - Ölçüt: CAC ve denemeden ödemeye oran.
   - Karar: Nitelikli olayın hacmi öğrenmeye yetmiyorsa pencereyi kısaltın.
3. **Yapı: tek set mi, ayrı setler mi? [K3 testi] [K9 testi]**
   - Ne değişir: Aynı toplam bütçeyle A) tek set ve 3–6 kreatif, B) her açı için ayrı set.
   - Süre: 10–14 gün; kol başına ~30–50 StartTrial.
   - Ölçüt: CAC ve kreatif başına harcama dağılımı.
   - Karar: B'nin CAC'si belirgin şekilde iyi değilse tek sette kalın.
4. **Kaç kreatif? [K5 testi] [K69 testi]**
   - Ne değişir: Önce 5 kreatif, sonra 10–12 kreatif (ya da 3'e karşı 8, gerçekten farklı açılarla).
   - Süre: 7–14 gün.
   - Ölçüt: StartTrial başına maliyet ve harcama alan kreatif sayısı.
   - Karar: Kreatif sayısını artırınca harcama alan kreatif sayısı ve maliyet iyileşmiyorsa düşük sayıda kalın.
5. **Kreatif yenileme ritmi [K262 testi]**
   - Ne değişir: 2 hafta kreatiflere dokunmayın, ardından 3–5 yeni kreatif ekleyin.
   - Ölçüt: StartTrial başına maliyet ve sıklık/CTR eğilimi.
   - Karar: Yenileme sonrası maliyet düşüyorsa bu takvimi sürdürün.
6. **Ölçekleme adımı [K7 testi]**
   - Ne değişir: Bir kampanyada 3 günde bir %15 artış, benzer bir kampanyada tek seferde %40–50 artış.
   - Süre: en az 10 gün.
   - Ölçüt: StartTrial CPA ve harcama istikrarı.
7. **MMP gerekli mi? [K18 testi]**
   - Ne değişir: SDK kampanyası sürerken MMP'yi de bağlayın, aynı olayları iki kaynakta karşılaştırın.
   - Süre: 2–4 hafta.
   - Karar: CAC hesabınız MMP verisiyle anlamlı ölçüde değişmiyorsa düşük bütçede MMP maliyetine girmeyin.
8. **Hedefleme [K31 testi] [K2 testi]**
   - Ne değişir: Tamamen geniş hedefleme ile B2B ilgi alanı/unvan önerili hedeflemeyi karşılaştırın. Ayrıca kreatifte hedef kitleyi açıkça adlandırmayı (ör. "İK yöneticileri için") deneyin.
   - Süre: 7–10 gün.
   - Ölçüt: CAC ve denemeden ödemeye oran.

## Tartışmalı ve koşullu noktalar

- **Tek set mi, ayrı setler mi?** Çoğunluk tek set ve çok kreatif öneriyor [K3]. Karşı görüşe göre küçük bütçede Meta harcamayı daha kötü kreatife yönlendirebiliyor [K3] [K9] [K47]. Fark bütçeden ve test/ölçekleme aşamasından kaynaklanıyor. [K9] "doubtful" bandında.
- **ABO ile test, CBO ile ölçekleme.** Üç kaynak bu yaklaşımı öneriyor ama doğrulama e-ticaret bağlamından [K14]. Tek kaynaklı Türkçe bir örneklemde rakamlar farklı yönde: tek CBO, küçük bütçede ABO'dan iyi [K523] [K525] [K279]. Başka bir kaynak Andromeda sonrası reklam seti bütçesini tercih ediyor [K347]. Abonelikli uygulamada doğrulanmış değil.
- **Kreatif sayısı.** Önerilen eşikler 3–7, 5–10 ve 20+ arasında değişiyor [K5] [K42]. Haftada 20–25+ kreatif önerisi yüksek bütçeye ait [K45].
- **Hangi derin olay?** Kaynaklar Purchase, ROAS/değer ve trial arasında ayrışıyor [K4]. Değer/tROAS önerisi tek kaynaklı [K160]. Hacim kısıtı düşük bütçede StartTrial'ı öne çıkarıyor [K11].
- **Uygulama Tanıtımı mı, Satış hedefi mi?** Bir kaynak abonelikte satış kampanyası öneriyor [K6].
- **Öğrenme süresi.** "24–48 saat" ile "7 gün/50 olay" arasındaki fark dönüşüm hacminden geliyor [K32].
- **Statik ve ham kreatifler.** "Algoritma statiği kayırır" iddiası doğrulanmamış [K51]. Ham kreatiflerin cilalı olanlardan iyi çalıştığı fikri koşullu [K55].
- **"Küçük bütçe" tanımı.** Pazara göre değişiyor; TL ve USD eşikleri birbirine doğrudan çevrilemez [K34].
- **Kazananı ayrı sete almak.** Yalnızca koşullu destek var [K44] [K50].

## Platform gerçekleri

- Öğrenme aşamasından çıkış için son önemli düzenlemeden sonraki 7 günde reklam seti başına ~50 optimizasyon olayı gerekir [K8] [K49]. Önemli düzenlemeler öğrenmeyi sıfırlar; bütçe için resmi bir yüzde eşiği yoktur [K66].
- SDK veya MMP bağlıysa uygulama içi olaylara (StartTrial dahil) optimize edilebilir. Aynı anda yalnızca tek bir olaya optimize edilir [K457] [K381].
- pLTV; Purchase, Subscribe, StartTrial, CompleteRegistration ve AddPaymentInfo olaylarını destekler [K459]. Ancak Conversions API ister ve son 4 haftada haftada en az 100 dönüşüm gerektirir. Doküman pLTV'nin şu an uygulama olaylarını desteklemediğini söylüyor [K531] [K327]. Aksini iddia eden [K462] dokümanla çelişiyor.
- iOS'ta ATT'yi reddeden kullanıcılar AEM ile toplulaştırılmış ve modellenmiş biçimde ölçülür [K54]. Android'de atıf Install Referrer üzerinden yapılır [K465].
- Events Manager atfedilmemiş olayları da gösterir, Ads Manager yalnızca reklama atfedilen ve tekilleştirilmiş olayları sayar [K288]. Ads Manager ile üçüncü taraf araçlar farklı rakamlar verebilir [K199].
- CBO'nun yeni adı "Advantage kampanya bütçesi". Bütçeyi reklam setleri arasında otomatik dağıtır [K280] [K281] [K560] [K25].
- Advantage+ audience'ta "kontroller" (konum, minimum yaş, dil, hariç tutma) Meta'nın aşamayacağı sınırlardır. "Öneriler" ise Meta'nın aşabileceği ipuçlarıdır [K147].
- Reklam incelemesi genelde 24 saat içinde biter; yeni hesaplarda daha uzun sürebilir [K23] [K172].
- Özel reklam kategorileri (istihdam, finans, konut, siyaset) beyan edilmelidir. İK veya işe alım odaklı bir B2B uygulama için bu doğrudan önemli olabilir [K52].
- Advantage+ Creative statik görseli hafif animasyonlu 9:16 videoya çevirebilir; özellik opt-in'dir [K486].
- Uygulama kampanyası form gerektirmez [K269]. Yerleşimler arasında WhatsApp Status, Threads ve Audience Network de var [K537].
- Andromeda, reklam dağıtımının aday seçme (retrieval) aşamasıdır [K346] [K388].

## Tek kaynaklı ama dikkat çekici (doğrulanmamış)

- StartTrial optimizasyonu yükleme maliyetini yaklaşık iki katına çıkarmış, ama kampanya toplamda daha kârlı olmuş [K448].
- Ucuz deneme peşindeki, tıklama odaklı reklamlar denemeden ödemeye oranını sert biçimde düşürmüş [K410]. CPI'si çok iyi bir kreatif bile denemeye dönüşmeyebiliyor [K153].
- Yalnızca Meta kaynaklı denemelerin ödemeye dönüşüm verisini Meta'ya geri göndermek öneriliyor [K309]. Ölçeklemeden önce soğuk trafik için yaklaşık bir aylık denemeden ödemeye taban değeri çıkarmak öneriliyor [K190].
- SKAN kullanılıyorsa StartTrial'ın dönüşüm değeri önceliği Düşük/Orta, Purchase'ınki Yüksek ayarlanmalı [K308].
- Küçük bütçede CPC, CPI'dan daha yararlı bir yön göstergesi olabilir [K480].
- Meta iş e-postalarını kişisel e-postalardan daha kötü eşleştiriyor; B2B listelerinde eşleşme oranı düşük çıkabilir [K122]. B2B'de geniş hedefleme ancak toplam pazar büyükse işe yarayabilir [K500].
- Doğrudan yüklenen, tamamen yapay zekâ üretimi kreatifler zayıf kalmış [K380].
- 14 günlük ücretsiz deneme, %20 indirimli "denemesiz" seçenekten iyi çalışmış [K193]. Birden fazla deneme seçeneği sunmak deneme başlangıcını artırmış [K450].
- RevenueCat'ten Meta'ya doğrudan entegrasyonun 2026 başında bozuk olduğu söyleniyor; doğrulanamadı [K532].

## Yorumlardan

Bu ipuçları izleyici yorumlarından geliyor ve doğrulanmadı.

- iOS'ta sinyal kaybı ciddi olabilir: bir izleyici 55 gerçek denemeye karşılık Meta'da 27 deneme görmüş. Bütçe kararlarında bu farkı hesaba katın.
- Ölçeklemeden önce denemeden ödemeye oranını ve 2.–3. ay elde tutmayı doğrulayın. Erken LTV tahmini kanıtlanmış değildir.
- SKAN verisi 1–2 gün gecikir; kararları buna göre yavaş okuyun.
- Kreatif testinde kreatif başına 2–3 dönüşüm hedefleyin. Haftalık bütçe = kreatif sayısı × 2–3 × hedef CPA.
- Opportunity Score önerilerini körü körüne uygulamayın; önce küçük bir testle ölçün.
- Meta işlemlerini tablet yerine bilgisayardan yapın; mobil ve tablet panelleri eksik görünebiliyor.
- Türkiye'de vergi kalemlerine (KDV, stopaj) dikkat edin [K63].

## Elenenler: satış, abartı, doğrulanamayanlar

- **Ücretli teklifler:** Ajans hizmetleri (yönetim, denetim, "done-for-you" kurulum), koçluk ve danışmanlık görüşmeleri, kurslar ve akademiler, ücretli Telegram ve Skool toplulukları, sponsor içerikleri. Bunun yanında konuşmacıların kendi attribution, abonelik ve AI reklam araçları da tanıtılıyor. Kaynakların çoğunda bu çıkar ilişkisi var; etkinlik iddialarının ağırlığı buna göre düşürüldü.
- **Abartılı başlıklar:** "%97" ve "tek değişiklikle %56 artış" gibi iddialar desteksiz ya da anekdot düzeyinde kaldı.
- **Doğrulanamayan gelir ve sonuç iddiaları:** B2B SaaS'ta 3–6 kat getiri [K16], 3–14 kat MRR artışı [K27], "ayda 2M$" [K436], "500$'a 1.200 indirme" [K429] ve CPI hesabıyla çelişen [K87]. Bunların hiçbiri ekranda gösterilmedi.
- **Kaynaksız eşikler:** Deneme başına 10–15$ CPA [K241], yükleme başına en az 3$ LTV [K195], denemeden ödemeye en az %30 [K452], install→paywall en az %80 [K253], "500$ ile 10–25 reklam" [K260]. Bunları kıyas değeri olarak kullanmayın.

## Sınırlar

- Örneklem 26 kanaldan 35 video. Kaynakların büyük kısmı İngilizce ve Türkçe. B2B abonelikli uygulamaya ve düşük bütçeli Advantage+ app'e özgü ilk el veri çok az; örneklerin çoğu B2C ya da lead/e-ticaret bağlamında.
- Hayatta kalma yanlılığı var: başarı hikâyeleri seçilerek anlatılıyor, başarısız kampanyalar görünmüyor.
- Rakamların neredeyse tamamı sözlü; Andromeda sonrası dönem için resmi eşikler sınırlı.
- Bu rapor 2026-10-27 tarihinde erişilebilen videoları yansıtıyor. Meta arayüzü ve politikaları (pLTV kapsamı, adlandırmalar, Andromeda) hızlı değişiyor; araştırmayı 3–6 ay içinde yeniden çalıştırın.
