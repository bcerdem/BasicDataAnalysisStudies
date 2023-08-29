########################################################################################################################
####################################################CONDA###############################################################
########################################################################################################################
# Sanal ortamların listelenmesi:
# conda env list

# Sanal ortam oluşturma:
# conda create -n <name>

# Sanal ortamı aktif etme
# conda activate <name>

# aktif olan sanal ortamı deaktif etmek için
# conda deactivate

# Sanal ortamdaki paketleri görme
# conda list

# Paket yüklemek istendiğinde
# conda install <paket_adi>

# Aynı anda birden fazla paket yükleme
# conda install <paket_adi> <paket_adi1> <paket_adi2>

# Paket silme
# conda remove <paket_adi>

# Belirli bir versiyona göre paket yüklemek için/pip'de iki == kullanılır
# conda install <paket_adi>=<versiyon>

# Paket yükseltme
# conda upgrade <paket_adi>

# Tüm paketleri güncelleme
# conda upgrade -all

# Paket listesinin çıktısı
# conda env export > environment.yaml

# Sanal ortamı silme
# conda env remove -n myenv

# Paket listesinin çıktısı ile yeni bir sanal ortam oluşturma
# conda env create -f environment.yaml

########################################################################################################################
####################################################PIP#################################################################
########################################################################################################################

# pip: pypi (python package index) paket yönetim aracı

# Paket yükleme
# pip install <paket_adi>

# Paket yükleme Versiyona göre
# pip install <paket_adi> == <versiyon>

# pip'de paketi yüklerken bir versiyon belirtilmiş ise ve yüklü olan versiyon varsa ve Daha önce yüklü olan versiyon daha
# yüksek bir versiyon olsa bile kaldırıp bellirtilen versiyonu yükler


# conda hem paket yönetimi hem de sanal ortam işlemleri için kullanılabilir. pip sadece paket yönetimi için kullanılabilir.

