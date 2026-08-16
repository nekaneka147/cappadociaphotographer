# -*- coding: utf-8 -*-
"""cappadociaphotographer.com — 6 dilli statik site ureticisi

Kullanim:  python _src/build_site.py            -> repo kokune uretir
           python _src/build_site.py <klasor>   -> baska klasore uretir (onizleme)

Yeni blog yazisi = _src/posts/ altina bir .json dosyasi (6 dil) + bu script.
"""
import os, json, sys, glob

_HERE = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(_HERE, "posts")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(_HERE)
DOMAIN = "https://cappadociaphotographer.com"
WA_NUM = "905537175240"
EMAIL = "cappadociaphotographer@gmail.com"
IG = "https://www.instagram.com/cappadociaphotographer.couple/"
FB = "https://www.facebook.com/cappadociaphotographercom/"
PIN = "https://tr.pinterest.com/cappadociaphotographer/"

LANG_META = {
    "en": {"dir": "",    "flag": "🇬🇧", "label": "English"},
    "ru": {"dir": "ru",  "flag": "🇷🇺", "label": "Русский"},
    "es": {"dir": "es",  "flag": "🇪🇸", "label": "Español"},
    "fr": {"dir": "fr",  "flag": "🇫🇷", "label": "Français"},
    "ko": {"dir": "ko",  "flag": "🇰🇷", "label": "한국어"},
    "zh": {"dir": "zh",  "flag": "🇨🇳", "label": "中文"},
}

T = {
"en": {
 "meta_title": "Cappadocia Photographer — Wife & Husband Photoshoot Team | Sunrise Balloon Sessions",
 "meta_desc": "Professional photoshoots in Cappadocia with a local wife & husband team. Sunrise hot-air balloon sessions, flying dress, wild horses, cave hotels. All photos included — book via WhatsApp.",
 "wa_text": "Hello! I would like to book a photoshoot in Cappadocia.",
 "nav": ["Packages","Experiences","Gallery","Reviews","About","FAQ"],
 "nav_cta": "Book Now",
 "hero_loc": "Göreme · Cappadocia · Türkiye",
 "hero_title": 'Your Cappadocia story, told in <em>golden light</em>',
 "hero_sub": "A local wife & husband photography team capturing couples, families and dreamers among hot-air balloons and fairy chimneys — since 2016.",
 "hero_cta1": "Book via WhatsApp",
 "hero_cta2": "See Packages",
 "hero_scroll": "scroll",
 "pk_kicker": "Photoshoot Packages",
 "pk_title": 'Choose your <em>light</em>',
 "pk_intro": "Every session includes hotel pick-up, the best photo spots in Cappadocia and ALL of your digital photos. No hidden fees — message us for current prices and available dates.",
 "pk_popular": "Most Popular",
 "pk_cta": "Get a Quote",
 "packs": [
  {"time":"Sunrise · 2–2.5 h","name":"Sunrise Session","tag":"Hundreds of balloons above you",
   "feats":["Hotel pick-up with our car","Shoot with hot-air balloons at dawn","3 best sunrise locations","3 signature props included","All digital photos + 20 fine edits","Unlimited outfit changes"]},
  {"time":"Sunset · 2–2.5 h","name":"Sunset Session","tag":"Golden hour over the valleys",
   "feats":["Hotel pick-up with our car","3 best sunset locations","Optional: 200–300 wild horses","3 signature props included","All digital photos + 20 fine edits","Unlimited outfit changes"]},
  {"time":"Full Day","name":"Full-Day Story","tag":"Sunrise to sunset, the whole dream",
   "feats":["Sunrise + sunset sessions","Cave hotel & valley scenes","Carpet shop & lantern shop","Camel & vintage props available","All digital photos + 40 fine edits","Your personal photo-guide all day"]},
  {"time":"Cinematic","name":"Video & Proposal","tag":"For once-in-a-lifetime moments",
   "feats":["Marriage proposal planning","Cinematic video clip add-on","Discreet shooting for surprises","Best viewpoints, zero crowds","All footage delivered","Combine with any photo package"]},
 ],
 "ex_kicker": "Signature Experiences",
 "ex_title": 'Only possible <em>here</em>',
 "ex_intro": "Cappadocia is the world's dreamiest backdrop — and we know every corner of it. These are the scenes our guests fly across the world for.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Traveler watching dozens of hot-air balloons rise over Cappadocia at sunrise",
   "t":"Hot-Air Balloon Sunrise","p":"Every clear morning, a hundred balloons fill the sky above the fairy chimneys. We position you on private viewpoints where the whole spectacle unfolds behind you — the photo everyone dreams of, done right."},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Bride in a flowing dress during a photoshoot in the Cappadocia valleys",
   "t":"Flying Dress & Bridal","p":"Our famous flowing-dress shots against sunrise valleys. We bring the dresses, help you pose, and catch the fabric at the perfect moment. Wedding, honeymoon or just because — you deserve this frame."},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Couple in wedding attire at golden hour in a Cappadocia valley",
   "t":"Wild Horses at Sunset","p":"A herd of 200–300 half-wild horses roams the valleys at golden hour. Riding or standing among them as the sun drops behind Erciyes is the most cinematic frame Cappadocia offers."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Guest standing under hundreds of glowing mosaic lanterns in a Cappadocia shop",
   "t":"Lantern & Carpet Shops","p":"Centuries-old carpet shops glowing with mosaic lanterns — Cappadocia's most magical indoor scene. Perfect for rainy days, and impossible to leave without a favorite photo."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Photoshoot on a cave hotel terrace overlooking Cappadocia",
   "t":"Cave Hotel Terraces","p":"Breakfast on a stone terrace while balloons drift past — we can start your session right at your hotel, then move through the valleys as the light changes."},
 ],
 "st_kicker": "How It Works",
 "st_title": 'Booking is <em>simple</em>',
 "steps": [
  {"t":"Pick your package","p":"Read every detail above and choose what fits your travel plan — or ask us what suits your dates best."},
  {"t":"Message us on WhatsApp","p":"We reply within hours with availability, current prices and everything you want to know. Ask us anything, anytime."},
  {"t":"Reserve your date","p":"A small booking payment locks your sunrise or sunset. The rest is paid on the day of your shoot."},
  {"t":"Enjoy your session","p":"We pick you up, guide every pose, and deliver all your photos — the 20 finest, hand-edited."},
 ],
 "ga_kicker": "Gallery",
 "ga_title": 'Frames from the <em>valleys</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Hot-air balloons floating close to the rock formations of Göreme valley","cap":"Göreme, first light"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Guest among colorful kilims and carpets in a Cappadocia carpet shop","cap":"Carpet shop session"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Wedding couple facing each other at golden hour in Cappadocia","cap":"Golden hour vows"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Couple during their photoshoot in Göreme, Cappadocia","cap":"Göreme mornings"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Bride and groom posing in soft light during a Cappadocia wedding shoot","cap":"Just married"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Photoshoot scene across the valleys of Cappadocia","cap":"Valley wandering"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Engagement photoshoot in Cappadocia","cap":"She said yes"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Couple celebrating their anniversary with a photoshoot in Cappadocia","cap":"Anniversary light"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Photographer at work during a session in Cappadocia","cap":"Behind the lens"},
 ],
 "rv_kicker": "Guest Words",
 "rv_title": 'Loved by travelers <em>worldwide</em>',
 "reviews": [
  {"txt":"Thank you so much for capturing the beautiful moments of our engagement. You guys are the sweetest couple photographers — assisting with the balloon setup, staying flexible, taking us to beautiful and cool spots. Still in awe. Highly recommend this duo for any Cappadocia moment you want to capture!","name":"Tim & Linh","type":"Engagement"},
  {"txt":"We always dreamt about seeing the hot-air balloons at Cappadocia and documenting it. The weather didn't let the balloons fly, but we still had an amazing time — the photoshoot was fun and natural, and the pictures turned out exactly how we hoped. Kudos to the both of them!","name":"Willius & Qinghui","type":"Couple"},
  {"txt":"Really loved the way these two handled our shoot. We had an infant with us and they were accommodating and patient throughout. We enjoyed the shoot and the locations a lot — a must-do activity!","name":"Aayushi & Aakash","type":"Family"},
 ],
 "ab_kicker": "About Us",
 "ab_title": 'A wife & husband <em>behind the lens</em>',
 "ab_p1": "We are a local couple who fell in love with photography — and with photographing love. For nearly a decade we have guided travelers through sunrise valleys, secret viewpoints and glowing lantern shops, turning their Cappadocia trip into images they keep forever.",
 "ab_p2": "Because we live here, we know exactly where the light lands at 6 a.m., which valley the horses cross at dusk, and how to time the balloons behind you. And because we are two, one of us guides your poses while the other catches the candid in-between moments — the ones you'll love most.",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","working since"],["1000+","happy guests"],["4 h","reply time"]],
 "ab_alt": "Cappadocia photographer couple at work in the valleys",
 "fq_kicker": "Questions",
 "fq_title": 'Before you <em>ask</em>',
 "faqs": [
  {"q":"When is the best time for a photoshoot in Cappadocia?","a":"Sunrise, all year round — that's when the balloons fly and the light is softest. Sunset is a close second with warm golden light and far fewer people. April–June and September–November have the most stable weather, but winter snow sessions are breathtaking too."},
  {"q":"Are the hot-air balloons guaranteed?","a":"Balloons fly on most clear mornings, but flights are weather-dependent and can be cancelled by the aviation authority. If they don't fly on your date, we adapt the session to the valleys and props — and the photos are still magical (our guests say so themselves)."},
  {"q":"How many photos do we receive?","a":"All of them. Every good digital photo from your session is yours, plus 20 professionally hand-edited picks (40 on full-day sessions). Delivery is via online gallery within days."},
  {"q":"What should we wear?","a":"Long flowing dresses photograph beautifully against the valleys — we also provide our famous flying dresses and props. Bring a second outfit; changes are unlimited. We'll send you a full style guide after booking."},
  {"q":"How do we book and pay?","a":"Message us on WhatsApp with your dates. A small booking payment secures your sunrise or sunset slot; the remainder is paid in cash or transfer on the day of the shoot."},
  {"q":"Do you speak English?","a":"Yes — we work with guests from all over the world every week and typically reply on WhatsApp within four hours."},
 ],
 "ct_kicker": "Ready when you are",
 "ct_title": 'Let’s plan your <em>Cappadocia</em> session',
 "ct_sub": "Tell us your travel dates and we'll take care of the rest — locations, props, timing and the light.",
 "ct_wa": "Message on WhatsApp",
 "ct_ig": "DM on Instagram",
 "ct_or": "or write to",
 "ft_follow": "Follow",
 "ft_rights": "All photographs © Cappadocia Photographer",
 "blog_kicker": "Journal",
 "blog_more": "Read the journal",
},

"ru": {
 "meta_title": "Фотограф в Каппадокии — семейная пара фотографов | Фотосессии на рассвете с шарами",
 "meta_desc": "Профессиональные фотосессии в Каппадокии от местной пары фотографов. Рассвет с воздушными шарами, летящее платье, дикие лошади, пещерные отели. Все фото включены — бронируйте в WhatsApp.",
 "wa_text": "Здравствуйте! Хочу забронировать фотосессию в Каппадокии.",
 "nav": ["Пакеты","Впечатления","Галерея","Отзывы","О нас","Вопросы"],
 "nav_cta": "Забронировать",
 "hero_loc": "Гёреме · Каппадокия · Турция",
 "hero_title": 'Ваша история в Каппадокии — в <em>золотом свете</em>',
 "hero_sub": "Местная пара фотографов — муж и жена. Снимаем пары, семьи и мечтателей среди воздушных шаров и сказочных дымоходов с 2016 года.",
 "hero_cta1": "Написать в WhatsApp",
 "hero_cta2": "Смотреть пакеты",
 "hero_scroll": "листайте",
 "pk_kicker": "Пакеты фотосессий",
 "pk_title": 'Выберите свой <em>свет</em>',
 "pk_intro": "В каждую сессию входит трансфер из отеля, лучшие локации Каппадокии и ВСЕ ваши цифровые фотографии. Без скрытых платежей — напишите нам, чтобы узнать актуальные цены и свободные даты.",
 "pk_popular": "Хит",
 "pk_cta": "Узнать цену",
 "packs": [
  {"time":"Рассвет · 2–2,5 ч","name":"Рассветная сессия","tag":"Сотни шаров над вами",
   "feats":["Трансфер из отеля на нашей машине","Съёмка с воздушными шарами на рассвете","3 лучшие рассветные локации","3 фирменных реквизита включены","Все цифровые фото + 20 в ретуши","Смена нарядов без ограничений"]},
  {"time":"Закат · 2–2,5 ч","name":"Закатная сессия","tag":"Золотой час над долинами",
   "feats":["Трансфер из отеля на нашей машине","3 лучшие закатные локации","Опция: 200–300 диких лошадей","3 фирменных реквизита включены","Все цифровые фото + 20 в ретуши","Смена нарядов без ограничений"]},
  {"time":"Весь день","name":"История на весь день","tag":"От рассвета до заката",
   "feats":["Рассветная + закатная сессии","Пещерный отель и долины","Магазин ковров и фонарей","Верблюд и винтажный реквизит","Все цифровые фото + 40 в ретуши","Личный фотогид на весь день"]},
  {"time":"Кино","name":"Видео и предложение","tag":"Для моментов раз в жизни",
   "feats":["Организация предложения руки и сердца","Кинематографичный видеоклип","Незаметная съёмка для сюрприза","Лучшие точки без толпы","Весь отснятый материал — ваш","Сочетается с любым фотопакетом"]},
 ],
 "ex_kicker": "Фирменные впечатления",
 "ex_title": 'Возможно только <em>здесь</em>',
 "ex_intro": "Каппадокия — самый сказочный фон в мире, и мы знаем здесь каждый уголок. Ради этих кадров наши гости летят через полмира.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Путешественница смотрит на десятки воздушных шаров над Каппадокией на рассвете",
   "t":"Рассвет с воздушными шарами","p":"Каждое ясное утро сотня шаров поднимается над сказочными дымоходами. Мы ставим вас на приватных точках, где всё это волшебство разворачивается у вас за спиной — кадр мечты, снятый как надо."},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Невеста в летящем платье на фотосессии в долинах Каппадокии",
   "t":"Летящее платье","p":"Наши знаменитые кадры с летящим платьем на фоне рассветных долин. Платья привозим мы, помогаем с позами и ловим ткань в идеальный момент. Свадьба, медовый месяц или просто так — вы заслужили этот кадр."},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Пара в свадебных нарядах в золотой час в долине Каппадокии",
   "t":"Дикие лошади на закате","p":"Табун из 200–300 полудиких лошадей гуляет по долинам в золотой час. Стоять среди них, когда солнце садится за Эрджиес, — самый кинематографичный кадр Каппадокии."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Гостья под сотнями светящихся мозаичных фонарей в лавке Каппадокии",
   "t":"Лавки ковров и фонарей","p":"Старинные ковровые лавки, залитые светом мозаичных фонарей, — самая волшебная «крытая» сцена Каппадокии. Идеально в дождливый день, и уйти без любимого кадра невозможно."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Фотосессия на террасе пещерного отеля с видом на Каппадокию",
   "t":"Террасы пещерных отелей","p":"Завтрак на каменной террасе, мимо плывут шары — мы можем начать съёмку прямо в вашем отеле, а затем отправиться по долинам вслед за светом."},
 ],
 "st_kicker": "Как это работает",
 "st_title": 'Бронировать <em>просто</em>',
 "steps": [
  {"t":"Выберите пакет","p":"Изучите детали выше и выберите то, что подходит под ваш маршрут, — или спросите нас, что лучше для ваших дат."},
  {"t":"Напишите в WhatsApp","p":"Мы отвечаем в течение нескольких часов: свободные даты, актуальные цены и ответы на любые вопросы."},
  {"t":"Закрепите дату","p":"Небольшая предоплата бронирует ваш рассвет или закат. Остальное — в день съёмки."},
  {"t":"Наслаждайтесь съёмкой","p":"Мы забираем вас из отеля, подсказываем каждую позу и отдаём все фотографии — 20 лучших в авторской ретуши."},
 ],
 "ga_kicker": "Галерея",
 "ga_title": 'Кадры из <em>долин</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Воздушные шары над скалами долины Гёреме","cap":"Гёреме, первый свет"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Гостья среди разноцветных килимов в ковровой лавке Каппадокии","cap":"Ковровая лавка"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Свадебная пара в золотой час в Каппадокии","cap":"Клятвы в золотой час"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Пара на фотосессии в Гёреме","cap":"Утро в Гёреме"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Жених и невеста в мягком свете на свадебной съёмке в Каппадокии","cap":"Молодожёны"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Сцена фотосессии в долинах Каппадокии","cap":"Прогулка по долинам"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Помолвка в Каппадокии","cap":"Она сказала «да»"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Пара отмечает годовщину фотосессией в Каппадокии","cap":"Свет годовщины"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Фотограф за работой в Каппадокии","cap":"За кадром"},
 ],
 "rv_kicker": "Слова гостей",
 "rv_title": 'Нас любят путешественники <em>всего мира</em>',
 "reviews": [
  {"txt":"Огромное спасибо за прекрасные моменты нашей помолвки! Вы — самая милая пара фотографов: помогли с шарами, были гибкими, отвезли нас в невероятно красивые места. До сих пор под впечатлением. Очень рекомендуем этот дуэт для любых кадров в Каппадокии!","name":"Тим и Линь","type":"Помолвка"},
  {"txt":"Мы всегда мечтали увидеть воздушные шары Каппадокии и запечатлеть это. Погода не дала шарам взлететь, но мы всё равно отлично провели время — съёмка была лёгкой и естественной, а фото получились ровно такими, как мы хотели!","name":"Виллиус и Цинхуэй","type":"Пара"},
  {"txt":"Очень понравилось, как эти двое провели нашу съёмку. С нами был младенец, и они были внимательны и терпеливы всё время. Локации чудесные — маст-ду активность!","name":"Аюши и Аакаш","type":"Семья"},
 ],
 "ab_kicker": "О нас",
 "ab_title": 'Муж и жена <em>за объективом</em>',
 "ab_p1": "Мы — местная пара, влюблённая в фотографию и в съёмку любви. Почти десять лет мы водим путешественников по рассветным долинам, тайным смотровым точкам и светящимся лавкам фонарей, превращая поездку в Каппадокию в кадры на всю жизнь.",
 "ab_p2": "Мы живём здесь, поэтому точно знаем, куда падает свет в 6 утра, какую долину лошади переходят в сумерках и как поймать шары у вас за спиной. А поскольку нас двое — один ставит позы, а другой ловит живые моменты между ними. Именно их вы полюбите больше всего.",
 "ab_sign": "— Кашиф и Бахар",
 "stats": [["2016","работаем с"],["1000+","счастливых гостей"],["4 ч","время ответа"]],
 "ab_alt": "Пара фотографов Каппадокии за работой в долинах",
 "fq_kicker": "Вопросы",
 "fq_title": 'Прежде чем <em>спросить</em>',
 "faqs": [
  {"q":"Когда лучше всего фотографироваться в Каппадокии?","a":"На рассвете, круглый год: именно тогда летают шары и свет самый мягкий. Закат — на втором месте: тёплый золотой свет и гораздо меньше людей. Самая стабильная погода — апрель–июнь и сентябрь–ноябрь, но зимние съёмки в снегу тоже потрясающие."},
  {"q":"Шары гарантированы?","a":"Шары летают почти каждое ясное утро, но полёты зависят от погоды и разрешения авиации. Если в вашу дату они не полетят, мы перестроим съёмку на долины и реквизит — фотографии всё равно получаются волшебными."},
  {"q":"Сколько фотографий мы получим?","a":"Все. Каждый удачный цифровой кадр с вашей съёмки — ваш, плюс 20 профессионально отретушированных (40 в пакете на весь день). Доставка через онлайн-галерею за несколько дней."},
  {"q":"Что надеть?","a":"Длинные летящие платья смотрятся в долинах великолепно — знаменитые «летящие платья» и реквизит мы привозим сами. Возьмите второй наряд: переодевания без ограничений. После бронирования пришлём гид по стилю."},
  {"q":"Как бронировать и платить?","a":"Напишите нам в WhatsApp с датами поездки. Небольшая предоплата закрепляет ваш рассвет или закат, остальное — наличными или переводом в день съёмки."},
  {"q":"Говорите ли вы по-английски?","a":"Да, мы каждую неделю работаем с гостями со всего мира и обычно отвечаем в WhatsApp в течение четырёх часов."},
 ],
 "ct_kicker": "Мы готовы, когда готовы вы",
 "ct_title": 'Спланируем вашу съёмку в <em>Каппадокии</em>',
 "ct_sub": "Напишите даты поездки — остальное мы возьмём на себя: локации, реквизит, тайминг и свет.",
 "ct_wa": "Написать в WhatsApp",
 "ct_ig": "Написать в Instagram",
 "ct_or": "или на почту",
 "ft_follow": "Соцсети",
 "ft_rights": "Все фотографии © Cappadocia Photographer",
 "blog_kicker": "Журнал",
 "blog_more": "Читать журнал",
},

"es": {
 "meta_title": "Fotógrafo en Capadocia — equipo de esposos | Sesiones al amanecer con globos",
 "meta_desc": "Sesiones de fotos profesionales en Capadocia con una pareja local de fotógrafos. Amanecer con globos aerostáticos, vestido volador, caballos salvajes, hoteles cueva. Todas las fotos incluidas — reserva por WhatsApp.",
 "wa_text": "¡Hola! Me gustaría reservar una sesión de fotos en Capadocia.",
 "nav": ["Paquetes","Experiencias","Galería","Opiniones","Nosotros","Preguntas"],
 "nav_cta": "Reservar",
 "hero_loc": "Göreme · Capadocia · Turquía",
 "hero_title": 'Tu historia en Capadocia, contada en <em>luz dorada</em>',
 "hero_sub": "Somos un matrimonio local de fotógrafos que retrata a parejas, familias y soñadores entre globos aerostáticos y chimeneas de hadas — desde 2016.",
 "hero_cta1": "Reservar por WhatsApp",
 "hero_cta2": "Ver paquetes",
 "hero_scroll": "desliza",
 "pk_kicker": "Paquetes de sesiones",
 "pk_title": 'Elige tu <em>luz</em>',
 "pk_intro": "Cada sesión incluye recogida en el hotel, los mejores rincones de Capadocia y TODAS tus fotos digitales. Sin costes ocultos — escríbenos para precios actuales y fechas disponibles.",
 "pk_popular": "Más popular",
 "pk_cta": "Pedir precio",
 "packs": [
  {"time":"Amanecer · 2–2,5 h","name":"Sesión al amanecer","tag":"Cientos de globos sobre ti",
   "feats":["Recogida en tu hotel con nuestro coche","Sesión con globos al alba","Las 3 mejores localizaciones del amanecer","3 props exclusivos incluidos","Todas las fotos digitales + 20 editadas","Cambios de vestuario ilimitados"]},
  {"time":"Atardecer · 2–2,5 h","name":"Sesión al atardecer","tag":"Hora dorada sobre los valles",
   "feats":["Recogida en tu hotel con nuestro coche","Las 3 mejores localizaciones del ocaso","Opcional: 200–300 caballos salvajes","3 props exclusivos incluidos","Todas las fotos digitales + 20 editadas","Cambios de vestuario ilimitados"]},
  {"time":"Día completo","name":"Historia de un día","tag":"Del amanecer al ocaso, el sueño entero",
   "feats":["Sesión de amanecer + atardecer","Hotel cueva y valles","Tienda de alfombras y farolillos","Camello y props vintage disponibles","Todas las fotos digitales + 40 editadas","Tu fotógrafo-guía todo el día"]},
  {"time":"Cine","name":"Vídeo y pedida","tag":"Para momentos únicos en la vida",
   "feats":["Organización de pedidas de mano","Videoclip cinematográfico","Fotografía discreta para sorpresas","Los mejores miradores sin multitudes","Todo el material entregado","Combinable con cualquier paquete"]},
 ],
 "ex_kicker": "Experiencias únicas",
 "ex_title": 'Solo posible <em>aquí</em>',
 "ex_intro": "Capadocia es el escenario más soñado del mundo — y conocemos cada rincón. Por estas imágenes nuestros huéspedes cruzan medio planeta.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Viajera contemplando decenas de globos aerostáticos sobre Capadocia al amanecer",
   "t":"Amanecer con globos","p":"Cada mañana despejada, cien globos llenan el cielo sobre las chimeneas de hadas. Te situamos en miradores privados donde todo el espectáculo se despliega a tu espalda — la foto que todos sueñan, bien hecha."},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Novia con vestido vaporoso durante una sesión en los valles de Capadocia",
   "t":"Vestido volador y novias","p":"Nuestras famosas fotos con vestidos al viento sobre los valles del amanecer. Traemos los vestidos, te guiamos en las poses y capturamos la tela en el momento exacto. Boda, luna de miel o simplemente porque sí."},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Pareja vestida de boda a la hora dorada en un valle de Capadocia",
   "t":"Caballos salvajes al ocaso","p":"Una manada de 200–300 caballos semisalvajes recorre los valles a la hora dorada. Posar entre ellos mientras el sol cae tras el Erciyes es el plano más cinematográfico de Capadocia."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Huésped bajo cientos de farolillos de mosaico encendidos en una tienda de Capadocia",
   "t":"Farolillos y alfombras","p":"Tiendas de alfombras centenarias iluminadas por farolillos de mosaico: la escena interior más mágica de Capadocia. Perfecta para días de lluvia, e imposible salir sin una foto favorita."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Sesión de fotos en la terraza de un hotel cueva con vistas a Capadocia",
   "t":"Terrazas de hoteles cueva","p":"Desayuno en una terraza de piedra mientras pasan los globos — podemos empezar tu sesión en tu propio hotel y seguir por los valles según cambia la luz."},
 ],
 "st_kicker": "Cómo funciona",
 "st_title": 'Reservar es <em>fácil</em>',
 "steps": [
  {"t":"Elige tu paquete","p":"Revisa los detalles y elige el que encaje con tu viaje — o pregúntanos qué conviene a tus fechas."},
  {"t":"Escríbenos por WhatsApp","p":"Respondemos en pocas horas con disponibilidad, precios actuales y todo lo que quieras saber."},
  {"t":"Asegura tu fecha","p":"Un pequeño pago de reserva bloquea tu amanecer o atardecer. El resto se paga el día de la sesión."},
  {"t":"Disfruta tu sesión","p":"Te recogemos, te guiamos en cada pose y te entregamos todas tus fotos — las 20 mejores, editadas a mano."},
 ],
 "ga_kicker": "Galería",
 "ga_title": 'Instantes de los <em>valles</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Globos aerostáticos flotando junto a las formaciones rocosas de Göreme","cap":"Göreme, primera luz"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Huésped entre kilims y alfombras de colores en Capadocia","cap":"Tienda de alfombras"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Pareja de novios a la hora dorada en Capadocia","cap":"Votos dorados"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Pareja en su sesión de fotos en Göreme","cap":"Mañanas de Göreme"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Novios posando con luz suave en Capadocia","cap":"Recién casados"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Sesión fotográfica en los valles de Capadocia","cap":"Paseo por los valles"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Sesión de pedida en Capadocia","cap":"Dijo que sí"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Pareja celebrando su aniversario en Capadocia","cap":"Luz de aniversario"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Fotógrafo trabajando durante una sesión en Capadocia","cap":"Tras el objetivo"},
 ],
 "rv_kicker": "Voces de huéspedes",
 "rv_title": 'Queridos por viajeros de <em>todo el mundo</em>',
 "reviews": [
  {"txt":"Mil gracias por capturar los momentos de nuestra pedida. Sois la pareja de fotógrafos más encantadora: ayudasteis con los globos, fuisteis flexibles y nos llevasteis a rincones preciosos. Aún estoy maravillado. ¡Recomendadísimos para cualquier momento en Capadocia!","name":"Tim y Linh","type":"Pedida"},
  {"txt":"Siempre soñamos con ver los globos de Capadocia y documentarlo. El clima no dejó volar los globos, pero lo pasamos genial igualmente: la sesión fue divertida y natural, y las fotos salieron exactamente como esperábamos.","name":"Willius y Qinghui","type":"Pareja"},
  {"txt":"Nos encantó cómo llevaron nuestra sesión. Íbamos con un bebé y fueron pacientes y atentos en todo momento. Disfrutamos muchísimo la sesión y las localizaciones — ¡actividad imprescindible!","name":"Aayushi y Aakash","type":"Familia"},
 ],
 "ab_kicker": "Nosotros",
 "ab_title": 'Un matrimonio <em>tras la cámara</em>',
 "ab_p1": "Somos una pareja local enamorada de la fotografía — y de fotografiar el amor. Desde hace casi una década guiamos a viajeros por valles al amanecer, miradores secretos y tiendas de farolillos, convirtiendo su viaje a Capadocia en imágenes para siempre.",
 "ab_p2": "Vivimos aquí, así que sabemos exactamente dónde cae la luz a las 6 de la mañana, qué valle cruzan los caballos al anochecer y cómo situar los globos a tu espalda. Y como somos dos, uno guía tus poses mientras el otro captura los momentos espontáneos — los que más amarás.",
 "ab_sign": "— Kaşif y Bahar",
 "stats": [["2016","desde"],["1000+","huéspedes felices"],["4 h","tiempo de respuesta"]],
 "ab_alt": "Pareja de fotógrafos de Capadocia trabajando en los valles",
 "fq_kicker": "Preguntas",
 "fq_title": 'Antes de <em>preguntar</em>',
 "faqs": [
  {"q":"¿Cuál es la mejor hora para una sesión en Capadocia?","a":"El amanecer, todo el año: es cuando vuelan los globos y la luz es más suave. El atardecer es el segundo mejor momento, con luz dorada y mucha menos gente. Abril–junio y septiembre–noviembre tienen el clima más estable, aunque las sesiones con nieve en invierno son impresionantes."},
  {"q":"¿Los globos están garantizados?","a":"Los globos vuelan casi todas las mañanas despejadas, pero dependen del clima y de la autoridad aérea. Si no vuelan en tu fecha, adaptamos la sesión a los valles y los props — y las fotos siguen siendo mágicas."},
  {"q":"¿Cuántas fotos recibimos?","a":"Todas. Cada buena foto digital de tu sesión es tuya, más 20 editadas profesionalmente (40 en el día completo). Entrega por galería online en pocos días."},
  {"q":"¿Qué nos ponemos?","a":"Los vestidos largos y vaporosos quedan preciosos en los valles — también traemos nuestros famosos vestidos voladores y props. Trae un segundo conjunto: los cambios son ilimitados. Tras reservar te enviamos una guía de estilo."},
  {"q":"¿Cómo reservamos y pagamos?","a":"Escríbenos por WhatsApp con tus fechas. Un pequeño pago asegura tu amanecer o atardecer; el resto se abona en efectivo o transferencia el día de la sesión."},
  {"q":"¿Habláis inglés?","a":"Sí — trabajamos cada semana con huéspedes de todo el mundo y solemos responder por WhatsApp en menos de cuatro horas."},
 ],
 "ct_kicker": "Listos cuando tú lo estés",
 "ct_title": 'Planeemos tu sesión en <em>Capadocia</em>',
 "ct_sub": "Cuéntanos tus fechas de viaje y nosotros nos ocupamos del resto: localizaciones, props, horarios y luz.",
 "ct_wa": "Escribir por WhatsApp",
 "ct_ig": "DM en Instagram",
 "ct_or": "o escribe a",
 "ft_follow": "Síguenos",
 "ft_rights": "Todas las fotografías © Cappadocia Photographer",
 "blog_kicker": "Diario",
 "blog_more": "Leer el diario",
},

"fr": {
 "meta_title": "Photographe en Cappadoce — couple de photographes | Séances au lever du soleil avec montgolfières",
 "meta_desc": "Séances photo professionnelles en Cappadoce avec un couple local de photographes. Lever de soleil avec montgolfières, robe volante, chevaux sauvages, hôtels troglodytes. Toutes les photos incluses — réservez via WhatsApp.",
 "wa_text": "Bonjour ! Je souhaite réserver une séance photo en Cappadoce.",
 "nav": ["Formules","Expériences","Galerie","Avis","À propos","FAQ"],
 "nav_cta": "Réserver",
 "hero_loc": "Göreme · Cappadoce · Turquie",
 "hero_title": 'Votre histoire en Cappadoce, écrite en <em>lumière dorée</em>',
 "hero_sub": "Couple local de photographes, nous immortalisons couples, familles et rêveurs parmi les montgolfières et les cheminées de fées — depuis 2016.",
 "hero_cta1": "Réserver sur WhatsApp",
 "hero_cta2": "Voir les formules",
 "hero_scroll": "défiler",
 "pk_kicker": "Formules de séances",
 "pk_title": 'Choisissez votre <em>lumière</em>',
 "pk_intro": "Chaque séance comprend la prise en charge à l'hôtel, les plus beaux spots de Cappadoce et TOUTES vos photos numériques. Aucun frais caché — écrivez-nous pour les tarifs actuels et les disponibilités.",
 "pk_popular": "Préférée",
 "pk_cta": "Demander un tarif",
 "packs": [
  {"time":"Aube · 2–2,5 h","name":"Séance au lever du soleil","tag":"Des centaines de montgolfières au-dessus de vous",
   "feats":["Prise en charge à votre hôtel","Séance avec les montgolfières à l'aube","Les 3 plus beaux spots du lever de soleil","3 accessoires signature inclus","Toutes les photos + 20 retouches fines","Changements de tenue illimités"]},
  {"time":"Crépuscule · 2–2,5 h","name":"Séance au coucher du soleil","tag":"L'heure dorée sur les vallées",
   "feats":["Prise en charge à votre hôtel","Les 3 plus beaux spots du couchant","Option : 200–300 chevaux sauvages","3 accessoires signature inclus","Toutes les photos + 20 retouches fines","Changements de tenue illimités"]},
  {"time":"Journée entière","name":"Histoire d'une journée","tag":"De l'aube au crépuscule, le rêve entier",
   "feats":["Séances lever + coucher du soleil","Hôtel troglodyte et vallées","Boutique de tapis et de lanternes","Chameau et accessoires vintage","Toutes les photos + 40 retouches fines","Votre photographe-guide toute la journée"]},
  {"time":"Cinéma","name":"Vidéo & demande en mariage","tag":"Pour les moments uniques d'une vie",
   "feats":["Organisation de demandes en mariage","Clip vidéo cinématographique","Prise de vue discrète pour les surprises","Les plus beaux points de vue, sans foule","Toutes les images livrées","Cumulable avec toute formule photo"]},
 ],
 "ex_kicker": "Expériences signature",
 "ex_title": 'Possible seulement <em>ici</em>',
 "ex_intro": "La Cappadoce est le décor le plus onirique du monde — et nous en connaissons chaque recoin. Ce sont ces images qui font traverser la planète à nos hôtes.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"Voyageuse contemplant des dizaines de montgolfières au-dessus de la Cappadoce à l'aube",
   "t":"Montgolfières à l'aube","p":"Chaque matin dégagé, une centaine de ballons emplit le ciel au-dessus des cheminées de fées. Nous vous plaçons sur des points de vue privés où tout le spectacle se déploie derrière vous — la photo dont tout le monde rêve, réalisée dans les règles de l'art."},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"Mariée en robe fluide lors d'une séance dans les vallées de Cappadoce",
   "t":"Robe volante & mariée","p":"Nos célèbres clichés de robes flottant au vent face aux vallées de l'aube. Nous apportons les robes, guidons vos poses et saisissons le tissu au moment parfait. Mariage, lune de miel ou juste pour le plaisir."},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Couple en tenue de mariage à l'heure dorée dans une vallée de Cappadoce",
   "t":"Chevaux sauvages au couchant","p":"Un troupeau de 200 à 300 chevaux semi-sauvages parcourt les vallées à l'heure dorée. Poser parmi eux tandis que le soleil plonge derrière l'Erciyes : le plan le plus cinématographique de Cappadoce."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"Invitée sous des centaines de lanternes en mosaïque dans une boutique de Cappadoce",
   "t":"Lanternes & tapis","p":"Des boutiques de tapis centenaires illuminées de lanternes en mosaïque — la scène intérieure la plus magique de Cappadoce. Parfaite les jours de pluie, impossible d'en repartir sans une photo préférée."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"Séance photo sur la terrasse d'un hôtel troglodyte dominant la Cappadoce",
   "t":"Terrasses des hôtels troglodytes","p":"Petit-déjeuner sur une terrasse de pierre pendant que passent les ballons — nous pouvons commencer votre séance à votre hôtel même, puis suivre la lumière à travers les vallées."},
 ],
 "st_kicker": "Comment ça marche",
 "st_title": 'Réserver, c’est <em>simple</em>',
 "steps": [
  {"t":"Choisissez votre formule","p":"Parcourez les détails ci-dessus et choisissez ce qui convient à votre voyage — ou demandez-nous conseil selon vos dates."},
  {"t":"Écrivez-nous sur WhatsApp","p":"Nous répondons en quelques heures : disponibilités, tarifs actuels et réponses à toutes vos questions."},
  {"t":"Bloquez votre date","p":"Un petit acompte réserve votre lever ou coucher de soleil. Le solde se règle le jour de la séance."},
  {"t":"Profitez de votre séance","p":"Nous venons vous chercher, guidons chaque pose et livrons toutes vos photos — dont les 20 plus belles, retouchées à la main."},
 ],
 "ga_kicker": "Galerie",
 "ga_title": 'Instantanés des <em>vallées</em>',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"Montgolfières flottant près des formations rocheuses de Göreme","cap":"Göreme, première lueur"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"Invitée parmi les kilims colorés d'une boutique de tapis de Cappadoce","cap":"Boutique de tapis"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"Couple de mariés à l'heure dorée en Cappadoce","cap":"Vœux dorés"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"Couple lors de sa séance photo à Göreme","cap":"Matins de Göreme"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"Mariés posant dans une lumière douce en Cappadoce","cap":"Jeunes mariés"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"Scène de séance photo dans les vallées de Cappadoce","cap":"Balade dans les vallées"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"Séance de fiançailles en Cappadoce","cap":"Elle a dit oui"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"Couple fêtant son anniversaire de mariage en Cappadoce","cap":"Lumière d'anniversaire"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"Photographe au travail lors d'une séance en Cappadoce","cap":"Derrière l'objectif"},
 ],
 "rv_kicker": "Paroles d'invités",
 "rv_title": 'Aimés par des voyageurs du <em>monde entier</em>',
 "reviews": [
  {"txt":"Merci infiniment d'avoir immortalisé notre demande en fiançailles. Vous êtes le couple de photographes le plus adorable : aide avec les ballons, grande flexibilité, spots magnifiques. Je suis encore émerveillé. Je recommande vivement ce duo pour tout moment en Cappadoce !","name":"Tim & Linh","type":"Fiançailles"},
  {"txt":"Nous rêvions de voir les montgolfières de Cappadoce et d'en garder la trace. La météo ne leur a pas permis de voler, mais nous avons passé un moment formidable — séance fun et naturelle, photos exactement comme espérées !","name":"Willius & Qinghui","type":"Couple"},
  {"txt":"Nous avons adoré leur façon de mener la séance. Nous avions un nourrisson avec nous : ils ont été patients et prévenants du début à la fin. Les lieux étaient superbes — une activité à ne pas manquer !","name":"Aayushi & Aakash","type":"Famille"},
 ],
 "ab_kicker": "À propos",
 "ab_title": 'Un couple <em>derrière l’objectif</em>',
 "ab_p1": "Nous sommes un couple local tombé amoureux de la photographie — et de la photographie de l'amour. Depuis près de dix ans, nous guidons les voyageurs à travers vallées à l'aube, belvédères secrets et boutiques de lanternes, transformant leur voyage en Cappadoce en images pour toujours.",
 "ab_p2": "Nous vivons ici : nous savons exactement où tombe la lumière à 6 h, quelle vallée les chevaux traversent au crépuscule, et comment placer les ballons derrière vous. Et comme nous sommes deux, l'un guide vos poses pendant que l'autre saisit les instants volés — ceux que vous aimerez le plus.",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","depuis"],["1000+","hôtes ravis"],["4 h","délai de réponse"]],
 "ab_alt": "Couple de photographes de Cappadoce au travail dans les vallées",
 "fq_kicker": "Questions",
 "fq_title": 'Avant de <em>demander</em>',
 "faqs": [
  {"q":"Quel est le meilleur moment pour une séance en Cappadoce ?","a":"Le lever du soleil, toute l'année : c'est là que volent les ballons et que la lumière est la plus douce. Le coucher du soleil arrive juste derrière, avec sa lumière dorée et bien moins de monde. Avril–juin et septembre–novembre offrent la météo la plus stable, mais les séances sous la neige sont époustouflantes."},
  {"q":"Les montgolfières sont-elles garanties ?","a":"Elles volent presque chaque matin dégagé, mais les vols dépendent de la météo et de l'autorité aérienne. Si elles ne volent pas à votre date, nous adaptons la séance aux vallées et aux accessoires — et les photos restent magiques."},
  {"q":"Combien de photos recevons-nous ?","a":"Toutes. Chaque bon cliché numérique de votre séance vous appartient, plus 20 retouches professionnelles (40 pour la journée entière). Livraison par galerie en ligne sous quelques jours."},
  {"q":"Comment s'habiller ?","a":"Les robes longues et fluides sont sublimes dans les vallées — nous apportons aussi nos célèbres robes volantes et nos accessoires. Prévoyez une seconde tenue : les changements sont illimités. Un guide de style vous est envoyé après réservation."},
  {"q":"Comment réserver et payer ?","a":"Écrivez-nous sur WhatsApp avec vos dates. Un petit acompte sécurise votre créneau ; le solde se règle en espèces ou par virement le jour de la séance."},
  {"q":"Parlez-vous anglais ?","a":"Oui — nous travaillons chaque semaine avec des hôtes du monde entier et répondons généralement sur WhatsApp en moins de quatre heures."},
 ],
 "ct_kicker": "Prêts quand vous l'êtes",
 "ct_title": 'Planifions votre séance en <em>Cappadoce</em>',
 "ct_sub": "Donnez-nous vos dates de voyage et nous nous occupons du reste : lieux, accessoires, horaires et lumière.",
 "ct_wa": "Écrire sur WhatsApp",
 "ct_ig": "DM sur Instagram",
 "ct_or": "ou écrivez à",
 "ft_follow": "Suivez-nous",
 "ft_rights": "Toutes les photographies © Cappadocia Photographer",
 "blog_kicker": "Journal",
 "blog_more": "Lire le journal",
},

"ko": {
 "meta_title": "카파도키아 스냅 사진작가 — 부부 포토그래퍼 팀 | 열기구 일출 촬영",
 "meta_desc": "현지 부부 사진작가와 함께하는 카파도키아 전문 스냅 촬영. 열기구 일출, 플라잉 드레스, 야생마, 동굴 호텔. 모든 원본 사진 제공 — WhatsApp으로 예약하세요.",
 "wa_text": "안녕하세요! 카파도키아 스냅 촬영을 예약하고 싶습니다.",
 "nav": ["패키지","시그니처","갤러리","후기","소개","FAQ"],
 "nav_cta": "예약하기",
 "hero_loc": "괴레메 · 카파도키아 · 튀르키예",
 "hero_title": '<em>황금빛</em>으로 기록하는 당신의 카파도키아',
 "hero_sub": "2016년부터 열기구와 요정 굴뚝 사이에서 커플, 가족, 여행자의 순간을 담아온 현지 부부 사진작가 팀입니다.",
 "hero_cta1": "WhatsApp 예약",
 "hero_cta2": "패키지 보기",
 "hero_scroll": "스크롤",
 "pk_kicker": "촬영 패키지",
 "pk_title": '당신의 <em>빛</em>을 선택하세요',
 "pk_intro": "모든 촬영에 호텔 픽업, 카파도키아 최고의 촬영 스팟, 그리고 모든 디지털 원본이 포함됩니다. 숨은 비용 없음 — 가격과 예약 가능 날짜는 메시지로 문의하세요.",
 "pk_popular": "인기 1위",
 "pk_cta": "가격 문의",
 "packs": [
  {"time":"일출 · 2–2.5시간","name":"선라이즈 스냅","tag":"머리 위로 수백 개의 열기구",
   "feats":["호텔 픽업 (전용 차량)","새벽 열기구와 함께 촬영","일출 명소 3곳","시그니처 소품 3종 포함","디지털 원본 전체 + 보정본 20장","의상 교체 무제한"]},
  {"time":"일몰 · 2–2.5시간","name":"선셋 스냅","tag":"계곡 위 골든아워",
   "feats":["호텔 픽업 (전용 차량)","일몰 명소 3곳","옵션: 야생마 200–300마리","시그니처 소품 3종 포함","디지털 원본 전체 + 보정본 20장","의상 교체 무제한"]},
  {"time":"풀데이","name":"풀데이 스토리","tag":"일출부터 일몰까지, 꿈의 하루",
   "feats":["일출 + 일몰 촬영","동굴 호텔과 계곡 촬영","카펫 상점 & 랜턴 상점","낙타·빈티지 소품 가능","디지털 원본 전체 + 보정본 40장","하루 종일 전담 포토 가이드"]},
  {"time":"시네마틱","name":"영상 & 프러포즈","tag":"일생에 단 한 번의 순간",
   "feats":["프러포즈 기획 및 진행","시네마틱 영상 클립 추가 가능","서프라이즈를 위한 비밀 촬영","붐비지 않는 최고의 뷰포인트","촬영 원본 전체 제공","모든 사진 패키지와 결합 가능"]},
 ],
 "ex_kicker": "시그니처 촬영",
 "ex_title": '오직 <em>이곳</em>에서만',
 "ex_intro": "카파도키아는 세상에서 가장 꿈같은 배경입니다. 저희는 이곳의 구석구석을 알고 있죠. 전 세계 손님들이 이 장면을 위해 날아옵니다.",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"일출에 카파도키아 하늘을 가득 채운 열기구를 바라보는 여행자",
   "t":"열기구 일출","p":"맑은 날 아침마다 백여 개의 열기구가 요정 굴뚝 위로 떠오릅니다. 저희만 아는 프라이빗 뷰포인트에서, 그 장관이 당신 뒤로 펼쳐지도록 촬영합니다. 모두가 꿈꾸는 바로 그 사진을 제대로."},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"카파도키아 계곡에서 드레스 자락을 날리며 촬영 중인 신부",
   "t":"플라잉 드레스 & 웨딩","p":"일출 계곡을 배경으로 한 저희의 시그니처 플라잉 드레스 컷. 드레스 준비부터 포즈 디렉팅, 천이 가장 아름답게 날리는 순간 포착까지 모두 저희가 합니다."},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"골든아워 카파도키아 계곡에서 웨딩 촬영 중인 커플",
   "t":"일몰의 야생마","p":"골든아워가 되면 200–300마리의 반야생마 무리가 계곡을 가로지릅니다. 에르지예스산 뒤로 해가 질 때 말들 사이에 서는 것 — 카파도키아에서 가장 영화 같은 장면입니다."},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"카파도키아 상점에서 수백 개의 모자이크 랜턴 아래 서 있는 손님",
   "t":"랜턴 & 카펫 상점","p":"모자이크 랜턴 빛으로 가득한 백 년 카펫 상점 — 카파도키아에서 가장 마법 같은 실내 씬입니다. 비 오는 날에도 완벽하고, 인생샷 없이는 나올 수 없는 곳이죠."},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"카파도키아가 내려다보이는 동굴 호텔 테라스에서의 촬영",
   "t":"동굴 호텔 테라스","p":"열기구가 지나가는 돌 테라스에서의 아침 — 촬영을 당신의 호텔에서 시작해, 빛이 바뀌는 대로 계곡으로 이동할 수 있습니다."},
 ],
 "st_kicker": "이용 방법",
 "st_title": '예약은 <em>간단해요</em>',
 "steps": [
  {"t":"패키지 선택","p":"위의 상세 내용을 보고 여행 일정에 맞는 패키지를 고르세요. 어떤 게 좋을지 저희에게 물어보셔도 됩니다."},
  {"t":"WhatsApp 문의","p":"몇 시간 안에 답장드립니다 — 예약 가능 날짜, 현재 가격, 궁금한 모든 것."},
  {"t":"날짜 확정","p":"소액의 예약금으로 일출/일몰 시간대가 확정됩니다. 잔금은 촬영 당일에 지불하세요."},
  {"t":"촬영 즐기기","p":"픽업부터 포즈 디렉팅까지 저희가 함께합니다. 모든 사진과 함께 정성껏 보정한 20장을 보내드려요."},
 ],
 "ga_kicker": "갤러리",
 "ga_title": '<em>계곡</em>에서 온 장면들',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"괴레메 계곡 바위 위로 떠오르는 열기구","cap":"괴레메의 첫 빛"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"카파도키아 카펫 상점의 킬림 사이에서","cap":"카펫 상점 스냅"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"골든아워의 웨딩 커플","cap":"황금빛 서약"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"괴레메에서 커플 스냅 촬영","cap":"괴레메의 아침"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"부드러운 빛 속의 신랑 신부","cap":"결혼했어요"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"카파도키아 계곡에서의 촬영 장면","cap":"계곡 산책"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"카파도키아 프러포즈 스냅","cap":"그녀가 승낙했어요"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"카파도키아에서 기념일 촬영 중인 커플","cap":"기념일의 빛"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"카파도키아에서 촬영 중인 사진작가","cap":"렌즈 뒤에서"},
 ],
 "rv_kicker": "손님들의 이야기",
 "rv_title": '<em>전 세계</em> 여행자들의 선택',
 "reviews": [
  {"txt":"약혼의 아름다운 순간을 담아주셔서 정말 감사해요. 두 분은 최고로 다정한 부부 작가님들이에요 — 풍선 세팅을 도와주시고, 유연하게 맞춰주시고, 멋진 스팟들로 안내해 주셨어요. 아직도 여운이 남아요. 카파도키아의 어떤 순간이든 이 두 분을 강력 추천합니다!","name":"Tim & Linh","type":"약혼 촬영"},
  {"txt":"카파도키아의 열기구를 보고 사진으로 남기는 게 저희의 꿈이었어요. 날씨 때문에 열기구가 뜨지 못했지만 두 분과 정말 즐거운 시간을 보냈고, 촬영은 자연스럽고 재미있었어요. 사진도 기대한 그대로 나왔습니다!","name":"Willius & Qinghui","type":"커플 촬영"},
  {"txt":"두 분의 촬영 진행 방식이 정말 좋았어요. 아기와 함께였는데 처음부터 끝까지 배려심 있고 인내심 있게 대해주셨어요. 촬영도 장소도 모두 만족 — 꼭 해야 할 액티비티입니다!","name":"Aayushi & Aakash","type":"가족 촬영"},
 ],
 "ab_kicker": "소개",
 "ab_title": '렌즈 뒤의 <em>부부</em>',
 "ab_p1": "저희는 사진과, 사랑을 찍는 일과 사랑에 빠진 현지 부부입니다. 십 년 가까이 여행자들과 함께 일출 계곡, 비밀 전망대, 랜턴 상점을 누비며 카파도키아 여행을 평생 간직할 이미지로 만들어 왔습니다.",
 "ab_p2": "이곳에 살기에 새벽 6시의 빛이 어디로 떨어지는지, 해 질 녘 말들이 어느 계곡을 건너는지, 열기구를 어떻게 당신 뒤에 배치할지 정확히 압니다. 그리고 둘이기에 — 한 명이 포즈를 이끄는 동안 다른 한 명이 그 사이의 자연스러운 순간을 담습니다. 당신이 가장 사랑하게 될 사진들이죠.",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","시작 연도"],["1000+","행복한 손님"],["4시간","평균 응답"]],
 "ab_alt": "계곡에서 촬영 중인 카파도키아 부부 사진작가",
 "fq_kicker": "자주 묻는 질문",
 "fq_title": '궁금하신가요<em>?</em>',
 "faqs": [
  {"q":"카파도키아 촬영은 언제가 가장 좋나요?","a":"일 년 내내 일출 시간대가 최고입니다 — 열기구가 뜨고 빛이 가장 부드러운 시간이죠. 일몰은 따뜻한 황금빛에 사람도 훨씬 적어 두 번째로 좋습니다. 4–6월과 9–11월이 날씨가 가장 안정적이지만, 겨울 설경 촬영도 숨막히게 아름답습니다."},
  {"q":"열기구는 보장되나요?","a":"맑은 아침에는 거의 매일 뜨지만, 비행은 날씨와 항공 당국의 허가에 달려 있습니다. 촬영일에 뜨지 않으면 계곡과 소품 중심으로 촬영을 조정합니다 — 그래도 사진은 충분히 마법 같습니다."},
  {"q":"사진은 몇 장 받나요?","a":"전부 다요. 촬영한 모든 괜찮은 디지털 원본이 여러분 것이고, 전문 보정본 20장(풀데이는 40장)이 추가됩니다. 며칠 내 온라인 갤러리로 전달됩니다."},
  {"q":"어떤 옷을 입어야 하나요?","a":"길고 하늘거리는 드레스가 계곡과 가장 잘 어울립니다 — 시그니처 플라잉 드레스와 소품은 저희가 준비합니다. 의상 교체는 무제한이니 여벌을 챙겨오세요. 예약 후 스타일 가이드를 보내드립니다."},
  {"q":"예약과 결제는 어떻게 하나요?","a":"여행 날짜와 함께 WhatsApp으로 메시지를 보내주세요. 소액의 예약금으로 시간대가 확정되고, 잔금은 촬영 당일 현금 또는 이체로 지불하시면 됩니다."},
  {"q":"영어로 소통 가능한가요?","a":"네 — 매주 전 세계 손님들과 작업하고 있으며, WhatsApp 답장은 보통 4시간 이내입니다."},
 ],
 "ct_kicker": "준비되셨나요?",
 "ct_title": '<em>카파도키아</em> 촬영을 계획해요',
 "ct_sub": "여행 날짜만 알려주세요. 장소, 소품, 타이밍, 빛 — 나머지는 저희가 챙깁니다.",
 "ct_wa": "WhatsApp 메시지",
 "ct_ig": "Instagram DM",
 "ct_or": "또는 이메일",
 "ft_follow": "팔로우",
 "ft_rights": "모든 사진 © Cappadocia Photographer",
 "blog_kicker": "저널",
 "blog_more": "저널 읽기",
},

"zh": {
 "meta_title": "卡帕多奇亚摄影师 — 夫妻摄影团队 | 热气球日出旅拍",
 "meta_desc": "卡帕多奇亚本地夫妻摄影师专业旅拍：热气球日出、飞天裙、野马群、洞穴酒店。所有照片全部赠送 — 通过 WhatsApp 预订。",
 "wa_text": "您好！我想预订卡帕多奇亚的旅拍。",
 "nav": ["套餐","特色场景","作品","评价","关于我们","常见问题"],
 "nav_cta": "立即预订",
 "hero_loc": "格雷梅 · 卡帕多奇亚 · 土耳其",
 "hero_title": '用<em>金色晨光</em>，记录你的卡帕多奇亚',
 "hero_sub": "我们是本地夫妻摄影团队，自2016年起在热气球与精灵烟囱之间，为情侣、家庭与旅行者定格梦境般的瞬间。",
 "hero_cta1": "WhatsApp 预订",
 "hero_cta2": "查看套餐",
 "hero_scroll": "下滑",
 "pk_kicker": "旅拍套餐",
 "pk_title": '选择属于你的<em>光</em>',
 "pk_intro": "每个套餐均包含酒店接送、卡帕多奇亚最佳机位，以及全部数码原片。无隐藏费用 — 请私信咨询最新价格与档期。",
 "pk_popular": "最受欢迎",
 "pk_cta": "咨询价格",
 "packs": [
  {"time":"日出 · 2–2.5小时","name":"日出旅拍","tag":"数百热气球在你头顶升起",
   "feats":["专车酒店接送","黎明与热气球同框拍摄","3个最佳日出机位","含3种招牌道具","全部原片 + 20张精修","不限换装次数"]},
  {"time":"日落 · 2–2.5小时","name":"日落旅拍","tag":"山谷之上的黄金时刻",
   "feats":["专车酒店接送","3个最佳日落机位","可选：200–300匹野马群","含3种招牌道具","全部原片 + 20张精修","不限换装次数"]},
  {"time":"全天","name":"全天故事","tag":"从日出到日落的完整梦境",
   "feats":["日出 + 日落双场拍摄","洞穴酒店与山谷场景","地毯店与灯笼店","可加骆驼与复古道具","全部原片 + 40张精修","全天专属摄影向导"]},
  {"time":"电影感","name":"视频与求婚","tag":"一生一次的时刻",
   "feats":["求婚策划与执行","可加电影感视频短片","惊喜求婚隐蔽跟拍","人少景美的最佳机位","全部素材交付","可与任意摄影套餐组合"]},
 ],
 "ex_kicker": "招牌场景",
 "ex_title": '只有<em>这里</em>才有',
 "ex_intro": "卡帕多奇亚是世界上最梦幻的背景板，而我们熟悉它的每个角落。全球旅客正是为了这些画面飞越半个地球。",
 "exps": [
  {"img":"cappadocia-hot-air-balloons-sunrise.jpg","alt":"旅行者在日出时分眺望卡帕多奇亚上空的热气球群",
   "t":"热气球日出","p":"每个晴朗的清晨，上百只热气球升上精灵烟囱的上空。我们会带你到私藏机位，让整片气球海在你身后展开 — 人人梦想的那张照片，由专业的人来拍。"},
  {"img":"bridal-photoshoot-cappadocia.jpg","alt":"新娘在卡帕多奇亚山谷中拍摄飞扬的裙摆",
   "t":"飞天裙与婚纱","p":"我们的招牌飞天裙大片，以日出山谷为背景。裙子我们准备，姿势我们指导，在裙摆扬起的完美瞬间按下快门。婚礼、蜜月，或者只为取悦自己。"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"黄金时刻卡帕多奇亚山谷中的婚纱情侣",
   "t":"日落野马","p":"黄金时刻，200–300匹半野生马群穿越山谷。当太阳沉入埃尔吉耶斯山后，站在马群之间 — 这是卡帕多奇亚最具电影感的画面。"},
  {"img":"lantern-shop-photoshoot-cappadocia.jpg","alt":"客人站在卡帕多奇亚店铺数百盏马赛克灯笼之下",
   "t":"灯笼店与地毯店","p":"百年地毯老店被马赛克灯笼点亮 — 卡帕多奇亚最魔幻的室内场景。雨天也完美，没有人能空手（无片）而归。"},
  {"img":"cave-hotel-photoshoot-cappadocia.jpg","alt":"在俯瞰卡帕多奇亚的洞穴酒店露台上拍摄",
   "t":"洞穴酒店露台","p":"在石头露台上吃早餐，热气球从身边飘过 — 拍摄可以从你入住的酒店开始，再随着光线的变化转往山谷。"},
 ],
 "st_kicker": "预订流程",
 "st_title": '预订很<em>简单</em>',
 "steps": [
  {"t":"选择套餐","p":"查看上方详情，选择适合行程的套餐 — 也可以直接告诉我们日期，由我们推荐。"},
  {"t":"WhatsApp 联系我们","p":"数小时内回复：档期、最新价格，以及你想了解的一切。"},
  {"t":"锁定日期","p":"支付少量定金即可锁定你的日出或日落时段，尾款拍摄当天支付。"},
  {"t":"享受拍摄","p":"接送、摆姿指导全程包办，交付全部原片外加20张精修。"},
 ],
 "ga_kicker": "作品集",
 "ga_title": '来自<em>山谷</em>的画面',
 "gallery": [
  {"img":"hot-air-balloons-goreme-valley.jpg","alt":"热气球贴着格雷梅山谷的岩石飘过","cap":"格雷梅的第一缕光"},
  {"img":"carpet-shop-photoshoot-cappadocia.jpg","alt":"客人置身卡帕多奇亚地毯店的彩色基里姆之间","cap":"地毯店旅拍"},
  {"img":"sunset-wedding-photoshoot-cappadocia.jpg","alt":"黄金时刻的婚纱情侣","cap":"金色誓言"},
  {"img":"couple-photoshoot-goreme.jpg","alt":"格雷梅情侣旅拍","cap":"格雷梅的清晨"},
  {"img":"wedding-couple-cappadocia.jpg","alt":"柔光中的新郎新娘","cap":"新婚快乐"},
  {"img":"cappadocia-valley-photoshoot.jpg","alt":"卡帕多奇亚山谷中的拍摄场景","cap":"漫步山谷"},
  {"img":"engagement-photoshoot-cappadocia.jpg","alt":"卡帕多奇亚求婚旅拍","cap":"她说愿意"},
  {"img":"anniversary-photoshoot-cappadocia.jpg","alt":"在卡帕多奇亚拍摄纪念日的情侣","cap":"纪念日之光"},
  {"img":"photographer-cappadocia-at-work.jpg","alt":"正在卡帕多奇亚拍摄的摄影师","cap":"镜头之后"},
 ],
 "rv_kicker": "客人评价",
 "rv_title": '来自<em>世界各地</em>旅行者的喜爱',
 "reviews": [
  {"txt":"非常感谢你们记录下我们订婚的美好瞬间！你们是最贴心的夫妻摄影师 — 帮忙布置气球、灵活配合、带我们去了超美的机位。至今仍然回味。强烈推荐这对搭档记录你在卡帕多奇亚的任何时刻！","name":"Tim & Linh","type":"订婚拍摄"},
  {"txt":"我们一直梦想亲眼看到卡帕多奇亚的热气球并拍下来。虽然天气原因气球没能起飞，但我们依然玩得非常开心 — 拍摄轻松自然，照片和我们期待的一模一样！","name":"Willius & Qinghui","type":"情侣拍摄"},
  {"txt":"非常喜欢两位的拍摄方式。我们带着婴儿，他们全程耐心又体贴。拍摄和取景地都令人满意 — 来卡帕多奇亚必做的体验！","name":"Aayushi & Aakash","type":"家庭拍摄"},
 ],
 "ab_kicker": "关于我们",
 "ab_title": '镜头背后的<em>夫妻档</em>',
 "ab_p1": "我们是一对爱上摄影、也爱拍摄爱情的本地夫妻。近十年来，我们带着旅行者穿越日出山谷、私藏观景台和灯火通明的灯笼店，把卡帕多奇亚之旅变成可以珍藏一生的影像。",
 "ab_p2": "因为住在这里，我们清楚清晨六点的光落在哪里、黄昏马群会穿过哪条山谷、如何让热气球恰好出现在你身后。因为是两个人 — 一人指导姿势，另一人抓拍之间最自然的瞬间，那往往是你最爱的照片。",
 "ab_sign": "— Kaşif & Bahar",
 "stats": [["2016","开始于"],["1000+","满意客人"],["4小时","平均回复"]],
 "ab_alt": "卡帕多奇亚夫妻摄影师在山谷中工作",
 "fq_kicker": "常见问题",
 "fq_title": '拍摄前<em>须知</em>',
 "faqs": [
  {"q":"卡帕多奇亚旅拍什么时间最好？","a":"全年都推荐日出时段 — 热气球升空、光线最柔和。日落紧随其后：温暖的金色光线，人也少得多。4–6月和9–11月天气最稳定，冬季雪景拍摄同样震撼。"},
  {"q":"热气球一定会飞吗？","a":"晴天清晨几乎每天都飞，但受天气和航空管制影响可能取消。如果拍摄日气球停飞，我们会把拍摄调整为山谷与道具场景 — 照片依然足够梦幻（客人们亲口说的）。"},
  {"q":"我们能拿到多少照片？","a":"全部。当天所有拍得好的数码原片都归你，另加20张专业精修（全天套餐40张）。数日内通过在线相册交付。"},
  {"q":"应该穿什么？","a":"长款飘逸的裙子在山谷里最上镜 — 招牌飞天裙和道具由我们提供。建议多带一套衣服，换装不限次数。预订后我们会发送完整的穿搭指南。"},
  {"q":"如何预订和付款？","a":"通过 WhatsApp 告诉我们你的行程日期。支付少量定金即锁定时段，尾款在拍摄当天以现金或转账支付。"},
  {"q":"沟通语言？","a":"我们每周都接待来自世界各地的客人，英语沟通无障碍，WhatsApp 通常4小时内回复。"},
 ],
 "ct_kicker": "随时恭候",
 "ct_title": '一起规划你的<em>卡帕多奇亚</em>之拍',
 "ct_sub": "告诉我们你的旅行日期，其余交给我们：机位、道具、时间与光线。",
 "ct_wa": "WhatsApp 联系",
 "ct_ig": "Instagram 私信",
 "ct_or": "或邮件至",
 "ft_follow": "关注我们",
 "ft_rights": "所有照片版权所有 © Cappadocia Photographer",
 "blog_kicker": "手记",
 "blog_more": "阅读手记",
},
}

# --- gorsel eslesme duzeltmeleri (gercek fotograflara gore) ---
_HORSE_ALT = {
    "en": "Couple running hand in hand toward a herd of wild horses at sunset near Cappadocia",
    "ru": "Пара бежит, держась за руки, к табуну диких лошадей на закате возле Каппадокии",
    "es": "Pareja corriendo de la mano hacia una manada de caballos salvajes al atardecer cerca de Capadocia",
    "fr": "Couple courant main dans la main vers un troupeau de chevaux sauvages au coucher du soleil près de la Cappadoce",
    "ko": "일몰 무렵 야생마 무리를 향해 손잡고 달리는 커플",
    "zh": "日落时分，情侣手牵手奔向野马群",
}
for _l in T:
    T[_l]["exps"][1]["img"] = "cave-hotel-photoshoot-cappadocia.jpg"      # kirmizi ucan elbise, sutunlar
    T[_l]["exps"][2]["img"] = "cappadocia-valley-photoshoot.jpg"          # gun batiminda at surusu
    T[_l]["exps"][2]["alt"] = _HORSE_ALT[_l]
    T[_l]["exps"][4]["img"] = "couple-photoshoot-goreme.jpg"              # magara oteli havuz terasi
    T[_l]["gallery"][3]["img"] = "bridal-photoshoot-cappadocia.jpg"       # salincak sahnesi

# --- rakip analizi guncellemesi (16Tem): baslangic fiyatlari + Instagram Reels ---
_PRICES = ["400", "400", "1,500", "750"]  # sunrise, sunset, fullday, video&proposal
_FROM = {"en": "from €{}", "ru": "от {} €", "es": "desde {} €", "fr": "à partir de {} €", "ko": "€{}부터", "zh": "€{}起"}
_SEP = {"ru": ".", "es": ".", "fr": " "}  # binlik ayraci yerellestir
_REEL = {
    "en": "Instagram reel video included",
    "ru": "Видео-reel для Instagram включено",
    "es": "Vídeo reel para Instagram incluido",
    "fr": "Vidéo reel Instagram incluse",
    "ko": "인스타그램 릴스 영상 포함",
    "zh": "含 Instagram Reels 视频",
}
_REEL_DAY = {
    "en": "Instagram reels from the whole day",
    "ru": "Instagram Reels со всего дня",
    "es": "Reels de Instagram de todo el día",
    "fr": "Reels Instagram de toute la journée",
    "ko": "하루 전체의 인스타그램 릴스",
    "zh": "全天多条 Instagram Reels",
}
_INTRO = {
    "en": "Every session includes hotel pick-up, the best photo spots in Cappadocia and ALL of your digital photos. Prices below are starting rates — message us for your date and a tailored quote.",
    "ru": "В каждую сессию входит трансфер из отеля, лучшие локации Каппадокии и ВСЕ ваши цифровые фотографии. Указаны стартовые цены — напишите нам, чтобы получить расчёт под вашу дату.",
    "es": "Cada sesión incluye recogida en el hotel, los mejores rincones de Capadocia y TODAS tus fotos digitales. Los precios son tarifas iniciales — escríbenos para un presupuesto a tu medida.",
    "fr": "Chaque séance comprend la prise en charge à l'hôtel, les plus beaux spots de Cappadoce et TOUTES vos photos numériques. Les prix indiqués sont des tarifs de départ — écrivez-nous pour un devis personnalisé.",
    "ko": "모든 촬영에 호텔 픽업, 카파도키아 최고의 촬영 스팟, 모든 디지털 원본이 포함됩니다. 아래는 시작 가격입니다 — 날짜를 알려주시면 맞춤 견적을 드립니다.",
    "zh": "每个套餐均包含酒店接送、卡帕多奇亚最佳机位与全部数码原片。以下为起步价 — 告诉我们你的日期，获取专属报价。",
}
_TRANSFER = {
    "en": "Hotel pick-up & all transfers included",
    "ru": "Трансфер из отеля и все переезды включены",
    "es": "Recogida en el hotel y todos los traslados incluidos",
    "fr": "Prise en charge à l'hôtel et tous les transferts inclus",
    "ko": "호텔 픽업 & 모든 이동 포함",
    "zh": "含酒店接送及全程交通",
}
for _l in T:
    T[_l]["pk_intro"] = _INTRO[_l]
    for _p in T[_l]["packs"][:2]:
        _p["feats"][0] = _TRANSFER[_l]
    for _i, _p in enumerate(T[_l]["packs"]):
        _val = _PRICES[_i].replace(",", _SEP.get(_l, ","))
        _p["price"] = _FROM[_l].format(_val)
    T[_l]["packs"][0]["feats"].insert(5, _REEL[_l])
    T[_l]["packs"][1]["feats"].insert(5, _REEL[_l])
    T[_l]["packs"][2]["feats"].insert(5, _REEL_DAY[_l])

WA_SVG = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2a10 10 0 0 0-8.66 15L2 22l5.2-1.3A10 10 0 1 0 12 2zm5.47 14.13c-.23.65-1.35 1.24-1.86 1.28-.5.05-.97.23-3.27-.68-2.77-1.09-4.53-3.9-4.67-4.08-.13-.18-1.11-1.48-1.11-2.82 0-1.34.7-2 .95-2.27.25-.28.55-.35.73-.35.18 0 .37 0 .53.01.17.01.4-.06.62.48.23.55.78 1.9.85 2.04.07.14.11.3.02.48-.09.18-.13.29-.27.45-.13.16-.28.35-.4.47-.13.13-.27.28-.12.54.16.27.7 1.16 1.5 1.87 1.03.92 1.9 1.2 2.17 1.34.27.13.42.11.58-.07.16-.18.67-.78.85-1.05.18-.27.36-.22.6-.13.25.09 1.57.74 1.84.88.27.13.45.2.51.31.07.11.07.65-.16 1.3z"/></svg>'

# ============================================================
#  BLOG / JOURNAL — 6 dil, 2 haftada 1 yayin
#  Yeni yazi eklemek: _src/posts/ altina <YYYY-AA-GG>-<slug>.json koy,
#  sonra `python _src/build_site.py` calistir. Baska hicbir yere dokunma.
# ============================================================
BLOG_T = {
"en": {"nav":"Journal","kicker":"The Journal","title":'Notes from the <em>valleys</em>',
 "intro":"Honest guides from a wife-and-husband team who shoot in these valleys almost every morning — seasons, timing, what to wear, and what a shoot day really looks like.",
 "index_title":"Cappadocia Photoshoot Journal — Seasons, Timing & Practical Guides",
 "index_desc":"Guides for planning a photoshoot in Cappadocia: when the balloons fly, the best month for your session, what to wear and how a shoot morning actually runs.",
 "read":"Read the guide","back":"← Back to the Journal","home":"Home","published":"Published",
 "more":"More from the Journal",
 "cta_title":"Planning your own Cappadocia session?",
 "cta_sub":"Send us your dates and we'll tell you honestly what's possible that week.",
 "cta_btn":"Ask on WhatsApp"},
"ru": {"nav":"Журнал","kicker":"Журнал","title":'Заметки из <em>долин</em>',
 "intro":"Честные гиды от пары фотографов, которая снимает в этих долинах почти каждое утро — сезоны, время, что надеть и как на самом деле проходит съёмочное утро.",
 "index_title":"Журнал о фотосессиях в Каппадокии — сезоны, время и советы",
 "index_desc":"Гиды по планированию фотосессии в Каппадокии: когда летают шары, какой месяц лучше, что надеть и как проходит съёмочное утро.",
 "read":"Читать статью","back":"← Назад в журнал","home":"Главная","published":"Опубликовано",
 "more":"Ещё из журнала",
 "cta_title":"Планируете свою съёмку в Каппадокии?",
 "cta_sub":"Напишите нам даты — честно скажем, что возможно на этой неделе.",
 "cta_btn":"Написать в WhatsApp"},
"es": {"nav":"Diario","kicker":"El Diario","title":'Notas desde los <em>valles</em>',
 "intro":"Guías honestas de un matrimonio de fotógrafos que trabaja en estos valles casi cada mañana: temporadas, horarios, qué ponerte y cómo transcurre de verdad un día de sesión.",
 "index_title":"Diario de fotografía en Capadocia — temporadas, horarios y guías",
 "index_desc":"Guías para planificar tu sesión de fotos en Capadocia: cuándo vuelan los globos, cuál es el mejor mes, qué ponerte y cómo es una mañana de sesión.",
 "read":"Leer la guía","back":"← Volver al diario","home":"Inicio","published":"Publicado",
 "more":"Más del diario",
 "cta_title":"¿Estás planeando tu sesión en Capadocia?",
 "cta_sub":"Escríbenos tus fechas y te diremos con sinceridad qué es posible esa semana.",
 "cta_btn":"Escríbenos por WhatsApp"},
"fr": {"nav":"Journal","kicker":"Le Journal","title":'Notes des <em>vallées</em>',
 "intro":"Des guides honnêtes d'un couple de photographes qui travaille dans ces vallées presque chaque matin : saisons, horaires, quoi porter et comment se déroule vraiment une matinée de séance.",
 "index_title":"Journal photo de Cappadoce — saisons, horaires et guides pratiques",
 "index_desc":"Guides pour préparer votre séance photo en Cappadoce : quand volent les montgolfières, le meilleur mois, quoi porter et comment se passe la matinée.",
 "read":"Lire le guide","back":"← Retour au journal","home":"Accueil","published":"Publié le",
 "more":"Plus dans le journal",
 "cta_title":"Vous préparez votre séance en Cappadoce ?",
 "cta_sub":"Envoyez-nous vos dates — nous vous dirons honnêtement ce qui est possible cette semaine-là.",
 "cta_btn":"Écrire sur WhatsApp"},
"ko": {"nav":"저널","kicker":"저널","title":'<em>계곡</em>에서 보내는 기록',
 "intro":"거의 매일 아침 이 계곡에서 촬영하는 부부 사진가의 솔직한 가이드 — 계절, 시간대, 무엇을 입을지, 그리고 촬영 당일이 실제로 어떻게 흘러가는지.",
 "index_title":"카파도키아 사진 촬영 저널 — 계절, 시간대, 실전 가이드",
 "index_desc":"카파도키아 촬영을 준비하는 가이드: 열기구가 뜨는 시기, 가장 좋은 달, 의상 선택, 촬영 당일의 흐름.",
 "read":"가이드 읽기","back":"← 저널로 돌아가기","home":"홈","published":"게시일",
 "more":"저널의 다른 글",
 "cta_title":"카파도키아 촬영을 계획 중이신가요?",
 "cta_sub":"원하시는 날짜를 보내주시면 그 주에 무엇이 가능한지 솔직하게 알려드립니다.",
 "cta_btn":"WhatsApp으로 문의"},
"zh": {"nav":"日志","kicker":"摄影日志","title":'来自<em>山谷</em>的手记',
 "intro":"一对几乎每天清晨都在这些山谷里拍摄的夫妻摄影师，为你写下的实用指南——季节、时间、穿什么，以及拍摄当天真实的样子。",
 "index_title":"卡帕多奇亚拍摄日志 — 季节、时间与实用指南",
 "index_desc":"筹备卡帕多奇亚拍摄的实用指南：热气球何时起飞、哪个月份最好、穿什么，以及拍摄当天的真实流程。",
 "read":"阅读指南","back":"← 返回日志","home":"首页","published":"发布于",
 "more":"更多日志",
 "cta_title":"正在筹备你的卡帕多奇亚拍摄？",
 "cta_sub":"把你的日期发给我们，我们会如实告诉你那一周能做什么。",
 "cta_btn":"用 WhatsApp 咨询"},
}

def load_posts():
    """_src/posts/*.json -> yeniden eskiye sirali liste."""
    posts = []
    for path in glob.glob(os.path.join(POSTS_DIR, "*.json")):
        with open(path, encoding="utf-8") as f:
            p = json.load(f)
        eksik = [c for c in LANG_META if c not in p.get("i18n", {})]
        if eksik:
            raise SystemExit(f"HATA {os.path.basename(path)}: eksik dil {eksik} — 6 dil zorunlu")
        posts.append(p)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts

POSTS = load_posts()

def lang_base(lang):
    return "/" if lang == "en" else f"/{LANG_META[lang]['dir']}/"

def blog_index_url(lang):
    return f"{DOMAIN}{lang_base(lang)}blog/"

def post_url(lang, slug):
    return f"{DOMAIN}{lang_base(lang)}blog/{slug}.html"

def blog_depth(lang):
    """blog sayfasindan site kokune donus (css/img icin)."""
    return "../" if lang == "en" else "../../"

def blog_hreflangs(slug=None):
    def u(c):
        return post_url(c, slug) if slug else blog_index_url(c)
    out = [f'<link rel="alternate" hreflang="x-default" href="{u("en")}">']
    out += [f'<link rel="alternate" hreflang="{c}" href="{u(c)}">' for c in LANG_META]
    return "\n".join(out)

def blog_chrome_head(lang, title, desc, canonical, image, hreflang_block, extra_ld=""):
    root = blog_depth(lang)
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{hreflang_block}
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{DOMAIN}/img/{image}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🎈%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;1,400;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css">
<link rel="stylesheet" href="{root}css/blog.css">
{extra_ld}'''

def blog_header(lang, url_for):
    t = T[lang]
    b = BLOG_T[lang]
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    return f'''<header class="nav scrolled" id="top">
  <a class="brand" href="{lang_base(lang)}"><b>Cappadocia</b><span>Photographer</span></a>
  <ul class="nav-links" id="navlinks">
    <li><a href="{lang_base(lang)}#packages">{t["nav"][0]}</a></li>
    <li><a href="{lang_base(lang)}#gallery">{t["nav"][2]}</a></li>
    <li><a href="{lang_base(lang)}blog/">{b["nav"]}</a></li>
    <li><a class="nav-cta" href="{wa}" target="_blank" rel="noopener">{t["nav_cta"]}</a></li></ul>
  <div style="display:flex;gap:14px;align-items:center">
    {lang_switcher(lang, url_for)}
    <button class="burger" id="burger" aria-label="Menu">☰</button>
  </div>
</header>'''

def blog_footer(lang):
    t = T[lang]
    b = BLOG_T[lang]
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    return f'''<section class="contact"><div class="wrap">
  <h2 class="contact-title">{b["cta_title"]}</h2>
  <p class="contact-sub">{b["cta_sub"]}</p>
  <div class="contact-ctas">
    <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{b["cta_btn"]}</a>
  </div>
</div></section>

<footer class="site">
  <div>{t["ft_rights"]} · Göreme, Cappadocia</div>
  <div class="foot-social">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    <a href="{FB}" target="_blank" rel="noopener">Facebook</a>
    <a href="{PIN}" target="_blank" rel="noopener">Pinterest</a>
  </div>
</footer>

<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>

<script>
const burger=document.getElementById('burger'),links=document.getElementById('navlinks');
burger.addEventListener('click',()=>links.classList.toggle('open'));
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
</script>'''

def post_cards(lang, posts, root):
    b = BLOG_T[lang]
    out = []
    for p in posts:
        i = p["i18n"][lang]
        out.append(f'''<a class="blog-card reveal" href="{lang_base(lang)}blog/{p["slug"]}.html">
      <div class="blog-card-img"><img src="{root}img/{p["image"]}" alt="{i["alt"]}" loading="lazy"></div>
      <div class="blog-card-body">
        <time datetime="{p["date"]}">{p["date"]}</time>
        <h3>{i["title"]}</h3>
        <p>{i["desc"]}</p>
        <span class="blog-card-more">{b["read"]} →</span>
      </div></a>''')
    return "".join(out)

def blog_index(lang):
    t, b = T[lang], BLOG_T[lang]
    root = blog_depth(lang)
    canonical = blog_index_url(lang)
    ld = {"@context":"https://schema.org","@type":"Blog","@id":canonical,
          "name":b["index_title"],"description":b["index_desc"],"inLanguage":lang,
          "publisher":{"@id":DOMAIN+"/#business"},
          "blogPost":[{"@type":"BlogPosting","headline":p["i18n"][lang]["title"],
                       "datePublished":p["date"],"url":post_url(lang,p["slug"])} for p in POSTS]}
    head = blog_chrome_head(lang, b["index_title"], b["index_desc"], canonical, "og-cover.jpg",
                            blog_hreflangs(),
                            f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>')
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head}
</head>
<body class="blog-page">
{blog_header(lang, lambda c: f"{lang_base(c)}blog/")}
<section class="blog-hero"><div class="wrap">
  <div class="kicker reveal">{b["kicker"]}</div>
  <h1 class="sec-title reveal">{b["title"]}</h1>
  <p class="sec-intro reveal">{b["intro"]}</p>
  <div class="blog-grid">{post_cards(lang, POSTS, root)}</div>
</div></section>
{blog_footer(lang)}
</body>
</html>'''

def blog_post(lang, p):
    t, b = T[lang], BLOG_T[lang]
    i = p["i18n"][lang]
    root = blog_depth(lang)
    canonical = post_url(lang, p["slug"])
    art = {"@context":"https://schema.org","@type":"BlogPosting",
           "headline":i["title"],"description":i["desc"],
           "datePublished":p["date"],"dateModified":p.get("modified", p["date"]),
           "inLanguage":lang,"mainEntityOfPage":canonical,
           "image":f"{DOMAIN}/img/{p['image']}",
           "author":{"@type":"Organization","name":"Cappadocia Photographer","url":DOMAIN},
           "publisher":{"@id":DOMAIN+"/#business"}}
    crumbs = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":b["home"],"item":DOMAIN+lang_base(lang)},
        {"@type":"ListItem","position":2,"name":b["nav"],"item":blog_index_url(lang)},
        {"@type":"ListItem","position":3,"name":i["title"],"item":canonical}]}
    ld = (f'<script type="application/ld+json">{json.dumps(art,ensure_ascii=False)}</script>\n'
          f'<script type="application/ld+json">{json.dumps(crumbs,ensure_ascii=False)}</script>')
    head = blog_chrome_head(lang, i["title"] + " | Cappadocia Photographer", i["desc"],
                            canonical, p["image"], blog_hreflangs(p["slug"]), ld)
    others = [q for q in POSTS if q["slug"] != p["slug"]][:3]
    more = (f'''<section class="blog-more"><div class="wrap">
  <div class="kicker reveal">{b["more"]}</div>
  <div class="blog-grid">{post_cards(lang, others, root)}</div>
</div></section>''' if others else "")
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
{head}
</head>
<body class="blog-page">
{blog_header(lang, lambda c: post_url(c, p["slug"]).replace(DOMAIN, ""))}
<article class="post">
  <div class="post-head">
    <nav class="crumbs"><a href="{lang_base(lang)}">{b["home"]}</a> · <a href="{lang_base(lang)}blog/">{b["nav"]}</a></nav>
    <h1>{i["title"]}</h1>
    <div class="post-meta">{b["published"]} <time datetime="{p["date"]}">{p["date"]}</time></div>
  </div>
  <figure class="post-hero"><img src="{root}img/{p["image"]}" alt="{i["alt"]}" fetchpriority="high"></figure>
  <div class="post-body">
{i["body"]}
  </div>
  <a class="post-back" href="{lang_base(lang)}blog/">{b["back"]}</a>
</article>
{more}
{blog_footer(lang)}
</body>
</html>'''

BLOG_CSS = """/* Journal — blog indeksi + yazi sayfasi (build_site.py uretir, elle duzenleme) */
.blog-page{padding-top:76px}
.blog-hero .wrap{padding-bottom:clamp(48px,7vh,80px)}
/* auto-fill: tek yazi varken kart tum satiri kaplamasin, 1/3 kalsin */
.blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:26px}
.blog-card{display:flex;flex-direction:column;background:var(--ink-2);border:1px solid rgba(201,162,107,.16);
  border-radius:4px;overflow:hidden;color:inherit;transition:transform .35s ease,border-color .35s ease,box-shadow .35s ease}
.blog-card:hover{transform:translateY(-4px);border-color:rgba(201,162,107,.5);box-shadow:0 20px 44px rgba(0,0,0,.4)}
.blog-card-img{aspect-ratio:3/2;overflow:hidden}
.blog-card-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s ease}
.blog-card:hover .blog-card-img img{transform:scale(1.05)}
.blog-card-body{padding:22px 24px 26px;display:flex;flex-direction:column;gap:10px;flex:1}
.blog-card-body time{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
.blog-card-body h3{font-size:21px;line-height:1.25}
.blog-card-body p{color:var(--cream-dim);font-size:15px;flex:1}
.blog-card-more{color:var(--gold-soft);font-size:13.5px;letter-spacing:.06em}

/* --- yazi --- */
.post{max-width:760px;margin:0 auto;padding:clamp(40px,7vh,72px) clamp(18px,4vw,32px) 0}
.crumbs{font-size:12.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--cream-faint);margin-bottom:20px}
.crumbs a{color:var(--cream-faint)}
.crumbs a:hover{color:var(--gold)}
.post-head h1{font-size:clamp(29px,4.4vw,46px);margin-bottom:14px}
.post-meta{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
.post-hero{margin:34px 0 40px;border-radius:4px;overflow:hidden}
.post-hero img{width:100%;aspect-ratio:3/2;object-fit:cover}
.post-body{font-size:17.5px;line-height:1.85;color:var(--cream-dim)}
.post-body h2{font-size:clamp(23px,3vw,31px);margin:44px 0 14px;color:var(--cream)}
.post-body h3{font-size:20px;margin:32px 0 10px;color:var(--cream)}
.post-body p{margin-bottom:20px}
.post-body ul,.post-body ol{margin:0 0 22px 22px}
.post-body li{margin-bottom:9px}
.post-body strong{color:var(--cream);font-weight:500}
.post-body a{border-bottom:1px solid rgba(227,199,149,.4)}
.post-body blockquote{border-left:2px solid var(--gold);padding:6px 0 6px 22px;margin:28px 0;
  font-family:var(--serif);font-style:italic;font-size:19px;color:var(--cream)}
.post-body table{width:100%;border-collapse:collapse;margin:26px 0;font-size:15.5px}
.post-body th,.post-body td{padding:11px 12px;border-bottom:1px solid rgba(201,162,107,.18);text-align:left}
.post-body th{color:var(--gold);font-weight:500;letter-spacing:.08em;text-transform:uppercase;font-size:12.5px}
.post-back{display:inline-block;margin:14px 0 0;color:var(--gold-soft);font-size:14px;letter-spacing:.06em}
.blog-more .wrap{padding-top:clamp(56px,8vh,90px)}

/* --- ana sayfa vitrini --- */
.home-journal .blog-grid{margin-top:8px}
@media(max-width:700px){
  .post-body{font-size:16.5px}
  .blog-page{padding-top:66px}
  /* dar ekranda tablo sayfayi yatay kaydirmasin, kendi icinde kaysin */
  .post-body table{display:block;overflow-x:auto;white-space:nowrap}
  .post-body td,.post-body th{white-space:normal;min-width:118px}
}
"""

def lang_switcher(current, url_for=None):
    items = []
    for code, m in LANG_META.items():
        href = url_for(code) if url_for else ("/" if code == "en" else f"/{m['dir']}/")
        cls = ' class="active"' if code == current else ""
        items.append(f'<a href="{href}"{cls}><span>{m["flag"]}</span>{m["label"]}</a>')
    cur = LANG_META[current]
    return f'''<details class="lang"><summary>{cur["flag"]} {current.upper()} ▾</summary>
      <nav class="lang-menu">{"".join(items)}</nav></details>'''

def hreflangs():
    out = [f'<link rel="alternate" hreflang="en" href="{DOMAIN}/">',
           f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">']
    for code, m in LANG_META.items():
        if code == "en":
            continue
        out.append(f'<link rel="alternate" hreflang="{code}" href="{DOMAIN}/{m["dir"]}/">')
    return "\n".join(out)

def schema(t, lang):
    biz = {
      "@context":"https://schema.org","@type":["LocalBusiness","Photograph"],
      "@id": DOMAIN+"/#business",
      "name":"Cappadocia Photographer","url":DOMAIN,
      "image":DOMAIN+"/img/og-cover.jpg",
      "description":t["meta_desc"],
      "telephone":"+90 553 717 52 40","email":EMAIL,
      "priceRange":"$$",
      "address":{"@type":"PostalAddress","addressLocality":"Göreme","addressRegion":"Nevşehir","addressCountry":"TR"},
      "geo":{"@type":"GeoCoordinates","latitude":38.6431,"longitude":34.8289},
      "sameAs":[IG,FB,PIN],
      "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"04:30","closes":"22:00"},
    }
    faq = {
      "@context":"https://schema.org","@type":"FAQPage",
      "mainEntity":[{"@type":"Question","name":f["q"],
                     "acceptedAnswer":{"@type":"Answer","text":f["a"]}} for f in t["faqs"]]
    }
    return (f'<script type="application/ld+json">{json.dumps(biz,ensure_ascii=False)}</script>\n'
            f'<script type="application/ld+json">{json.dumps(faq,ensure_ascii=False)}</script>')

def page(lang):
    t = T[lang]
    m = LANG_META[lang]
    canonical = DOMAIN + ("/" if lang == "en" else f"/{m['dir']}/")
    root = "" if lang == "en" else "../"
    wa = f"https://wa.me/{WA_NUM}?text=" + t["wa_text"].replace(" ", "%20")
    nav_ids = ["packages","experiences","gallery","reviews","about","faq"]
    nav_html = "".join(f'<li><a href="#{i}">{n}</a></li>' for i, n in zip(nav_ids, t["nav"]))
    if POSTS:
        nav_html += f'<li><a href="{lang_base(lang)}blog/">{BLOG_T[lang]["nav"]}</a></li>'

    packs = []
    for i, p in enumerate(t["packs"]):
        pop = ' popular' if i == 0 else ''
        badge = f'<span class="pack-badge">{t["pk_popular"]}</span>' if i == 0 else ''
        feats = "".join(f"<li>{f}</li>" for f in p["feats"])
        packs.append(f'''<article class="pack{pop} reveal">{badge}
          <div class="pack-time">{p["time"]}</div><h3>{p["name"]}</h3>
          <div class="pack-tag">{p["tag"]}</div>
          <div class="pack-price">{p["price"]}</div><ul>{feats}</ul>
          <a class="btn btn-gold" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["pk_cta"]}</a></article>''')

    exps = []
    for i, e in enumerate(t["exps"]):
        exps.append(f'''<div class="exp-row reveal">
          <div class="exp-img"><img src="{root}img/{e["img"]}" alt="{e["alt"]}" loading="lazy" width="800" height="1000"></div>
          <div class="exp-body"><div class="exp-num">0{i+1}</div><h3>{e["t"]}</h3><p>{e["p"]}</p></div></div>''')

    steps = "".join(f'<div class="step reveal"><h3>{s["t"]}</h3><p>{s["p"]}</p></div>' for s in t["steps"])

    gal = "".join(f'''<figure class="gitem reveal"><img src="{root}img/{g["img"]}" alt="{g["alt"]}" loading="lazy">
      <figcaption>{g["cap"]}</figcaption></figure>''' for g in t["gallery"])

    revs = []
    for r in t["reviews"]:
        init = r["name"][0]
        revs.append(f'''<article class="rev reveal"><div class="rev-stars">★★★★★</div>
          <p>{r["txt"]}</p><footer><div class="rev-avatar">{init}</div>
          <div><div class="rev-name">{r["name"]}</div><div class="rev-type">{r["type"]}</div></div></footer></article>''')

    faqs = "".join(f'<details class="faq reveal"><summary>{f["q"]}</summary><div>{f["a"]}</div></details>' for f in t["faqs"])
    stats = "".join(f'<div class="stat"><b>{a}</b><span>{b}</span></div>' for a, b in t["stats"])

    bt = BLOG_T[lang]
    journal = f'''<section class="home-journal" id="journal"><div class="wrap">
  <div class="kicker reveal">{bt["kicker"]}</div>
  <h2 class="sec-title reveal">{bt["title"]}</h2>
  <p class="sec-intro reveal">{bt["intro"]}</p>
  <div class="blog-grid">{post_cards(lang, POSTS[:3], root)}</div>
</div></section>''' if POSTS else ""

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["meta_title"]}</title>
<meta name="description" content="{t["meta_desc"]}">
<link rel="canonical" href="{canonical}">
{hreflangs()}
<meta property="og:type" content="website">
<meta property="og:title" content="{t["meta_title"]}">
<meta property="og:description" content="{t["meta_desc"]}">
<meta property="og:image" content="{DOMAIN}/img/og-cover.jpg">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E🎈%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,600;1,400;1,600&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}css/style.css">
<link rel="stylesheet" href="{root}css/blog.css">
{schema(t, lang)}
</head>
<body>
<header class="nav" id="top">
  <a class="brand" href="{canonical}"><b>Cappadocia</b><span>Photographer</span></a>
  <ul class="nav-links" id="navlinks">{nav_html}
    <li><a class="nav-cta" href="{wa}" target="_blank" rel="noopener">{t["nav_cta"]}</a></li></ul>
  <div style="display:flex;gap:14px;align-items:center">
    {lang_switcher(lang)}
    <button class="burger" id="burger" aria-label="Menu">☰</button>
  </div>
</header>

<section class="hero">
  <div class="hero-bg"><img src="{root}img/cappadocia-hot-air-balloons-sunrise.jpg" alt="{t["exps"][0]["alt"]}" fetchpriority="high"></div>
  <div class="hero-inner">
    <div class="hero-loc">{t["hero_loc"]}</div>
    <h1>{t["hero_title"]}</h1>
    <p class="hero-sub">{t["hero_sub"]}</p>
    <div class="hero-ctas">
      <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["hero_cta1"]}</a>
      <a class="btn btn-ghost" href="#packages">{t["hero_cta2"]}</a>
    </div>
  </div>
  <div class="hero-scroll">{t["hero_scroll"]}</div>
</section>

<section class="packages" id="packages"><div class="wrap">
  <div class="kicker reveal">{t["pk_kicker"]}</div>
  <h2 class="sec-title reveal">{t["pk_title"]}</h2>
  <p class="sec-intro reveal">{t["pk_intro"]}</p>
  <div class="pack-grid">{"".join(packs)}</div>
</div></section>

<section id="experiences"><div class="wrap">
  <div class="kicker reveal">{t["ex_kicker"]}</div>
  <h2 class="sec-title reveal">{t["ex_title"]}</h2>
  <p class="sec-intro reveal">{t["ex_intro"]}</p>
  {"".join(exps)}
</div></section>

<section class="steps"><div class="wrap">
  <div class="kicker reveal">{t["st_kicker"]}</div>
  <h2 class="sec-title reveal">{t["st_title"]}</h2>
  <div class="step-grid">{steps}</div>
</div></section>

<section id="gallery"><div class="wrap">
  <div class="kicker reveal">{t["ga_kicker"]}</div>
  <h2 class="sec-title reveal">{t["ga_title"]}</h2>
  <div class="gallery-grid">{gal}</div>
</div></section>

<section class="reviews" id="reviews"><div class="wrap">
  <div class="kicker reveal">{t["rv_kicker"]}</div>
  <h2 class="sec-title reveal">{t["rv_title"]}</h2>
  <div class="rev-grid">{"".join(revs)}</div>
</div></section>

<section id="about"><div class="wrap about-grid">
  <div class="about-img reveal"><img src="{root}img/photographer-cappadocia-at-work.jpg" alt="{t["ab_alt"]}" loading="lazy"></div>
  <div class="about reveal">
    <div class="kicker">{t["ab_kicker"]}</div>
    <h2 class="sec-title">{t["ab_title"]}</h2>
    <p>{t["ab_p1"]}</p><p>{t["ab_p2"]}</p>
    <div class="about-sign">{t["ab_sign"]}</div>
    <div class="stats">{stats}</div>
  </div>
</div></section>

<section id="faq"><div class="wrap">
  <div class="kicker reveal">{t["fq_kicker"]}</div>
  <h2 class="sec-title reveal">{t["fq_title"]}</h2>
  <div class="faq-list">{faqs}</div>
</div></section>

{journal}

<section class="contact" id="contact"><div class="wrap">
  <div class="kicker reveal">{t["ct_kicker"]}</div>
  <h2 class="contact-title reveal">{t["ct_title"]}</h2>
  <p class="contact-sub reveal">{t["ct_sub"]}</p>
  <div class="contact-ctas reveal">
    <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{WA_SVG}{t["ct_wa"]}</a>
    <a class="btn btn-ghost" href="{IG}" target="_blank" rel="noopener">{t["ct_ig"]}</a>
  </div>
  <div class="contact-alt reveal"><span>{t["ct_or"]}</span> <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="tel:+{WA_NUM}">+90 553 717 52 40</a></div>
</div></section>

<footer class="site">
  <div>{t["ft_rights"]} · Göreme, Cappadocia</div>
  <div class="foot-social">
    <a href="{IG}" target="_blank" rel="noopener">Instagram</a>
    <a href="{FB}" target="_blank" rel="noopener">Facebook</a>
    <a href="{PIN}" target="_blank" rel="noopener">Pinterest</a>
  </div>
</footer>

<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>

<script>
const nav=document.querySelector('.nav');
addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>40),{{passive:true}});
const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const burger=document.getElementById('burger'),links=document.getElementById('navlinks');
burger.addEventListener('click',()=>links.classList.toggle('open'));
links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('open')));
</script>
</body>
</html>'''

# ---- sayfa uret ----
for lang, m in LANG_META.items():
    d = OUT if lang == "en" else os.path.join(OUT, m["dir"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(lang))
    print(f"OK {lang}: {d}\\index.html")

# ---- blog uret ----
if POSTS:
    os.makedirs(os.path.join(OUT, "css"), exist_ok=True)
    with open(os.path.join(OUT, "css", "blog.css"), "w", encoding="utf-8") as f:
        f.write(BLOG_CSS)
    for lang, m in LANG_META.items():
        d = os.path.join(OUT, "blog") if lang == "en" else os.path.join(OUT, m["dir"], "blog")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(blog_index(lang))
        for p in POSTS:
            with open(os.path.join(d, p["slug"] + ".html"), "w", encoding="utf-8") as f:
                f.write(blog_post(lang, p))
    print(f"OK blog: {len(POSTS)} yazi x {len(LANG_META)} dil = {len(POSTS)*len(LANG_META)} sayfa + 6 indeks")
else:
    print("UYARI: _src/posts/ bos — blog uretilmedi")

# ---- eski URL yonlendirmeleri ----
REDIR = '''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={url}"><link rel="canonical" href="{url}">
<title>Redirecting…</title></head><body><a href="{url}">Redirecting…</a></body></html>'''
for old, new in [("page1.html", DOMAIN+"/#packages"), ("page2.html", DOMAIN+"/#faq"), ("page3.html", DOMAIN+"/#experiences")]:
    with open(os.path.join(OUT, old), "w", encoding="utf-8") as f:
        f.write(REDIR.format(url=new))
print("OK redirects")

# ---- 404 ----
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(REDIR.format(url=DOMAIN+"/"))

# ---- sitemap ----
urls = []
for lang, m in LANG_META.items():
    loc = DOMAIN + ("/" if lang == "en" else f"/{m['dir']}/")
    alts = "".join(
        f'<xhtml:link rel="alternate" hreflang="{c}" href="{DOMAIN + ("/" if c=="en" else "/"+LANG_META[c]["dir"]+"/")}"/>'
        for c in LANG_META)
    urls.append(f"<url><loc>{loc}</loc>{alts}<changefreq>monthly</changefreq></url>")

# blog indeksi + yazilar (6 dil, karsilikli hreflang)
for lang in LANG_META:
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{blog_index_url(c)}"/>' for c in LANG_META)
    urls.append(f"<url><loc>{blog_index_url(lang)}</loc>{alts}<changefreq>weekly</changefreq></url>")
for p in POSTS:
    for lang in LANG_META:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{c}" href="{post_url(c, p["slug"])}"/>' for c in LANG_META)
        urls.append(f'<url><loc>{post_url(lang, p["slug"])}</loc>{alts}'
                    f'<lastmod>{p.get("modified", p["date"])}</lastmod><changefreq>yearly</changefreq></url>')
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>")
print("OK sitemap")

with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("OK robots")
print("BITTI")
