# -*- coding: utf-8 -*-
"""[Tiffany] CBF.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19swMefiBkEjYtF8XdG23cofQdfHcM5gp
"""

# Mengimpor pustaka Pandas untuk manipulasi dan analisis data
import pandas as pd
# Mengimpor pustaka NumPy untuk komputasi numerik dan operasi array
import numpy as np
# Mengimpor modul untuk mengakses Google Drive, memungkinkan penggunaan file yang disimpan di sana
from google.colab import drive
drive.mount('/content/drive')

# Membaca file CSV yang berisi data profil pelanggan dari Google Drive
cust_df = pd.read_csv('/content/drive/Shareddrives/Capstone Project/data/SMEs Pack Project CSV - Customer Profile.csv')
cust_df.head()

# Menghapus kolom 'No.' dari DataFrame karena kolom ini kemungkinan hanya berisi nomor urut
# yang tidak relevan untuk analisis lebih lanjut
cust_df.drop(columns=['No.'], inplace=True)
# Menampilkan 5 baris pertama dari DataFrame setelah kolom 'No.' dihapus
cust_df.head()

# Membaca file CSV yang berisi data historis dari Google Drive
history_df = pd.read_csv('/content/drive/Shareddrives/Capstone Project/data/SMEs Pack Project CSV - Historical Data - Raw.csv')
history_df.head()

# Menghapus kolom 'NO' dari DataFrame karena kolom ini kemungkinan hanya berisi nomor urut
# yang tidak relevan untuk analisis atau manipulasi data lebih lanjut
history_df.drop(columns=['NO'], inplace=True)
history_df.head()

# Memodifikasi kolom 'SMEs Name' dengan membagi nilai-nilainya berdasarkan spasi (' ')
# dan hanya mengambil bagian pertama (kata pertama) dari setiap nama
history_df['SMEs Name'] = history_df['SMEs Name'].str.split(' ').str[0]
history_df.head()

# Membaca file CSV yang berisi data penilaian supplier dari Google Drive
supplier_df = pd.read_csv('/content/drive/Shareddrives/Capstone Project/data/SMEs Pack Project CSV - Supplier - Assesment .csv')
supplier_df.head()

# Memodifikasi kolom 'Company' dengan membagi nilai-nilainya berdasarkan spasi (' ')
# dan hanya mengambil bagian pertama (kata pertama) dari setiap nama perusahaan
supplier_df['Company'] = supplier_df['Company'].str.split(' ').str[0]
supplier_df.head()

# Menggabungkan DataFrame 'cust_df' dan 'history_df' berdasarkan kolom:'Kode' dari 'cust_df' sebagai kunci kiri dan 'Buyers' dari 'history_df' sebagai kunci kanan
# Metode penggabungan menggunakan 'inner' untuk hanya menyertakan baris yang memiliki nilai kunci yang cocok di kedua DataFrame
merged_df = pd.merge(cust_df, history_df, left_on='Kode', right_on='Buyers', how='inner')
# Menggabungkan DataFrame 'merged_df' dengan 'supplier_df' berdasarkan kolom:'SMEs Name' dari 'merged_df' sebagai kunci kiri dan 'Company' dari 'supplier_df' sebagai kunci kanan
# Metode penggabungan juga menggunakan 'inner' untuk memastikan hanya data yang cocok di kedua DataFrame yang disertakan
final_df = pd.merge(merged_df, supplier_df, left_on='SMEs Name', right_on='Company', how='inner')
final_df.head()

# Menampilkan seluruh isi DataFrame 'final_df' ke layar
print(final_df)

# Iterasi melalui setiap kolom di DataFrame 'final_df'
for col in final_df.columns:
    print(f"Column Name: {col}")
    print("First 5 data:")
    print(final_df[col].head().to_list())
# Menampilkan pemisah untuk memperjelas setiap kolom
    print("-" * 30)

# Menampilkan nilai unik dari kolom 'Unnamed: 15' di DataFrame 'final_df'
# Ini berguna untuk mengetahui berbagai nilai yang ada dalam kolom tersebut dan memahami tipe data atau kategori yang terkandung
final_df['Unnamed: 15'].unique()

# Menampilkan nilai unik dari kolom 'Channel Penjualan' di DataFrame 'final_df'
final_df['Channel Penjualan'].unique()

# Menampilkan nilai unik dari kolom 'Type' di DataFrame 'final_df'
final_df['Type'].unique()

# Menampilkan nilai unik dari kolom 'Business Ownership' di DataFrame 'final_df'
final_df['Business Ownership'].unique()

"""Semua Channel Penjualan, Type, Byusiness Ownership valuenya sama, jd kita drop aja"""

# Menampilkan nilai unik dari kolom 'Monthly Cohort' di DataFrame 'final_df'
final_df['Monthly Cohort'].unique()

# Menampilkan daftar nama kolom yang terdapat dalam DataFrame 'final_df'
final_df.columns

# Membuat DataFrame baru 'df' yang hanya berisi kolom-kolom yang relevan dari 'final_df'
# Dengan memilih kolom-kolom tertentu yang dibutuhkan untuk analisis lebih lanjut
df = final_df[['Kode', 'Lead Source', 'City', 'State', 'Type Of Customer', 'Country', 'Unnamed: 15',
              'SMEs Name', 'SKU', 'Transaction Value', 'Buyers', 'Monthly Cohort', 'Q Cohort', 'Q Cohort2',
              'Q Cohort3', 'Company', ' Production Capacity (40ft/month)', 'Size of Factory (SQM)',
              'Number of Employees', 'Established', 'Specialization', 'Capacity', 'Price', 'Production',
              'Product.1', 'Finishing', 'Quality', 'helper', 'Total Score', 'Status']]

"""# Drop useless Variables"""

# Menampilkan 5 baris pertama dari DataFrame 'df' untuk mendapatkan gambaran awal tentang data yang telah dipilih
df.head()

"""# Preprocessing"""

# Menampilkan jumlah nilai unik di setiap kolom dalam DataFrame 'df'
df.nunique()

# Iterasi melalui kolom 'City' dan 'State' di DataFrame 'df'
# Menampilkan nilai unik dari kedua kolom tersebut untuk memahami variasi data di masing-masing kolom
for column, values in df[['City', 'State']].items():
    print(f"Unique values in '{column}':")
    print(values.unique())
    print()

# Membandingkan apakah nilai di kolom 'State' dan 'City' adalah sama di setiap baris di DataFrame 'cust_df'
# Fungsi .all() digunakan untuk memeriksa apakah semua nilai dalam hasil perbandingan bernilai True
are_values_equal = (cust_df['State'] == cust_df['City']).all()
# Menampilkan pesan tergantung apakah semua nilai di 'State' dan 'City' sama atau tidak
if are_values_equal:
    print("All values in 'State' and 'City' are the same in every row.")
else:
    print("There are rows where the values in 'State' and 'City' are different.")

# Menghapus kolom 'State' dari DataFrame 'df'
# Kolom ini dihapus karena dianggap tidak relevan atau duplikat (misalnya, kolom 'City' sudah cukup)
df = df.drop(columns=['State'])
df.head()

# Menampilkan informasi ringkas tentang DataFrame 'df'
df.info()

# Membuat dictionary 'label_mapping' untuk memetakan label kategori 'Type Of Customer' menjadi angka
label_mapping = {
    'Dying Star Customer': 1,
    'Star Customer': 2,
    'Regular Customer': 3,
    'New Customer': 4
}
# Menggunakan metode .map() untuk mengganti nilai di kolom 'Type Of Customer' dengan angka sesuai dengan 'label_mapping'
df['Type Of Customer'] = df['Type Of Customer'].map(label_mapping)

df.head()

# Menampilkan nilai unik dari kolom 'Status' di DataFrame 'df'
df['Status'].unique()

# Membuat dictionary 'label_mapping' untuk memetakan nilai kategori dalam kolom 'Status' menjadi angka
label_mapping = {
    'Outstanding': 1,
    'Good': 2,
    'Fair': 3,
}
# Menggunakan metode .map() untuk mengganti nilai di kolom 'Status' dengan angka sesuai dengan 'label_mapping'
df['Status'] = df['Status'].map(label_mapping)
# Menampilkan 5 baris pertama DataFrame setelah perubahan
df.head()

# Mengambil daftar nama kolom yang memiliki tipe data 'object' (biasanya tipe string) dari DataFrame 'df'
object_columns = df.select_dtypes(include='object').columns.tolist()
# Menampilkan daftar kolom yang bertipe data 'object'
print(object_columns)

# Mengonversi nilai di kolom 'Kode', 'Buyers', dan 'SMEs Name'
df['Kode'] = df['Kode'].str.split('-').str[1].astype(int)
df['Buyers'] = df['Buyers'].str.split('-').str[1].astype(int)
df['SMEs Name'] = df['SMEs Name'].str.split('-').str[1].astype(int)
# Untuk kolom 'Company' dan 'SKU', selain melakukan split berdasarkan tanda '-',
# juga menghapus angka nol di depan string dengan str.lstrip('0'), lalu mengonversinya menjadi integer.
df['Company'] = df['Company'].str.split('-').str[1].str.lstrip('0').astype(int)
df['SKU'] = df['SKU'].str.split('-').str[1].str.lstrip('0').astype(int)
# Menampilkan DataFrame setelah perubahan
print(df)

# Menampilkan informasi ringkas tentang DataFrame 'df'
df.info()

# Mengambil kolom-kolom dengan tipe data 'object' dari DataFrame 'df'
object_columns = df.select_dtypes(include='object').columns
# Mengambil nilai unik untuk setiap kolom bertipe 'object' dan menyimpannya dalam dictionary 'unique_values'
unique_values = {column: df[column].unique() for column in object_columns}
# Menampilkan nilai unik untuk setiap kolom bertipe 'object'
for column, values in unique_values.items():
    print(f"Unique values in '{column}':")
    print(values)
    print()

# Menampilkan informasi ringkas tentang DataFrame 'df'
df

# Membersihkan dan mengubah tipe data 'Transaction Value' ke float
df['Transaction Value'] = df['Transaction Value'].str.replace(',', '', regex=False).astype(float)
# Menampilkan 5 nilai pertama dari kolom 'Transaction Value' setelah perubahan
print(df['Transaction Value'].head())
# Menampilkan tipe data dari kolom 'Transaction Value' untuk memastikan bahwa tipe data sudah diubah menjadi float
print(df['Transaction Value'].dtype)

# Menghapus whitespace di awal atau akhir nilai pada kolom 'Specialization'
df['Specialization'] = df['Specialization'].str.strip()
# Menampilkan nilai unik yang ada dalam kolom 'Specialization' setelah whitespace dihapus
print(df['Specialization'].unique())

# Menggunakan pd.get_dummies() untuk melakukan one-hot encoding pada kolom kategorikal yang disebutkan.
# Kolom-kolom yang akan diubah menjadi kolom dummy (biner) adalah 'Lead Source', 'City', 'Country',
# 'Monthly Cohort', 'Q Cohort', 'Q Cohort2', 'Q Cohort3', dan 'Specialization'.
df = pd.get_dummies(df, columns=['Lead Source', 'City', 'Country', 'Monthly Cohort', 'Q Cohort', 'Q Cohort2', 'Q Cohort3', 'Specialization'])
# Menampilkan 5 baris pertama DataFrame setelah proses one-hot encoding
df.head()

# Menampilkan informasi ringkas tentang DataFrame 'df'
df.info()

"""# Modeling"""

from sklearn.preprocessing import StandardScaler, OneHotEncoder
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Separate buyer and supplier data
buyer_features = ['Lead Source', 'City', 'Type Of Customer', 'Monthly Cohort']
supplier_features = [' Production Capacity (40ft/month)', 'Size of Factory (SQM)', 'Specialization', 'Price', 'Status', 'Quality', 'Capacity']

# One-hot encoding for categorical variables
encoder = OneHotEncoder()
buyer_encoded = encoder.fit_transform(final_df[buyer_features]).toarray()
supplier_encoded = encoder.fit_transform(final_df[supplier_features]).toarray()

# Membersihkan dan mengubah tipe data kolom 'Transaction Value' dan 'Number of Employees'
final_df['Transaction Value'] = final_df['Transaction Value'].str.replace(',', '').astype(float)

# Jika 'Number of Employees' juga berbentuk string, ubah menjadi float
final_df['Number of Employees'] = final_df['Number of Employees'].astype(float)

# Terapkan feature scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(final_df[['Transaction Value', 'Number of Employees']])

# Combine buyer and supplier features
X_buyer = pd.concat([pd.DataFrame(buyer_encoded), pd.DataFrame(scaled_features)], axis=1)
X_supplier = pd.concat([pd.DataFrame(supplier_encoded), pd.DataFrame(scaled_features)], axis=1)

# Target variable (example: buyer's satisfaction or rating)
y = final_df['Total Score']  # Replace with actual target column

from sklearn.model_selection import train_test_split
# Split data into training and testing
X_train_buyer, X_test_buyer, y_train, y_test = train_test_split(X_buyer, y, test_size=0.2, random_state=42)
X_train_supplier, X_test_supplier = train_test_split(X_supplier, test_size=0.2, random_state=42)

# Define the neural network model
def create_model(input_dim):
    model = Sequential([
        Dense(128, activation='relu', input_dim=input_dim),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(1, activation='sigmoid')  # Regression or binary classification
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])  # Adjust loss for task type
    return model

# Build models for buyer and supplier
model_buyer = create_model(X_train_buyer.shape[1])
model_supplier = create_model(X_train_supplier.shape[1])

# Train the buyer model
model_buyer.fit(X_train_buyer, y_train, epochs=20, batch_size=32, validation_split=0.2)

#Train the supplier model
model_supplier.fit(X_train_supplier, y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate models
buyer_eval = model_buyer.evaluate(X_test_buyer, y_test)
supplier_eval = model_supplier.evaluate(X_test_supplier, y_test)

print(f"Buyer model evaluation: {buyer_eval}")
print(f"Supplier model evaluation: {supplier_eval}")

