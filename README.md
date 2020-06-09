# Cars Crawler

Install
----
Projeyi docker üzerinde çalıştırmak için:
    
    $ git clone git@github.com:omeraslandogdu/carscrawler.git
    $ cd /Projenin konumu
    $ docker-compose up --build
    $ docker-compose up -d
    
Start
---
Yeni terminal sekmesinde bashlere erişmek için:

    $ docker-compose exec app bash
    
Uygulamayı çalıştırmak için :

    root:/app# python manage.py migrate
    
Scrapy'yi çalıştırıp crawl işlemlerini başlatmak için:
    
     scrapy crawl cars -a brand=ford
     scrapy crawl cars -a brand=bmw
     
Bu crawl işlemlerinin sonuna,
       
       -s CONCURRENT_ITEMS=1 -s CONCURRENT_REQUESTS=1 -s DOWNLOAD_DELAY=6.0  -s RANDOMIZE_DOWNLOAD_DELAY=False -s DOWNLOAD_TIMEOUT=30.0
    
parametrelerini ekleyerek crawl işlemi sırasında sisteme bindirilen yükü de kontrol altında tutabiliriz.