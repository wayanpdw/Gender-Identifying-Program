# Gender Prediction Program

from sklearn import tree
print("\n=========================")
print("GENDER IDENTIFYING PRORAM\n")
#[height, weight, shoe size]
X = [[181,80,44], [165, 70, 41], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,45], [154,44,38]]
Y = ['Laki-Laki', 'Laki-Laki', 'Laki-Laki', 'Perempuan', 'Perempuan', 'Perempuan', 'Laki-Laki', 'Perempuan']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

Tinggi = int(input("Masukan Tinggi Badan : "))
Berat = int(input("Masukan Berat Badan : "))
Sepatu = int(input("Masukan Ukuran Sepatu : "))

prediction = clf.predict([[Tinggi,Berat,Sepatu]])
print("\nPrediksi gender: ", prediction, "")
print("=========================\n")
