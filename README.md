CRM Optimizasyon Projesi: Müşteri Destek ve Pazarlama Kampanyası Seçimi
Bu proje, CRM (Müşteri İlişkileri Yönetimi) sistemini geliştirerek iki temel işlevin optimize edilmesini amaçlamaktadır:

Müşteri Destek Temsilcisi Yönlendirme:
CRM sistemi, müşteri taleplerine ve temsilcinin uygunluğuna göre belirli şehirlerdeki müşterilere müşteri destek temsilcilerini yönlendirecek şekilde tasarlanmıştır. Bu yönlendirme, maliyetin en aza indirilmesi hedeflenerek yapılır.

Pazarlama Kampanyası Seçimi:
CRM sistemi, verilen bir bütçe dahilinde en uygun pazarlama kampanyalarını seçerek yatırım getirisini (ROI) en üst düzeye çıkarmayı hedefler. Her kampanyanın belirli bir maliyeti ve beklenen getirisi vardır.

Amaç
Bu iki işlevi bir araya getirerek, müşteri destek süreçlerini ve pazarlama yatırımlarını optimize eden bir CRM çözümü geliştirmek amaçlanmaktadır.

Algoritma Tasarımı
Her iki işlev de Dinamik Programlama ilkeleri ile optimize edilmiştir:

Müşteri Destek Temsilcisi Yönlendirme:
Dinamik programlama kullanılarak, her müşteriye en uygun temsilcinin atanması sağlanır ve toplam maliyet minimize edilir.

Pazarlama Kampanyası Seçimi:
Dinamik programlama kullanılarak, bütçe dahilindeki en verimli pazarlama kampanyaları seçilir ve ROI maksimize edilir.

Karmaşıklık Analizi
Algoritmaların zaman karmaşıklığı T(n) ve Big-O (O(n)) adım adım hesaplanmış ve açıklanmıştır.

Kullanılan Araçlar ve Teknolojiler
Programlama Dili: Python
Kütüphaneler:
NumPy (matris işlemleri için)
Matplotlib (sonuçları görselleştirmek için)
Proje Adımları
Müşteri Destek Temsilcisi Yönlendirme Algoritması
Pazarlama Kampanyası Seçimi Algoritması
Test ve Doğrulama
Sonuçların Sunumu
Projeyi Çalıştırmak İçin Talimatlar
Depoyu bilgisayarınıza klonlayın:

git clone https://github.com/kullanıcı-adınız/crm-optimization.git
Proje dizinine gidin:

cd crm-optimization
Gerekli bağımlılıkları yükleyin (varsa):

pip install -r requirements.txt
Python dosyasını çalıştırın:

python customer_support_assignment.py
python marketing_campaign_selection.py

