<!-- iso-work README -->

iso-work
========

Pisi Linux ISO oluşturma araçları ve dosyaları.

Not: Bu proje Python 2 ile geliştirilmiş ve python2 ile çalıştırılmalıdır. Sisteminizde python2 yüklü olduğundan emin olun.

required_packages.txt dosyasındaki programların sisteminizde kurulu olması gerekmektedir.  
Otomatik kurulum ve çalıştırma için pisiman dizininde:
```sh
sh ./run.sh
```
komutunu çalıştırmanız yeterli. Not: konsolda kurulum ve çalıştırma için sudo ile parola istenmektedir.  

Çalıştırmadan önce NOT dosyasını okuyun.

---

Aşağıda proje içeriği, kullanım ve önemli noktalar özetlenmiştir.

Özet
----
Bu depo, Pisi GNU/Linux için canlı (live) ve kurulum (install) ISO'ları ile ilgili repo/image oluşturma araçlarını içerir. Ana yapı app/repotools/ dizininde bulunur; arayüz ise pisiman.py tarafından başlatılır.

Hızlı başlatma
--------------
1. Host sistemi için gerekli paketleri yükleyin (required_packages.txt içeriğine bakın).  
2. GUI veya yardımcı betikleri inşa etmek için (varsa):
```sh
./make.sh
```
3. CLI ile imaj oluşturmak için:
```sh
python pisiman.py make <project.xml>
```
(Not: yukarıdaki komut python2 kullanılarak çalıştırılmalıdır: python2 pisiman.py ...)
4. GUI ile: app/gui/main.py üzerinden projeyi açın ve "Make Repo / Make Image / Make ISO" işlemlerini kullanın.

Önemli betikler ve modüller
--------------------------
- Proje modeli: app/repotools/project.py — proje yükleme/kaydetme, dizin ve yardımcılar.
- Temel iş akışları (app/repotools/maker.py):
  - make_repos: repo hazırlama
  - make_image: imaj oluşturma (chroot, configure pending)
  - squash_image: squashfs oluşturma
  - make_iso: ISO oluşturma, EFI/isolinux ayarları
  - setup_isolinux / setup_efi: önyükleyici kurulumları
  - mkinitcpio: initramfs oluşturma yardımcıları
  - load_grub_params: GRUB yapılandırma şablonları
- GUI: app/gui/main.py — Qt tabanlı arayüz.

Tipik iş akışı
--------------
- project XML dosyasını düzenleyin veya oluşturun (project-files dizini örnekleri).
- GUI: projeyi açın, paketleri kontrol edin, "Make Repo / Make Image / Make ISO" tıklayın.
- CLI: python pisiman.py make <project.xml>

Önemli dosyalar
---------------
- pisiman.py — ana giriş noktasına yakın betik
- app/repotools/maker.py — yapım mantığı
- app/repotools/project.py — proje model ve dizin yardımcıları
- app/gui/main.py — GUI
- pisiman/required_packages.txt — host bağımlılıkları
- make.sh — UI / build yardımcı betiği

Notlar & Hata giderme
---------------------
- Birçok işlem mount, chroot, pisi, xorriso gibi sistem komutları çalıştırır — gerekli yetkiler (root) ile çalıştırın.
- Hata durumunda çıktıdaki mesajları kontrol edin; work_dir içindeki finished.txt ve log dosyaları hangi aşamaya gelindiğini gösterir.
- Paket/repoyla ilgili sorunlarda proje içindeki repo cache ve work_dir yollarını kontrol edin.

Katkıda bulunma
---------------
- Yapı mantığı için app/repotools; UI için app/gui üzerinde değişiklik yapın.
- Yeni host bağımlılığı eklenirse pisiman/required_packages.txt güncellensin.
- UI değişikliklerinden sonra ./make.sh çalıştırın (varsa).
