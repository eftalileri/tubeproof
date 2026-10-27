# Meta Advantage+ app ile abonelikli B2B uygulamaya düşük bütçede deneme ve ödeyen müşteri getirmek

## Kısa cevap

Kanıtlar birkaç konuda net. Abonelikli bir uygulamada kampanyayı yüklemeye (install) optimize etmek ucuz yükleme getirir, ama bu yüklemeler denemeye ve ödemeye nadiren dönüşür. StartTrial gibi daha derin bir olaya optimize etmek daha iyi sonuç verir [K4](#k4) [K381](#k381). Öte yandan Meta'nın öğrenebilmesi için reklam seti başına haftada yaklaşık 50 optimizasyon olayı gerekir. Bu yüzden düşük bütçede Purchase yerine StartTrial seçmek, yapıyı tek reklam setinde toplamak ve geniş hedefleme kullanmak en tutarlı öneri [K8](#k8) [K11](#k11) [K3](#k3). Kurulum tarafında önce Meta SDK ile olayları doğru göndermek, sonra birbirinden belirgin biçimde farklı kreatifler test etmek, değerlendirmeyi 7 günlük pencerelerle yapmak ve bütçeyi kademeli artırmak destekleniyor [K18](#k18) [K24](#k24) [K15](#k15) [K7](#k7).

Kanıtın zayıf kaldığı yerler de var. Çoğu kaynak ajans ya da kurs satıyor ve kendi verisini göstermiyor. B2B'ye özgü, düşük bütçeli bir Advantage+ app vakası corpus'ta neredeyse hiç yok; örneklerin çoğu B2C (fitness, bebek uygulaması) ya da B2B lead kampanyası. "Ödeyen müşteri maliyeti" konusunda güvenilir bir kıyas değeri bulunmuyor. Bunu kendi verinizle ölçmeniz gerekecek.

## Platformun söyledikleri ve uygulayıcıların aktardıkları

Aşağıdaki maddelerde uygulayıcı kanıtı var ama resmi dokümanlar konuda sessiz (practice_only). Dokümanla doğrudan çelişen pratik bir bulgu yok. Dokümanla çelişen iki iddia ayrıca not edildi.

| Konu | Platform / dokümanlar | Uygulayıcılar (kendi deneyimi) | Hangisi ne zaman geçerli | Kümeler |
|---|---|---|---|---|
| Ham deneme yerine "nitelikli deneme" olayı | Optimize ettiğiniz olayı yapacak kişileri bulur; deneme ile ödeme arasında ayrım yapmaz | Denemeden 1–3 saat sonra hâlâ aktif olan kullanıcıyı ayrı olay olarak gönderip ona optimize etmek, hemen iptal edenleri eler | Olay hacmi yetiyorsa nitelikli deneme. Hacim düşükse pencereyi kısaltın ya da ham StartTrial'da kalın | [K13](#k13) [K381](#k381) |
| Hedefleme genişliği | Advantage+ audience'ı tarif ediyor, performans hakkında bir şey demiyor | Tek ülke ve geniş hedefleme, dar segmentasyondan iyi | Kitle havuzu büyükse geniş. Çok niş B2B kitlede belirsiz | [K31](#k31) [K147](#k147) |
| Tıklama/etkileşime optimizasyon | Yalnızca "optimizasyon olayına göre dağıtım" ilkesi var | Tıklayan ama dönüşmeyen kişileri getirir | Hedef deneme ya da ödemeyse dönüşüm olayına optimize edin | [K10](#k10) |
| Bütçenin kolay dönüşüme yığılması | Sessiz | CBO veya tek sette harcama tek kreatife ya da kolay dönüşüme toplanabiliyor | Küçük bütçe ve çok kreatifli tek sette risk daha yüksek | [K47](#k47) |
| Öğrenme süresi | Haftada ~50 olay eşiği | Süre hacme bağlı; düşük bütçede setler uzun süre "öğrenme sınırlı" kalabiliyor | Düşük bütçeli StartTrial kampanyasında sabit bir süre beklemeyin | [K32](#k32) [K8](#k8) |
| Onboarding içinde paywall | Konu Meta'nın alanı değil | Deneme başlangıcını artırıyor; ancak denemeden ödemeye oranı ayrıca izlenmeli | Uygulama içi taktik; kampanyadan bağımsız test edin | [K17](#k17) |
| Web quiz'e yönlendirme | Sessiz; Advantage+ app trafiği doğrudan mağazaya götürür | B2C'de doğrudan mağazaya göre daha iyi dönüşüm | Yalnızca B2C'de görülmüş. Web dönüşüm kampanyası gerektirir | [K68](#k68) |
| LTV:CAC hedefi | Eşik vermiyor | Kabaca 3:1 (en az 2–3 kat) | LTV verisi olan, orta ve yüksek bütçeli hesaplar | [K1](#k1) |
| Organik içeriği reklamda yeniden kullanmak | Sessiz | Organikte iyi giden içerik reklamda da çoğunlukla iyi çalışır | Organik etkileşimle deneme dönüşümü aynı şey değil; test edin | [K29](#k29) |
| Kazanan kreatif oranı | Yalnızca çeşitlilik öneriyor | Ayda çok sayıda kreatif test ediliyor, ~%5–10'u kazanıyor | Yüksek bütçe; düşük bütçeye doğrudan aktarılamaz | [K21](#k21) |

**Dokümanla çelişen iddialar:** "SDK ve sunucudan aynı event_id ile gönderilirse pLTV, ATT'ye rağmen çalışır" iddiası, Meta'nın pLTV rehberiyle çelişiyor. Rehbere göre pLTV şu an uygulama olaylarını desteklemiyor [K462](#k462). "Andromeda ile 100 kat daha kısa yanıt süresi" de resmi yazıyla uyuşmuyor; resmi yazıda %6 recall artışı ve 10 kat verimlilik geçiyor [K348](#k348).

**Pratik ile dokümanın örtüştüğü yerler:** Birbirinden belirgin biçimde farklı konseptlerle test etmek [K24](#k24). Reklam incelemesinin genelde 24 saat içinde bitmesi [K23](#k23). Günlük dalgalanmalara tepki vermemek [K39](#k39).

## Kaldıraçlar (etkisine göre sıralı)

1. **Optimizasyon olayını StartTrial (ya da nitelikli deneme) yapmak.**
   - Ne yapılır: Install yerine StartTrial'a optimize edin. Hacim yeterliyse nitelikli deneme olayına geçin.
   - Beklenen etki: Yükleme maliyeti artar, ama ödeyen müşteri başına maliyet (CAC) düşmesi beklenir. Tek kaynaklı bir ilk el örnekte deneme optimizasyonu yükleme maliyetini yaklaşık iki katına çıkarmış, buna rağmen kampanya toplamda daha kârlı çıkmış [K448](#k448).
   - Kanıt: güçlü [K4](#k4) [K11](#k11) [K381](#k381) [K457](#k457). Nitelikli deneme için olası [K13](#k13).

2. **Olay hacmine göre bütçe ve yapı kurmak.**
   - Ne yapılır: Reklam seti başına haftada ~50 olay hedefleyin. Bütçe kaba olarak "olay maliyeti × 50 / hafta" (günde ×7–10) eder.
   - Beklenen etki: Set öğrenme aşamasından çıkabilir ve maliyetler istikrar kazanır.
   - Kanıt: güçlü, docs destekli [K8](#k8) [K11](#k11) [K492](#k492). Tek set ve konsolidasyon için [K3](#k3) [K53](#k53).

3. **Sinyal ve ölçüm kalitesi.**
   - Ne yapılır: Önce Meta SDK ile StartTrial ve abonelik olaylarını gönderin. Events Manager, Ads Manager ve mağaza sayılarını birbiriyle karşılaştırın.
   - Beklenen etki: Yanlış olaya optimize etmenin ve yanlış bütçe kararlarının önüne geçer.
   - Kanıt: güçlü [K18](#k18) [K457](#k457) [K288](#k288) [K54](#k54). "Önce sinyal, sonra kreatif" sıralaması olası düzeyde [K35](#k35).

4. **Kreatif çeşitliliği.**
   - Ne yapılır: Kanca, format ve açı olarak birbirinden ayrışan 5–10 konsept kullanın. Varyasyonlara ancak kazanan konsept çıktıktan sonra geçin.
   - Beklenen etki: Andromeda sonrası dağıtımda kreatif, reklamı kimin göreceğini belirleyen ana sinyallerden biri.
   - Kanıt: güçlü [K24](#k24) [K2](#k2) [K5](#k5) [K262](#k262) [K69](#k69). Kesin sayılar tartışmalı.

5. **Geniş hedefleme, Advantage+ yerleşim, en yüksek hacim teklifi.**
   - Ne yapılır: Hedefleme ve yerleşimi Meta'ya bırakın. Başlangıçta teklif sınırı ya da maliyet hedefi koymayın.
   - Kanıt: güçlü ya da olası [K28](#k28) [K65](#k65) [K31](#k31).

6. **Sabır ve düzenleme disiplini.**
   - Ne yapılır: Değerlendirmeyi 7 günlük pencerede yapın, önemli düzenlemeleri seyrek tutun.
   - Beklenen etki: Öğrenme aşamasının tekrar tekrar sıfırlanmasını önler.
   - Kanıt: olası [K15](#k15) [K39](#k39) [K36](#k36) [K66](#k66).

7. **Kademeli ölçekleme.**
   - Ne yapılır: Bütçeyi adım başına %10–20 artırın, 2–4 günde bir. Küçük bütçede aralığı 7–10 güne uzatın.
   - Kanıt: güçlü, ama rakamlar sektör pratiği [K7](#k7).

8. **Uygulama içi dönüşüm.**
   - Ne yapılır: Paywall'u onboarding içine alın, deneme teklifini açık sunun.
   - Kanıt: olası, B2C kaynaklı [K17](#k17).

## Pratik tarif

1. Uygulamanız gerçekten mobilse Uygulama Tanıtımı / Advantage+ app hedefini kullanın. iOS 14+ ayarlarını yapın [K6](#k6). Reklam hesabını açarken para birimi ve saat dilimini doğru seçin [K12](#k12).
2. Meta SDK'yı kurun. Install, StartTrial ve abonelik/satın alma olaylarını gönderin [K18](#k18) [K457](#k457). MMP'yi birden fazla mecra ölçecekseniz ya da bütçe büyüdüğünde ekleyin [K18](#k18).
3. Ölçümü doğrulayın. Events Manager ile Ads Manager arasında fark çıkması normaldir [K288](#k288). iOS'ta ATT'yi reddeden kullanıcılar toplulaştırılmış ve modellenmiş biçimde, gecikmeli ölçülür [K54](#k54). Ads Manager'daki rakamı tek başına doğru kabul etmeyin [K199](#k199).
4. Beklenen deneme maliyetinizle bütçeyi hesaplayın: haftalık bütçe ≈ deneme maliyeti × 50, günlük karşılığı ≈ deneme maliyeti × 7–10 [K8](#k8) [K11](#k11) [K492](#k492).
   - Bu bütçe karşılanabiliyorsa ya da ona yakın bir bütçeniz varsa StartTrial'a optimize edin [K4](#k4) [K11](#k11).
   - Purchase ancak haftada ~50 satın alma çıkıyorsa mantıklı [K11](#k11).
5. Tek kampanya ve tek reklam seti kurun. Hedeflemeyi geniş, yerleşimleri Advantage+ (varsayılan) bırakın [K3](#k3) [K31](#k31) [K65](#k65). Reklam setini bölmeyin [K53](#k53).
6. Teklif stratejisi olarak en yüksek hacmi (varsayılan) seçin. Gerçek maliyeti öğrenene kadar maliyet hedefi ya da teklif sınırı koymayın [K28](#k28).
7. Birbirinden belirgin biçimde farklı 5–10 konseptle başlayın [K24](#k24) [K5](#k5) [K262](#k262). Düşük bütçede bu sayının alt ucunda kalın, çünkü Meta harcamayı birkaç kreatife topluyor [K5](#k5) [K47](#k47). Reklam yapısında kanca, sorun/çözüm, kanıt ve CTA bulunsun; mağaza sayfası reklamla uyumlu olsun [K26](#k26).
8. 7 gün dolmadan karar vermeyin [K15](#k15) [K39](#k39). Kreatifleri gün sayısına göre değil harcamaya göre değerlendirin. Hedef CPA'ya göre önceden bir harcama eşiği koyun; eşiği geçip hedefin açıkça kötüsünde kalan kreatifi kapatın [K19](#k19) [K20](#k20). Önemli düzenlemeleri seyrek yapın [K36](#k36) [K66](#k66).
9. Kreatifleri 2–4 haftada bir, ya da maliyet ve sıklık yükselince yenileyin. Haftalık yenileme yüksek bütçe içindir [K262](#k262) [K30](#k30).
10. Kampanya öğrenme aşamasından çıkıp kazanmaya başlayınca bütçeyi adım başına %10–20 artırın. Küçük bütçede bu aralığı 7–10 güne uzatın [K7](#k7).
11. Başarıyı deneme başına maliyetle değil, ödeyen müşteri başına maliyetle (CAC) ölçün. LTV verisi biriktikçe LTV:CAC ≈ 3:1 hedefini kendi kohortunuzla kontrol edin [K1](#k1) [K381](#k381).
12. Uygulama içinde paywall'u onboarding'e alın, ama denemeden ödemeye oranını ayrıca izleyin [K17](#k17).

## Kendi verinizle doğrulama

Aşağıdaki testler önem sırasıyla dizildi. Her test için kendi panelinizdeki StartTrial ve ödeme verisini kullanın.

1. **Install mi, StartTrial mı? [K4 testi](#k4) [K8 testi](#k8)**
   - Ne değişir: Aynı kitle ve bütçeyle iki kampanya; biri Install'a, biri StartTrial'a optimize.
   - Süre: en az 7–14 gün.
   - Ölçüt: deneme başına maliyet ve CAC.
   - Karar: CPI'ya göre değil CAC'ye göre verin. StartTrial kolunun CAC'si düşükse ona geçin. StartTrial kolu "öğrenme sınırlı"da takılıp hiç teslimat alamıyorsa bütçeyi artırın ya da setleri birleştirin.
2. **Ham deneme mi, nitelikli deneme mi? [K13 testi](#k13)**
   - Ne değişir: Bir kol "StartTrial"a, diğeri "1–2 saat sonra hâlâ aktif" olayına optimize.
   - Süre: en az 2 hafta ya da kol başına ~50 olay.
   - Ölçüt: CAC ve denemeden ödemeye oran.
   - Karar: Nitelikli olayın hacmi öğrenmeye yetmiyorsa pencereyi kısaltın.
3. **Yapı: tek set mi, ayrı setler mi? [K3 testi](#k3) [K9 testi](#k9)**
   - Ne değişir: Aynı toplam bütçeyle A) tek set ve 3–6 kreatif, B) her açı için ayrı set.
   - Süre: 10–14 gün; kol başına ~30–50 StartTrial.
   - Ölçüt: CAC ve kreatif başına harcama dağılımı.
   - Karar: B'nin CAC'si belirgin şekilde iyi değilse tek sette kalın.
4. **Kaç kreatif? [K5 testi](#k5) [K69 testi](#k69)**
   - Ne değişir: Önce 5 kreatif, sonra 10–12 kreatif (ya da 3'e karşı 8, gerçekten farklı açılarla).
   - Süre: 7–14 gün.
   - Ölçüt: StartTrial başına maliyet ve harcama alan kreatif sayısı.
   - Karar: Kreatif sayısını artırınca harcama alan kreatif sayısı ve maliyet iyileşmiyorsa düşük sayıda kalın.
5. **Kreatif yenileme ritmi [K262 testi](#k262)**
   - Ne değişir: 2 hafta kreatiflere dokunmayın, ardından 3–5 yeni kreatif ekleyin.
   - Ölçüt: StartTrial başına maliyet ve sıklık/CTR eğilimi.
   - Karar: Yenileme sonrası maliyet düşüyorsa bu takvimi sürdürün.
6. **Ölçekleme adımı [K7 testi](#k7)**
   - Ne değişir: Bir kampanyada 3 günde bir %15 artış, benzer bir kampanyada tek seferde %40–50 artış.
   - Süre: en az 10 gün.
   - Ölçüt: StartTrial CPA ve harcama istikrarı.
7. **MMP gerekli mi? [K18 testi](#k18)**
   - Ne değişir: SDK kampanyası sürerken MMP'yi de bağlayın, aynı olayları iki kaynakta karşılaştırın.
   - Süre: 2–4 hafta.
   - Karar: CAC hesabınız MMP verisiyle anlamlı ölçüde değişmiyorsa düşük bütçede MMP maliyetine girmeyin.
8. **Hedefleme [K31 testi](#k31) [K2 testi](#k2)**
   - Ne değişir: Tamamen geniş hedefleme ile B2B ilgi alanı/unvan önerili hedeflemeyi karşılaştırın. Ayrıca kreatifte hedef kitleyi açıkça adlandırmayı (ör. "İK yöneticileri için") deneyin.
   - Süre: 7–10 gün.
   - Ölçüt: CAC ve denemeden ödemeye oran.

## Tartışmalı ve koşullu noktalar

- **Tek set mi, ayrı setler mi?** Çoğunluk tek set ve çok kreatif öneriyor [K3](#k3). Karşı görüşe göre küçük bütçede Meta harcamayı daha kötü kreatife yönlendirebiliyor [K3](#k3) [K9](#k9) [K47](#k47). Fark bütçeden ve test/ölçekleme aşamasından kaynaklanıyor. [K9](#k9) "doubtful" bandında.
- **ABO ile test, CBO ile ölçekleme.** Üç kaynak bu yaklaşımı öneriyor ama doğrulama e-ticaret bağlamından [K14](#k14). Tek kaynaklı Türkçe bir örneklemde rakamlar farklı yönde: tek CBO, küçük bütçede ABO'dan iyi [K523](#k523) [K525](#k525) [K279](#k279). Başka bir kaynak Andromeda sonrası reklam seti bütçesini tercih ediyor [K347](#k347). Abonelikli uygulamada doğrulanmış değil.
- **Kreatif sayısı.** Önerilen eşikler 3–7, 5–10 ve 20+ arasında değişiyor [K5](#k5) [K42](#k42). Haftada 20–25+ kreatif önerisi yüksek bütçeye ait [K45](#k45).
- **Hangi derin olay?** Kaynaklar Purchase, ROAS/değer ve trial arasında ayrışıyor [K4](#k4). Değer/tROAS önerisi tek kaynaklı [K160](#k160). Hacim kısıtı düşük bütçede StartTrial'ı öne çıkarıyor [K11](#k11).
- **Uygulama Tanıtımı mı, Satış hedefi mi?** Bir kaynak abonelikte satış kampanyası öneriyor [K6](#k6).
- **Öğrenme süresi.** "24–48 saat" ile "7 gün/50 olay" arasındaki fark dönüşüm hacminden geliyor [K32](#k32).
- **Statik ve ham kreatifler.** "Algoritma statiği kayırır" iddiası doğrulanmamış [K51](#k51). Ham kreatiflerin cilalı olanlardan iyi çalıştığı fikri koşullu [K55](#k55).
- **"Küçük bütçe" tanımı.** Pazara göre değişiyor; TL ve USD eşikleri birbirine doğrudan çevrilemez [K34](#k34).
- **Kazananı ayrı sete almak.** Yalnızca koşullu destek var [K44](#k44) [K50](#k50).

## Platform gerçekleri

- Öğrenme aşamasından çıkış için son önemli düzenlemeden sonraki 7 günde reklam seti başına ~50 optimizasyon olayı gerekir [K8](#k8) [K49](#k49). Önemli düzenlemeler öğrenmeyi sıfırlar; bütçe için resmi bir yüzde eşiği yoktur [K66](#k66).
- SDK veya MMP bağlıysa uygulama içi olaylara (StartTrial dahil) optimize edilebilir. Aynı anda yalnızca tek bir olaya optimize edilir [K457](#k457) [K381](#k381).
- pLTV; Purchase, Subscribe, StartTrial, CompleteRegistration ve AddPaymentInfo olaylarını destekler [K459](#k459). Ancak Conversions API ister ve son 4 haftada haftada en az 100 dönüşüm gerektirir. Doküman pLTV'nin şu an uygulama olaylarını desteklemediğini söylüyor [K531](#k531) [K327](#k327). Aksini iddia eden [K462](#k462) dokümanla çelişiyor.
- iOS'ta ATT'yi reddeden kullanıcılar AEM ile toplulaştırılmış ve modellenmiş biçimde ölçülür [K54](#k54). Android'de atıf Install Referrer üzerinden yapılır [K465](#k465).
- Events Manager atfedilmemiş olayları da gösterir, Ads Manager yalnızca reklama atfedilen ve tekilleştirilmiş olayları sayar [K288](#k288). Ads Manager ile üçüncü taraf araçlar farklı rakamlar verebilir [K199](#k199).
- CBO'nun yeni adı "Advantage kampanya bütçesi". Bütçeyi reklam setleri arasında otomatik dağıtır [K280](#k280) [K281](#k281) [K560](#k560) [K25](#k25).
- Advantage+ audience'ta "kontroller" (konum, minimum yaş, dil, hariç tutma) Meta'nın aşamayacağı sınırlardır. "Öneriler" ise Meta'nın aşabileceği ipuçlarıdır [K147](#k147).
- Reklam incelemesi genelde 24 saat içinde biter; yeni hesaplarda daha uzun sürebilir [K23](#k23) [K172](#k172).
- Özel reklam kategorileri (istihdam, finans, konut, siyaset) beyan edilmelidir. İK veya işe alım odaklı bir B2B uygulama için bu doğrudan önemli olabilir [K52](#k52).
- Advantage+ Creative statik görseli hafif animasyonlu 9:16 videoya çevirebilir; özellik opt-in'dir [K486](#k486).
- Uygulama kampanyası form gerektirmez [K269](#k269). Yerleşimler arasında WhatsApp Status, Threads ve Audience Network de var [K537](#k537).
- Andromeda, reklam dağıtımının aday seçme (retrieval) aşamasıdır [K346](#k346) [K388](#k388).

## Tek kaynaklı ama dikkat çekici (doğrulanmamış)

- StartTrial optimizasyonu yükleme maliyetini yaklaşık iki katına çıkarmış, ama kampanya toplamda daha kârlı olmuş [K448](#k448).
- Ucuz deneme peşindeki, tıklama odaklı reklamlar denemeden ödemeye oranını sert biçimde düşürmüş [K410](#k410). CPI'si çok iyi bir kreatif bile denemeye dönüşmeyebiliyor [K153](#k153).
- Yalnızca Meta kaynaklı denemelerin ödemeye dönüşüm verisini Meta'ya geri göndermek öneriliyor [K309](#k309). Ölçeklemeden önce soğuk trafik için yaklaşık bir aylık denemeden ödemeye taban değeri çıkarmak öneriliyor [K190](#k190).
- SKAN kullanılıyorsa StartTrial'ın dönüşüm değeri önceliği Düşük/Orta, Purchase'ınki Yüksek ayarlanmalı [K308](#k308).
- Küçük bütçede CPC, CPI'dan daha yararlı bir yön göstergesi olabilir [K480](#k480).
- Meta iş e-postalarını kişisel e-postalardan daha kötü eşleştiriyor; B2B listelerinde eşleşme oranı düşük çıkabilir [K122](#k122). B2B'de geniş hedefleme ancak toplam pazar büyükse işe yarayabilir [K500](#k500).
- Doğrudan yüklenen, tamamen yapay zekâ üretimi kreatifler zayıf kalmış [K380](#k380).
- 14 günlük ücretsiz deneme, %20 indirimli "denemesiz" seçenekten iyi çalışmış [K193](#k193). Birden fazla deneme seçeneği sunmak deneme başlangıcını artırmış [K450](#k450).
- RevenueCat'ten Meta'ya doğrudan entegrasyonun 2026 başında bozuk olduğu söyleniyor; doğrulanamadı [K532](#k532).

## Yorumlardan

Bu ipuçları izleyici yorumlarından geliyor ve doğrulanmadı.

- iOS'ta sinyal kaybı ciddi olabilir: bir izleyici 55 gerçek denemeye karşılık Meta'da 27 deneme görmüş. Bütçe kararlarında bu farkı hesaba katın.
- Ölçeklemeden önce denemeden ödemeye oranını ve 2.–3. ay elde tutmayı doğrulayın. Erken LTV tahmini kanıtlanmış değildir.
- SKAN verisi 1–2 gün gecikir; kararları buna göre yavaş okuyun.
- Kreatif testinde kreatif başına 2–3 dönüşüm hedefleyin. Haftalık bütçe = kreatif sayısı × 2–3 × hedef CPA.
- Opportunity Score önerilerini körü körüne uygulamayın; önce küçük bir testle ölçün.
- Meta işlemlerini tablet yerine bilgisayardan yapın; mobil ve tablet panelleri eksik görünebiliyor.
- Türkiye'de vergi kalemlerine (KDV, stopaj) dikkat edin [K63](#k63).

## Elenenler: satış, abartı, doğrulanamayanlar

- **Ücretli teklifler:** Ajans hizmetleri (yönetim, denetim, "done-for-you" kurulum), koçluk ve danışmanlık görüşmeleri, kurslar ve akademiler, ücretli Telegram ve Skool toplulukları, sponsor içerikleri. Bunun yanında konuşmacıların kendi attribution, abonelik ve AI reklam araçları da tanıtılıyor. Kaynakların çoğunda bu çıkar ilişkisi var; etkinlik iddialarının ağırlığı buna göre düşürüldü.
- **Abartılı başlıklar:** "%97" ve "tek değişiklikle %56 artış" gibi iddialar desteksiz ya da anekdot düzeyinde kaldı.
- **Doğrulanamayan gelir ve sonuç iddiaları:** B2B SaaS'ta 3–6 kat getiri [K16](#k16), 3–14 kat MRR artışı [K27](#k27), "ayda 2M$" [K436](#k436), "500$'a 1.200 indirme" [K429](#k429) ve CPI hesabıyla çelişen [K87](#k87). Bunların hiçbiri ekranda gösterilmedi.
- **Kaynaksız eşikler:** Deneme başına 10–15$ CPA [K241](#k241), yükleme başına en az 3$ LTV [K195](#k195), denemeden ödemeye en az %30 [K452](#k452), install→paywall en az %80 [K253](#k253), "500$ ile 10–25 reklam" [K260](#k260). Bunları kıyas değeri olarak kullanmayın.

## Sınırlar

- Örneklem 26 kanaldan 35 video. Kaynakların büyük kısmı İngilizce ve Türkçe. B2B abonelikli uygulamaya ve düşük bütçeli Advantage+ app'e özgü ilk el veri çok az; örneklerin çoğu B2C ya da lead/e-ticaret bağlamında.
- Hayatta kalma yanlılığı var: başarı hikâyeleri seçilerek anlatılıyor, başarısız kampanyalar görünmüyor.
- Rakamların neredeyse tamamı sözlü; Andromeda sonrası dönem için resmi eşikler sınırlı.
- Bu rapor 2026-10-27 tarihinde erişilebilen videoları yansıtıyor. Meta arayüzü ve politikaları (pLTV kapsamı, adlandırmalar, Andromeda) hızlı değişiyor; araştırmayı 3–6 ay içinde yeniden çalıştırın.


---

## Kanıt eki

Raporda geçen her küme için kaynak videolar ve iddianın geçtiği an. Bant ve güven puanı kodla hesaplanır (kural sürümü `r3`).


### <a id="k1"></a>K1 · muhtemel · güven 0.67

Ücretli edinimde hedef LTV:CAC oranı kabaca 3:1 olmalıdır (en az 2–3x; satış ekipli B2B'de daha yüksek); yani izin verilen maksimum CAC, müşteri yaşam boyu değerinin bir kısmıdır.


*Değerlendirme:* Altı kanal 3:1 civarında örtüşüyor, ancak hepsi genel bilgiye dayanıyor ve çoğu ajans/kurs satıyor; bu yüzden bağımsız uygulayıcı kanıtı sayılmaz. Adapty konuşmacısı 100K+ aylık harcamalı uygulamalar için 2–3x diyor ve bu görece en güçlü işaret, ancak ekranda veri gösterilmiyor. Meta dokümanları bir LTV:CAC eşiği vermiyor. Oran sektör kuralıdır; nakit akışı, geri ödeme süresi ve düşük bütçeli deneme aşaması için kesin eşik değildir.


*Kendi verinle test:* Kendi verinizle 60–90 günlük kohort LTV'nizi (brüt kâr bazlı) hesaplayın, hedef CAC = LTV/3 olarak belirleyin ve kampanyada bu değeri cost cap/hedef maliyet olarak deneyin. Başarı ölçütü: ödeyen müşteri başı maliyetin hedef CAC altında kalması ve geri ödeme süresi.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=78) @1:18 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > The golden ratio for this is one to three.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=791) @13:11 · Gui Costa · 2026-07-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > your LTV to CAC needs to be three per one to be healthy.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=233) @3:53 · Lorenzo Pravatà · 2026-03-26 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > So usually, you want to have an LTV2COG that is at least 3x.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1348) @22:28 · App Leaders by Adapty · 2026-09-11 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > Every successful, and by that I mean 100K plus meta-spenders have an LTV of 2 to 3x minimal.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=311) @5:11 · Lorenzo Pravatà · 2026-03-26 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > even higher LTV2COG, maybe out 5x or more

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=75) @1:15 · Alessandro Cutri · 2026-06-04 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > ideally, you want that to be in that $2,000 to $3,000 range

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=868) @14:28 · Gui Costa · 2026-07-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > the average of people stay for three months. Right? Your LTV is $75.

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=685) @11:25 · Aprendamos Marketing · 2026-01-13 · *contradicts* · kaynak: genel bilgi
  > Yo debería estar dispuesto a invertir hasta 2 mil pesos para generar un cliente.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1296) @21:36 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > So what are you willing to pay to get that customer?

### <a id="k2"></a>K2 · sağlam · güven 0.90

Meta'nın Andromeda sonrası dağıtımında reklamı kimin göreceğini belirlemede kreatif (görsel, konuşma, metin) ana sinyallerden biridir; bu yüzden manuel kitle ayarlarından daha belirleyicidir.


*Değerlendirme:* Sekiz üye de aynı fikirde, ancak hiçbiri bağımsız ölçüm göstermiyor; çoğu Meta'nın söylemini veya genel bilgiyi tekrar ediyor ve birçoğu kurs veya ajans satıyor. Meta'nın mühendislik yazıları Andromeda'nın retrieval aşamasında kreatif çeşitliliğini ve kreatif temsilini kullandığını gösteriyor. Ancak "kreatif artık hedeflemenin kendisidir" ve "piksel piksel" gibi güçlü ifadeler resmi dokümanda doğrudan yer almıyor, abartılı bir yorum olabilir. Kitle ayarları tamamen anlamsız değil; sinyal ve dönüşüm verisi de önemli.


*Kendi verinle test:* Aynı bütçeyle iki kampanya kur: biri genel mesajlı kreatif, diğeri açıkça hedef kitleyi (ör. 'İK yöneticileri için') adlandıran kreatif; ikisi de geniş hedefleme. En az 7-10 gün çalıştır ve StartTrial başına maliyeti ile deneme sahibi kitlenin niteliğini (ödeyen oranı) karşılaştır.


- Resmi kaynak: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=233) @3:53 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_course, affiliate
  > The creative in this new update is now the targeting

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=912) @15:12 · Aprendamos Marketing · 2026-01-13 · *supports* · kaynak: platform dokümanı
  > analizando y literal así dice en la documentación, pixel por pixel de la imagen o el video que tú le pongas

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=152) @2:32 · Mark Builds Brands · 2026-05-11 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > Facebook is mostly looking at creative to determine targeting, not what you have going on within your ad sets.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=556) @9:16 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > They're going to transcribe your video. They're going to read the text on your static ads, and they're going to try to find the best ICP.

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=0) @0:00 · Menaf Avcı · 2025-12-28 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > Meta bugün reklamları sizin seçtiğiniz hedef kitlelere göre değil, yüklediğiniz kreatifin içeriğine göre kime göstereceğini biliyor

- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1436) @23:56 · Sub Club by RevenueCat · 2026-09-02 · *supports* · kaynak: genel bilgi
  > a lot of the targeting on Meta is specifically done through the creatives

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=148) @2:28 · Sabri Suby · 2026-06-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > So, if you want to target different people, you actually have to put that in the creative and in the body copy.

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=776) @12:56 · AdConversion · 2025-11-12 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services, sells_course
  > you want to make sure that you are explicitly calling out who the ad is for and who it's not for.

### <a id="k3"></a>K3 · sağlam · güven 0.91

Meta uygulama/yeni müşteri kampanyalarında tek kampanya ve tek geniş reklam setinin içine çok sayıda farklı kreatif koymak, format veya açıları ayrı reklam setlerine bölmekten daha iyidir.


*Değerlendirme:* Çoğu üye tek reklam seti + çok kreatif yapısını öneriyor ve Meta'nın Advantage+ app yapısı da tek reklam setini esas alıyor. Ancak bu üyelerin çoğu kanıtsız, kurs/ajans satan kaynaklar; bağımsız deneyim sınırlı. Karşı görüş ise ekranla gösterilmiş küçük bütçe deneyimine (Gui Costa) dayanıyor: Meta bütçeyi CPC'si daha kötü kreatife yönlendirmiş. Düşük bütçede bu risk gerçekçi, ama tek örnek.


*Kendi verinle test:* Aynı bütçeyle iki kampanya kur: A) 1 reklam seti, 6 kreatif; B) her açı için ayrı set (2-3 set). En az 7-10 gün çalıştır; başarı ölçütü deneme (StartTrial) başına maliyet ve ödeyen müşteri başına maliyet (CAC), ayrıca her kreatife giden harcama dağılımı.</test_tr>
<parameter name="caveats_tr">["Docs sadece Advantage+ app için tek reklam seti yapısını gösteriyor; 'ayrı set daha iyi' veya 'çok kreatif daha iyi' konusunda sessiz.","Menaf Avcı üyesi satış/e-ticaret bağlamında, uygulama değil.","Alessandro Cutri üyesi B2B lead bağlamında, uygulama kampanyası değil."]</caveats_tr>
</invoke>



- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “Manually test up to 50 creative combinations.”

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=388) @6:28 · Menaf Avcı · 2025-12-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > Bu reklam setinin altına da olabildiğince çok fazla kreatif ekliyoruz.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1097) @18:17 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > Yani hatta başlangıçta tek kampanya yapın.

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=703) @11:43 · Alessandro Cutri · 2026-06-04 · *contradicts* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > if you have these formats within a different ad set, you're giving yourself the best shot at success

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1181) @19:41 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > bir reklam grubu içerisine farklı formatlarda reklamlar eklemek.

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=310) @5:10 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > You need one campaign, one ad set, and a lot of creatives in that ad set.

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=304) @5:04 · Gui Costa · 2026-07-25 · *contradicts* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > But Meta was sending the budget here to G's one.

### <a id="k4"></a>K4 · sağlam · güven 0.96

Abonelikli bir uygulamada Meta kampanyasını yüklemeye (install) optimize etmek ucuz ama deneme/ödemeye nadiren dönüşen yüklemeler getirir; trial/purchase gibi derin olaylara optimize etmek daha iyi sonuç verir.


*Değerlendirme:* Altı üyenin hepsi yüklemeye optimizasyonun abonelikli uygulamada zayıf olduğunu söylüyor; Meta dokümanı da install optimizasyonunu geniş erişim/düşük yükleme maliyeti için, event optimizasyonunu ise belirli eylem yapacak kişiler için tarif ediyor. Ancak kanıtların çoğu genel bilgi veya başka yaratıcıdan aktarma; ajans/kurs satan kaynaklar var, sayısal veri gösterilmiyor. Hangi derin olayın seçileceği (trial, purchase, değer bazlı) bütçeye bağlı: düşük bütçede purchase için yeterli olay çıkmayabilir.


*Kendi verinle test:* İki kampanya aç: biri Install, biri StartTrial optimizasyonlu; aynı kitle ve bütçe, en az 7–14 gün. Başarı ölçütü: ödeyen müşteri başına maliyet (CAC) ve deneme başına maliyet.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “display mobile app install ads to people likely to take a specific action in your app”

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=389) @6:29 · Sub Club by RevenueCat · 2026-09-15 · *supports* · kaynak: başka içerik üreticisi
  > The common failure case is targeting for installs because they look cheap.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=791) @13:11 · Gui Costa · 2026-07-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > It doesn't necessarily mean that people downloaded this and created an account and paid for it.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1431) @23:51 · App Leaders by Adapty · 2026-09-11 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > Please do not use cost gaps. Do not use cost per purchase optimizations.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=238) @3:58 · Benji · 2026-10-20 · *qualifies* · kaynak: genel bilgi
  > Most likely if you're running a hard paywall consumer app, you want to optimize for purchase.

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=459) @7:39 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > if you optimize for installs, you might get a cheap install, maybe a dollar to $2, but nobody pays.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=389) @6:29 · Sub Club by RevenueCat · 2026-09-15 · *supports* · kaynak: başka içerik üreticisi
  > I haven't seen a case where an install optimized campaigns got anywhere near the performance of a deeper funnel event

### <a id="k5"></a>K5 · sağlam · güven 0.81

Uygulama tanıtımı kampanyalarında her reklam setinde Meta'nın test edebileceği yeterli sayıda kreatif (yaklaşık 5–10+, hatta 20+) bulunmalıdır.


*Değerlendirme:* Kaynaklar eşik konusunda net biçimde ayrışıyor: 3-7, en az 5, en az 10 ve 20+ gibi farklı sayılar var. Hiçbiri yayımlanmış bir veri göstermiyor; çoğu genel bilgi ya da sözlü deneyim, ikisi kurs/ajans satıyor. Meta dokümanları reklam seti başına sabit bir sayı vermiyor, yalnızca yüksek kreatif hacmini ve düzenli yenilemeyi öneriyor. Yorumlarda 10 kreatifin yalnızca 3'üne harcama gittiği ve gayrimenkulde 10+ kreatifin mümkün olmadığı belirtiliyor. Bu da "en az 10" eşiğini zayıflatıyor.


*Kendi verinle test:* İki kampanya kur ya da sırayla çalıştır: A'da 5 kreatif, B'de 10-12 kreatif. Bütçe, hedef ülke ve kitle aynı olsun. En az 7-10 gün çalıştır (kampanya başına ~50 optimizasyon olayı). Başarı ölçütü: StartTrial başına maliyet ve harcama alan kreatif sayısı. Ardından ödeyen müşteri başına maliyete (CAC) bak.


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns](https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1403) @23:23 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > you want to make sure that you have at least 10 ads per ad set

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=79) @1:19 · Burak Mermi · 2026-02-16 · *qualifies* · kaynak: platform dokümanı · çıkar çatışması: sells_course
  > More than 20 creatives, for example. This is because meta describes and recommends it this way.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1097) @18:17 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: kendi tecrübesi
  > Adset'in içerisinde de en az 5 tane

- [1500+ B2B lead Meta Ads-ből ~620 Ft/lead kampánnyal [ESETTANULMÁNY]](https://youtu.be/OW74dQjjOBo?t=242) @4:02 · Fluid Digital · 2025-12-16 · *qualifies* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > 21 különböző kreatívot használtunk híret és sorozatonként, amelyek mindegyike, három különböző méretben volt létrehozva

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=544) @9:04 · Menaf Avcı · 2025-12-28 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > Her reklam setinin altına 3-7 arası kreatif ekleyebiliriz.

### <a id="k6"></a>K6 · sağlam · güven 0.97

Gerçekten bir mobil uygulamanız varsa, uygulamayı tanıtmak için Meta'nın Uygulama Tanıtımı (App Promotion / Advantage+ uygulama kampanyası) hedefi kullanılır; iOS için ilgili iOS 14+ ayarları dikkate alınır.


*Değerlendirme:* Beş üye de temelde aynı şeyi söylüyor: uygulaman varsa Uygulama Tanıtımı hedefi, yoksa kullanma. Hepsi genel bilgiye dayanıyor, bağımsız uygulayıcı verisi yok; ders/ajans satışı çıkar çatışması var ama iddia sıradan bir platform mekaniği olduğu için ağırlığı düşürmüyor. Meta'nın yardım sayfaları Advantage+ uygulama kampanyasının uygulama kurulumu/tanıtımı için olduğunu doğruluyor. Ancak Gui Costa abonelikte satış kampanyası öneriyor; bu, B2B abonelik/StartTrial hedefi için önemli bir koşul. Tam sayfa alıntısı doğrulanamadığı için alıntı verilmedi.


*Kendi verinle test:* Aynı bütçeyle (örn. günlük 20–30 $) 7–10 gün boyunca Advantage+ uygulama kampanyası (kurulum/uygulama olayı) ile Satış/Dönüşüm hedefli kampanyayı A/B bölünmüş teste koyun; başarı ölçütü StartTrial başına maliyet ve ödeyen müşteri başına maliyet (CAC).


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns](https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1093) @18:13 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > You absolutely have to turn iOS 14 plus on

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1015) @16:55 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Uygulama tanıtım reklamlarında biz mobil uygulamamız varsa bunların tanıtımını yapıyoruz.

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=609) @10:09 · Gui Costa · 2026-07-25 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > always that you create iOS campaigns you put app install campaigns as the goal.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=742) @12:22 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > If you've got an app, obviously the option to use. If you don't, don't use it.

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=703) @11:43 · Nida Yıldırım · 2026-04-29 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Yani bu uygulama tanıtımını kullanmanız için çok kullanan bir kampanya türü değildir.

### <a id="k7"></a>K7 · sağlam · güven 0.82

Meta (uygulama) kampanyalarını ölçeklerken bütçe kademeli artırılmalı: adım başına yaklaşık %10–20, 2–4 günde bir (küçük bütçede daha seyrek); daha büyük veya sık artışlar öğrenmeyi/teslimatı bozabilir.


*Değerlendirme:* Altı üye de aynı yönde: kademeli artış, yaklaşık %10–20 ve birkaç günde bir. Meta dokümanı büyük bütçe değişikliklerinin önemli düzenleme sayılıp öğrenmeyi sıfırlayabileceğini söylüyor ama %20 gibi bir eşik vermiyor; yani rakam sektör pratiği. Üyeler ya Meta'yı tekrar ediyor ya da genel bilgi/kişisel deneyim; bağımsız veri gösterilmiyor. Ben Heath'in 7–10 gün önerisi kurs/ajans satan birinden ve küçük bütçe için, daha muhafazakâr.


*Kendi verinle test:* Öğrenmeden çıkmış bir kampanyada 7–10 gün boyunca her 3 günde bir %15 artış uygulayın; benzer ikinci bir kampanyada tek seferde %40–50 artış yapın. Deneme başına maliyet (StartTrial CPA) ve harcama kararlılığını karşılaştırın; en az 10 gün.


- Resmi kaynak: [https://www.facebook.com/business/help/942374239243867](https://www.facebook.com/business/help/942374239243867) — “Changes to bid strategy or budget may also be significant, but it depends on the magnitude of the change.”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > %20'nin üstüne çıktığında learning'i bozuyor hakikaten.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1947) @32:27 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > Bütçe arttırımını 3-4 günde bir 2-3 günde bir hadi %10-15 şeklinde arttırmanız gerekiyor.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=635) @10:35 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > A good rule is about 20% every 48 hours.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > 3-4 günde bir %20'nin altında bu bütçe artışını yapabilirsiniz.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=314) @5:14 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > CBO kampanyamızın bütçesini %15-20 olacak şekilde 3 günde bir, 4 günde bir artırarak ölçekleyebiliyorduk.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=229) @3:49 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > So decide, I'm going to adjust my campaigns no more than once every seven days or 10 days.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=314) @5:14 · Burak Mermi · 2026-07-06 · *supports* · kaynak: genel bilgi
  > her gün bütçesini artırırsanız, burada bu kampanyanın stabil ilerlemesini bozabilirsiniz.

### <a id="k8"></a>K8 · sağlam · güven 0.96

Meta'nın optimizasyonu (öğrenme aşamasından çıkış) reklam seti başına haftada yaklaşık 50 optimizasyon eventine ihtiyaç duyar; bazı üreticiler bunun yerine günde ~5 veya ~10 event der.


*Değerlendirme:* Meta'nın yardım sayfası, bir reklam setinin son önemli düzenlemeden sonraki bir haftada yaklaşık 50 optimizasyon eventi alması gerektiğini söylüyor. Dört üretici bu rakamı tekrarlıyor ama hiçbiri ekranda veri göstermiyor; çoğu dokümandan veya diğer üreticilerden aktarıyor. Günde 5 (≈35/hafta) ve günde 10 (≈70/hafta) iddiaları 50/hafta eşiğine yakın ama farklı bir kural olarak sunuluyor. Bu rakamlar kesin bir sınır değil, öğrenme aşaması için bir kılavuzdur.


*Kendi verinle test:* Düşük bütçede StartTrial yerine install optimizasyonu ile 2 hafta, sonra StartTrial ile tek reklam setinde 2 hafta çalıştırın; 'Learning limited' durumu ve deneme başına maliyeti (cost per trial) karşılaştırın.


- Resmi kaynak: [https://www.facebook.com/business/help/269269737396981](https://www.facebook.com/business/help/269269737396981) — “Once it gets 50 events, it will move from learning limited to active.”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=1076) @17:56 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > Meta needs at least 50 events per week.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1478) @24:38 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > Dediğim gibi haftada en az 50 event gerekiyor.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1018) @16:58 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > haftada yani 7 gün içerisinde 50 tane bu optimizasyon eventini toplarsa

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=75) @1:15 · Sub Club by RevenueCat · 2026-09-15 · *supports* · kaynak: başka içerik üreticisi
  > The ballpark is always like 50, 50 a week.

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=774) @12:54 · App Leaders by Adapty · 2025-12-26 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sponsored
  > you need to give at least a day five events to optimize for meta, for a campaign properly.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1431) @23:51 · App Leaders by Adapty · 2026-09-11 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > I want to see 10 events per day in at least one ad set. Sorry, in all ad sets, in all your campaigns.

### <a id="k9"></a>K9 · şüpheli · güven 0.38

Küçük bütçede hesap yapısını sade tutmak (az reklam seti, her sette birkaç reklam) gerekir; çok sayıda minik reklam setine bölmek, setlerin öğrenmeden çıkması için yeterli dönüşüm toplamasını engeller.


*Değerlendirme:* İki kaynak (Ben Heath, Burak Mermi C20) tek/az reklam setini savunurken, Gui Costa ve Burak Mermi C10 aynı bütçe bandında ayrı, çok küçük bütçeli test setlerini öneriyor. Ayrıca Burak Mermi'nin kendi yorumunda 500 TL için ABO test + CBO ölçekleme önerdiği görülüyor; yani aynı kişi bile test ve ölçekleme aşamasını ayırıyor. Resmi sayfa içerik vermediği için doğrulanamadı; genel bilgi (haftada ~50 olay) konsolidasyonu destekler ama test amaçlı bölmeyi çürütmez. Konu B2B abonelik uygulaması StartTrial olduğundan olay hacmi zaten düşük; bu yüzden konsolidasyon daha mantıklı görünüyor.


*Kendi verinle test:* 14 gün boyunca aynı toplam bütçeyle iki yapıyı karşılaştırın: (A) tek reklam seti, 3-4 kreatif; (B) kreatif başına ayrı reklam seti. Başarı ölçütü: StartTrial başına maliyet ve ödeyen müşteri başına maliyet (CAC); her kolda en az ~30-50 StartTrial hedefleyin.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700](https://www.facebook.com/business/help/112167992830700) — “”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=151) @2:31 · Gui Costa · 2026-07-25 · *contradicts* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > we were just putting $2 per ad set and we were running for United States and Europe

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=707) @11:47 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Her adsetin altına en fazla 5 tane reklam koyun. Adsetlerin altına minimum bütçe koyun ki bütün o adsetler para harcayabilsin gibi.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=391) @6:31 · Burak Mermi · 2026-07-06 · *contradicts* · kaynak: başka içerik üreticisi
  > sepete ekleme başına maliyet düşükse buradaki reklamı başarılı olarak nitelendirip CBO kampanyasına atıyorsunuz.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1525) @25:25 · Ben Heath · 2026-02-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > So let's say we have five ad sets and we're generating 20 conversions a week. Well, that's four conversions per ad set on average.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1795) @29:55 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > eğer bütçeniz 2000 TL'nin altındaysa yani çok fazla bütçeniz yok

### <a id="k10"></a>K10 · muhtemel · güven 0.77

Meta dağıtımı, optimize edilen olaydan ve kullanıcı tepkilerinden öğrenir; tıklama/trafik veya etkileşim için optimize etmek, tıklayan ya da etkileşen ama dönüşmeyen kişileri bulma eğilimindedir, bu yüzden optimizasyon olayı daha derin dönüşüm (ör. deneme/satın alma) olmalıdır.


*Değerlendirme:* Trafik/tıklama optimizasyonunun düşük dönüşümlü kitle bulduğu fikri birbirinden bağımsız iki Ben Heath videosunda ve genel sektör deneyiminde tutarlı; ancak ikisi de aynı kişi ve kurs/ajans satıyor, veri gösterilmiyor. Deniz Pulcu'nun "Meta yeni insanlara göstermez" iddiası ve AdConversion'un "etkileşim doğrulama sinyalidir" iddiası mekanik olarak kanıtsız ve kısmen birbiriyle çelişen çerçeveler. RevenueCat kanalı "etkileşim kalite puanını yükseltir" diyor ama bu başka bir yaratıcıdan aktarım. Resmi doküman bu mekanizmayı bu biçimde doğrulamıyor; yalnızca optimizasyon olayına göre dağıtım yapıldığı genel ilkesi var.


*Kendi verinle test:* Aynı kreatiflerle iki kampanya kur: biri StartTrial (uygulama olayı) optimizasyonlu, diğeri link click/trafik optimizasyonlu; eşit bütçeyle en az 7-14 gün çalıştır. Başarı ölçütü: deneme başına maliyet ve denemeden ödemeye dönüşen müşteri başına maliyet (CAC).


- [Meta'nın Gizli Kuralı: Reklam Maliyetlerini Düşüren Yapı](https://youtu.be/PwokUZ0NB9Q?t=879) @14:39 · Deniz Pulcu · 2026-07-29 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Tıklama geliyor ama satış gelmiyor. Metada ne oluyor? Yeni insanlara gitmiyor.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=992) @16:32 · Ben Heath · 2026-02-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > If you say you want traffic, they're going to find really clicky people. Those people won't necessarily go on and convert.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=667) @11:07 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > Meta is very good at finding people that are likely to click. But those people don't necessarily go on to convert.

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=776) @12:56 · AdConversion · 2025-11-12 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > the people that are engaging with your ads, that are responding with your ads, these are all signs of validation to meta's algorithm

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=310) @5:10 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · kaynak: başka içerik üreticisi
  > meta loves engagement and more engagement means a high quality score

### <a id="k11"></a>K11 · sağlam · güven 0.94

Optimizasyon olayı hacme göre seçilmelidir: satın alma/satış olayı ancak Meta'nın öğrenmesi için yeterli sayıda (haftada yaklaşık 50) olay üretiyorsa seçilmeli; aksi halde olay başına daha ucuz olan, hunide daha üstteki bir olay (kayıt, deneme) seçilmelidir.


*Değerlendirme:* Dört kaynak da aynı mantığı söylüyor: yeterli hacim varsa derin olay, yoksa üst huni olayı. Meta'nın öğrenme aşaması belgeleri de ad set başına son önemli düzenlemeden sonra haftada yaklaşık 50 optimizasyon olayı gerektiğini söyler. Shatalin'in "iki haftada 50" eşiği belgedeki "haftada 50" ile tam örtüşmüyor (daha gevşek) ve kaynağı yok. Kaynakların hepsi genel bilgiye dayanıyor, ilk elden veri gösterilmiyor; ama belgeyle uyumlu.


- Resmi kaynak: [https://www.facebook.com/business/help/269269737396981](https://www.facebook.com/business/help/269269737396981) — “Meta suggests choosing a more frequent optimization event, such as add to cart instead of purchase”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=80) @1:20 · Denis Shatalin · 2025-12-29 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > If you can get 50 sales events in a two-week time frame, you can go for sales

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2266) @37:46 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you cannot send a signal that it's not happening quite often and that you cannot afford it

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1558) @25:58 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > My preference would be to go for purchases provided you're generating enough purchases for Meta to be able to learn.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1335) @22:15 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: genel bilgi
  > purchase olması için cost daha pahalı olacak elbette

### <a id="k12"></a>K12 · sağlam · güven 0.80

Reklam hesabı oluşturulurken para birimi ve saat dilimi doğru seçilmelidir; sonradan düzenlenemez (değiştirmek fiilen yeni hesap açmak demektir).


*Değerlendirme:* Dört video de aynı kurulum tavsiyesini veriyor; Meta yardım sayfalarının arama özetine göre para birimi/saat dilimi değişikliği mevcut hesabı düzenlemez, yeni hesap açar ve eski hesap kapanır. Bu yüzden "kalıcı" ifadesi biraz abartılı, "değiştirmek çok zor" ise daha doğru. Kanıtların hepsi genel bilgi; bağımsız uygulayıcı verisi yok, ancak iddia düşük riskli ve resmi davranışla uyumlu. Sayfanın gövde metnine ulaşamadığım için birebir alıntı veremedim.


- Resmi kaynak: [https://www.facebook.com/business/help/291404291014138](https://www.facebook.com/business/help/291404291014138) — “”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=458) @7:38 · Aprendamos Marketing · 2026-01-13 · *qualifies* · kaynak: genel bilgi
  > esa se va a quedar permanentemente en tu cuenta publicitaria

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=397) @6:37 · Nida Yıldırım · 2026-04-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Sonrasında buradaki saat dilimini kesinlikle değiştirelim.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=472) @7:52 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Para birimi kısmı çok kritik. Türkiye'de reklamlarınızı yayınlıyorsanız ve TL ile ödeme yapmak istiyorsanız burada İstanbul'u ve Türk lirasını seçmeniz gerekiyor.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=222) @3:42 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > Make sure you get these right. If you don't, uh it's very difficult to change them uh later on.

### <a id="k13"></a>K13 · muhtemel · güven 0.78

Meta uygulama kampanyalarında abonelikli uygulamalar için, ham "deneme başladı" yerine deneme başladıktan yaklaşık 1–3 saat sonra hâlâ aktif olan "nitelikli deneme" olayına optimizasyon yapmak, hemen iptal edenleri eleyerek daha iyi bir sinyaldir.


*Değerlendirme:* Kaynaklar aynı yönde: anlık iptalleri filtreleyen gecikmeli bir olay göndermek. Ancak hepsi aynı ekosistemden (RevenueCat, Adapty) geliyor, çıkar çatışması var ve ekranda sonuç verisi yok; yalnızca Adapty'nin client_data iddiası zayıf da olsa pratik gözleme dayanıyor. Mantık makul (Meta iptal edilen denemeyi ayırt edemez), ama sinyal hacmi düşük bütçede sorun olabilir; bu yüzden koşullu.


*Kendi verinle test:* Aynı bütçeyle iki ad set/kampanya aç: biri "StartTrial", diğeri "nitelikli deneme" (1–2 saat sonra aktif) olayına optimize olsun. En az 2 hafta veya her kolda ~50 olay boyunca çalıştır; başarı ölçütü: ödeyen müşteri başına maliyet (CAC) ve denemeden ücretliye dönüşüm oranı; nitelikli denemenin olay hacmi öğrenmeye yetmezse pencereyi kısalt.


- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1249) @20:49 · RevenueCat · 2026-09-12 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > we check if after two hours the user didn't cancel the event okay if the trial started is still active then we will count that as a trial qualified

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1416) @23:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: müşteri verisi
  > Bir saat ya da iki saat içerisinde iptal etmeyen kullanıcıların sinyalini metaya gönderelim.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1409) @23:29 · RevenueCat · 2026-09-12 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > so you should know that at least you should drop 25 to 30 percent of the data to make sure that it's like high quality

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1097) @18:17 · App Leaders by Adapty · 2025-12-26 · *supports* · kaynak: genel bilgi · çıkar çatışması: sponsored
  > You can create a custom event, which says, for instance, trial started, but not canceled in the same hour.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1172) @19:32 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > a 30 second cancellation from a trial started looks exactly like a six month subscriber for meta

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1185) @19:45 · App Leaders by Adapty · 2026-09-11 · *supports* · kaynak: başka içerik üreticisi · çıkar çatışması: sells_agency_services
  > We are just sending the signals if the user didn't cancel the trial in three hours.

### <a id="k14"></a>K14 · sağlam · güven 0.84

Yeni kreatifleri ABO'da (sabit reklam seti bütçesiyle) test edip kazananları CBO (Advantage kampanya bütçesi) kampanyasına taşıyarak ölçeklemek en iyi yaklaşımdır.


*Değerlendirme:* ABO'da test, CBO'da ölçekleme önerisi üç bağımsız kanalda tutarlı ve bir izleyici yorumu da deneyimsel olarak doğruluyor; çelişen kaynak yok. Ancak Benji genel bilgiye dayanıyor, Gürkanzone kurs satıyor ve e-ticaret bağlamında, Burak Mermi'nin oranları sadece sözlü. Meta dokümanı yalnızca ABO/CBO mekaniğini anlatıyor, test yapısı hakkında sessiz; bu yüzden koşullu bir pratik kabul olarak görülmeli.


*Kendi verinle test:* Aynı kreatifleri iki yapıda 10–14 gün çalıştırın: (A) ABO'da her sete bir kreatif, kazananı CBO'ya taşıma; (B) doğrudan tek CBO/Advantage+ app kampanyası. Başarı ölçütü: deneme (StartTrial) başına maliyet ve ödeyen müşteri başına maliyet (CAC); sete en az ~50 optimizasyon olayı hedefleyin.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “you should provide budgets for all ad sets under the campaign.”

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=1297) @21:37 · Gürkanzone · 2026-08-15 · *qualifies* · kaynak: kendi tecrübesi · çıkar çatışması: sells_course
  > Bak tek bir set içerisinde 10 tane kreatif var.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > An ABO gives you control over how much budget goes into each ad set.

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=1373) @22:53 · Gürkanzone · 2026-08-15 · *qualifies* · kaynak: kendi tecrübesi · çıkar çatışması: sells_course
  > Hem burada ölçekliyoruz. Hem de gidip CBO'nun içerisine atıyoruz.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > Once something clearly works, move it out of testing and into a CBO campaign.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=700) @11:40 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > orta bütçelerde %28 çalışma oranı, yüksek bütçelerde ise %33 çalışma oranıyla

### <a id="k15"></a>K15 · muhtemel · güven 0.78

Meta kampanya ve reklam performansı, 1–2 günlük verilere tepki vermek yerine yaklaşık 7 günlük pencerelerde değerlendirilmeli (ör. kreatifler 1–2 günlük sonuçla kapatılmamalı).


*Değerlendirme:* Dört üye de aynı öneriyi yapıyor ve hiçbiri karşı çıkmıyor; ancak üçü genel bilgi/platform dokümanı tekrarı, yalnızca biri kişisel deneyim ve hiçbirinde ekranda veri gösterilmiyor. Meta yardım sayfaları 7 günlük tıklama ilişkilendirmesinin varsayılan olduğunu söylese de (sayfa içeriği alınamadı), "7 gün bekle" kuralını doğrudan öneren bir ifade bulunamadı. Düşük bütçeli StartTrial kampanyasında günlük veri çok seyrek olduğundan 7 gün mantıklı bir kural; ancak bu bir sezgisel yöntemdir, resmi eşik değil.


*Kendi verinle test:* İki benzer reklam setinden birini 3. günde, diğerini 7. günde değerlendir; en az 14 gün boyunca deneme başına maliyet (CPA-StartTrial) ve ödeyen müşteri maliyetini (CAC) karşılaştır.


- Resmi kaynak: [https://www.facebook.com/business/help/304909959680406](https://www.facebook.com/business/help/304909959680406) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=627) @10:27 · Denis Shatalin · 2025-12-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > I typically check in on results every seven days.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1490) @24:50 · Burak Mermi · 2026-07-06 · *supports* · kaynak: platform dokümanı
  > Meta'nın 7 günlük dönüşüm penceresi kuralını unutmayın.

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=774) @12:54 · Mark Builds Brands · 2026-05-11 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > Look at seven days. Look at the most amount of ads that you can.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2023) @33:43 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > bir kreatifi kapatıp kapatmama kararını 1 günlük 2 günlük sonuçlara göre kesinlikle vermemeniz gerekiyor.

### <a id="k16"></a>K16 · doğrulanamaz · güven 0.61

Meta reklamları B2B SaaS işletmelerine, ajansların bildirdiği müşteri sonuçlarına göre yaklaşık 3x–6x arasında pozitif bir reklam getirisi sağlayabilir.


*Değerlendirme:* Dört üye de ajans veya topluluk satan kişilerden geliyor ve hiçbiri ekranda doğrulanabilir veri göstermiyor. Denis'in 6x değeri ilk ay MRR'ının 3 aya projeksiyonuyla hesaplanmış, yani gerçekleşmiş nakit getirisi değil. Alessandro'nun "en az 3x" iddiası genel bilgiye dayanıyor ve satış vurgusu taşıyor. Ben Heath ise 3.2x'i yalnızca büyük ölçekte ve ajans verisi olarak sözlü anlatıyor. Bunlar bağımsız uygulayıcı kanıtı sayılmaz ve düşük bütçeli StartTrial odaklı uygulama kampanyasına doğrudan uygulanamaz.


*Kendi verinle test:* Kendi panelinizde 4–6 hafta düşük bütçeyle kampanya çalıştırın. Deneme başına maliyet, denemeden ödemeye dönüşüm oranı ve gerçekleşen ilk 3 aylık gelirle CAC'yi hesaplayarak gerçek getirinin 3x'e ulaşıp ulaşmadığına bakın.


- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=80) @1:20 · Denis Shatalin · 2025-12-29 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services, community_paid
  > Bilal, one of my clients, turned 3.1k in ad spend into 6.3k MRR within his first month

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=80) @1:20 · Denis Shatalin · 2025-12-29 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services, community_paid
  > This means a nice 6x return on his ad spend.

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=1063) @17:43 · Alessandro Cutri · 2026-06-04 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > put $1 in and get $3 out at a minimum

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1220) @20:20 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > We will also show businesses that get a 3.2x return on ad spend, but have done so at scale and that's really profitable

### <a id="k17"></a>K17 · muhtemel · güven 0.67

Abonelikli uygulamalarda paywall'u onboarding akışına koymak (deneme teklifi ve bildirim izni ekranlarıyla birlikte) deneme başlangıçlarını artırır; ancak denemeden ödemeye dönüşüm ayrıca izlenmelidir.


*Değerlendirme:* Üç üye yön olarak paywall/onboarding değişikliğinin deneme başlangıcını artırdığını söylüyor, ancak rakamlar sözlü, belirsiz ("20% or 30%" gibi) ve hepsi ajans/kurs satan kaynaklardan. Dördüncü üye genel bilgi olarak sert paywall'un deneme sayısını artırdığını ama denemeden ödemeye oranın düşebileceğini belirtiyor; bu da iddiayı koşullu yapıyor. Meta dokümanları uygulama içi paywall tasarımı hakkında bir şey söylemiyor, yani bu Meta reklam mekaniği değil uygulama içi dönüşüm taktiği.


*Kendi verinle test:* Yeni kullanıcıları ikiye bölerek A/B testi yapın: onboarding içinde paywall olan ve olmayan akış. En az 2 hafta veya her kolda ~100 deneme başlangıcı sonrası deneme başlangıcı oranını, deneme→ödeme oranını ve ödeyen müşteri başına maliyeti (CAC) karşılaştırın.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1474) @24:34 · Aazar Shad · 2026-04-02 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > free trial increased, I think it was like 20% or 30%

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=152) @2:32 · App Masters · 2026-06-09 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_course, sells_agency_services, sponsored
  > those two screens led to a 56% increase in trial activations

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=943) @15:43 · Gui Costa · 2026-07-28 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > We created a paywall in the onboarding process.

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=380) @6:20 · App Masters · 2026-06-09 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, sponsored
  > If you do a hard paywall, trial activations guaranteed will go up

### <a id="k18"></a>K18 · sağlam · güven 0.94

Abonelikli uygulamada Meta reklamlarına önce Meta SDK tabanlı dönüşüm kampanyalarıyla başlanmalı; MMP (ör. AppsFlyer) yanına ya da sonrasına eklenebilir ve daha iyi atıf verisi sağladığı söylenir.


*Değerlendirme:* İki üye (Benji, First Try) ilk kampanya için önce Meta SDK ile başlamayı öneriyor; Meta dokümanı da install takibi için SDK'yı zorunlu kılıyor, bu kısım tutarlı. MMP'nin "daha iyi atıf" verdiği ve web-to-app'in atıfı iyileştirdiği iddiaları genel bilgiye ve ajans satışı yapan bir kaynağa dayanıyor; dokümanlar MMP'yi SDK ile kıyaslamıyor. Hiçbir üye kendi ölçülmüş verisini göstermiyor, bu yüzden MMP üstünlüğü kanıtsız.


*Kendi verinle test:* MMP üstünlüğü için: SDK kampanyası çalışırken MMP'yi de bağlayıp 2-4 hafta boyunca aynı StartTrial ve ödeme olaylarını iki kaynakta karşılaştırın; başarı ölçütü, deneme başına maliyet ve CAC farkının MMP verisiyle ne kadar değiştiğidir.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/measuring/measuring-installs-and-in-app-conversions](https://developers.facebook.com/docs/app-ads/measuring/measuring-installs-and-in-app-conversions) — “The Facebook SDK is required to enable install tracking.”

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > First, implement the meta SDK, set up your important conversion events and start running SDK conversion campaigns right away.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=155) @2:35 · First Try · 2026-02-03 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > I recommend you to just use the Facebook SDK if this is your very first campaign.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *qualifies* · kaynak: genel bilgi
  > Understand a mobile measurement partner like AppSupplyer and AppStack will give you better attribution data compared to Metapixel.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1819) @30:19 · App Leaders by Adapty · 2026-09-11 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > If you share enough information through Cappy, you would get a better attribution to your meta campaigns on your MMP.

### <a id="k19"></a>K19 · muhtemel · güven 0.70

Bir kreatifi değerlendirmeden önce önceden belirlenmiş bir harcama eşiğine ulaşmasını bekleyin; hedef CPA'dan açıkça kötü olan kreatifleri bu eşikten sonra kapatın (eşik yaratıcıya göre yaklaşık 100–500 $ arasında değişiyor).


*Değerlendirme:* Dört üye de "önceden eşik belirle, açıkça kötüyse kapat" ilkesinde uyuşuyor, ancak rakamlar farklı (100 $, 500 $, 2.000 $) ve hiçbiri ekran verisiyle desteklenmiyor. Kaynaklar genel bilgi veya başka bir yaratıcıdan aktarım; Cravotta kurs sattığı için ağırlığı düşük. Meta dokümanları kreatif başına sabit bir harcama eşiği vermiyor; doğru eşik hedef CPA'ya ve öğrenme aşamasına bağlı.


*Kendi verinle test:* Hedef CPA'nızın (ör. StartTrial başına maliyet) 3 katını kreatif başına eşik olarak belirleyin. 2–3 hafta boyunca bu eşiğe ulaşan ve hedefin üzerinde kalan kreatifleri kapatın; kapatılanlarla bırakılanların toplam StartTrial başına maliyetini karşılaştırın.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1636) @27:16 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > I recommend spending at least a hundred dollars on each creative before you decide

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=310) @5:10 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · kaynak: başka içerik üreticisi
  > He would have killed that at like 2000 in ad spent.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=310) @5:10 · Sub Club by RevenueCat · 2026-09-15 · *supports* · kaynak: başka içerik üreticisi
  > I could tell it after 500 bucks.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=476) @7:56 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > And if it's clearly worse after enough spend, kill it.

### <a id="k20"></a>K20 · muhtemel · güven 0.67

Düşük bütçeli Meta reklamlarında reklamlar çalıştığı gün sayısına veya erken kayıplara göre değil, harcama miktarına göre değerlendirilmeli; harcamayı alan ve kazanan reklamlara odaklanılmalı, ancak erken harcama yoğunlaşması kısmen şans olabilir.


*Değerlendirme:* Üç üye de harcamayı temel alıp sayıya değil teslimat kararına bakmayı öneriyor, ancak hiçbiri veri göstermiyor; ikisi genel bilgi, biri başka bir yaratıcıdan aktarım. Üçüncü üye, erken harcama kazananının şans eseri olabileceğini söyleyerek öncekileri niteliyor. Resmî dokümanlar bu taktik konusunda açık bir şey söylemiyor; bu yüzden makul ama koşullu bir pratik kural olarak değerlendirildi.


*Kendi verinle test:* Aynı kampanyada harcama lideri 2–3 reklamı yeni bir kampanyada/ad sette tekrar çalıştır; en az 7 gün ve reklam başına ≥50 StartTrial olacak şekilde izle. Başarı ölçütü: deneme başına maliyetin ilk sonuca yakın kalması (±%25).


- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1094) @18:14 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Kayıplara odaklanmaktansa kazananlara odaklanmanın tekrar atlatmış olalım.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=476) @7:56 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > remember to judge ads by spend, not by days.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=231) @3:51 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · kaynak: başka içerik üreticisi
  > meta does some sort of a decision making around first five to 10,000 impressions.

### <a id="k21"></a>K21 · muhtemel · güven 0.64

Abonelikli uygulama/SaaS kampanyalarını ölçeklemek için ayda çok sayıda yeni reklam kreatifi test etmek gerekir; bunların yalnızca küçük bir kısmı (yaklaşık %5–10) ölçeklenen kazanan olur.


*Değerlendirme:* Üç kaynak da yönce aynı: yüksek kreatif hacmi ve düşük kazanan oranı. Ancak hepsi ajans/hizmet satan kanallardan geliyor, ekranda veri gösterilmiyor ve rakamlar (50 reklam, %5–10) kanıtsız sözlü tahmin. Meta'nın Andromeda sonrası kreatif çeşitliliği vurgulaması genel yönü destekliyor, ama düşük bütçeli hesaplarda ayda 50+ reklam gerçekçi değil.


*Kendi verinle test:* Aylık bütçenize uygun şekilde 4 hafta boyunca haftada 5–10 yeni kreatif test edin; her kreatifin deneme başına maliyetini (cost per trial) kaydedin. Hedef CPA'yı tutturan kreatif oranını hesaplayın; bu sizin gerçek 'kazanan oranınız' olur.


- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=2688) @44:48 · App Leaders by Adapty · 2026-09-11 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > I think the speed of creative production is a locomotive.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=919) @15:19 · Lorenzo Pravatà · 2026-03-26 · *qualifies* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > at least 50 new ads every month to just find one winner that actually scales the ad

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=934) @15:34 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > it's expected that around five to ten percent of the ads will reach uh this campaign

### <a id="k23"></a>K23 · sağlam · güven 0.94

Yayınla'dan sonra Meta reklamları gösterimden önce incelemeye girer; bu süre genelde yaklaşık 30 dakika ile bir gün arasındadır, yeni hesaplarda ve ilk reklamlarda daha uzun sürebilir.


*Değerlendirme:* Üç kanal da incelemenin varlığını ve genelde kısa sürdüğünü söylüyor; Meta belgesi de 24 saat içinde tamamlanmasının tipik olduğunu, uzayabileceğini belirtiyor. Üyeler bağımsız deneyim değil genel bilgi, ancak resmi belgeyle uyumlu. Yorumlardaki deneyimler (yeni hesapta 12-24 saat, bazen günler) "daha uzun sürebilir" kısmını destekliyor.


- Resmi kaynak: [https://www.facebook.com/business/ads/review-policy-guidelines](https://www.facebook.com/business/ads/review-policy-guidelines) — “While ad review is typically completed within 24 hours, it may take longer and ads can be reviewed again, including after they're live.”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=3850) @1:04:10 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > Normally takes about 30 minutes, but particularly with your first ads could take a while more.

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1166) @19:26 · Nida Yıldırım · 2026-04-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Bu birkaç saat olabilir, bir gün olabilir.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=2112) @35:12 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > yayınla butonuna tıkladıktan sonra reklamlarımız önce incelemeye değerlendirmeye giriyor.

### <a id="k24"></a>K24 · sağlam · güven 0.94

Meta reklam kreatiflerini test ederken önce birbirinden belirgin biçimde farklı konseptleri (kanca, format, açı) test edin; aynı reklamın küçük varyasyonlarını ancak kazanan konsept çıktıktan sonra inceltin.


*Değerlendirme:* Üç kanal da aynı öneriyi yapıyor ve Meta'nın kreatif çeşitlendirme (creative diversification) yaklaşımıyla ve Andromeda sonrası yaygın pratikle uyumlu. Ancak üyelerin ikisi genel bilgiye dayanıyor, biri kendi deneyimini sözlü anlatıyor; hiçbiri veri göstermiyor ve üçünün de kurs/ajans çıkarı var. Resmi sayfa çeşitliliği destekliyor ama "mikro varyasyonları test etmeyin" demiyor; bu kısım pratik çıkarımdır.


- Resmi kaynak: [https://www.facebook.com/business/ads/performance-marketing](https://www.facebook.com/business/ads/performance-marketing) — “Develop a variety of ad creative and enable AI to deliver the right message to the people most likely to be interested in it.”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=924) @15:24 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > We want to test out different concepts, right?

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=476) @7:56 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > When you start, don't mix five slightly different versions of the same ad.

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=389) @6:29 · AdConversion · 2025-11-12 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services, sells_course
  > we just test micro changes in our ads versus testing completely different look, feels, and concepts.

### <a id="k25"></a>K25 · sağlam · güven 0.94

Birden fazla reklam görselini/reklam setini tek kampanyada kampanya bütçesiyle (Advantage+ kampanya bütçesi/CBO) toplamak, Meta'nın harcamayı en iyi performans gösteren reklam setlerine/kreatiflere kaydırmasını ve dönüşüm verisinin birikmesini sağlar.


*Değerlendirme:* Bütçenin reklam setleri arasında performansa göre dağıtılması Meta'nın resmi sayfasıyla örtüşüyor; bu kısım platform mekaniği olarak sağlam. Ancak üç üye de genel bilgiye dayanıyor ve ajans/kurs satışı çıkar çatışması var; bağımsız uygulayıcı verisi yok. Kreatif düzeyinde "en iyisine kayar" iddiası ve "büyük bütçede hepsini tek ssette topla" önerisi dokümanda açıkça yazmıyor; Meta çoğu zaman bir kreatife aşırı yığılabiliyor ve diğerlerini denemeyebiliyor.


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/budget](https://www.facebook.com/business/ads/meta-advantage-plus/budget) — “Your budget, enabled by Meta AI, continuously distributes to ad sets with the best opportunities in real time throughout the course of your campaign.”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=761) @12:41 · Gui Costa · 2026-07-25 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > if you have a big budget I recommend you to put all the creatives in the same campaign or in the same ad set

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=817) @13:37 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > with campaign budget, the budget is set at the campaign level meaning that if you have multiple ad sets, budget will be distributed to those ad sets according to performance.

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=371) @6:11 · Sabri Suby · 2026-06-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you chuck them in a CBO, you let Facebook's AI do its thing and it's going to basically pivot the spend towards the creatives

### <a id="k26"></a>K26 · muhtemel · güven 0.63

Reklamlar sabit bir ikna yapısını izlemelidir (kanca/teklif, sorun/çözüm, sosyal kanıt, CTA; uygulama reklamlarında ise demo ve reklamla uyumlu App Store sayfası).


*Değerlendirme:* Üç üye de genel bilgiye dayanıyor, veri göstermiyor ve üçü de ajans/kurs satıyor; bu yüzden etkinlik iddiası olarak zayıf. Ortak çekirdek (erken kanca, teklif, kanıt, CTA) makul ve Meta'nın genel video önerileriyle (ilk saniyeler, net CTA) uyumlu, ancak sabit sıra veya tek yapı zorunluluğunu doğrulayan resmi bir kaynak bulunamadı. Yapılar B2B SaaS lead reklamları için tanımlanmış; düşük bütçeli StartTrial odaklı uygulama kampanyasına doğrudan aktarılabilirliği belirsiz.


*Kendi verinle test:* Aynı teklifle iki reklam hazırlayın: biri yapılandırılmış (kanca-teklif-kanıt-CTA), diğeri serbest biçimli. Eşit bütçeyle en az 7 gün veya her biri ~50 deneme olayı olana dek çalıştırın; başarı ölçütü deneme başına maliyet (StartTrial CPA) ve trial-to-paid oranı.


- Resmi kaynak: [https://www.facebook.com/business/help/711378409718185](https://www.facebook.com/business/help/711378409718185) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=474) @7:54 · Denis Shatalin · 2025-12-29 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > Direct offer, pain, solution, pain explained, solution explained, social proof, and CTA.

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=523) @8:43 · Alessandro Cutri · 2026-06-04 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you have some form of a hook, and then you also have an offer, you have proof that you can support that offer and you have a CTA

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=1000) @16:40 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > And at the end, make sure your App Store page connects with that ad.

### <a id="k27"></a>K27 · doğrulanamaz · güven 0.59

Küçük reklam bütçeli müşteriler, düşük veya sabit reklam harcamasıyla birkaç ay ile bir yıl içinde MRR/satışlarını katlayarak (3 kattan 14 kata kadar) artırdı.


*Değerlendirme:* Üç iddia da farklı dikeylerden (abonelik uygulaması, B2B SaaS, koçluk/bilgi ürünü) tek tek müşteri başarı hikâyeleridir ve hepsi ajans/kurs/araç satan kaynaklardan gelir. Ekranda doğrulanabilir veri yok; yalnızca sözlü rakamlar var. Seçilmiş en iyi vakalar olma ihtimali yüksek ve Meta uygulama tanıtımı (StartTrial) konusuna doğrudan genellenemez.


- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1107) @18:27 · App Leaders by Adapty · 2026-09-11 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > They tripled their MRR.

- [How to build a $100k MRR B2B SaaS business with ads](https://youtu.be/NMl7-u2UaRk?t=0) @0:00 · Denis Shatalin · 2025-11-03 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services, community_paid
  > one of my recent clients went from 10k to 140k in MRR in less than a year on just a 3k a month ad budget

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2962) @49:22 · Ben Heath · 2026-01-06 · *qualifies* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > from 30 euros a day ad spend to a 100K month in sales in just 3 months

### <a id="k28"></a>K28 · sağlam · güven 0.94

Küçük bütçeyle yeni bir uygulama/dönüşüm kampanyasına başlarken varsayılan en yüksek hacim (en düşük maliyet) teklif stratejisi kullanılmalı; gerçek maliyetler öğrenilene kadar sonuç başı maliyet hedefi veya teklif sınırından kaçınılmalıdır.


*Değerlendirme:* Üç farklı kanal aynı başlangıç tavsiyesini veriyor; Meta'nın yardım sayfaları da en yüksek hacmin varsayılan olduğunu, teklif sınırının ise sonuç sayısını kısıtlayabileceğini belirtiyor (arama özetine göre; sayfa gövdesi alınamadığı için birebir alıntı yok). Üçü de ekran verisi olmadan genel bilgiye dayanıyor ve ajans/eğitim satıyor, ancak tavsiye resmi dokümanla örtüşüyor ve karşıt görüş yok. Küçük bütçede kısıtlayıcı teklif stratejisi öğrenme ve teslimatı zorlaştırdığı için makul.


- Resmi kaynak: [https://www.facebook.com/business/help/317364032619502](https://www.facebook.com/business/help/317364032619502) — “”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1038) @17:18 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > Highest volume is the default. That's exactly what I want to go with here because that will determine how Meta optimizes the campaign.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1084) @18:04 · First Try · 2026-02-03 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > I advise you to stick to highest volume or value because you are looking to understand the costs

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1859) @30:59 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Bitcap koymayın derim. Çünkü siz atıyorum küçük bütçeniz de zaten en ucuz cost per purchase'ı alacaksınızdır.

### <a id="k29"></a>K29 · muhtemel · güven 0.65

Organik olarak iyi performans gösteren içerikler (TikTok, Instagram Reels, YouTube) Meta reklamı olarak yeniden kullanıldığında da çoğunlukla iyi çalışır; organik performans reklam kreatifi için faydalı bir ön testtir.


*Değerlendirme:* Üç farklı kanal aynı taktiği öneriyor ve hepsi kendi deneyimine ya da müşteri verisine dayanıyor; ancak hiçbirinde ekranda gösterilen veri yok ve üçü de ajans/kurs satıyor. Meta'nın resmi dokümanları organik performansın reklam performansını öngördüğü konusunda sessiz. Taktik mantıklı ama garanti değil; organik beğeni ile deneme başlatma (StartTrial) dönüşümü aynı şey olmadığı için doğrulanması gerekir.


*Kendi verinle test:* Son 30 günde organikte en yüksek etkileşimi alan 3 videoyu, aynı kitle ve bütçeyle 3 yeni (organiği olmayan) kreatifle yan yana reklam olarak çalıştırın; en az 7 gün veya her kreatif için ~50 deneme başlatma sonrası deneme başına maliyeti (cost per trial) karşılaştırın.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/threads-ads/creation/use-posts-as-ads](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ad-creative/threads-ads/creation/use-posts-as-ads) — “Existing Threads organic posts cannot be promoted as ads.”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1090) @18:10 · Aazar Shad · 2026-04-02 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > the TikTok organic videos that go viral in TikTok, if we use them in meta, it's also like they're winner ads.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1068) @17:48 · Ben Heath · 2026-02-20 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > the ones that get significantly more engagement than others, you can take those, add a five, 10 second call to action to the end

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=445) @7:25 · Sabri Suby · 2026-06-12 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > I'm taking that winning creative and then I'm just running that as an ad because I already know that that content bangs organically

### <a id="k30"></a>K30 · sağlam · güven 0.94

Uygulama kampanyalarında yorgunluğu önlemek ve sürekli kazanan reklam havuzu oluşturmak için her hafta yeni kreatifler yayınlanmalı (yeni açılar test edilmeli, zayıflar durdurulmalı, kazananlar ölçeklenmeli).


*Değerlendirme:* Üç üye de aynı genel tavsiyeyi veriyor, ancak hepsi genel bilgiye dayanıyor, kanıt göstermiyor ve ajans/hizmet satıyor; bağımsız uygulayıcı verisi yok. Meta'nın Advantage+ app önerisi yenilemeyi "ayda birkaç kez" olarak tanımlıyor, yani yönün doğru olduğunu ama "her hafta" ritminin evrensel bir kural olmadığını gösteriyor. Düşük bütçede haftalık yeni kreatif, öğrenme verisini bölebilir ve üretim maliyeti yaratabilir. Not: sayfa gövdesi fetch ile alınamadı, alıntı arama sonucundan geliyor.


*Kendi verinle test:* Dört hafta boyunca iki kollu deneme: birinde her hafta 2-3 yeni kreatif ekle, diğerinde iki haftada bir ekle. Başarı ölçütü: deneme başına maliyet (cost per StartTrial), frekans ve kreatif başına harcama dağılımı; en az 30-50 deneme birikene kadar sürdür.


- Resmi kaynak: [https://www.facebook.com/business/help/711378409718185](https://www.facebook.com/business/help/711378409718185) — “In order to maintain the best performance for your ads, we recommend that you upload a high volume of creative assets and refresh them a few times a month to avoid creative fatigue.”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=686) @11:26 · Gui Costa · 2026-07-25 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Be launching every week new creatives so you can start you can test more angles

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=934) @15:34 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > don't forget to keep pushing ads every single week that's a really important thing

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=148) @2:28 · Sabri Suby · 2026-06-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > dedicate one hour per week where you take your winning offer, your winning product or service

### <a id="k31"></a>K31 · muhtemel · güven 0.67

Meta'da hedeflemeyi geniş tutmak (ör. tek ülke) ve dar ilgi alanı/kitle segmentasyonundan kaçınmak, karmaşık segmentasyondan daha iyi sonuç verir.


*Değerlendirme:* Üç kaynak da geniş hedeflemeyi öneriyor, ancak üçü de kurs/ajans satıyor ve kanıt göstermiyor; RevenueCat üyesi genel bilgiye dayanıyor. Mark Builds Brands e-ticaret dönüşüm kampanyasından konuşuyor, abonelikli B2B uygulama deneme kampanyası için doğrudan kanıt değil. Resmi uygulama reklamı hedefleme sayfası konuya girmiyor. Andromeda sonrası geniş hedefleme yaygın tavsiye, ama sonuç hesap ve sinyal kalitesine bağlı.


*Kendi verinle test:* Aynı bütçeyle iki Advantage+ app kampanyası kur: biri tek ülke tamamen geniş, diğeri B2B ilgi alanı/iş unvanı önerili. En az 7–10 gün veya kolu başına ~50 StartTrial olana kadar çalıştır; başarı ölçütü deneme başına maliyet ve ödeyen müşteri başına maliyet (CAC).


- Resmi kaynak: [https://developers.facebook.com/documentation/app-ads/targeting](https://developers.facebook.com/documentation/app-ads/targeting) — “”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=779) @12:59 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > just be really broad just like i mean you can do one country but don't like start using audience segmentations

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=152) @2:32 · Mark Builds Brands · 2026-05-11 · *qualifies* · kaynak: kendi tecrübesi · çıkar çatışması: sells_course, community_paid
  > I literally just still run completely broad and most high scale advertisers that I speak to, they're doing something relatively similar

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2147) @35:47 · Ben Heath · 2026-01-06 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > Not something I'd recommend for most beginners. It overcomplicates it, and typically, we see better results now by giving Meta direction

### <a id="k32"></a>K32 · tartışmalı · güven 0.52

Meta'nın öğrenme aşamasının süresi dönüşüm hacmine bağlıdır (ad set başına yaklaşık 7 günde ~50 optimizasyon olayı); sabit bir süre yoktur ve hesaba/bütçeye göre değişir.


*Değerlendirme:* Dört üye de genel bilgiye dayanıyor; ikisi kurs satan aynı kreatörden geliyor, bağımsız pratik kanıt yok. Tek deneysel yorum (günde ~9 USD, 8 gün sonra hâlâ öğrenmede) süre iddiasını dönüşüm hacmine bağlı olarak sınırlıyor; 24–48 saat yalnızca yüksek hacimde makul. Resmî sayfa metni alınamadığı için doküman 'silent' sayıldı; yaygın bilinen kural ~50 olay/hafta.


*Kendi verinle test:* Aynı bütçeyle bir ad seti StartTrial (üst-huni) olayına, diğerini ödeme olayına optimize edin; 7–10 gün çalıştırın. Başarı ölçütü: öğrenme fazından çıkma durumu ve deneme başına maliyet (CPA/CAC).


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700?locale=en_US](https://www.facebook.com/business/help/112167992830700?locale=en_US) — “”

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=154) @2:34 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > The learning phase lasts typically, let's say 24 to 48 hours, but it is dependent on conversion volume.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1155) @19:15 · Burak Mermi · 2026-02-16 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course
  > The reason you see sales immediately when you launch a campaign is because the algorithm is trying to understand who to show ads to.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=384) @6:24 · Burak Mermi · 2026-02-16 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course
  > By default, many accounts have a learning curve of seven days for 50 conversions.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=384) @6:24 · Burak Mermi · 2026-02-16 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course
  > Some accounts have four days, four days for 20 conversions, and some have five days for 30 conversions.

### <a id="k34"></a>K34 · tartışmalı · güven 0.55

"Küçük" (veya "çok küçük") Meta reklam bütçesinin tanımı içerik üreticilerine ve pazara göre değişir (ör. Türkiye'de günlük ~5.000 TL'ye kadar; ABD doları bazında günde ~100 $ altı veya ~20 $).


*Değerlendirme:* "Küçük bütçe" resmî bir Meta tanımı değil, her üreticinin kendi sınıflandırması. Burak Mermi TL ile, Ben Heath USD ile ve kendi (satış çıkarı olan) pazar bakışıyla konuşuyor; eşikler doğrudan karşılaştırılamaz. Bir yorum 100 $/günün küçük sayılmayacağını söylüyor, yani tanım pazara ve satın alma gücüne bağlı. Düşük bütçeli B2B uygulama denemesi için kendi pazarınızdaki göreli ölçeği esas almak daha mantıklı.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=75) @1:15 · Burak Mermi · 2026-07-06 · *qualifies* · kaynak: kendi tecrübesi
  > Bunların 56 tanesi küçük bütçeli dediğimiz yani günde 5000 TL ve 6 harcayan hesaplar.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=0) @0:00 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > I would classify a small Facebook ads budget as anything less than $3,000 per month, so $100 or so per day

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=0) @0:00 · Ben Heath · 2026-02-20 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > I classify a tiny Facebook ads budget as $600 per month or less, or $20 or less per day

### <a id="k35"></a>K35 · muhtemel · güven 0.62

Meta uygulama kampanyalarında (abonelik uygulamaları) performansın temeli sinyal kalitesidir (Meta'ya gönderilen olaylar); ardından en büyük kaldıraç kreatiftir, kreatif fiilen hedeflemeyi yapar ve kampanya kurulumundan daha belirleyicidir.


*Değerlendirme:* Üç üye de aynı yönde: sinyal ve kreatif kampanya kurulumundan daha önemli. Ancak hepsi genel bilgiye dayanıyor, ekranda veri yok; biri ajans satan biri tarafından söyleniyor. Andromeda sonrası kreatifin hedeflemeyi ikame ettiği görüşü sektörde yaygın, ama resmi Meta sayfası bunu açıkça doğrulamıyor. Sıralama (önce sinyal, sonra kreatif) makul ama kanıtlanmış değil.


*Kendi verinle test:* Aynı bütçeyle iki kampanya/dönem karşılaştırın: (A) mevcut kreatiflerle optimizasyon olayını Install'dan StartTrial'a (veya ödemeye) çevirin; (B) olayı sabit tutup 5+ yeni kreatif konsepti ekleyin. En az 7-14 gün ve ~50 olay/hafta sonrası deneme başına maliyet (CPT) ve CAC'yi kıyaslayın.


- Resmi kaynak: [https://developers.facebook.com/blog/post/2025/06/03/advantage-plus-campaign-experience-for-sales-and-app/](https://developers.facebook.com/blog/post/2025/06/03/advantage-plus-campaign-experience-for-sales-and-app/) — “”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=785) @13:05 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: genel bilgi
  > İlki her zaman için sinyal yani sinyal kalitesi her şeyin temelinde.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=785) @13:05 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: genel bilgi
  > İkinci sıraya ben aslında kreativi koyarım.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=474) @7:54 · Gui Costa · 2026-07-28 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > The creatives is what we're going to differentiate your campaign results

### <a id="k36"></a>K36 · muhtemel · güven 0.60

Meta kampanyasında veya reklamlarda birkaç günde bir değişiklik yapmak ya da reklamları sürekli açıp kapamak öğrenme aşamasını bozar ve sonuçları kötüleştirir.


*Değerlendirme:* Üç üye de aynı yönde, ancak hiçbiri ekranda veri göstermiyor; genel bilgiye dayanıyor ve ikisi aynı kanaldan. Meta'nın yardım sayfaları önemli düzenlemelerin (duraklatma, kitle, kreatif, optimizasyon olayı, büyük bütçe/teklif değişikliği) öğrenme aşamasını yeniden başlatabileceğini söylüyor; yani mekanizma kısmen doğru. Ancak "her 2-4 günde bir her değişiklik zarar verir" iddiası abartılı: küçük bütçe değişiklikleri veya yeni reklam eklemek her zaman sıfırlama yapmaz. Düşük bütçede haftada 50 olay almak zaten zor olduğundan sık müdahale riski daha yüksek.


*Kendi verinle test:* Mevcut kampanyada 7-10 gün boyunca hiçbir düzenleme yapma (yalnızca gerçekten gerekirse), sonra önceki 7-10 günle karşılaştır. Başarı ölçütü: deneme başına maliyet (StartTrial CPA) ve 'Öğrenme sınırlı' durumundan çıkış; sonuçlar iyileşmezse sık düzenleme etkisi sınırlıdır.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=474) @7:54 · Denis Shatalin · 2025-12-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > they just every two and every four days keep making changes to their campaigns

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=551) @9:11 · Denis Shatalin · 2025-12-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > You switch off your ads too soon, or you keep making changes to your campaigns every day.

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1558) @25:58 · Nida Yıldırım · 2026-04-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > O yüzden reklam sürekli açmak ve kapamak doğru bir davranış değildir.

### <a id="k39"></a>K39 · muhtemel · güven 0.76

Meta teslimatı günlük değil çok günlük/haftalık pencerelerde optimize eder; bu yüzden tek günlük veya birkaç günlük dalgalanmalar normaldir ve tek başına değişiklik yapmayı gerektirmez.


*Değerlendirme:* İki bağımsız kanal aynı noktayı söylüyor; Burak Mermi'nin yorumlarında da gerçek CPA dalgalanması (270 → 159 → 750 TL; 27 → 4 sipariş) deneyimsel olarak doğrulanıyor. Meta'nın öğrenme aşaması sayfaları öğrenme sırasında performansın daha az istikrarlı olduğunu ima ediyor, ancak "Meta günlük değil haftalık düşünür" ifadesini birebir doğrulayan bir cümleyi çekemedim. Denis Shatalin ajans/topluluk satıyor ve kanıtı genel bilgi; yine de iddia yaygın ve makul. Ancak "değişiklik yapma" önerisi sınırsız değil: haftalar süren bariz kötü performans veya bütçenin öğrenme için yetersiz olması müdahale gerektirir.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=551) @9:11 · Denis Shatalin · 2025-12-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, community_paid
  > meta doesn't think in days, it thinks in weeks.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2401) @40:01 · Burak Mermi · 2026-07-06 · *supports* · kaynak: kendi tecrübesi
  > Meta yedi günlük bakıyor. Biz günlük bakıyoruz.

### <a id="k42"></a>K42 · muhtemel · güven 0.60

Meta uygulama kampanyalarında kreatif testi, birbirinden farklı en az ~5 konsept ve her konsept için birkaç (3-5+) hook/gövde varyasyonuyla planlanmalı; yeni konseptler haftalık denenmelidir.


*Değerlendirme:* İki kaynak da benzer sayıları (5-10 konsept, 5 varyasyon) öneriyor, ancak ikisi de ajans/hizmet satan kanallar ve kanıt göstermiyor; biri müşteri verisine dayandığını söylüyor ama ekranda veri yok. Meta belgeleri kesin sayı vermiyor, yalnızca kreatif çeşitliliğini genel olarak önerir. Bu sayılar sabit bir eşik değil, bütçe ve ölçeğe bağlı bir pratik kural olarak görülmeli; düşük bütçede bu kadar çok kreatif gösterim dağılımını böler.


*Kendi verinle test:* Kendi hesabınızda 2 hafta boyunca 3 farklı konsept × 2-3 hook ile 5+ konsept × 5 varyasyon yapısını karşılaştırın (aynı toplam bütçe). Başarı ölçütü: deneme başlatma (StartTrial) başına maliyet ve kreatif başına harcama dağılımı.


- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=1632) @27:12 · Lorenzo Pravatà · 2025-12-17 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > Then we often test for a lot of our clients. Five, ten constants a week.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=628) @10:28 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > En az 5 tane birbirinden çok farklı konseptiniz var.

### <a id="k44"></a>K44 · tartışmalı · güven 0.59

Güçlü bir kreatif olduğunda, kazanan reklamı tek başına (tek reklam seti/tek reklam olarak) ayrı bir reklam setinde tutmak, birden fazla reklam veya reklam setini birlikte çalıştırmaktan daha iyi sonuç verir.


*Değerlendirme:* İki üye benzer yönde ama farklı bağlamda: biri Türkiye'de yerel hizmet/mesaj hedefli tek reklam öneriyor, diğeri dönüşüm hedefinde kazananı ayrı ssete almayı öneriyor (amaç diğer kreatiflere pay vermek). Biri ajans satıyor, diğeri başka bir yaratıcıdan aktarıyor; ikisinde de gösterilen veri yok. Yorumlar Andromeda sonrası kreatif odağını destekliyor ama e-ticaret ile hizmet sektörü ayrımı yapıyor. Resmî dokümanda net bir hüküm bulunamadı.


*Kendi verinle test:* Aynı bütçeyle 14 gün: A) tek reklam setinde tek kazanan reklam, B) kazananın ayrı sette, diğer kreatiflerin ayrı sette olduğu yapı. Başarı ölçütü: deneme (StartTrial) başına maliyet ve ödeyen müşteri başına CAC; her kolda en az ~50 optimizasyon olayı hedefleyin.


- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1166) @19:26 · Nida Yıldırım · 2026-04-29 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > tek bir reklam seti ve tek bir reklam olarak devam etmelisiniz

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=310) @5:10 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · kaynak: başka içerik üreticisi
  > Pull that winning ad into its own ad set so everything else gets room to breathe

### <a id="k45"></a>K45 · tartışmalı · güven 0.60

Meta reklamverenlerin iyi sonuç için yüksek hacimde yeni kreatif test etmesi gerekir (haftada yaklaşık 20–25+, hatta çok daha fazlası).


*Değerlendirme:* İki üye de benzer bir hacim önerisi yapıyor ama ikisi de kanıtsız; biri başka bir yaratıcıdan aktarıyor, diğeri genel bilgi ve ajans satan bir kanaldan geliyor. Resmi belgeler haftalık kreatif sayısı için bir eşik vermiyor; Meta kreatif çeşitliliğini vurguluyor, adet sayısını değil. Bu yüzden rakamlar yüksek harcama yapan e-ticaret/oyun hesapları için bir pratik kuralı sayılır, düşük bütçeli B2B abonelik uygulaması için geçerli olmayabilir.


*Kendi verinle test:* Düşük bütçede 4 hafta boyunca haftada 3–5 gerçekten farklı kreatif (farklı açı/format) ile haftada 15+ kreatif karşılaştır; başarı ölçütü StartTrial başına maliyet ve ödeyen müşteri başına maliyet (CAC).


- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=75) @1:15 · Sub Club by RevenueCat · 2026-09-15 · *supports* · kaynak: başka içerik üreticisi
  > serious accounts are testing at least 25 new creatives a week.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=860) @14:20 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Bu kreatiflerde benim anladığım 20-25 bile yetmeyebiliyor.

### <a id="k47"></a>K47 · muhtemel · güven 0.73

Meta, yapı ayrıştırılmadığında bütçeyi en kolay dönüşümlere (eski müşteriler, ucuz ürünler, tek reklam seti/kreatif) yoğunlaştırma eğilimindedir.


*Değerlendirme:* İki farklı kanal aynı mekanizmayı anlatıyor; ikincisinin yorumlarında (1300 TL CBO'da tek kreatife tüm bütçenin gitmesi, seyahat acentesi örneği) deneyimsel doğrulama var. Ancak ilk üye genel bilgiye dayanıyor, kanıt göstermiyor ve ajans/kurs satıyor. Resmi sayfa içerik vermedi; bütçenin "kolay dönüşüme" gittiği iddiası genel eğilim olarak makul ama koşullara bağlı. Konu (B2B uygulama StartTrial) ile doğrudan ilgisi dolaylı: satış/e-ticaret bağlamı.


- Resmi kaynak: [https://www.facebook.com/business/help/153514848493595](https://www.facebook.com/business/help/153514848493595) — “”

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=698) @11:38 · Menaf Avcı · 2025-12-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > meta bütçenin çoğunu bu kampanya yapısı olmadan en kolay dönüşümlere, yani eski müşterilere yönlendirir.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=543) @9:03 · Burak Mermi · 2026-07-06 · *supports* · kaynak: genel bilgi
  > Meta en kolay bir şekilde satabileceği reklam grubuna ağırlık vererek bütçeyi orada yoğunlaştırabilir demiştik.

### <a id="k49"></a>K49 · sağlam · güven 0.90

Reklam setleri yaklaşık 50 optimizasyon olayından sonra öğrenme aşamasından çıkar ve öğrenmede takılı kalan set ölçeklemeye hazır değildir; buna karşın bir görüşe göre reklamlar hiç öğrenmeyi bırakmaz ve "öğrenmeden çıkmak" bir mittir.


*Değerlendirme:* Meta yardım sayfaları öğrenme aşamasını ve yaklaşık 50 olayla "Öğrenme sınırlı"dan çıkışı tanımlıyor; yani resmî çerçeve "çıkış" kavramını destekliyor. İlk üye genel bilgiye dayanıyor, kurs satıyor ve belgeyi çürütecek veri göstermiyor; yine de "sürekli öğrenme" vurgusu pratikte haklı bir nüans (sürekli optimizasyon, Andromeda sonrası dağıtım). İkinci üye dokümana dayanıyor ve bağımsız pratik kanıtı yok. Düşük bütçeli StartTrial kampanyasında 50 olay çoğu zaman yakalanamadığından öğrenme sınırlı durumu sık görülür.


*Kendi verinle test:* Düşük bütçeli kampanyada iki seti karşılaştırın: biri StartTrial, diğeri daha sık bir olay (ör. uygulama yükleme/kayıt) için optimize edilsin. 7-14 gün çalıştırıp öğrenme durumu ve deneme başına maliyeti (CPA) ölçün; ölçeklemeyi öğrenmeden çıkan sete göre yapıp CAC'nin korunup korunmadığına bakın.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=694) @11:34 · Mark Builds Brands · 2026-05-11 · *contradicts* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > Your ads are always learning. They never stop learning.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2357) @39:17 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > Yani learning'e sıkışmış adsetler varsa kampanya içerisinde demek ki o an iskeyle etmeye hazır değil diyebiliriz.

### <a id="k50"></a>K50 · tartışmalı · güven 0.59

Bir kreatif konsept işe yaradığında, tamamen farklı bir formata geçmek yerine onun varyasyonları (başlık, ortam, CTA, indirim/sosyal kanıt) üretilip kazanan kampanyaya ya da paralel bir kampanyaya eklenmelidir.


*Değerlendirme:* İki üye de aynı genel taktiği söylüyor; ikisi de genel bilgiye dayanıyor, kanıt göstermiyor ve ajans/kurs satışı çıkarı var. Taktik sektörde yaygın bir pratik, ancak bağımsız ve veriyle desteklenmiş bir kanıt yok. Resmi dokümanlar konuya açıkça değinmiyor. Varyasyonların aynı kampanyada mı yoksa paralel kampanyada mı olacağı bütçeye ve kampanya yapısına bağlı.


*Kendi verinle test:* Kazanan reklamın 3 varyasyonunu mevcut kampanyaya ekleyin, diğer kampanyada farklı bir konsept deneyin; en az 7–10 gün çalıştırıp deneme başına maliyeti (cost per trial) karşılaştırın.


- Resmi kaynak: [https://www.facebook.com/business/help/1738164643098669](https://www.facebook.com/business/help/1738164643098669) — “”

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=2390) @39:50 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Paralelde yine CPI kampanyası olarak olabilir ya da çok yakınsa varyasyon direkt kampanyanın içine de atabilirsiniz.

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=1087) @18:07 · Menaf Avcı · 2025-12-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > Başarılı olan bir görselin başlığını değiştirip, ortamı değiştirip, CT'yi değiştirip

### <a id="k51"></a>K51 · tartışmalı · güven 0.56

Meta'nın dağıtım algoritması statik reklamlara yanlıdır; bu yüzden statik reklamlar, videolarla birlikte karma format setinde tutulmalıdır.


*Değerlendirme:* İki üye farklı iddialar taşıyor: Suby algoritmanın statiği tercih ettiğini söylüyor (kanıtsız, ajans satan biri, yorumlarda deneyimsel çürütme var). App Leaders Club ise sadece format çeşitliliğini öneriyor; bu Meta'nın "kreatif çeşitliliğine öncelik verin" yönlendirmesiyle uyumlu. Resmi dokümanlar statik yanlılığı hakkında sessiz; çeşitlilik tavsiyesi makul ama statik yanlılığı belgelenmemiş.


*Kendi verinle test:* Aynı bütçeyle iki reklam seti/kampanya çalıştırın: biri yalnızca statik, diğeri statik+4:5 video+9:16 video karması. En az 7–10 gün veya set başına ~50 deneme sonrası deneme başına maliyet (cost per StartTrial) ve ödeyen müşteri başına maliyeti (CAC) karşılaştırın.


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns](https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns) — “Kreatif çeşitliliği ve farklılığına öncelik verin.”

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=74) @1:14 · Sabri Suby · 2026-06-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > their algorithm is actually has a bias towards static ads because they can show way more statics to people within one session of Facebook

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1726) @28:46 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *qualifies* · kaynak: genel bilgi
  > Farklı formatlarda 4'e 5'te 9-16 video gerek statik

### <a id="k52"></a>K52 · sağlam · güven 0.92

Özel reklam kategorilerine (finansal ürünler, istihdam, konut, siyaset) giren reklamlar kampanya oluşturulurken beyan edilmelidir; aksi halde reklamlar reddedilebilir, kampanya veya reklam hesabı kısıtlanabilir.


*Değerlendirme:* İki farklı kanal aynı mekaniği anlatıyor ve resmi Meta dokümanı reklamların reddedilebileceğini doğruluyor. Ben Heath'in "tüm reklam hesabı devre dışı kalabilir" ifadesi dokümanda açıkça geçmiyor; daha güçlü bir uyarı, ama makul bir risk. Her iki üye de genel bilgiye dayanıyor, ancak doküman bunu destekliyor.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/special-ad-category) — “Ads may be rejected if the advertiser does not choose an appropriate Special Ad Category.”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=761) @12:41 · Aprendamos Marketing · 2026-01-13 · *supports* · kaynak: genel bilgi
  > si tú tienes una que cae en estas categorías y no lo pones, lo que va a pasar después es que te van a restringir la campaña

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1113) @18:33 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > a good chance not only your ads will be rejected, but your whole ad account can get disapproved

### <a id="k53"></a>K53 · muhtemel · güven 0.64

Meta kampanyasına sınırsız sayıda reklam seti/reklam eklenebilir, ancak tek reklamlı onlarca (ör. 50) reklam setine bölmek veriyi parçalar ve öğrenme aşamasından çıkışı zorlaştırır; bu yüzden birleştirmek önerilir.


*Değerlendirme:* İki üye aslında farklı şeyleri söylüyor: biri teknik olarak limit olmadığını (platform mekaniği), diğeri çok sayıda reklam setinin yönetilemez olduğunu ve öğrenmeyi engellediğini söylüyor; bunlar çelişmiyor. Konsolidasyon tavsiyesi sektörde yaygın ve bütçe/dönüşüm sayısına bağlı olarak mantıklı, fakat üye ajans satıyor ve veri göstermiyor. Resmi sayfa içeriği alınamadığı için doküman sessiz sayıldı.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700](https://www.facebook.com/business/help/112167992830700) — “”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2111) @35:11 · RevenueCat · 2026-09-12 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > running one campaign with 50 ad set and one ad in each ad set and it's impossible to manage

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1251) @20:51 · Kamil YILDIRIM · 2026-05-31 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Canım sıkılırsa birer tane daha ekleyebilirim. Bunun bir limiti yok arkadaşlar.

### <a id="k54"></a>K54 · sağlam · güven 0.93

iOS App Tracking Transparency (ATT) kapsamında takibi reddeden kullanıcıların dönüşümleri Meta'ya bireysel düzeyde iletilmez; bu nedenle Meta'nın dönüşüm verisi eksik kalır (Meta boşluğu kısmen Aggregated Event Measurement ve modelleme ile doldurur).


*Değerlendirme:* Her iki üye de ATT'nin Meta'ya giden veriyi kısıtladığını söylüyor ve bu, Meta'nın kendi yardım sayfalarıyla (AEM, iOS 14.5+ opt-out kullanıcıları) örtüşüyor. Ancak "hiç raporlanmaz" ve "veri yanlış olur" ifadeleri fazla kesin: Meta, reddeden kullanıcılar için toplulaştırılmış ve modellenmiş ölçüm yapıyor. İki üye de genel bilgiye dayanıyor, kanıt göstermiyor ve ajans/kurs satışı çıkarı var. Mekanik doğru, ama kesinlik düzeyi koşullu.


- Resmi kaynak: [https://developers.facebook.com/documentation/app-events/guides/aggregated-event-measurement](https://developers.facebook.com/documentation/app-events/guides/aggregated-event-measurement) — “”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=458) @7:38 · Gui Costa · 2026-07-25 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > So people that accept it, Meta receives the information right away.

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=852) @14:12 · Mark Builds Brands · 2026-05-11 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > The issue is because of what the update that iOS launched, all the users can now opt out of tracking from Facebook.

### <a id="k55"></a>K55 · tartışmalı · güven 0.59

Kaba/ev yapımı, organik görünümlü reklam kreatifleri, mesaj daha güçlüyse cilalı profesyonel kreatiflerden daha iyi performans gösterebilir; bu yüzden mükemmel video üretmeye yatırım yapmadan önce test edilmelidir.


*Değerlendirme:* İki farklı kanal aynı yönde konuşuyor; biri kendi deneyimine dayanıyor (Aazar Shad), diğeri genel bilgiye dayanıyor ve kanıt göstermiyor. İkisi de ajans hizmeti satıyor ve ekranda veri gösterilmiyor. Meta dokümanları cilalı/ham ayrımı konusunda sessiz, yalnızca kreatif testini öneriyor. Bu yüzden iddia yaygın bir pratik gözlem olarak makul ama kanıtı zayıf; genel bir kural değil, koşullu.


*Kendi verinle test:* Aynı mesajı iki biçimde çekin: telefonla çekilmiş ham video ve cilalı video. Aynı kampanyada, eşit bütçeyle en az 7 gün (veya kreatif başına ~50 deneme) çalıştırın. Başarı ölçütü: deneme başına maliyet (CPT) ve ödeyen müşteri başına maliyet (CAC).


- Resmi kaynak: [https://www.facebook.com/business/help/711378409718185](https://www.facebook.com/business/help/711378409718185) — “”

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=555) @9:15 · Gui Costa · 2026-07-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > the ugly video is performing better or the ugly ads performing better because the message on it was better than the very polished ad video

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1550) @25:50 · Aazar Shad · 2026-04-02 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > sometimes what it looks more organic, homemade, made by normal people tends to work way better than really produced and perfect content.

### <a id="k63"></a>K63 · muhtemel · güven 0.65

Türkiye'de reklam hesabının faturalandırma/işletme bilgilerine vergi numarası girilmezse reklam harcamasının üzerine %20 KDV eklenir.


*Değerlendirme:* İki video da aynı mekaniği söylüyor, ancak ikisi de genel bilgiye dayanıyor ve ajans hizmeti satıyor; bağımsız uygulayıcı kanıtı yok. Meta'nın KDV yardım sayfası açılıp doğrulanamadı (sayfa içeriği alınamadı), arama özeti Türkiye için geçerli KDV numarası girilmezse yerel oranda KDV eklendiğini gösteriyor, bu da iddiayla uyumlu. Yorumlardaki "son dönemde çalışmıyor" ve TC kimlik numarasının son hanesi konusu, uygulamanın kişi/şirket durumuna göre değiştiğini düşündürüyor.


*Kendi verinle test:* Reklam hesabı faturalandırma ayarlarında vergi bilgisini girdikten sonra bir sonraki fatura/ödeme dökümünde KDV satırının kaybolup kaybolmadığını kontrol edin (1 faturalama döngüsü). Başarı ölçütü: harcanan tutar ile tahsil edilen tutar farkı.


- Resmi kaynak: [https://www.facebook.com/business/help/155641834501332](https://www.facebook.com/business/help/155641834501332) — “”

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=319) @5:19 · Nida Yıldırım · 2026-04-29 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Diğer türlü her girdiğiniz reklamdan %20 KDV ödersiniz.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=779) @12:59 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Eğer reklamlarınıza fazladan ödeme yapıyorsanız bu vergi bilgilerinizi, işletme bilgilerinizi girmemenizden kaynaklanıyor.

### <a id="k65"></a>K65 · sağlam · güven 0.92

Potansiyel müşteri/satış gibi dönüşüm kampanyalarında reklam alanlarını Meta'nın varsayılanında (Advantage+ / tüm alanlar) bırakmak, elle kısıtlamaktan daha iyidir.


*Değerlendirme:* Ben Heath varsayılanı bırakmayı açıkça öneriyor; Kamil Yıldırım ise yalnızca varsayılanın ne olduğunu anlatıp istenmeyen alanların kaldırılıp yalnızca Instagram'da çalıştırılabileceğini ekliyor, yani öneri değil mekanik bilgi. Meta'nın sayfaları da otomatik yerleşimi öneriyor, ancak bu Meta'nın kendi iddiası ve bir alanı hariç tutmak Advantage+ yerleşimi kapatıyor. Her iki üye de genel bilgiye dayanıyor; bağımsız uygulayıcı verisi yok.


*Kendi verinle test:* Aynı kitle ve bütçeyle iki ad set kur: biri Advantage+ yerleşim, diğeri yalnızca Instagram akış/Reels. En az 7-10 gün veya her biri ~50 StartTrial olana dek çalıştır; ölçüt: deneme başına maliyet ve ödeyen müşteri başına maliyet (CAC).


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/placements](https://www.facebook.com/business/ads/meta-advantage-plus/placements) — “”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2221) @37:01 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > If you are using a leads campaign or a sales campaign, just leave it as is.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1721) @28:41 · Kamil YILDIRIM · 2026-05-31 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Reklam alanları kısmına herhangi bir müdahale etmezsem benim reklamlarım arkadaşlar. Facebook'ta da gösterilir, Instagram'da da gösterilir.

### <a id="k66"></a>K66 · muhtemel · güven 0.64

Önemli düzenlemeler (yeni reklam, reklam seti/kampanya ayarı değişikliği, büyük bütçe artışı) Meta kampanyasını öğrenme aşamasına geri döndürür; bütçe eşiği sabit bir sayı değildir (ör. %50 artış resmi bir kural değil).


*Değerlendirme:* Genel mekanizma (önemli düzenleme öğrenmeyi sıfırlar) Meta yardım sayfalarının başlıklarıyla ve arama özetleriyle uyumlu; ancak sayfa gövdesini alıntılayamadım, bu yüzden resmi alıntı veremiyorum. Ben Heath'in iddiası genel ve doğru yönde; yorumlardaki deneyimler de destekliyor. Burak Mermi'nin "%50 artış sıfırlar" iddiası ise sabit bir eşik veriyor; Meta'nın bilinen anlatımı büyüklüğe bağlı olduğunu söylüyor ve net bir yüzde yayımlamıyor. İkisi de kurs satan, doğrudan deneyim göstermeyen kaynaklar.


*Kendi verinle test:* Düşük bütçeli kampanyada bütçeyi 5–7 gün arayla %20 ve ardından %50 artırıp Ads Manager'daki durumu (Öğrenme / Öğrenme sınırlı) ve deneme başına maliyeti (StartTrial CPA) en az 7 gün izleyin; durum sıfırlanıyor mu ve CPA ne kadar bozuluyor kaydedin.


- Resmi kaynak: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=154) @2:34 · Ben Heath · 2026-02-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, sells_agency_services, affiliate, sponsored, community_paid
  > potentially even change some of the settings at the campaign level, you will re-enter the learning phase.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1310) @21:50 · Burak Mermi · 2026-02-16 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_course
  > If you increase this budget by 50%, you will reset the learning process.

### <a id="k68"></a>K68 · muhtemel · güven 0.67

Abonelikli uygulamalarda soğuk reklam trafiğini doğrudan App Store sayfasına/uygulama indirmeye yönlendirmek yerine kişiselleştirilmiş bir web quizine yönlendirmek daha iyi dönüşüm sağlar.


*Değerlendirme:* İki üye de quiz'in doğrudan indirmeden iyi dönüştürdüğünü söylüyor; biri kendi testinden (fitness B2C), diğeri ajans müşteri verisinden, ancak ikisinde de rakam gösterilmiyor. Ajans satışı çıkar çatışması yaratıyor ve ikisi de B2C abonelik bağlamında. Meta dokümanları web quiz yönlendirmesi hakkında bir şey söylemiyor; ayrıca Advantage+ app kampanyası trafiği doğrudan mağazaya götürür, quiz için web dönüşüm kampanyası gerekir. B2B ve düşük bütçe için kanıt yok.


*Kendi verinle test:* Aynı hedef kitle ve bütçeyle iki kampanya kur: biri doğrudan App Store'a, biri kısa (5-8 soru) quiz sayfasına yönlendirsin. En az 2 hafta veya kampanya başına ~50 deneme başlangıcına kadar çalıştır; deneme başına maliyet ve ödeyen müşteri başına maliyeti (CAC) karşılaştır.


- Resmi kaynak: [https://www.facebook.com/business/help/711378409718185](https://www.facebook.com/business/help/711378409718185) — “”

- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1513) @25:13 · Sub Club by RevenueCat · 2026-09-02 · *supports* · kaynak: kendi tecrübesi
  > we've noticed that the quiz just has a much higher conversion

- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=542) @9:02 · Lorenzo Pravatà · 2025-12-17 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > that's why a quiz is much better than just sending to download the app.

### <a id="k69"></a>K69 · sağlam · güven 0.92

Meta'nın Andromeda sistemi altında, performansı korumak ve reklam yorgunluğunu önlemek için çok sayıda çeşitli ve taze kreatif sunmak gerekir.


*Değerlendirme:* İki video da aynı fikri söylüyor, ancak ikisi de ajans satan kişilerden geliyor ve genel bilgiye dayanıyor; veri gösterilmiyor. Meta'nın sayfası kreatif çeşitliliğini destekliyor ama gereken hacim konusunda sayı vermiyor ve "absürt miktar" ifadesini doğrulamıyor. Yön doğru görünüyor; miktar ise bütçeye bağlı. Düşük bütçeli bir B2B uygulama için çeşitlilik, hacimden daha anlamlı olabilir.


*Kendi verinle test:* Aynı bütçeyle 2 hafta boyunca 3 kreatiflik ile 8 kreatiflik (gerçekten farklı açılar) kampanyayı karşılaştırın; başarı ölçütü deneme başına maliyet (StartTrial) ve frekans artışı.


- Resmi kaynak: [https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance) — “as businesses upload more and more creatives to support a diversification strategy, Meta Andromeda works behind the scenes.”

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=0) @0:00 · Sabri Suby · 2026-06-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you need to feed it with an absolutely absurd amount of fresh creatives in order for your ads not to fatigue

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=555) @9:15 · Gui Costa · 2026-07-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > one of the most important things here on meta right now and Andromeda to perform pretty well is volume

### <a id="k87"></a>K87 · doğrulanamaz · güven 0.56

Video sahibi, 500 dolarlık bütçe için yükleme başına maliyetin yaklaşık 2 dolar olduğunu söylüyor; ancak bu rakam bildirilen toplamlarla (1.200 indirme için yaklaşık 0,42 dolar) uyuşmuyor.


- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=0) @0:00 · Gui Costa · 2026-07-25 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > Our budget is $500, right? So make the math $500, it's about $2 CPI, okay?

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=791) @13:11 · Gui Costa · 2026-07-28 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > 1.93 on Google, 2.38 CPI on Meta.

### <a id="k122"></a>K122 · tek kaynak · güven 0.58

Meta, iş e-posta adreslerini kişisel e-postalara ve LinkedIn gibi platformlara kıyasla daha kötü eşleştirir; bu yüzden B2B müşteri listelerinde eşleşme oranı düşük olur, yine de eldeki tüm veriyi yükleyip eşleşme oranını kontrol etmek gerekir.


*Değerlendirme:* Tek kaynak, kendi deneyimine dayanıyor ve ekranda veri gösterilmiyor; ayrıca ajans ve kurs satışı çıkar çatışması var, ancak iddia bir etkinlik iddiası değil, makul bir mekanik gözlem. Üçüncü taraf bir satıcı testi kişisel e-posta için %32, iş e-postası için %13 eşleşme bulmuş; bu yön olarak uyumlu ama resmî değil. Meta dokümanı bu konuda açık bir şey söylemiyor.


*Kendi verinle test:* Kendi listenizi iki parça olarak yükleyin: yalnızca iş e-postaları ve e-posta + telefon + ad-soyad. Her ikisi için Audience Manager'da gösterilen eşleşme oranını karşılaştırın (aynı gün, birkaç dakika sürer). Başarı ölçütü: eşleşme oranı ve en az 1.000 eşleşen kişi.


- Resmi kaynak: [https://www.facebook.com/business/help/341425252616329](https://www.facebook.com/business/help/341425252616329) — “”

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=156) @2:36 · AdConversion · 2025-11-12 · *supports* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services, sells_course
  > meta does not do the best in terms of matching business email addresses

### <a id="k147"></a>K147 · sağlam · güven 0.90

Meta'nın Advantage+ hedef kitle ayarında kontrol bölümündeki ayarlar (konum, minimum yaş, dil, özel kitle hariç tutma) yapay zekanın aşamayacağı sert sınırlardır; hedef kitle önerileri ise Meta'nın aşabileceği ipuçlarıdır.


*Değerlendirme:* Meta'nın resmî Advantage+ hedef kitle sayfası, kontrolleri yapay zekanın aşmaması gereken işletme kısıtları, önerileri ise öncelik verilen ama genişletilebilen profiller olarak anlatıyor. Bu, videodaki "kontrol bölümü sert sınırdır" iddiasıyla örtüşüyor. Üye tek bir kaynaktan (Ben Heath, genel bilgi) geliyor ve ajans/kurs satışı çıkarı var; ancak mekanik bir iddia olduğu için resmî doküman doğrulaması yeterli.


- Resmi kaynak: [https://www.facebook.com/business/ads/meta-advantage-plus/audience](https://www.facebook.com/business/ads/meta-advantage-plus/audience) — “Hedef kitle önerileri eklediğinizde sistem, bu profille eşleşen hedef kitlelere öncelik verir.”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1706) @28:26 · Ben Heath · 2026-01-06 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, community_paid
  > anything set within the control section is a hard constraint, a hard boundary.

### <a id="k153"></a>K153 · tek kaynak · güven 0.55

CPI'si çok iyi olan bir kreatif bile trial ya da purchase'a dönüşmeyebilir; bu yüzden tek başına install verimliliği güvenilir bir başarı ölçütü değil.


- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1171) @19:31 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > Banner mesela çok iyi insul getiriyor. Hiçbir şekilde böyle purchase'a ya da trial'a dönüşmeyen çok iyi CPI'li şeylerim de oldu.

### <a id="k160"></a>K160 · tek kaynak · güven 0.59

Install veya satın alma maliyeti yerine değer optimizasyonu/ROAS (dalgalanmalarda daha istikrar için TROAS) önerilen Meta optimizasyon hedefidir.


- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1431) @23:51 · App Leaders by Adapty · 2026-09-11 · *—* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you can definitely optimize for return on ad spend, slash VO, whatever you call it, value optimization or return on ad spend.

### <a id="k172"></a>K172 · sağlam · güven 0.92

Yayınladıktan sonra bir reklam setinin işlenmesi/incelenmesi 24-48 saati bulabilir; bu sürede reklam seti etkin değil ya da incelemede görünür.


*Değerlendirme:* Meta, reklam incelemesinin genellikle 24 saat içinde bittiğini ancak daha uzun sürebileceğini söylüyor; 24-48 saat üst sınırı bu ifadeyle uyumlu. Ancak tek bir üye var ve dayanağı genel bilgi; çoğu reklam çok daha çabuk onaylanır. Alıntı, sayfanın kendisi çekilemediği için arama özetinden alındı.


- Resmi kaynak: [https://www.facebook.com/business/help/204798856225114](https://www.facebook.com/business/help/204798856225114) — “While ad review is typically completed within 24 hours, it may take longer and ads can be reviewed again, including after they're live.”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=1823) @30:23 · Aprendamos Marketing · 2026-01-13 · *supports* · kaynak: genel bilgi
  > puede tardar este proceso hasta 24 a 48 horas

### <a id="k190"></a>K190 · tek kaynak · güven 0.63

Meta harcamasını ölçeklendirmeden önce soğuk ücretli trafik için bir deneme-ödeme taban değeri (yaklaşık bir aylık veri) belirleyin; ardından kabul edilebilir müşteri edinme maliyetini hesaplayın.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1188) @19:48 · Sub Club by RevenueCat · 2026-09-02 · *—* · kaynak: kendi tecrübesi
  > we just needed to get a baseline of what that number would be in order for us to calculate how much we could actually spend to our customer

### <a id="k193"></a>K193 · tek kaynak · güven 0.63

Peşin ödemeyle %20 indirimli 'denemesiz' seçenek, 30 gün para iade garantisi olmasına rağmen 14 günlük ücretsiz denemeye göre daha kötü performans gösterdi; sürtünme eklediği düşünülüyor.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=3326) @55:26 · Sub Club by RevenueCat · 2026-09-02 · *—* · kaynak: kendi tecrübesi
  > we're seeing it's quite negative just because it does, of course, add a little more friction

### <a id="k195"></a>K195 · doğrulanamaz · güven 0.55

Abonelikli bir uygulama için Meta reklamlarına başlamadan önce yükleme başına yaşam boyu değer (LTV) en az yaklaşık 3 dolar olmalıdır.


*Değerlendirme:* Tek bir kaynak var ve kanaat genel bilgiye dayanıyor; veri veya kanıt gösterilmiyor. Kanal ajans/kurs satıyor ve sponsorlu içerik üretiyor, bu yüzden eşik değerin ağırlığı düşük. Meta dokümanları LTV için sayısal bir alt sınır vermiyor; yalnızca LTV modeli kullananların teklif sınırı koyabileceğini söylüyor. 3 dolar, ülke, CPI ve dönüşüm oranına göre değişebilecek keyfi bir kural gibi duruyor.


*Kendi verinle test:* Kendi panelinizde 2–4 haftalık veriyle şunu hesaplayın: yükleme başına gerçekleşen gelir (deneme→ödeme oranı × ortalama ilk dönem geliri) ile yükleme başına maliyeti (CPI) karşılaştırın. Başarı ölçütü: LTV/CPI ≥ 1 (ya da hedef geri ödeme süresi içinde CAC'nin LTV'yi aşmaması). 3 dolar eşiğini sabit kabul etmeyin.


- Resmi kaynak: [https://www.facebook.com/business/help/317364032619502](https://www.facebook.com/business/help/317364032619502) — “”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=384) @6:24 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > we're going to stick with at least a $3 LTV per install

### <a id="k199"></a>K199 · sağlam · güven 0.90

Meta panelinde raporlanan ROAS, web sitesi veya üçüncü taraf analizlerde ölçülen ROAS'tan ciddi biçimde farklı olabilir; bu yüzden kararlar tek bir platformun rakamına dayanmamalıdır.


*Değerlendirme:* Meta'nın kendi duyurusu, tıklama tanımı farkları nedeniyle Ads Manager ile üçüncü taraf araçlar arasında tutarsızlık olabileceğini kabul ediyor. Üye genel bilgiye dayanıyor ve kurs/ajans satıyor, ama iddia genel ve doğrulanabilir bir mekanik; 8 vs 2-3 örneği yalnızca örnek. Konu abonelikli B2B uygulamada StartTrial için de geçerli; orada ölçüm farkı ayrıca SKAN/MMP gecikmelerinden de gelebilir.


- Resmi kaynak: [https://www.facebook.com/business/news/click-attribution](https://www.facebook.com/business/news/click-attribution) — “This difference in what is attributed as a "click" conversion can lead to inconsistency”

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=698) @11:38 · Menaf Avcı · 2025-12-28 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > Facebook paneline baktığımızda Ruas 8 iken, belki web sitemizde Ruas 2 veya 3'tür.

### <a id="k241"></a>K241 · doğrulanamaz · güven 0.54

Meta'da abonelikli mobil uygulamaların ücretsiz deneme veya kredi kartı gerektiren hunilerinde, deneme/edinim başına maliyet (CPA) yaklaşık 10–15 $ seviyesinde gerçekleşebilir.


*Değerlendirme:* Tek bir kaynak var: ajans hizmeti satan bir konuşmacı, rakamı ekranda göstermeden sözlü olarak veriyor. Meta'nın belgeleri deneme başı maliyetin nasıl hesaplandığını tanımlıyor ama hiçbir kıyas değeri vermiyor. Rakam sektöre, ülkeye, fiyata ve hedef kitleye çok bağlı, bu yüzden genelleştirilemez.


*Kendi verinle test:* Kendi uygulamanız için StartTrial optimizasyonlu tek bir Advantage+ app kampanyasını 7–14 gün, günlük bütçe en az ~50 × hedef CPA olacak şekilde çalıştırın. Ads Manager'daki 'Cost per start trial' ve deneme→ödeme oranından gerçek CAC'yi hesaplayıp 10–15 $ ile karşılaştırın.


- Resmi kaynak: [https://en-gb.facebook.com/business/help/636861880016583](https://en-gb.facebook.com/business/help/636861880016583) — “”

- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=1397) @23:17 · Lorenzo Pravatà · 2025-12-17 · *supports* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > You can, like we can see CPAs also $10, $15. For example, for a free trial or credit card.

### <a id="k253"></a>K253 · doğrulanamaz · güven 0.53

Abonelikli bir uygulamada install-to-paywall view oranı yaklaşık %80'in altındaysa huni sorunludur ve Meta'ya bütçe harcamadan önce düzeltilmelidir.


*Değerlendirme:* Tek bir kaynak var; konuşmacı bunu açıkça "bence" diyerek kişisel görüş olarak sunuyor, veri veya kanıt göstermiyor. Ajans hizmeti sattığı için çıkar çatışması var. Meta'nın resmi belgeleri paywall görüntüleme eşiği hakkında bir şey söylemiyor. %80 eşiği, onboarding tasarımına göre (paywall'un ilk ekranda olması gibi) değişebilecek, doğrulanamayan bir kural.


*Kendi verinle test:* Kendi panelinde install→paywall view oranını son 2-4 haftalık organik/ücretli kurulumlar için ölç. Oran %80 altındaysa onboarding'i kısaltıp paywall'u öne çek (A/B), en az 1-2 hafta ve ~1.000 kurulum sonrası paywall view oranını ve deneme başına maliyeti (cost per trial) karşılaştır.


- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=320) @5:20 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Benim fikrimce bu %80'nin altındaysa bence sıkıntılı. Yani %80'nin altında install to paywall view'niz varsa.

### <a id="k260"></a>K260 · doğrulanamaz · güven 0.55

Küçük bir Advantage+ uygulama kampanyası testinde yaklaşık 10–25 reklam yayına alıp toplam yaklaşık 500 dolar harcayarak deneme (trial qualified) olayına optimize etmek yeterli bir başlangıçtır.


*Değerlendirme:* Tek bir kaynak var; ajans hizmeti satan bir kanal, genel bilgiye dayanarak sözlü bir tavsiye veriyor, ekranda veri gösterilmiyor. Resmi dokümanlar önerilen bütçe veya reklam sayısı konusunda sessiz (yalnızca 50 reklamlık geçiş sınırı var). 500 dolarlık bütçe, öğrenme aşaması için gereken ~50 olayı karşılayıp karşılamayacağı CPA'ya bağlıdır; B2B abonelik uygulamasında deneme maliyeti yüksekse yetersiz kalabilir.


*Kendi verinle test:* 500 dolarlık bütçeyi 10–15 reklamla 10–14 gün çalıştırın. Başarı ölçütü: trial qualified başına maliyet ve en az ~50 olay (veya ödeyen müşteri başına CAC). Olay sayısı çok düşükse bütçeyi artırın veya üst huni olayına geçin.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/advantage-campaigns](https://developers.facebook.com/docs/marketing-api/advantage-campaigns) — “ASC/AAC campaigns that have more than 50 ads within the adset and cannot be migrated.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2733) @45:33 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > just deploy like 10 to 25 ads and see how it goes and maybe put 500 dollars

### <a id="k262"></a>K262 · sağlam · güven 0.90

Performans düşüşünü önlemek için kampanya başına en az 5–10 farklı kreatif kullanılmalı ve bunlar 2 haftada bir ya da ayda bir yenilenmelidir.


*Değerlendirme:* Meta'nın en iyi uygulamalar sayfası çok sayıda kreatif yüklemeyi ve yorgunluğu önlemek için ayda birkaç kez yenilemeyi öneriyor; bu, konuşmacının yönüyle uyumlu. Ancak "minimum 5–10" ve "2 hafta/1 ay" rakamları resmi bir eşik değil, tek bir kanalın deneyimine dayanan kaba bir kural. İzleyici soruları (düşük bütçede 5 kreatif yeterli mi, nasıl uygulanır) da kuralın bütçeye bağlı olduğunu gösteriyor.


*Kendi verinle test:* Mevcut kampanyada kreatifleri 2 hafta değiştirmeden izleyin, sonra 3–5 yeni kreatif ekleyip 2 hafta daha izleyin. Başarı ölçütü: deneme başına maliyet (StartTrial CPA) ve sıklık/CTR eğilimi; yenileme sonrası maliyet düşüyorsa takvimi sürdürün.


- Resmi kaynak: [https://www.facebook.com/business/help/711378409718185](https://www.facebook.com/business/help/711378409718185) — “upload a high volume of creative assets and refresh them a few times a month to avoid creative fatigue”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=1138) @18:58 · Aprendamos Marketing · 2026-01-13 · *qualifies* · kaynak: müşteri verisi
  > mínimo entre 5 y 10 diferentes y las tienes que ir rotando cada 2 semanas o cada mes

### <a id="k269"></a>K269 · sağlam · güven 0.93

Reklam kurulumunda form oluşturma zorunluluğu yalnızca potansiyel müşteri (lead generation) gibi bazı kampanya türleri için geçerlidir; uygulama tanıtımı gibi diğer türlerde gerekmez.


*Değerlendirme:* İddia temel bir platform mekaniğidir ve Meta yardım sayfalarıyla uyumludur: form, Potansiyel Müşteri hedefi seçilip anında form (instant form) yöntemi kullanıldığında oluşturulur. Kaynak tek bir ajans sahibi anlatıcıdır ve genel bilgiye dayanır, ancak iddia düşük riskli ve doğrulanabilirdir. Uygulama tanıtımı (Advantage+ app) kampanyalarında form gerekmez; bu da konuyla ilgili asıl bağlamdır.


- Resmi kaynak: [https://www.facebook.com/business/help/375478503258484?id=735435806665862](https://www.facebook.com/business/help/375478503258484?id=735435806665862) — “Go to Meta Ads Manager, click Create, and choose the Lead Generation objective; create a new form, duplicate an existing one, or edit a saved draft”

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1172) @19:32 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > sadece bazı kampanya türlerinde işte potansiyel müşteri reklamlarında bir form oluşturmanızı beklemeniz gerekiyor.

### <a id="k279"></a>K279 · tek kaynak · güven 0.62

Hem test hem ölçekleme kampanyasının CBO olarak kurgulandığı yapı, küçük bütçede %28, orta bütçede %32 başarı vermiş; yüksek bütçede oranı düşmüştür.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=700) @11:40 · Burak Mermi · 2026-07-06 · *—* · kaynak: kendi tecrübesi
  > küçük bütçelerde daha iyi çalışmış %28, orta bütçelerde %32, yüksek bütçelerde bu kampanyanın başarı oranı düşmüş.

### <a id="k280"></a>K280 · sağlam · güven 0.92

Ads Manager'da CBO (Kampanya Bütçesi Optimizasyonu) seçeneği artık "Advantage Campaign Budget" (Advantage kampanya bütçesi) olarak adlandırılıyor.


*Değerlendirme:* Tek üyelik var ve genel bilgiye dayanıyor; ancak bu basit bir adlandırma bilgisi. Meta'nın geliştirici dokümanı, kampanya bütçesini ad setlerine dağıtan "Advantage campaign budget" özelliğini tanımlıyor. Doküman "CBO ile aynıdır" demiyor ama işlev tanımı CBO ile örtüşüyor ve üçüncü taraf kaynaklar da yeniden adlandırmayı doğruluyor.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “An Advantage campaign budget is a way of optimizing the distribution of a campaign budget across your campaign's ad sets.”

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · kaynak: genel bilgi
  > In Ads Manager, it's now called Advantage Campaign Budget.

### <a id="k281"></a>K281 · sağlam · güven 0.91

CBO (Advantage kampanya bütçesi) bütçeyi gerçek zamanlı olarak en iyi fırsatlara sahip reklam setlerine otomatik dağıtır; ABO'da ise bütçe reklam seti başına manuel belirlenir.


*Değerlendirme:* Temel mekanik (CBO bütçeyi reklam setleri arasında otomatik dağıtır, ABO'da bütçeyi sen belirlersin) Meta'nın geliştirici dokümanıyla uyuşuyor. Ancak "her kullanıcıya en iyi reklam, zaman ve yerleşim" kısmı dokümanda geçmiyor; bu detay genel bilgi ve biraz abartılı. Yorumlar ABO'nun hâlâ kullanılabileceğini belirtiyor, bu iddiayla çelişmiyor, sadece bağlam ekliyor. Kurs satan bir kanaldan geldiği için etkinlik iddiası olarak değil, mekanik tanım olarak değerlendirildi.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “Facebook automatically and continuously finds the best available opportunities for results across your ad sets”

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=232) @3:52 · Burak Mermi · 2026-02-16 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course
  > the CBO campaign uses dynamic intelligent distribution.

### <a id="k288"></a>K288 · sağlam · güven 0.92

Events Manager'daki olay verisi Ads Manager'da her zaman aynen görünmez; hangisine güvenmeden önce ikisinin tutarlılığı kontrol edilmelidir.


*Değerlendirme:* Meta'nın yardım sayfası, Events Manager'ın atfedilmiş ve atfedilmemiş tüm olayları (tekilleştirme öncesi) gösterdiğini, Ads Manager'ın ise yalnızca reklama atfedilen, tekilleştirilmiş olayları saydığını belirtiyor. Bu nedenle farkın olması beklenen bir durum ve iddia resmi dokümanla uyumlu. Üye tek kaynaklı, genel bilgiye dayalı ve kanıtsız; ancak iddia zaten yaygın biçimde doğrulanmış ve düşük riskli bir mekanik bilgi.


- Resmi kaynak: [https://www.facebook.com/business/help/337196340694086](https://www.facebook.com/business/help/337196340694086) — “Ads Manager and Ads Reporting only show events that are attributed to a Meta user who viewed your ad, excluding duplicate events.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2187) @36:27 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > the data that is there doesn't mean that it's reflected on the ads manager

### <a id="k308"></a>K308 · tek kaynak · güven 0.60

Facebook SDK ile SKAN kullanılıyorsa Start Trial olayının dönüşüm değeri önceliği Düşük veya Orta, Purchase olayınınki ise Yüksek olarak ayarlanmalıdır.


- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1006) @16:46 · First Try · 2026-02-03 · *—* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Select the Start Trial Event as Low or Medium.

### <a id="k309"></a>K309 · tek kaynak · güven 0.63

Meta'dan gelen deneme kayıtlarını özel bir panelle izleyip yalnızca Meta kaynaklı deneme-ödeme verisini Meta'ya geri gönderin; böylece Meta en yüksek niyetli kullanıcıları hedefler.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1354) @22:34 · Sub Club by RevenueCat · 2026-09-02 · *—* · kaynak: kendi tecrübesi
  > we're feeding the highest intent users back to Meta

### <a id="k327"></a>K327 · sağlam · güven 0.91

Meta'nın tahmini yaşam boyu değer (PLTV) optimizasyonu mevcut bir Conversions API entegrasyonu ve haftada 100'den fazla dönüşüm gerektirir; bu da yeni uygulamalar için engel olabilir.


*Değerlendirme:* Resmi Meta dokümanı, Conversions API entegrasyonunu ve son 4 hafta boyunca haftada en az 100 Meta'ya atfedilen dönüşümü şart koşuyor; üye bu eşiği doğru aktarıyor. Ancak doküman ayrıca "pLTV does not support app events at this time" diyor ve entegrasyonun web tabanlı olduğunu belirtiyor. Dolayısıyla uygulama (app) kampanyaları için PLTV'nin kullanılabilirliği şüpheli. Üye platform dokümanını tekrarlıyor, bağımsız pratik kanıt değil; eşik "4 hafta üst üste" nüansını da atlıyor.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “You have a minimum of 100 conversion events per week attributed to Meta for each of the last 4 weeks.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1639) @27:19 · RevenueCat · 2026-09-12 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > you need to have at least more than 100 conversions per week this could be the issue for new applications

### <a id="k346"></a>K346 · sağlam · güven 0.91

Andromeda güncellemesi reklam dağıtımının retrieval (aday seçme) aşamasını değiştirdi; bunun nedeni bildirildiğine göre yapay zekâ ile üretilen kreatif bolluğu.


*Değerlendirme:* Meta mühendislik yazısı Andromeda'nın reklam retrieval motoru olduğunu ve üretken YZ araçlarıyla reklam adayı sayısının arttığını doğruluyor. Ancak "sıralama mantığı değişti" ve "neden YZ kreatif seli" ifadesi gevşek bir yorum; belgeler daha çok altyapı/model yükseltmesi olarak anlatıyor. Üye tek kaynak, kurs satan bir kanal ve genel bilgiye dayanıyor; yorumdaki kampanya düşüşü ise Andromeda ile ilişkilendirilmiş kanıt değil, sadece soru.


- Resmi kaynak: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “Meta Andromeda is a personalized ads retrieval engine that leverages the NVIDIA Grace Hopper Superchip”

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=152) @2:32 · Mark Builds Brands · 2026-05-11 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > Andromeda was an update to the sorting process of the retrieval steps specifically

### <a id="k347"></a>K347 · tek kaynak · güven 0.55

İçerik üreticisi bütçeyi kampanya seviyesi yerine reklam seti seviyesinde belirlemeyi tercih ediyor ve Andromeda güncellemesinden sonra reklam seti bütçesiyle daha iyi sonuç gördüğünü söylüyor.


- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=781) @13:01 · Nida Yıldırım · 2026-04-29 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > ben reklam seti bütçesinde çok daha iyi sonuçlar alındığını görüyorum

### <a id="k348"></a>K348 · şüpheli · güven 0.05

Andromeda güncellemesi sonrası Meta reklam getirme sisteminde yaklaşık %6 iyileşme ve 100 kat daha kısa yanıt süresi görüldü.


*Değerlendirme:* Meta mühendislik yazısı %6 recall artışını doğruluyor; ancak bu "alaka" değil retrieval recall metriğidir. "100 kat daha az bekleme" resmi kaynakta yok; orada 10x çıkarım verimliliği ve 10.000x model kapasitesi geçiyor. Konuşmacı ajans/kurs satıyor ve bilgi genel bilgiye dayanıyor; rakamın bir kısmı karışmış veya abartılmış olabilir.


- Resmi kaynak: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “has achieved +6% recall improvement to the retrieval system”

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=236) @3:56 · Menaf Avcı · 2025-12-28 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course
  > %6 bir iyileşme görüyoruz burada. 100 kat daha az bekleme süresi.

### <a id="k380"></a>K380 · tek kaynak · güven 0.62

Yazarın örnekleminde, doğrudan reklama yüklenen tamamen yapay zeka üretimi görsel ve videolar her bütçede düşük performans göstermiş; insan tasarımı ve gerçek içerikler daha iyi çalışmıştır (yalnızca arka planı değiştirilen görseller bu kapsama girmemiştir).


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2251) @37:31 · Burak Mermi · 2026-07-06 · *—* · kaynak: kendi tecrübesi
  > Bu tarz hesaplar bütçe fark etmeksizin başarısız olmuş.

### <a id="k381"></a>K381 · sağlam · güven 0.93

Meta, optimize ettiğiniz olayı (event) gerçekleştirmesi olası kişilere gösterim yapar; deneme başlangıcı için optimize ederseniz deneme başlatanlar gelir, bunlar ödemeye dönüşmeyebilir.


*Değerlendirme:* Meta'nın geliştirici belgeleri, uygulama olayı optimizasyonunun reklamı seçilen eylemi yapması olası kişilere gösterdiğini söylüyor; iddianın mekanik kısmı bununla örtüşüyor. "Denemeler ödemeye dönüşmeyebilir" kısmı mantıksal bir sonuç ve genel olarak kabul gören bir uyarı, ancak tek kaynaktan (Adapty'nin kanalı) geliyor ve ekranda veri gösterilmiyor. Belge ayrıca üst düzey bir olayın (ör. satın alma) seçilebileceğini destekliyor.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “display mobile app install ads to people likely to take a specific action in your app”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1335) @22:15 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > hangi event için optimize ediyorsak Meta'da biz onu getiriyor

### <a id="k388"></a>K388 · sağlam · güven 0.91

Meta reklam dağıtımı dört aşamada işler: retrieval (aday seçimi), hafif sıralama, ağır sıralama ve açık artırma.


*Değerlendirme:* Meta'nın mühendislik yazısı çok aşamalı bir sistemi doğruluyor: önce retrieval, sonra daha ağır sıralama modelleri. "Hafif" ve "ağır" sıralama ayrımı ile açık artırma bu sayfada açıkça geçmiyor. Açık artırma ise Meta'nın başka belgelerinde ayrıca anlatılıyor. Ayrıca Zuckerberg'in 2025 Q3 konuşmasına göre retrieval ile erken sıralama tek modelde birleşti. Bu yüzden dört aşamalı tarif genel olarak doğru ama basitleştirilmiş ve güncelliğini yitirmiş olabilir. Kaynak kurs satan bir kanal ve kanıt göstermiyor.


- Resmi kaynak: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “Retrieval is the first step in our multi-stage ads recommendation system.”

- [the entire meta ads algorithm explained in 21 mins](https://youtu.be/JMw6SmRdYQY?t=75) @1:15 · Mark Builds Brands · 2026-05-11 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, community_paid
  > First, you have retrieval. Second is light ranking. Third is heavy ranking. And the final piece is the auction.

### <a id="k410"></a>K410 · tek kaynak · güven 0.63

Ucuz deneme başlatmaya odaklanan tıklama odaklı Meta reklamları deneme-ödeme oranında büyük düşüşe yol açtı; yani tek başına ucuz deneme iyi bir kalite göstergesi değil.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1354) @22:34 · Sub Club by RevenueCat · 2026-09-02 · *—* · kaynak: kendi tecrübesi
  > we'll see a huge drop in trial to pay

### <a id="k429"></a>K429 · doğrulanamaz · güven 0.60

Video sahibi, bir müşterisinin iOS uygulamasının yaklaşık 500 dolarlık Meta reklam harcamasıyla yaklaşık 30 günde 1.200 ilk kez indirme aldığını bildiriyor.


- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=0) @0:00 · Gui Costa · 2026-07-25 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > how I got 1,200 first-time downloads for this client of mine in about 30 days

### <a id="k436"></a>K436 · doğrulanamaz · güven 0.55

İddia: B2B SaaS şirketleri Meta'yı birincil kanal olarak kullanıp ayda 200.000$'dan fazla harcayarak ayda 2M$'a ulaşıyor. Hiçbir vaka, ekran görüntüsü veya zaman aralığı gösterilmedi.


- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=0) @0:00 · Lorenzo Pravatà · 2026-03-26 · *—* · kaynak: müşteri verisi · çıkar çatışması: sells_agency_services
  > These B2B SaaS scale to $2 million a month using Meta as their primary channel

### <a id="k448"></a>K448 · tek kaynak · güven 0.60

Yüklemeye değil ücretsiz deneme başlangıcına optimize etmek yükleme maliyetini yaklaşık iki katına çıkardı, ama ücretsiz deneme kampanyası toplamda daha kârlı çıktı.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1015) @16:55 · Steven Cravotta · 2026-07-30 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_course, affiliate
  > the cost per install was double on this free trial optimized campaign, but ultimately it ended up being more profitable for us

### <a id="k450"></a>K450 · tek kaynak · güven 0.55

Tek bir deneme yerine birden fazla deneme seçeneği sunmak (örn. 7 gün ücretsiz ya da düşük fiyatlı bir aylık deneme) deneme başlatmaları artırdı.


- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1474) @24:34 · Aazar Shad · 2026-04-02 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > instead of only giving the option of seven days, try for free, we give the option of you can try for free seven days

### <a id="k452"></a>K452 · doğrulanamaz · güven 0.55

Abonelikli bir uygulamada Meta reklamlarını ölçeklemeden önce denemeden ücretliye dönüşüm oranı %30'un üzerinde olmalıdır.


*Değerlendirme:* Tek bir kaynak var; üstelik kanal ajans/kurs satıyor, affiliate ve sponsorlu içerik içeriyor, dayanağı genel bilgi ve kanıt yok. Meta dokümanları böyle bir eşikten söz etmiyor. RevenueCat gibi üçüncü taraf verilerde genel ortalama %38 civarı, yani %30 makul görünse de B2B, fiyat ve deneme süresine göre çok değişir; evrensel bir eşik değil.


*Kendi verinle test:* Kendi verinle: mevcut deneme→ücretli oranını son 30–60 günlük kohortta ölç, ardından CAC = deneme maliyeti ÷ dönüşüm oranı formülüyle hesapla. %30'un altında bile CAC, müşteri LTV'sinin izin verdiği sınırın altındaysa ölçeklemeyi küçük artışla (%20 bütçe) 7–14 gün dene; başarı ölçütü ödeyen müşteri başına maliyet.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=233) @3:53 · App Masters · 2026-10-20 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services, sells_course, affiliate, sponsored
  > the trial to paid should yield over 30%.

### <a id="k457"></a>K457 · sağlam · güven 0.93

SDK veya MMP bağlandığında Meta uygulama tanıtımı reklam seti, onboarding tamamlandı, ücretsiz deneme başladı veya satın alma gibi uygulama içi olaylar için optimize edilebilir.


*Değerlendirme:* Meta'nın resmi belgeleri Start Trial dahil uygulama içi olaylara göre optimizasyonu ve tek seferde yalnızca bir olaya optimize edilebildiğini doğruluyor. Üye ekranda Ads Manager'ı gösteriyor ve iddia temel bir platform mekaniği. Kurs satma/affiliate çıkar çatışması var, ancak bu iddia verimlilik değil mekanik olduğu için ağırlığı düşürmüyor. Yorumdaki sinyal kaybı sorusu iddiayı çürütmüyor, ayrı bir ölçüm konusu.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “Set `custom_event_type` in the promoted object to the app event you want to optimize.”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1169) @19:29 · Steven Cravotta · 2026-07-30 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_course, affiliate
  > You can choose onboarding completed, free trial started, customer purchased

### <a id="k459"></a>K459 · sağlam · güven 0.93

Meta'nın tahmini yaşam boyu değer (pLTV) optimizasyonu Purchase, Subscribe, StartTrial, CompleteRegistration ve AddPaymentInfo standart olaylarını ve özel olayları destekler.


*Değerlendirme:* Resmi Meta geliştirici belgesi aynı olay listesini (Purchase, Subscribe, StartTrial, CompleteRegistration, AddPaymentInfo ve özel olaylar) veriyor; konuşmacının söylediğiyle birebir örtüşüyor. Tek kaynak ve belge tekrarı olsa da doğrulanabilir bir platform mekaniği olduğundan güvenilir. Ajans hizmeti satma çıkarı bu tür olgusal iddiada ağırlığı düşürmüyor.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “The following events support pLTV value optimization:”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > supports a set of standard events the first one is purchase the second is subscribe the third one is star trial complete registration and add payment info

### <a id="k462"></a>K462 · şüpheli · güven 0.08

Tahmini yaşam boyu değer (pLTV) optimizasyonu, aynı olay kimliği hem SDK'dan hem sunucudan gönderilirse Meta verileri birleştirebildiği için iOS ATT kısıtlamalarına rağmen çalışmaya devam eder.


*Değerlendirme:* Tek kaynak (RevenueCat, hizmet satan, çıkar ilişkisi var) iddiayı sözlü olarak söylüyor; ekranda veri ya da birinci elden sonuç yok. Meta'nın pLTV rehberi ATT'den bahsetmiyor, deduplikasyonu yalnızca Pixel + Conversions API için anlatıyor ve pLTV'nin uygulama olaylarını desteklemediğini belirtiyor. Bu yüzden uygulama kampanyası bağlamındaki iddia mevcut dokümanla çelişiyor; sayfa güncel olmayabilir ama doğrulanamıyor.


*Kendi verinle test:* Reklam Yöneticisi'nde uygulama kampanyanızda pLTV/değer optimizasyonu seçeneğinin görünüp görünmediğine bakın. Görünüyorsa SDK ve sunucudan aynı event_id ile StartTrial gönderin, Events Manager'da en az 7 gün deduplikasyon oranını izleyin ve iOS'ta deneme başına maliyeti standart StartTrial optimizasyonuyla karşılaştırın.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “pLTV does not support app events at this time.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *supports* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > the cool thing about this new pltb logic is that it survives the att on ios

### <a id="k465"></a>K465 · sağlam · güven 0.91

Android'de Meta uygulama kampanyaları kurulumları GAID ve Install Referrer ile ilişkilendirir; SKAdNetwork kullanılmaz.


*Değerlendirme:* Meta'nın geliştirici dokümanı Android'de Install Referrer (GPIR ve Meta Install Referrer) ile atıf yapıldığını doğruluyor. GAID ve SKAdNetwork'ün yokluğu bu sayfada geçmiyor. SKAdNetwork'ün iOS'a özgü olduğu genel olarak bilinen bir bilgidir. Tek kaynak, ajans satan bir kanalın genel bilgiye dayalı sözlü anlatımı; yine de teknik olarak makul.


- Resmi kaynak: [https://developers.facebook.com/docs/app-ads/meta-install-referrer](https://developers.facebook.com/docs/app-ads/meta-install-referrer) — “The Meta install referrer provides last touch info for the install, including ad campaign metadata”

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=388) @6:28 · First Try · 2026-02-03 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Like they use GAID and another thing, which is called InstallRiffer.

### <a id="k480"></a>K480 · tek kaynak · güven 0.60

Küçük bütçede tıklama maliyeti (CPC), CPI'dan daha yararlı bir yön gösterici sinyaldir; örnekte bir kreatifin CPC'si yaklaşık 0,11 dolar, diğerininki yaklaşık 0,25 dolardı.


- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=534) @8:54 · Gui Costa · 2026-07-25 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services
  > Cost per click, 11 cents per click, right?

### <a id="k486"></a>K486 · sağlam · güven 0.93

Meta'nın Advantage+ Creative özelliği, uygulama kampanyalarında statik görselleri otomatik olarak 9:16 dikey videoya dönüştürebilir.


*Değerlendirme:* Resmi geliştirici dokümanı, image_animation ile statik görselin kısa animasyonlu videoya çevrilebildiğini ve adapt_to_placement ile 9:16 yerleşimlerin varsayılan açık olduğunu söylüyor. Üye yalnızca platform özelliğini aktarıyor, tek kaynak ve pratik kanıt yok. Doküman 'dönüştürme'nin ince hareket animasyonu olduğunu ve opt-in olduğunu belirtiyor; bu da iddiayı kısmen nüanslı kılıyor.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started) — “By default, 4:5 and 9:16 placements are enabled.”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=624) @10:24 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · kaynak: platform dokümanı
  > 9-16 video şeklinde çevirebiliyor.

### <a id="k492"></a>K492 · sağlam · güven 0.89

Kanal/reklam seti başına minimum günlük bütçe, optimizasyon olayı başına maliyet × günde 10 olay kadardır (haftalık ~50 olay eşiği aslında yaklaşık ×7 anlamına gelir).


*Değerlendirme:* Meta'nın oyun reklamı bütçe rehberi, reklam seti başına haftada yaklaşık 50 olay ve olay maliyeti × 50 mantığını veriyor; bu günlük yaklaşık 7-8 olaya denk gelir. Videodaki ×10 çarpanı bu mantığa yakın, biraz muhafazakâr bir yuvarlama; resmi bir kural değil. Tek kaynak, genel bilgiye dayalı, kanıt gösterilmemiş ve ajans satışı çıkarı var. Düşük bütçeli B2B deneme (StartTrial) hedefinde, olay maliyeti yüksekse çıkan bütçe gerçekçi olmayabilir; bu yüzden daha üst hunideki bir olay seçilebilir.


- Resmi kaynak: [https://developers.facebook.com/documentation/games/acquire/click-to-play-ads/budget](https://developers.facebook.com/documentation/games/acquire/click-to-play-ads/budget) — “needs approximately 50 optimization events per week”

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=2214) @36:54 · App Leaders by Adapty · 2026-09-11 · *qualifies* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > you need to multiply that with 10 every day.

### <a id="k500"></a>K500 · tek kaynak · güven 0.54

Meta'da geniş hedefleme B2B için yalnızca ABM yapmıyorsanız ve toplam pazarınız büyükse (küçük işletme veya alt orta pazar) işe yarayabilir.


- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=699) @11:39 · AdConversion · 2025-11-12 · *—* · kaynak: kendi tecrübesi · çıkar çatışması: sells_agency_services, sells_course
  > If you have a large total addressable market, I'm talking about you're going after small business or lower mid-market

### <a id="k523"></a>K523 · tek kaynak · güven 0.62

Tek reklam grubu içinde çok sayıda kreatif bulunan tek CBO kampanyası, küçük bütçeli hesaplarda %21, orta bütçelide %16 ve yüksek bütçelide %14 başarı oranı vermiştir; bütçe arttıkça başarı düşmüştür.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=543) @9:03 · Burak Mermi · 2026-07-06 · *—* · kaynak: kendi tecrübesi
  > küçük bütçelerde %21 başarı oranına sahipmiş bu kampanya. Orta bütçelerde %16 yüksek bütçelerde %14.

### <a id="k525"></a>K525 · tek kaynak · güven 0.62

Her reklam grubuna sabit bütçe harcatılan ABO kampanyaları küçük bütçede %7, orta bütçede %9, yüksek bütçede %3 başarı oranı vermiştir; yazara göre günde 30.000 TL'nin üzerinde ABO tercih edilecek bir yapı değildir.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=620) @10:20 · Burak Mermi · 2026-07-06 · *—* · kaynak: kendi tecrübesi
  > küçük bütçelerde %7, orta bütçelerde %9, yüksek bütçelerde de %3 başarı oranına sahip diyebiliriz

### <a id="k531"></a>K531 · sağlam · güven 0.91

Meta'nın tahmini yaşam boyu değer (pLTV) optimizasyonu, olayların Conversions API ile sunucu tarafından gönderilmesini gerektirir; yalnızca SDK ile kurulum tam çalışmaz.


*Değerlendirme:* Meta'nın pLTV rehberi Conversions API ile göndermeyi zorunlu kılıyor; bu, konuşmacının iddiasının çekirdeğini destekliyor. Ancak aynı sayfa "pLTV does not support app events at this time" diyor; yani mobil uygulama olayları için pLTV şu an desteklenmiyor olabilir. Dolayısıyla iddia web/CAPI için doğru, uygulama kampanyası için ise "tam çalışmaz"dan daha kısıtlayıcı olabilir. Tek kaynak, ajans satışı çıkarı olan ve Meta dokümanını tekrarlayan bir anlatım.


*Kendi verinle test:* Yeni uygulama kampanyası kurmadan önce Events Manager'da uygulama veri setinizin pLTV seçeneğini sunup sunmadığını kontrol edin. Sunmuyorsa SDK ile standart değer optimizasyonunu (StartTrial değeri) 7–14 gün deneyin ve deneme başına maliyeti ölçün.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “Sending through the Conversions API is required.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *qualifies* · kaynak: platform dokümanı · çıkar çatışması: sells_agency_services
  > with the app plus sdk is not uh going to work completely it needs to work through the conversions api

### <a id="k532"></a>K532 · doğrulanamaz · güven 0.56

RevenueCat'in Meta (Conversions API) ile doğrudan entegrasyonu 2026 başında bozuk; bu yüzden olaylar (deneme→ödeme) RevenueCat'ten doğrudan Meta'ya gönderilmemeli.


*Değerlendirme:* Tek üyeli grup: iddia genel bilgi temelli, kanıt gösterilmemiş ve konuşmacı ajans hizmeti satıyor. Bir yorum benzer bir şikayet aktarıyor ama bu bağımsız ve doğrulanabilir bir kanıt değil. Meta dokümanları RevenueCat'ten hiç söz etmiyor; RevenueCat kendi dokümanında Conversions API'yi önermeye devam ediyor, bu da sorunun geçici veya kurulum kaynaklı olabileceğini düşündürüyor.


*Kendi verinle test:* RevenueCat'in Meta entegrasyonunu test dataset'iyle açın, sandbox'ta bir deneme başlatıp 24-48 saat içinde Events Manager'ın Test Events/Overview sekmesinde StartTrial ve Subscribe olaylarının görünüp görünmediğine bakın. Başarı ölçütü: olayların eşleşme kalitesiyle birlikte görünmesi. Görünmezse Meta SDK + kendi sunucunuzdan CAPI gönderimini deneyin.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/app-events.md](https://developers.facebook.com/documentation/ads-commerce/conversions-api/app-events.md) — “To implement a partner platform integration, please follow the instructions”

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=155) @2:35 · First Try · 2026-02-03 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > I recommend you not to send the events to MetaAds from RevenueCat.

### <a id="k537"></a>K537 · sağlam · güven 0.92

Meta reklamları Facebook, Instagram, Threads ve Audience Network'te yayınlanabiliyor ve WhatsApp Durum (Status) alanına da açılıyor.


*Değerlendirme:* Resmi Meta geliştirici dokümanı WhatsApp Status, Threads ve Audience Network yerleşimlerinin var olduğunu doğruluyor. Konuşmacı bunu kesin olmayan bir ifadeyle ("sanırım") söylüyor ve ajans satan biri, ancak iddia genel bilgi niteliğinde ve doğrulanabilir. Konuyla ilgili haberler de Eylül 2025 sonrası kullanıma açıldığını gösteriyor.


- Resmi kaynak: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audiences/reference/placement-targeting) — “To use the WhatsApp Status placement, you must select the Instagram story placement as well.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2891) @48:11 · RevenueCat · 2026-09-12 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > actually now i think they're releasing ads into whatsapp status

### <a id="k560"></a>K560 · sağlam · güven 0.93

Advantage+ kampanya bütçesi açıldığında Meta bütçeyi reklam setleri arasında otomatik dağıtır; kapatılırsa her reklam seti için bütçeyi elle belirlemek gerekir.


*Değerlendirme:* İddia temel bir platform mekaniğidir ve Meta'nın resmi geliştirici dokümanıyla birebir uyumludur. Dokümana göre Meta, sonuçlar için en iyi fırsatları sürekli bulup bütçeyi gerçek zamanlı dağıtır; kapatılırsa ad set bütçeleri verilmelidir. Tek üyeli bir grup ve konuşmacı ajans satıyor, ancak iddia doğrulanabilir ve tartışmalı değil.


- Resmi kaynak: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “If you disable the Advantage campaign budget, you should provide budgets for all ad sets under the campaign.”

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1251) @20:51 · Kamil YILDIRIM · 2026-05-31 · *supports* · kaynak: genel bilgi · çıkar çatışması: sells_agency_services
  > Ama ben her reklam setime kendim bir bütçe tanımlamak istiyorum diyorsanız bu seçenekleri kapatmanız gerekir