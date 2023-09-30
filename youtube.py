from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("Bilinmeyen bir hata oluştu. Lütfen internet bağlantınızı kontrol ediniz :)")
    print("İndirme işlemi başarıyla tamamlandı :D")
    print("44shell tarafından yapılmıştır.")


link = input("İndirmek istediğiniz videonun linkini giriniz: ")
Download(link)
