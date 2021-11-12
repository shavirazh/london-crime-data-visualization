# London Crime Data Visualization
## Assignment Project Overview

Data visualization using matplotlib.pyplot of London Crime Data, 2008-2016
Data yang digunakan adalah data kejahatan/kriminal yang tercatat di wilayah metropolitan utama London. Data ini mencakup jumlah laporan kriminal menurut bulan, LSOA borough, dan kategori mayor/minor dari Jan 2008 sampai dengan Des 2016 yang dapat di akses [di sini](https://www.kaggle.com/jboysen/london-crime). Dari kumpulan data ini, akan divisualisasikan dengan bantuan matplotlib.pyplot pada Python yang mencakup Line Plot, Area Plot, Histogram, dan lain-lain guna mendapatkan informasi tentang kejahatan/kriminal yang terjadi di wilayah metropolitan London dari Jan 2008-Des 2016.

Berikut library Python yang digunakan:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import follium
```

### Informasi Data & Preprocessing

Berdasarkan _overview_ sebelumnya, diketahui bahwa data mengandung informasi tentang kejahatan/kriminal di wilayah metropolitan utama London. Selanjutnya akan dilakukan data preparation/preprocessing guna memperoleh informasi baris/kolom, missing values pada data, dan lain-lain sebelum masuk ke tahap visualisasi.
```python
london_crime = pd.read_csv("london_crime_by_lsoa.csv") #import data
london_crime.head() #5 data pertama pada dataframe london_crime
```
|   | lsoa_code |    borough |              major_category |              minor_category | value | year | month |
|--:|----------:|-----------:|----------------------------:|----------------------------:|------:|-----:|-------|
| 0 | E01001116 |    Croydon |                    Burglary | Burglary in Other Buildings |     0 | 2016 |    11 |
| 1 | E01001646 |  Greenwich | Violence Against the Person |              Other violence |     0 | 2016 |    11 |
| 2 | E01000677 |    Bromley | Violence Against the Person |              Other violence |     0 | 2015 |     5 |
| 3 | E01003774 |  Redbridge |                    Burglary | Burglary in Other Buildings |     0 | 2016 |     3 |
| 4 | E01004563 | Wandsworth |                     Robbery |           Personal Property |     0 | 2008 |     6 |

```python
london_crime.tail() #5 data terakhir pada dataframe london_crime
```
|          | lsoa_code | borough    | major_category              | minor_category              | value | year | month |
|----------|-----------|------------|-----------------------------|-----------------------------|-------|------|-------|
| 13490599 | E01000504 | Brent      | Criminal Damage             | Criminal Damage To Dwelling | 0     | 2015 | 2     |
| 13490600 | E01002504 | Hillingdon | Robbery                     | Personal Property           | 1     | 2015 | 6     |
| 13490601 | E01004165 | Sutton     | Burglary                    | Burglary in a Dwelling      | 0     | 2011 | 2     |
| 13490602 | E01001134 | Croydon    | Robbery                     | Business Property           | 0     | 2011 | 5     |
| 13490603 | E01003413 | Merton     | Violence Against the Person | Wounding/GBH                | 0     | 2015 | 6     |

```python
london_crime.info() #informasi tentang data type masing-masing kolom pada dataframe
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 13490604 entries, 0 to 13490603
Data columns (total 7 columns):
 #   Column          Dtype 
---  ------          ----- 
 0   lsoa_code       object
 ---  ------          ----- 
 1   borough         object
 ---  ------          ----- 
 2   major_category  object
 ---  ------          ----- 
 3   minor_category  object
 ---  ------          ----- 
 4   value           int64 
 ---  ------          ----- 
 5   year            int64 
 ---  ------          ----- 
 6   month           int64 
 ---  ------          ----- 
dtypes: int64(3), object(4)
---  ------          ----- 
memory usage: 720.5+ MB
---  ------          ----- 

```python
london_crime.shape #(jumlah baris, kolom)
```
(13490604, 7)

Berdasarkan output dataframe london_crime di atas, dapat diketahui bahwa dataframe terdiri dari 13490604 baris/observasi dan 7 kolom/features, di mana kolom ini berisi informasi tentang berapa jumlah kriminal berdasarkan kategori mayor/minor yang tercatat di borough tertentu pada bulan dan tahun tertentu. Dengan detail sebagai berikut:

borough: Common name for London borough.
_major_category: High level categorization of crime._
_minor_category: Low level categorization of crime within major category._
value: monthly reported count of categorical crime in given borough.
year: Year of reported counts, 2008-2016.
month: Month of reported counts, 1-12.

Selanjutnya, akan diketahui jumlah dan nama-nama borough, serta kategori kriminal mayor apa saja yang ada dalam data.

```python
print("Jumlah borough yang tercatat:", london_crime["borough"].nunique())
print(london_crime["borough"].unique())
```
Jumlah borough yang tercatat: 33
'Croydon' 'Greenwich' 'Bromley' 'Redbridge' 'Wandsworth' 'Ealing'
 'Hounslow' 'Newham' 'Sutton' 'Haringey' 'Lambeth' 'Richmond upon Thames'
 'Hillingdon' 'Havering' 'Barking and Dagenham' 'Kingston upon Thames'
 'Westminster' 'Hackney' 'Enfield' 'Harrow' 'Lewisham' 'Brent' 'Southwark'
 'Barnet' 'Waltham Forest' 'Camden' 'Bexley' 'Kensington and Chelsea'
 'Islington' 'Tower Hamlets' 'Hammersmith and Fulham' 'Merton'
 'City of London'
 
 ```python
 print("Jumlah kriminal kategori mayor yang tercatat:", london_crime["major_category"].nunique())
print(london_crime["major_category"].unique())
```
Jumlah kriminal kategori mayor yang tercatat: 9
'Burglary' 'Violence Against the Person' 'Robbery' 'Theft and Handling'
 'Criminal Damage' 'Drugs' 'Fraud or Forgery' 'Other Notifiable Offences'
 'Sexual Offences'
 
Berdasarkan output di atas, diketahui terdapat 33 borough atau wilayah metropolitan di London dan terdapat 9 jenis kriminal dengan kategori mayor.
Selanjutnya, akan dilakukan pengecekan apakah ada missing values pada dataframe london_crime.

```python
london_crime.isnull().sum()
```
lsoa_code         0
borough           0
major_category    0
minor_category    0
value             0
year              0
month             0
dtype: int64


Karena tidak terdapat missing values pada data, maka dapat dilakukan proses visualisasi dengan Line Plot, Histogram, dan lain-lain. Hasil visualisasi beserta interpretasinya dilampirkan pada tabel berikut:
| Plot Names   |
|--------------|
| [Line Plot](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Line-Plot.ipynb)    |
| [Area Plot](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Area-Plot.ipynb)    |
| [Histogram](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Histogram.ipynb)    |
| [Bar Chart](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Bar-Chart.ipynb)    |
| [Pie Chart](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Pie-Chart.ipynb)    |
| [Box Plot](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Box-Plot.ipynb)     |
| [Scatterplot](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Scatterplot.ipynb)  |
| [Follium Maps](https://github.com/shavirazh/london-crime-data-visualization/blob/main/PYTN_Assgn_1_KS03_ShaviraZhalsabilla/Follium-Maps.ipynb) |
