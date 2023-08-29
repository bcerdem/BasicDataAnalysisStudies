############################################################
# Numpy Array Özellikleri (Attibutes of Numpy Arrays)
############################################################

from data_analysis_with_python.numpy import numpy_ as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype