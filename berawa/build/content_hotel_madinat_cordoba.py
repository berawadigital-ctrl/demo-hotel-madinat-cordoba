# Contenido de la demo Hotel Madinat (Córdoba) (es/ca/en/fr). Hechos de hotelmadinat.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Adarve · Doble Superior','Dobles Deluxe con bañera','Hamama · Junior Suite'],
'ca':['Adarve · Doble Superior','Dobles Deluxe amb banyera','Hamama · Junior Suite'],
'en':['Adarve · Superior Double','Deluxe Doubles with bathtub','Hamama · Junior Suite'],
'fr':['Adarve · Double Supérieure','Doubles Deluxe avec baignoire','Hamama · Junior Suite']}
RD={
'es':['26 m² en la primera planta, con el suelo hidráulico original del siglo XIX, zona de estar y dos balcones al patio central.','En la primera crujía de la casa, con suelos hidráulicos recuperados y pinturas y yesería originales del siglo XIX.','40 m² en lo más alto de la casa, con vista a la Mezquita-Catedral, cama King y una bañera estilo alberca.'],
'ca':['26 m² a la primera planta, amb el sòl hidràulic original del segle XIX, zona d\'estar i dos balcons al pati central.','A la primera crugia de la casa, amb sòls hidràulics recuperats i pintures i guixeria originals del segle XIX.','40 m² al més alt de la casa, amb vista a la Mesquita-Catedral, llit King i una banyera estil alberca.'],
'en':['26 m² on the first floor, with the original 19th-century hydraulic tile floor, a seating area and two balconies onto the central patio.','In the first bay of the house, with recovered hydraulic tile floors and original 19th-century paintings and plasterwork.','40 m² at the top of the house, with a view of the Mosque-Cathedral, a King bed and an alberca-style bathtub.'],
'fr':['26 m² au premier étage, avec le sol hydraulique d\'origine du XIXe siècle, un coin salon et deux balcons sur le patio central.','Dans la première travée de la maison, avec des sols hydrauliques récupérés et des peintures et plâtreries d\'origine du XIXe siècle.','40 m² tout en haut de la maison, avec vue sur la Mosquée-Cathédrale, un lit King et une baignoire style alberca.']}
ART={
'hero':('arches',9501,['#efe3cc','#dcc6a0','#c07a3a','#3f4f82','#2f3e6b']),
'intro':('columns',9502,['#ece2cd','#f4ead6','#c07a3a','#8190b8','#2f3e6b']),
'r1':('arches',9511,['#efe2c8','#dac39b','#b8723a','#3d4d80','#2c3b68']),
'r2':('columns',9512,['#ece0ca','#f3e8d3','#bd7737','#7f8eb6','#30406e']),
'r3':('skyline',9513,['#3d4468','#e68f5d','#f9d29a','#3c4366','#2c3250','#1d2135']),
'g1':('arches',9521,['#f0e4cb','#dcc7a2','#bb7538','#3f4f82','#2f3e6b']),
'g2':('hills',9522,['#e4e8d6','#f3e7c6','#fbdc9f','#a8c3a1','#80a487','#587b6b']),
'g3':('skyline',9523,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g4':('columns',9524,['#eee3ce','#f5ebd8','#bf7a3a','#8493ba','#2f3e6b']),
'g5':('waves',9525,['#f3e0b4','#e8a374','#fff0c6','#7cb4c4','#4a8ba3','#2f6a83','#1d475d']),
'g6':('skyline',9526,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Madinat · Hotel 4 estrellas en una casa-patio de la Judería de Córdoba',see_rooms='Ver habitaciones',hero_k='Córdoba · Judería',hero_t='En el corazón de la antigua medina',hero_s='Una casa-patio de estilo señorial, a pocos pasos de la Mezquita-Catedral.',
 intro_t='Una casa-patio con habitaciones con nombre propio',intro_p1='El Hotel Madinat es un edificio protegido de cuatro estrellas en la calle Cabezas 17, con 11 habitaciones, todas diferentes y con nombre propio.',
 intro_p2='Tiene dos terrazas con vistas panorámicas a la Mezquita-Catedral, recepción 24 h y wifi gratuito en todo el hotel. Reservas por su web, por teléfono o por correo.',
 stats=['11 habitaciones','Dos terrazas','Recepción 24 h','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de las once habitaciones, todas con nombre propio.',
 svcs=['Recepción 24 h','Wifi gratuito','Dos terrazas con vistas','Desayuno buffet','Cuarto de equipaje gratuito','Habitaciones adaptadas','Cama supletoria en dobles superiores','Detector de humo'],
 loc_p='Calle Cabezas 17, 14003 Córdoba, en la Judería.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay parking?','¿Aceptan mascotas?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Madinat · Hotel de 4 estrelles en una casa-pati de la Jueria de Còrdova',see_rooms='Veure habitacions',hero_k='Còrdova · Jueria',hero_t='Al cor de l\'antiga medina',hero_s='Una casa-pati d\'estil senyorial, a pocs passos de la Mesquita-Catedral.',
 intro_t='Una casa-pati amb habitacions amb nom propi',intro_p1='L\'Hotel Madinat és un edifici protegit de quatre estrelles al carrer Cabezas 17, amb 11 habitacions, totes diferents i amb nom propi.',
 intro_p2='Té dues terrasses amb vistes panoràmiques a la Mesquita-Catedral, recepció 24 h i wifi gratuït a tot l\'hotel. Reserves per la seva web, per telèfon o per correu.',
 stats=['11 habitacions','Dues terrasses','Recepció 24 h','Wifi gratuït'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres de les onze habitacions, totes amb nom propi.',
 svcs=['Recepció 24 h','Wifi gratuït','Dues terrasses amb vistes','Esmorzar bufet','Sala d\'equipatge gratuïta','Habitacions adaptades','Llit supletori en dobles superiors','Detector de fum'],
 loc_p='Carrer Cabezas 17, 14003 Còrdova, a la Jueria.',
 chips=['Quantes habitacions té?','Hi ha pàrquing?','Accepten mascotes?','Com es reserva?']),
'en':dict(title='Hotel Madinat · 4-star hotel in a patio house in the Jewish Quarter of Córdoba',see_rooms='See the rooms',hero_k='Córdoba · Jewish Quarter',hero_t='In the heart of the old medina',hero_s='A stately patio house, a few steps from the Mosque-Cathedral.',
 intro_t='A patio house with individually named rooms',intro_p1='Hotel Madinat is a protected four-star building on Calle Cabezas 17, with 11 rooms, all different and each with its own name.',
 intro_p2='It has two terraces with panoramic views of the Mosque-Cathedral, 24-hour reception and free wifi throughout the hotel. Book through its website, by phone or by email.',
 stats=['11 rooms','Two terraces','24-hour reception','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the eleven rooms, each with its own name.',
 svcs=['24-hour reception','Free wifi','Two terraces with views','Buffet breakfast','Free luggage room','Adapted rooms','Extra bed in superior doubles','Smoke detector'],
 loc_p='Calle Cabezas 17, 14003 Córdoba, in the Jewish Quarter.',
 chips=['How many rooms does it have?','Is there parking?','Are pets accepted?','How do I book?']),
'fr':dict(title='Hotel Madinat · Hôtel 4 étoiles dans une maison-patio de la Juiverie de Cordoue',see_rooms='Voir les chambres',hero_k='Cordoue · Juiverie',hero_t='Au cœur de l\'ancienne médina',hero_s='Une maison-patio de style seigneurial, à quelques pas de la Mosquée-Cathédrale.',
 intro_t='Une maison-patio aux chambres nommées',intro_p1='L\'Hotel Madinat est un bâtiment protégé quatre étoiles calle Cabezas 17, avec 11 chambres, toutes différentes et chacune avec son propre nom.',
 intro_p2='Il dispose de deux terrasses avec vue panoramique sur la Mosquée-Cathédrale, d\'une réception 24 h et du wifi gratuit dans tout l\'hôtel. Réservations par son site, par téléphone ou par e-mail.',
 stats=['11 chambres','Deux terrasses','Réception 24 h','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des onze chambres, chacune avec son propre nom.',
 svcs=['Réception 24 h','Wifi gratuit','Deux terrasses avec vue','Petit-déjeuner buffet','Bagagerie gratuite','Chambres adaptées','Lit d\'appoint en doubles supérieures','Détecteur de fumée'],
 loc_p='Calle Cabezas 17, 14003 Cordoue, dans la Juiverie.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un parking ?','Les animaux sont-ils acceptés ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hotelmadinat.com')
D=dict(name='Hotel Madinat',ac='#2f3e6b',ac2='#c07a3a',ac2_a11y='#7a4412',book=BOOK,around=[],foot=FOOT,
 address='Calle Cabezas 17 · 14003 Córdoba',phones=['957 395 000'],emails=['info@hotelmadinat.com'],maps='Hotel Madinat, Calle Cabezas 17, Córdoba',t=T)
META=dict(repo='demo-hotel-madinat-cordoba',name='Hotel Madinat',legal_name='Madinat S.L.',registry_ids=['CIF B23899628'],
 url='https://www.hotelmadinat.com/',domain='hotelmadinat.com',municipality='Córdoba',province='Córdoba',sector='hotel 4 estrellas en casa-patio',
 read_at='2026-10-29T04:49:00+01:00',created_at='2026-10-29T04:51:00+01:00',built_at='2026-10-29T04:53:00+01:00',audit_date='2026-10-29T04:51:00+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T04:27:05+01:00',url='https://www.google.com/maps/place/Hotel+Madinat/@37.8803757,-4.7767409,17z/data=!4m9!3m8!1s0xd6d20825e4eb1d1:0xd83d703789a145fb!5m2!4m1!1i2!8m2!3d37.8803757!4d-4.7767409!16s%2Fg%2F11c2l1s3x_'),
 book=dict(mode='mail',email='info@hotelmadinat.com',note='La web del negocio tiene su propio motor de reservas; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel urbano con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿A qué hora es el check-in?','K02'),('¿Hay wifi?','K03'),('¿Hay parking?','K04'),('¿Aceptan mascotas?','K05'),('¿Hay habitaciones adaptadas?','K06'),('¿Hay desayuno?','K08'),('¿Hay terraza?','K09'),('¿Dónde está el hotel?','K10'),('¿Cómo reservo?','K11'),('¿Cuál es el teléfono?','K12'),('¿Qué historia tiene la casa?','K13'),('¿Quién es el titular?','K14'),('¿Tienen piscina?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K11')],
'ca':[('Quantes habitacions té?','K01'),('A quina hora és el check-in?','K02'),('Hi ha wifi?','K03'),('Hi ha pàrquing?','K04'),('Accepten mascotes?','K05'),('Hi ha habitacions adaptades?','K06'),('Hi ha esmorzar?','K08'),('Hi ha terrassa?','K09'),('On és l\'hotel?','K10'),('Com reservo?','K11'),('Quin és el telèfon?','K12'),('Quina història té la casa?','K13'),('Qui és el titular?','K14'),('Teniu piscina?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K11')],
'en':[('How many rooms does it have?','K01'),('What time is check-in?','K02'),('Is there wifi?','K03'),('Is there parking?','K04'),('Are pets accepted?','K05'),('Are there adapted rooms?','K06'),('Is there breakfast?','K08'),('Is there a terrace?','K09'),('Where is the hotel?','K10'),('How do I book?','K11'),('What is the phone number?','K12'),('What history does the house have?','K13'),('Who is the owner?','K14'),('Do you have a swimming pool?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K11')],
'fr':[('Combien de chambres a-t-il ?','K01'),('À quelle heure est le check-in ?','K02'),('Y a-t-il du wifi ?','K03'),('Y a-t-il un parking ?','K04'),('Les animaux sont-ils acceptés ?','K05'),('Y a-t-il des chambres adaptées ?','K06'),('Y a-t-il un petit-déjeuner ?','K08'),('Y a-t-il une terrasse ?','K09'),('Où est l\'hôtel ?','K10'),('Comment réserver ?','K11'),('Quel est le téléphone ?','K12'),('Quelle histoire a la maison ?','K13'),('Qui est le titulaire ?','K14'),('Avez-vous une piscine ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K11')]}
