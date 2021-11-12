# London Crime Data Visualization
## Assignment Project Overview
---
Data visualization using matplotlib.pyplot of London Crime Data, 2008-2016
Data yang digunakan adalah data kejahatan/kriminal yang tercatat di wilayah metropolitan utama London. Data ini mencakup jumlah laporan kriminal menurut bulan, LSOA borough, dan kategori mayor/minor dari Jan 2008 sampai dengan Des 2016 yang dapat di akses di sini. Dari kumpulan data ini, akan divisualisasikan dengan bantuan matplotlib.pyplot pada Python yang mencakup Line Plot, Area Plot, Histogram, dan lain-lain guna mendapatkan informasi tentang kejahatan/kriminal yang terjadi di wilayah metropolitan London dari Jan 2008-Des 2016.

Berikut library Python yang digunakan:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import follium
```
---
### Informasi Data & Preprocessing
---
Berdasarkan _overview_ sebelumnya, diketahui bahwa data mengandung informasi tentang kejahatan/kriminal di wilayah metropolitan utama London. Selanjutnya akan dilakukan data preparation/preprocessing guna memperoleh informasi baris/kolom, missing values pada data, dan lain-lain sebelum masuk ke tahap visualisasi.
```python
london_crime = pd.read_csv("london_crime_by_lsoa.csv") #import data
```
