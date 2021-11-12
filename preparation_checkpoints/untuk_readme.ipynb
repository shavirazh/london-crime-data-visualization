{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "399df431",
   "metadata": {},
   "source": [
    "# Assignment Project Overview\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a19c894f",
   "metadata": {},
   "source": [
    "Data yang digunakan adalah data kejahatan/kriminal yang tercatat di wilayah metropolitan utama London. Data ini mencakup jumlah laporan kriminal menurut bulan, _LSOA borough_, dan kategori mayor/minor dari Jan 2008 sampai dengan Des 2016 yang dapat di akses [di sini](https://www.kaggle.com/jboysen/london-crime). Dari kumpulan data ini, akan divisualisasikan dengan bantuan `matplotlib.pyplot` pada Python yang mencakup Line Plot, Area Plot, Histogram, dan lain-lain guna mendapatkan informasi tentang kejahatan/kriminal yang terjadi di wilayah metropolitan London dari Jan 2008-Des 2016.\n",
    "\n",
    "---\n",
    "Berikut library Python yang digunakan:\n",
    "```python\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import follium\n",
    "```"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1a483e58",
   "metadata": {},
   "source": [
    "## Informasi Data & Preprocessing\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9fa32a2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be8b8313",
   "metadata": {},
   "source": [
    "Berdasarkan _overview_ sebelumnya, diketahui bahwa data mengandung informasi tentang kejahatan/kriminal di wilayah metropolitan utama London. Selanjutnya akan dilakukan data preparation/preprocessing guna memperoleh informasi baris/kolom, _missing values_ pada data, dan lain-lain sebelum masuk ke tahap visualisasi."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3cb4a017",
   "metadata": {},
   "outputs": [],
   "source": [
    "london_crime = pd.read_csv(\"london_crime_by_lsoa.csv\") #import data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "96cabe0a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lsoa_code</th>\n",
       "      <th>borough</th>\n",
       "      <th>major_category</th>\n",
       "      <th>minor_category</th>\n",
       "      <th>value</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>E01001116</td>\n",
       "      <td>Croydon</td>\n",
       "      <td>Burglary</td>\n",
       "      <td>Burglary in Other Buildings</td>\n",
       "      <td>0</td>\n",
       "      <td>2016</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>E01001646</td>\n",
       "      <td>Greenwich</td>\n",
       "      <td>Violence Against the Person</td>\n",
       "      <td>Other violence</td>\n",
       "      <td>0</td>\n",
       "      <td>2016</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>E01000677</td>\n",
       "      <td>Bromley</td>\n",
       "      <td>Violence Against the Person</td>\n",
       "      <td>Other violence</td>\n",
       "      <td>0</td>\n",
       "      <td>2015</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>E01003774</td>\n",
       "      <td>Redbridge</td>\n",
       "      <td>Burglary</td>\n",
       "      <td>Burglary in Other Buildings</td>\n",
       "      <td>0</td>\n",
       "      <td>2016</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>E01004563</td>\n",
       "      <td>Wandsworth</td>\n",
       "      <td>Robbery</td>\n",
       "      <td>Personal Property</td>\n",
       "      <td>0</td>\n",
       "      <td>2008</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   lsoa_code     borough               major_category  \\\n",
       "0  E01001116     Croydon                     Burglary   \n",
       "1  E01001646   Greenwich  Violence Against the Person   \n",
       "2  E01000677     Bromley  Violence Against the Person   \n",
       "3  E01003774   Redbridge                     Burglary   \n",
       "4  E01004563  Wandsworth                      Robbery   \n",
       "\n",
       "                minor_category  value  year  month  \n",
       "0  Burglary in Other Buildings      0  2016     11  \n",
       "1               Other violence      0  2016     11  \n",
       "2               Other violence      0  2015      5  \n",
       "3  Burglary in Other Buildings      0  2016      3  \n",
       "4            Personal Property      0  2008      6  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "london_crime.head() #5 data pertama pada dataframe london_crime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "15ab4227",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>lsoa_code</th>\n",
       "      <th>borough</th>\n",
       "      <th>major_category</th>\n",
       "      <th>minor_category</th>\n",
       "      <th>value</th>\n",
       "      <th>year</th>\n",
       "      <th>month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>13490599</th>\n",
       "      <td>E01000504</td>\n",
       "      <td>Brent</td>\n",
       "      <td>Criminal Damage</td>\n",
       "      <td>Criminal Damage To Dwelling</td>\n",
       "      <td>0</td>\n",
       "      <td>2015</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13490600</th>\n",
       "      <td>E01002504</td>\n",
       "      <td>Hillingdon</td>\n",
       "      <td>Robbery</td>\n",
       "      <td>Personal Property</td>\n",
       "      <td>1</td>\n",
       "      <td>2015</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13490601</th>\n",
       "      <td>E01004165</td>\n",
       "      <td>Sutton</td>\n",
       "      <td>Burglary</td>\n",
       "      <td>Burglary in a Dwelling</td>\n",
       "      <td>0</td>\n",
       "      <td>2011</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13490602</th>\n",
       "      <td>E01001134</td>\n",
       "      <td>Croydon</td>\n",
       "      <td>Robbery</td>\n",
       "      <td>Business Property</td>\n",
       "      <td>0</td>\n",
       "      <td>2011</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13490603</th>\n",
       "      <td>E01003413</td>\n",
       "      <td>Merton</td>\n",
       "      <td>Violence Against the Person</td>\n",
       "      <td>Wounding/GBH</td>\n",
       "      <td>0</td>\n",
       "      <td>2015</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          lsoa_code     borough               major_category  \\\n",
       "13490599  E01000504       Brent              Criminal Damage   \n",
       "13490600  E01002504  Hillingdon                      Robbery   \n",
       "13490601  E01004165      Sutton                     Burglary   \n",
       "13490602  E01001134     Croydon                      Robbery   \n",
       "13490603  E01003413      Merton  Violence Against the Person   \n",
       "\n",
       "                       minor_category  value  year  month  \n",
       "13490599  Criminal Damage To Dwelling      0  2015      2  \n",
       "13490600            Personal Property      1  2015      6  \n",
       "13490601       Burglary in a Dwelling      0  2011      2  \n",
       "13490602            Business Property      0  2011      5  \n",
       "13490603                 Wounding/GBH      0  2015      6  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "london_crime.tail() #5 data terakhir pada dataframe london_crime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c562df97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 13490604 entries, 0 to 13490603\n",
      "Data columns (total 7 columns):\n",
      " #   Column          Dtype \n",
      "---  ------          ----- \n",
      " 0   lsoa_code       object\n",
      " 1   borough         object\n",
      " 2   major_category  object\n",
      " 3   minor_category  object\n",
      " 4   value           int64 \n",
      " 5   year            int64 \n",
      " 6   month           int64 \n",
      "dtypes: int64(3), object(4)\n",
      "memory usage: 720.5+ MB\n"
     ]
    }
   ],
   "source": [
    "london_crime.info() #informasi tentang data type masing-masing kolom pada dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3c7fe294",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(13490604, 7)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "london_crime.shape #(jumlah baris, kolom)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "404c490f",
   "metadata": {},
   "source": [
    "Berdasarkan _output_ _dataframe_ `london_crime` di atas, dapat diketahui bahwa _dataframe_ terdiri dari 13490604 baris/observasi dan 7 kolom/_features_, di mana kolom ini berisi informasi tentang berapa jumlah kriminal berdasarkan kategori mayor/minor yang tercatat di _borough_ tertentu pada bulan dan tahun tertentu. Dengan detail sebagai berikut:\n",
    "\n",
    "_`borough`: Common name for London borough._\n",
    "\n",
    "_`major_category`: High level categorization of crime._\n",
    "\n",
    "_`minor_category`: Low level categorization of crime within major category._\n",
    "\n",
    "_`value`: monthly reported count of categorical crime in given borough._\n",
    "\n",
    "_`year`: Year of reported counts, 2008-2016._\n",
    "\n",
    "_`month`: Month of reported counts, 1-12._\n",
    "\n",
    "Selanjutnya, akan diketahui jumlah dan nama-nama _borough_, serta kategori kriminal mayor apa saja yang ada dalam data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "0c3ff0d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah borough yang tercatat: 33\n",
      "['Croydon' 'Greenwich' 'Bromley' 'Redbridge' 'Wandsworth' 'Ealing'\n",
      " 'Hounslow' 'Newham' 'Sutton' 'Haringey' 'Lambeth' 'Richmond upon Thames'\n",
      " 'Hillingdon' 'Havering' 'Barking and Dagenham' 'Kingston upon Thames'\n",
      " 'Westminster' 'Hackney' 'Enfield' 'Harrow' 'Lewisham' 'Brent' 'Southwark'\n",
      " 'Barnet' 'Waltham Forest' 'Camden' 'Bexley' 'Kensington and Chelsea'\n",
      " 'Islington' 'Tower Hamlets' 'Hammersmith and Fulham' 'Merton'\n",
      " 'City of London']\n"
     ]
    }
   ],
   "source": [
    "print(\"Jumlah borough yang tercatat:\", london_crime[\"borough\"].nunique())\n",
    "print(london_crime[\"borough\"].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "943a1eec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah kriminal kategori mayor yang tercatat: 9\n",
      "['Burglary' 'Violence Against the Person' 'Robbery' 'Theft and Handling'\n",
      " 'Criminal Damage' 'Drugs' 'Fraud or Forgery' 'Other Notifiable Offences'\n",
      " 'Sexual Offences']\n"
     ]
    }
   ],
   "source": [
    "print(\"Jumlah kriminal kategori mayor yang tercatat:\", london_crime[\"major_category\"].nunique())\n",
    "print(london_crime[\"major_category\"].unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9ca246f8",
   "metadata": {},
   "source": [
    "Berdasarkan _output_ di atas, diketahui terdapat 33 _borough_ atau wilayah metropolitan di London dan terdapat 9 jenis kriminal dengan kategori mayor.\n",
    "\n",
    "Selanjutnya, akan dilakukan pengecekan apakah ada _missing values_ pada _dataframe_ `london_crime`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "88846cff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "lsoa_code         0\n",
       "borough           0\n",
       "major_category    0\n",
       "minor_category    0\n",
       "value             0\n",
       "year              0\n",
       "month             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "london_crime.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cee2ce25",
   "metadata": {},
   "source": [
    "Karena tidak terdapat _missing values_ pada data, maka dapat dilakukan proses visualisasi dengan Line Plot, Histogram, dan lain-lain. Hasil visualisasi beserta interpretasinya dilampirkan pada tabel berikut: "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c7e444f4",
   "metadata": {},
   "source": [
    "## Table of Contents\n",
    "\n",
    "----"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9751c7c",
   "metadata": {},
   "source": [
    "| **Plot Names**|\n",
    "| -------------|\n",
    "|Line Plot   |\n",
    "|Area Plot     |\n",
    "|Histogram     | \n",
    "|Bar Chart     |\n",
    "|Pie Chart     |\n",
    "|Box Plot      |\n",
    "|Scatterplot   |\n",
    "|Follium Maps  |"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "837dfa32",
   "metadata": {},
   "source": [
    "## Conclusions\n",
    "\n",
    "---"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": false,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
