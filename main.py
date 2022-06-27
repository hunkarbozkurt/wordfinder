def harf_say():
    d=input("büyük metni giriniz : ")
    g=input("aranacak metni giriniz")
    a=-1
    f=0
    while a<11111:
        i=d.find(g,a+1)
        a=i
        if not a==-1:
            b=a+1
            f+=1
            print(f,". sıradaki",":",b,". harfte")
        if a==-1:
            break
# b ve f'ye +1'lerin koyulma sebepleri sayaçların 0'dan başlamasını engelleyip 1'den başlatmaktır.
# -1 break yapmamın sebebi -1'i de saymasın diye. çünkü anlamsızca -1'i de hesaba katıyor.
# a'ya -1 dememin sebebi hem a+1 ile sayısını artırsın hem de ilk sayının 0 olabilmesi için yapılmıştır.
# while a<sayı demememin sebebi while döngüsünde bir sınır olması gerektiği içindir. aksi taktirde kendisini durduramaz.


print(harf_say())






