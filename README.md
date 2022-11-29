# Todo-App-With-Using-Fast-API
1) Dosyaları çalıştırmak için ilk olarak Todo App klasörü indirilir.
2) connection.py dosyası,identifier.sqlite ve Todoapp.py dosyaları aynı klasör içinde olacak şekilde compilerda görüntülenir.
3) Terminale " -pip install fastapi " yazılarak. Fast API kurulur.
4) Terminale " -pip install uvicorn " yazılarak sanal çevre oluşturulur. 
5) " uvicorn Todoapp:app --reload " komutu kullanılarak uygulama çalıştırılır.
6) DB ile bağlantı sağlanır ve URL alınır. 
7) Alınan URL postman üzerinde çalıştırılır ve DB görüntülenir.
8) URL sonuna /docs eklenerek postman açılır.
9) Postman üzerinde GET - POST -PUT- DELETE işlemleri gerçekleştirilir.
10) Görev 1 deki bütün isterler postman üzerinde gerekli fonksiyonlar kullanılar gerçeklenir.

NOT: Görev-1 sırasında karşılatığım sorunlardan en önemlisi DB ilişkilendirmesi oldu. Bulduğum kod bloklarını kendi DB'ime konfigüre ederken ve anlamaya çalışırken zorlandım. İkinci önemli sorunum uuid atamak oldu. Oluşturduğum DB üzerindeki ID kısmına uuid yerine DB nin sıralı oluşturduğu id atanıyordu ( 1-2-3 diye sırasıyla).Bu sorunu SQL sorgularıyla sıfırdan DB oluşturarak çözdüm. 

# Reverse-String
1) RS.py dosyası indirilir.
2) Compiler da run komutu ile çalıştırılır.
3) Kullanıcıdan girdi istenir.
4) Ekrana girdinin tersi yazırılır.
5) Görev 2 için bütün isterler karşılanır.
